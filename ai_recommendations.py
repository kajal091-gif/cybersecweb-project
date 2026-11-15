# ai_recommendations.py

def generate_recommendations(vulnerabilities):

    recommendations = []

    if not vulnerabilities:
        return [
            "No major vulnerabilities detected.",
            "Continue regular security monitoring.",
            "Keep all services updated."
        ]

    for vuln in vulnerabilities:

        service = vuln["service"]
        risk = vuln["risk"]
        solution = vuln["solution"]

        recommendations.append(
            f"{service}: {solution}"
        )

        if risk == "Critical":
            recommendations.append(
                f"URGENT: Fix {service} immediately."
            )

        elif risk == "High":
            recommendations.append(
                f"HIGH RISK: Secure {service} as soon as possible."
            )

    # Remove duplicates
    recommendations = list(dict.fromkeys(recommendations))

    return recommendations