from app.services.llm_service import ask_llm


def generate_spring_controller(summary):

    prompt = f"""
You are a Senior Java Spring Boot Architect.

Generate a production-ready Spring Boot REST Controller.

API Summary:

{summary}

Requirements:

1. Use Spring Boot 3

2. Use @RestController

3. Use @RequestMapping

4. Use ResponseEntity

5. Add request mappings

6. Use clean coding practices

Return only code.
"""

    return ask_llm(prompt)