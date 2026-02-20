
# Import necessary libraries for the chatbot
from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage

# Initialize the Large Language Model (LLM) using ChatOllama
# Model: qwen2.5:7B, Temperature: 0 for deterministic responses
llm = ChatOllama(
    model="qwen2.5:7B",
    temperature=0
)

# Define the state structure for the chatbot
# It holds a list of messages, with automatic message addition
class BasicChatState(TypedDict):
    messages: Annotated[list, add_messages]

# Define the chatbot function that processes the state
# It invokes the LLM with the current messages and returns the response
def chatbot(state: BasicChatState):
    return {
        "messages": [llm.invoke(state["messages"])]
    }

# Create a StateGraph for managing the chatbot flow
graph = StateGraph(BasicChatState)

# Add the chatbot node to the graph
graph.add_node("chatbot", chatbot)

# Set the entry point of the graph to the chatbot node
graph.set_entry_point("chatbot")

# Add an edge from chatbot to END, indicating the flow ends after processing
graph.add_edge("chatbot", END)

# Compile the graph into an executable application
app = graph.compile()

# Main interaction loop: Continuously take user input and respond
while True:
    # Get user input
    user_input = input("User: ")
    # Check if user wants to exit
    if(user_input in ["exit", "end"]):
        break
    else:
        # Invoke the app with the user's message
        result = app.invoke({
            "messages": [HumanMessage(content=user_input)]
        })

        # Print the latest message from the result (the chatbot's response)
        print(result["messages"][-1].content)

