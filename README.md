## 🧠 Multi-Step Reasoning Agent with Self-Checking ##
📌 Overview

A Python-based reasoning agent that solves structured math, logic, and constraint problems using multi-step reasoning, self-verification, and retry mechanisms, while exposing only the final validated answer to the user.

**🎯 Objective**

Solve problems using step-by-step internal reasoning

Validate answers before returning results

Retry automatically on incorrect reasoning

Return clean, structured JSON output

Hide raw chain-of-thought reasoning

**🏗️ Architecture**

Planner – Creates a step-by-step solution plan

Executor – Performs reasoning and calculations

Verifier – Validates results and triggers retries if needed

📤 Output

Final answer and status (success / failed)

Short user-facing explanation

Debug metadata (plan, checks, retries)

 **🧠 Approach**

Plan → Execute → Verify reasoning loop

Deterministic calculations using Python

LLM used for logical reasoning

Validation before final output

**🛠️ Technologies Used**

Python

LLM APIs (OpenAI / Anthropic / Gemini or mock)

JSON-based structured responses

Modular prompt design
