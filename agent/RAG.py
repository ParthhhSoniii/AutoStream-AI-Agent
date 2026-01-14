import ollama


def retrieve_knowledge():
    """
    Loads the knowledge base from a local markdown file.
    This acts as the retrieval step in RAG.
    """
    with open("data/knowledge_base.md", "r") as f:
        return f.read()


def answer_with_rag(user_question: str) -> str:
    """
    Uses a local Ollama LLM (llama3) to answer questions
    strictly based on the retrieved knowledge.
    """
    knowledge = retrieve_knowledge()

    prompt = f"""
You are AutoStream's AI assistant.

Rules:
- Answer ONLY using the information provided below.
- If the answer is not present, say:
  "I don't have that information right now."

INFORMATION:
{knowledge}

USER QUESTION:
{user_question}

ANSWER:
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()

