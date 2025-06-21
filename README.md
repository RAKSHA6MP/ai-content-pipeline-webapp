# 📚 Automated Book Publication Workflow

An AI-powered system that automates the end-to-end content pipeline for book publication — from web scraping and rewriting to review, feedback, and version management.

## 🚀 Overview

This project demonstrates a complete workflow combining AI and human-in-the-loop processes to streamline book content publication. It includes:

- 🔎 **Web Scraping** using Playwright  
- ✍️ **AI-Powered Rewriting** via Gemini Pro / GPT  
- 👁️ **Human Review & Feedback Integration**  
- 🗃 **Content Versioning** with ChromaDB  
- 🧠 **Agent Communication** and RL-enhanced Search  

---

## 📌 Features

- ✅ Extracts book chapters and captures screenshots
- ✅ Sends content to LLM for rewriting
- ✅ Enables review cycles with feedback comparison
- ✅ Stores and retrieves content versions efficiently
- ✅ Enhances search with reinforcement-learning tuning

---

## 🧰 Tech Stack

| Tool/Tech        | Purpose                          |
|------------------|----------------------------------|
| **Python**       | Core logic                       |
| **Playwright**   | Web scraping & screenshots       |
| **Gemini Pro** / **GPT** | AI text generation           |
| **ChromaDB**     | Vector storage & versioning      |
| **LangChain**    | LLM orchestration & agents       |
| **RL Algorithm** | Search optimization (rewarding better rewrites) |

---

## 🔧 How to Run

1. **Clone this repository**
```bash
git clone https://github.com/yourusername/automated-book-workflow.git
cd automated-book-workflow

