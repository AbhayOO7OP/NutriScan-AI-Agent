# ---------------------------------------------------------
# advisor_agent.py
# Personalized nutritional advice based on risk analysis
# ---------------------------------------------------------

def generate_advice(risk_report, user_profile):
    """
    Use the risk report + user preferences to generate final health advice.
    """

    total_risk = 0
    warnings = []

    for item in risk_report:
        # Higher score = unhealthy
        total_risk += (100 - item["score"])

        # Allergen warning
        if "Allergen Risk" in item["risks"]:
            warnings.append(f"Contains allergen: {item['ingredient']}")

        # Diabetic warning
        if user_profile.get("diabetic") and "Hidden Sugar" in item["risks"]:
            warnings.append(f"Unsafe for diabetics: {item['ingredient']}")

    # Final recommendation
    if total_risk > 250:
        suggestion = "❌ Avoid this product (High risk ingredients detected)."
    elif total_risk > 150:
        suggestion = "⚠️ Consume in moderation (Medium risk)."
    else:
        suggestion = "✅ Safe to consume (Low risk)."

    return {
        "total_risk_score": total_risk,
        "warnings": warnings,
        "suggestion": suggestion
    }
