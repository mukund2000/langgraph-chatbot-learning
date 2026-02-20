# LangGraph Chatbot Learning

A **progressive learning series of chatbot implementations** using **LangGraph** — starting from a basic conversational AI and evolving to include **memory persistence**, **tool integration**, and **SQLite-based storage** for educational purposes. :contentReference[oaicite:1]{index=1}

This repository is designed to help developers, students, and AI practitioners understand how to build stateful chatbots using LangGraph through incremental, hands-on Python examples.

---

## 🚀 Overview

LangGraph is a framework for building **graph-based conversational agents** and workflows. Unlike traditional single-step prompt systems, LangGraph organizes interactions using nodes and edges (a finite state machine), allowing more structured, contextual conversations. :contentReference[oaicite:2]{index=2}

This learning series gradually introduces concepts such as:

- Basic chatbot flow  
- Memory management  
- Persistent storage (SQLite)  
- Integration with tools and APIs  

---

## 📁 Repository Structure

| File/Script                         | Purpose |
|------------------------------------|---------|
| `chatbot.py`                      | Basic LangGraph chatbot example |
| `chatbot_with_memory.py`          | Chatbot with simple in-memory conversation state |
| `chatbot_with_sqlite_memory.py`   | Chatbot with persistent memory stored in SQLite |
| `chatbot_with_tools.py`           | Chatbot that integrates external tools (e.g., APIs, plugins) |
| `README.md`                       | Project documentation (this file) |

---

## 🧠 What You’ll Learn

### ✅ Basic Chatbot
Start with a simple conversational agent using core LangGraph constructs:
- Define dialogue states  
- Build state graph flows  
- Handle user inputs and responses

### 🧠 Memory Persistence
Extend the bot to:
- Store conversation context  
- Recall past interactions  
- Improve response relevance

### 💾 SQLite-Based Storage
Introduce a lightweight database for persistence:
- Save memory beyond runtime  
- Support longer session continuity

### 🧰 Tool Integration
Learn how to:
- Call external tools (e.g., web search, calculators, custom integrations)
- Enhance the chatbot’s capabilities beyond static responses

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **Ollama**: Download from [ollama.ai](https://ollama.ai)
- **Qwen2.5 Model** (or your preferred model): Run `ollama pull qwen2.5:7B` or `ollama pull qwen2.5:14B`
- **pip** or **poetry** for package management

## 🚀 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/mukund2000/langgraph-chatbot-learning.git
cd langgraph-chatbot-learning
```

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install langchain langgraph langchain-community langchain-ollama langgraph-checkpoint-sqlite
```

4. **Ensure Ollama is running**:
```bash
ollama serve
```

In another terminal, pull the required model:
```bash
ollama pull qwen2.5:7B
```

## ⚙️ Configuration

### Model Configuration

Edit the model parameters in the scripts:

```python
llm = ChatOllama(
    model="qwen2.5:7B",      # Change model name
    temperature=0             # 0 = deterministic, 1 = creative
)
```

Available models via Ollama:
- `qwen2.5:7B` (7B parameters - faster)
- `qwen2.5:14B` (14B parameters - more capable)
- `mistral:latest`
- `llama2:latest`
- And many more

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to functions and classes
- Test your changes before submitting a PR
- Update README if adding new features

## 📚 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Ollama Documentation](https://ollama.ai)
- [ReAct Pattern Paper](https://arxiv.org/abs/2210.03629)

## 📝 License

This project is open source and available under the MIT License. See the LICENSE file for details.

## 🙋 Support

If you encounter any issues or have questions:

1. Check the existing GitHub Issues
2. Create a new GitHub Issue with a detailed description
3. Include error messages and steps to reproduce

## 🎓 Learning Resources

- Understanding ReAct: https://arxiv.org/abs/2210.03629
- LangChain Agents: https://python.langchain.com/docs/modules/agents/
- Multi-Agent Systems: https://arxiv.org/abs/2308.03688

---
