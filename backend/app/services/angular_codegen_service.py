from app.services.llm_service import ask_llm


def generate_angular_service(summary):

    prompt = f"""
You are a Senior Angular Developer.

Generate:

1. Angular Service

2. Interface

3. HttpClient methods

4. Proper typing

5. Injectable

6. Observable based

API Summary:

{summary}

Return only TypeScript code.
"""

    return ask_llm(prompt)