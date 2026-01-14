AutoStream AI Assistant – Setup Instructions
===========================================

This project is a stateful AI assistant built using Streamlit and a local LLM
powered by Ollama, the other LLM providers like Openai ,Gemini , Claude were inaccessible 
in some regions and I was facing some similar issue so I deployed the project using Ollama locally.
It uses intent detection, RAG, and tool invocation for lead capture.

--------------------------------------------
1. Python Requirements
--------------------------------------------

Python version required:
- Python 3.10 or higher

Create and activate a virtual environment:
- python3 -m venv venv
- source venv/bin/activate

Install Python dependencies:
- pip install -r requirements.txt

--------------------------------------------
2. Ollama (System Dependency)
--------------------------------------------

This project uses Ollama as a local LLM server.
Ollama is a system-level dependency and is NOT installed via pip.

Install Ollama (for Windows):
-Go to:
    https://ollama.com

Download the Windows installer (.exe)

Install Ollama (Next → Next → Finish) https://ollama.com

Linux / macOS quick install:
- curl -fsSL https://ollama.com/install.sh | sh

Pull the required model (Windows/Linux/macOS):
- ollama pull llama3

Verify Ollama is running:
- ollama run llama3

You should see the model respond in the terminal.

--------------------------------------------
3. Running the Application
--------------------------------------------

From the project root directory:

- streamlit run app.py

The assistant will open in your browser.

--------------------------------------------
4. Expected Demo Flow
--------------------------------------------

Use the following conversation to test full functionality:

- hi
- price
- I am interested
- Parth
- parth@email.com
- YouTube

Terminal output:
- Lead captured successfully: Parth Soni, parthhhsoniii@email.com, YouTube

--------------------------------------------
5. Notes
--------------------------------------------

- Ollama must be running in the background for the assistant to work.
- requirements.txt contains only Python dependencies.
- Ollama is documented separately because it runs as a system service.

--------------------------------------------
6. Project Highlights
--------------------------------------------

- Streamlit chat UI
- Local LLM inference (no paid APIs)
- Retrieval-Augmented Generation (RAG)
- Stateful conversation handling
- Tool-based lead capture
- Cost-efficient and offline-capable

--------------------------------------------
End of File
--------------------------------------------
