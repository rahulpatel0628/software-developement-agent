# AI Software Development Agent

An AI-powered Multi-Agent Software Development System built using LangGraph, LangChain, Groq, and Streamlit.

The system automatically converts natural language software requirements into a complete software project architecture, backend code, frontend code, code review reports, and testing reports using specialized AI agents.

---

# Overview

Traditional LLMs generate code in a single response. This project simulates a real software engineering workflow by dividing responsibilities among multiple AI agents.

The user provides a project requirement, and the system:

1. Designs the software architecture.
2. Generates backend code.
3. Generates frontend code.
4. Reviews the generated code.
5. Tests the generated code.
6. Returns a complete development report.

---

# System Architecture
```
User Requirement
↓
Team Lead Agent
↓
┌─────────────┐
│             │
Backend     Frontend
│             │
└──────┬──────┘
↓
Reviewer
↓
Tester
↓
Final Output
```
---

# Agents

## 1. Team Lead Agent

Responsibilities:

* Analyze project requirements.
* Design software architecture.
* Select technology stack.
* Define APIs.
* Define database entities.
* Define folder structure.
* Plan deployment strategy.

Output:

* Project architecture plan.

---

## 2. Backend Agent

Responsibilities:

* Generate backend source code.
* Generate API routes.
* Generate database models.
* Generate database configuration.
* Implement authentication logic.
* Follow backend best practices.

Generated Files:

* main.py
* database.py
* models.py
* routes.py

---

## 3. Frontend Agent

Responsibilities:

* Generate frontend source code.
* Create reusable UI components.
* Implement API integration.
* Create dashboard pages.
* Create authentication pages.

Generated Files:

* App.jsx
* Login.jsx
* Dashboard.jsx
* api.js
* styles.css

---

## 4. Reviewer Agent

Responsibilities:

* Review generated backend code.
* Review generated frontend code.
* Analyze architecture quality.
* Identify security issues.
* Identify scalability issues.
* Provide improvement suggestions.

Output:

* Review score.
* Issues.
* Suggestions.

---

## 5. Tester Agent

Responsibilities:

* Analyze backend implementation.
* Analyze frontend implementation.
* Verify architecture consistency.
* Evaluate code quality.
* Evaluate maintainability.

Output:

* Backend score.
* Frontend score.
* Backend issues.
* Frontend issues.

---

# Tech Stack

## AI & Agent Framework

* LangGraph
* LangChain
* Groq API
* Pydantic

## Frontend

* Streamlit

## Backend

* Python

## LLM

* Llama 3.3 70B Versatile (Groq)

---

# 📂 Project Structure
```
software-dev-agent/
├── agents/
│   ├── team_lead.py
│   ├── backend.py
│   ├── frontend.py
│   ├── reviewer.py
│   └── tester.py
│
├── prompts/
│   ├── team_lead.txt
│   ├── backend.txt
│   ├── frontend.txt
│   ├── reviewer.txt
│   └── tester.txt
│
├── graphs/
│   └── workflow.py
│
├── state/
│   └── state.py
│
├── tools/
│   └── file_tool.py
│
├── generated/
│   ├── backend/
│   └── frontend/
│
├── app.py
├── main.py
└── requirements.txt
```
---

# Installation
```
Clone repository:

git clone https://github.com/rahulpatel0628/software-developement-agent.git

cd software-developement-agent

Create virtual environment:

python -m venv venv

Activate virtual environment:

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
```
---

#  Environment Variables
```
Create a .env file:

GROQ_API_KEY=your_groq_api_key
```
---

#  Run Application
```
Terminal Version:

python main.py

Streamlit Version:

streamlit run app.py
```
---

# Example Input
```
Build a Student Management System
```
---

# Example Output
```
Architecture Plan

* Tech Stack
* APIs
* Database Design
* Folder Structure

Backend Files

* main.py
* database.py
* models.py
* routes.py

Frontend Files

* App.jsx
* Login.jsx
* Dashboard.jsx
* api.js
* styles.css

Review Report

* Score
* Issues
* Suggestions

Testing Report

* Backend Score
* Frontend Score
* Backend Issues
* Frontend Issues
```
---

# Key Features
```
* Multi-Agent Workflow
* Architecture Planning
* Backend Code Generation
* Frontend Code Generation
* Automated Code Review
* Automated Testing
* Structured Outputs with Pydantic
* LangGraph State Management
* Streamlit Interface
* Production-Ready Agent Pipeline
```
---

# Future Improvements
```
* User Approval Workflow
* Code Regeneration
* RAG-Based Project Memory
* Repository Understanding
* Automated Bug Fixing
* Docker Integration
* CI/CD Generation
* Deployment Agent
* Security Agent
* Database Agent
* Multi-Language Support
* OpenAI / Claude / GLM Support
```
---

# Learning Outcomes

This project demonstrates:
```
* Agentic AI Systems
* LangGraph Workflows
* Multi-Agent Architecture
* Prompt Engineering
* Structured Output Generation
* State Management
* Software Engineering Automation
* LLM-Based Code Generation
```
---

# Author

Rahul Patel

B.Tech ICT | AI & ML Enthusiast

Built as a learning project to explore Multi-Agent Software Engineering using LangGraph and Large Language Models.
