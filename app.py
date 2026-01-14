import streamlit as st
import time
from agent.graph import run_agent

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AutoStream AI Assistant",
    page_icon="🎬",
    layout="centered"
)

# ---------------- Sidebar ----------------
with st.sidebar:
    st.header("🎬 AutoStream")
    st.markdown(
        """
        **AI Assistant for Content Creators**

        I can help you with:
        - Pricing & plans
        - Product features
        - Getting started 🚀
        """
    )
    st.divider()
    st.caption("Internship Project • Local LLM (Ollama)")

# ---------------- Title ----------------
st.title("🎬 AutoStream AI Assistant")
st.caption("Ask about pricing, features, or getting started")

# ---------------- Typing Effect ----------------
def typewriter_effect(text, delay=0.02):
    placeholder = st.empty()
    rendered = ""
    for char in text:
        rendered += char
        placeholder.markdown(rendered)
        time.sleep(delay)

# ---------------- Session State ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "stage" not in st.session_state:
    st.session_state.stage = "start"

if "lead" not in st.session_state:
    st.session_state.lead = {}

# ---------------- Display Chat History ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- Suggested Prompts ----------------
if len(st.session_state.messages) == 0:
    st.markdown("**Try asking:**")
    cols = st.columns(3)
    prompts = [
        "What is the price of the Pro plan?",
        "What features does AutoStream offer?",
        "I want to buy AutoStream"
    ]

    for col, prompt in zip(cols, prompts):
        if col.button(prompt):
            st.session_state.messages.append(
                {"role": "user", "content": prompt}
            )
            st.rerun()

# ---------------- User Input ----------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Run agent (NO try/except masking logic errors)
    response, new_stage, updated_lead = run_agent(
        user_input,
        st.session_state.stage,
        st.session_state.lead
    )

    # Update state
    st.session_state.stage = new_stage
    st.session_state.lead = updated_lead

    # Save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    # Show assistant message
    with st.chat_message("assistant"):
        typewriter_effect(response)

    # Success feedback
    if "Lead captured successfully" in response:
        st.success("🎉 Thank you! Our team will reach out soon.")

# ---------------- Footer ----------------
st.caption("🟢 Assistant running locally with Ollama")
