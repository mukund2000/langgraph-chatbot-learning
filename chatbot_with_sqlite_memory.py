# Install required package: pip install langgraph-checkpoint-sqlite

# Import necessary libraries for the chatbot with tools and SQLite memory
from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.checkpoint.sqlite import SqliteSaver

# Initialize SQLite-based memory saver for persistent storage across sessions
# Creates or connects to 'memory.db' database file
memory_cm = SqliteSaver.from_conn_string("memory.db")
# Enter the context manager to get the memory object
memory = memory_cm.__enter__()

# Initialize the Large Language Model (LLM) using ChatOllama
# Model: qwen2.5:7B, Temperature: 0 for deterministic responses
llm = ChatOllama(
    model="qwen2.5:7B",
    temperature=0
)

# Define a tool function to search DuckDuckGo
def search_duckduckgo(query: str):
    """Searches DuckDuckGo using LangChain's DuckDuckGoSearchRun tool."""
    search = DuckDuckGoSearchRun()
    return search.invoke(query)

# Define a tool function to add two numbers
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

# Define a tool function to multiply two numbers
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

# List of tools available to the chatbot
tools = [search_duckduckgo, add, multiply]

# Bind the tools to the LLM so it can call them
llm_with_tools = llm.bind_tools(tools)

# Define the state structure for the chatbot
# It holds a list of messages, with automatic message addition
class BasicChatState(TypedDict):
    messages: Annotated[list, add_messages]

# Define the chatbot function that processes the state
# It invokes the LLM with tools using the current messages and returns the response
def chatbot(state: BasicChatState):
    return {
        "messages": [llm_with_tools.invoke(state["messages"])]
    }

# Define a router function to decide the next step based on tool calls
def tools_router(state: BasicChatState):
    last_message = state["messages"][-1]
    print("last message: ", last_message)
    # Check if the last message has tool calls
    if(hasattr(last_message, "tool_calls") and len(last_message.tool_calls) > 0):
        return "tool_node"  # Route to tool execution
    else:
        return END  # End the conversation

# Create a ToolNode to handle tool executions
tool_node = ToolNode(tools=tools)

# Create a StateGraph for managing the chatbot flow with tools
graph = StateGraph(BasicChatState)

# Add the chatbot node to the graph
graph.add_node("chatbot", chatbot)

# Add the tool node to the graph
graph.add_node("tool_node", tool_node)

# Set the entry point of the graph to the chatbot node
graph.set_entry_point("chatbot")

# Add conditional edges from chatbot to either tool_node or END based on router
graph.add_conditional_edges("chatbot", tools_router)

# Add an edge from tool_node back to chatbot for continued conversation
graph.add_edge("tool_node", "chatbot")

# Compile the graph into an executable application with SQLite memory checkpointer
app = graph.compile(checkpointer=memory)

# Configuration for the conversation thread
config = {"configurable": {
    "thread_id": 1  # Unique thread ID for persisting conversation state in SQLite
}}

# Main interaction loop: Continuously take user input and respond
while True:
    # Get user input
    user_input = input("User: ")
    # Check if user wants to exit
    if(user_input in ["exit", "end"]):
        break
    else:
        # Invoke the app with the user's message and config for SQLite memory
        result = app.invoke({
            "messages": [HumanMessage(content=user_input)]
        }, config=config)

        # Print the AI's response with a label
        print("AI: " + result["messages"][-1].content)

