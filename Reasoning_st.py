import streamlit as st
import json
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="JSON Answer Generator",
    layout="centered"
)

st.title("🧠 Reasoning Agent (JSON Output)")
st.caption("Input: Plain text question → Output: Structured JSON")

# =========================
# USER INPUT
# =========================
question = st.text_area(
    "Enter your question",
    placeholder="Type your question here..."
)

# =========================
# PROCESSING FUNCTION
# =========================
def generate_response(question: str) -> dict:
    if not question.strip():
        return {
            "answer": "",
            "status": "failed",
            "reasoning_visible_to_user": "No question provided.",
            "metadata": {
                "plan": "Validate input",
                "checks": [
                    {
                        "check_name": "Input provided",
                        "passed": False,
                        "details": "Question text was empty"
                    }
                ],
                "retries": 0
            }
        }

    # Example logic (replace with LLM / RAG / rules)
    answer = "This is a sample answer generated for your question."

    return {
        "answer": answer,
        "status": "success",
        "reasoning_visible_to_user": "The system analyzed the question and generated a concise response.",
        "metadata": {
            "plan": "Analyze question → Generate answer → Validate output",
            "checks": [
                {
                    "check_name": "Input validation",
                    "passed": True,
                    "details": "Valid question received"
                },
                {
                    "check_name": "Answer generated",
                    "passed": True,
                    "details": "Answer text successfully created"
                }
            ],
            "retries": 0
        }
    }

# =========================
# BUTTON ACTION
# =========================
if st.button("Generate JSON Response"):
    response = generate_response(question)

    st.subheader("📤 Output JSON")
    st.json(response)

    # Optional: Download JSON
    json_str = json.dumps(response, indent=4)
    st.download_button(
        label="⬇️ Download JSON",
        data=json_str,
        file_name="response.json",
        mime="application/json"
    )
