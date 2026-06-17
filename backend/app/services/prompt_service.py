import json

def build_prompt(summary, question):

    return f"""
SYSTEM:
You are an expert API Architect.

API SUMMARY:

{json.dumps(summary, indent=2)}

QUESTION:

{question}

ANSWER:
"""