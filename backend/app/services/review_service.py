from app.services.llm_service import ask_llm
from app.services.review_storage_service import save_review

def review_api(summary):

    architecture_score = 100
    security_score = 100
    rest_score = 100

    issues = []
    recommendations = []

    endpoints = summary.get("endpoints", [])

    # --------------------------
    # Check 1 - Missing Summary
    # --------------------------

    for endpoint in endpoints:

        if endpoint.get("summary", "").strip() == "":

            architecture_score -= 5

            issues.append(
                f"{endpoint['method']} {endpoint['path']} is missing summary."
            )

            recommendations.append(
                "Add summaries for all operations."
            )

    # --------------------------
    # Check 2 - Version
    # --------------------------

    version = summary.get("version", "")

    if version == "":

        architecture_score -= 5

        issues.append(
            "API version is missing."
        )

        recommendations.append(
            "Version your APIs."
        )

    # --------------------------
    # Check 3 - Servers
    # --------------------------

    servers = summary.get("servers", [])

    if len(servers) == 0:

        architecture_score -= 5

        issues.append(
            "Server information missing."
        )

        recommendations.append(
            "Define OpenAPI servers."
        )

    # --------------------------
    # Check 4 - REST Naming
    # --------------------------

    for endpoint in endpoints:

        path = endpoint["path"]

        if "_" in path:

            rest_score -= 2

            issues.append(
                f"{path} uses underscore."
            )

            recommendations.append(
                "Prefer hyphenated or plural resource names."
            )

    # --------------------------
    # Check 5 - Authentication
    # --------------------------

    security = summary.get("security", [])

    if len(security) == 0:

        security_score -= 15

        issues.append(
            "Authentication not defined."
        )

        recommendations.append(
            "Use OAuth2 or JWT authentication."
        )

    # --------------------------
    # LLM Explanation
    # --------------------------

    prompt = f"""

You are a Senior Solution Architect.

API Summary:

{summary}

Detected Issues:

{issues}

Recommendations:

{recommendations}

Explain:

1. Architecture quality

2. Security quality

3. REST maturity

4. Best practices

5. Improvements

"""

    ai_review = ask_llm(prompt)

    result = {

    "architectureScore": architecture_score,

    "securityScore": security_score,

    "restScore": rest_score,

    "issues": issues,

    "recommendations": recommendations,

    "aiReview": ai_review
    }
    save_review(result)
    return result