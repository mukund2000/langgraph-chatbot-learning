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

## 🛠️ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/mukund2000/langgraph-chatbot-learning.git
cd langgraph-chatbot-learning
