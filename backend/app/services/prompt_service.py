import json
from app.rag.retriever import retrieve

def build_prompt(summary, question):

    context = retrieve(question)

    return f"""
You are an Expert API Architect.

OpenAPI Summary:

{json.dumps(summary, indent=2)}

Knowledge Base:

{" ".join(context)}

Question:

{question}

Answer:
"""