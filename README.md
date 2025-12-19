🎯 Objective

To build a multi-step reasoning agent that can solve structured word problems by planning, executing, and verifying solutions internally, while presenting only the final validated answer and a short explanation to the user.

🛠️ Technologies Used

Python

Jupyter Notebook

LLM APIs (OpenAI / compatible LLMs or mocked interfaces)

JSON-based structured outputs

Prompt Engineering

🧠 Approach

Planner Phase: Analyze the input question and generate a clear step-by-step plan for solving it.

Executor Phase: Follow the plan to compute intermediate results using LLM reasoning and/or Python-based calculations.

Verifier Phase: Independently validate the solution by re-checking calculations, constraints, and logical consistency.

If verification fails, retry the reasoning process a limited number of times or return a failure status.

Return a structured JSON response containing the final answer, reasoning summary, verification checks, and metadata—without exposing raw chain-of-thought.
