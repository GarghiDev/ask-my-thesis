# 🎓 Ask My Thesis

A RAG-powered chatbot that answers questions about my Master's thesis: "Neurophysiological Responses to Distractors" (DTU, 2023).

## 🔗 [Try the Live Demo](https://huggingface.co/spaces/Garghi/AskMyThesis)

## Tech Stack
- **LLM:** Groq (Llama 3 / Mixtral)
- **Framework:** LangChain
- **Vector Store:** ChromaDB
- **Embeddings:** HuggingFace sentence-transformers
- **UI:** Gradio
- **Deployment:** Hugging Face Spaces

## What It Does
Upload a thesis or academic document and ask questions about it in natural language. The app retrieves relevant sections and generates accurate, sourced answers using RAG (Retrieval-Augmented Generation).

## How to Run Locally
1. Clone this repo: `git clone https://github.com/GarghiDev/ask-my-thesis.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Groq API key as an environment variable
4. Run: `python app.py`

## Author
**Garghi Seenevas** — Engineer pivoting from acoustics to AI engineering.
[LinkedIn](https://www.linkedin.com/in/garghi/) · seegarghi@gmail.com
