# K.A.R.U.P. — Personal Agentic AI System

> **K.A.R.U.P. (Knowledge-Augmented Reasoning & Utility Personal Agent)** is a personal-use, extensible agentic AI system designed to act as a long-term digital assistant.

K.A.R.U.P. is designed around a modular architecture where reasoning, memory, orchestration, tools, external integrations, security, observability, and infrastructure are independently managed.

The system is intended for **personal use**. Anyone creating their own deployment must provide and configure their **own API credentials, OAuth applications, cloud resources, databases, and third-party integrations**.

---

## 🎯 Project Vision

K.A.R.U.P. is not intended to be a conventional chatbot.

The long-term goal is to build a persistent AI system capable of:

- Understanding natural-language requests
- Planning multi-step tasks
- Executing tasks through tools
- Maintaining short- and long-term memory
- Using external APIs
- Managing personal workflows
- Operating development environments
- Interacting with AWS infrastructure
- Working with GitHub repositories
- Managing email and calendars
- Performing research
- Running autonomous workflows
- Asking for approval for sensitive operations
- Verifying completed actions
- Learning the user's preferences and operating style

The architecture is designed so that **new capabilities can be added as tools without redesigning the core agent**.

---

# 🏗️ Architecture

```text
                              USER
                                │
                    WhatsApp / API / Web
                                │
                                ▼
                     ┌──────────────────┐
                     │   FastAPI API    │
                     │   Interface      │
                     └────────┬─────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │    SUPERVISOR    │
                     │      AGENT       │
                     └────────┬─────────┘
                              │
                    ┌─────────┼─────────┐
                    ▼         ▼         ▼
                 MEMORY    PLANNER    POLICY
                    │         │         │
                    └─────────┼─────────┘
                              │
                              ▼
                       LANGGRAPH STATE
                              │
                              ▼
                       TOOL REGISTRY
                              │
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
          NATIVE TOOLS       MCP             WORKFLOWS
              │               │                │
              └───────────────┼────────────────┘
                              ▼
                          ADAPTERS
                              │
                              ▼
                           CLIENTS
                              │
          ┌────────┬──────────┼─────────┬─────────┐
          ▼        ▼          ▼         ▼         ▼
       Google  Microsoft     AWS      GitHub   LinkedIn
          │        │          │         │         │
          └────────┴──────────┴─────────┴─────────┘
                              │
                              ▼
                          EXECUTION
                              │
                              ▼
                           VERIFY
                              │
                              ▼
                            MEMORY
