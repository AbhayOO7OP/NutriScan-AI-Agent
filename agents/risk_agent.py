# ---------------------------------------------------------
# risk_agent.py
# Analyze ingredients for health risks
# ---------------------------------------------------------

hidden_sugars = [
    "dextrose", "maltodextrin", "invert syrup", "fructose syrup",
    "corn syrup", "glucose syrup", "malt extract"
]

preservatives = [
    "e110", "e129", "e407", "msg", "e621", "tbhq", "bht"
]

allergens = [
    "milk", "soy", "nuts", "almond", "egg", "gluten", "wheat"
]


def analyze_ingredients(ingredients):
    """
    Classify each ingredient based on risk and generate scores.
    """

    analysis = []

    for ing in ingredients:
        item = ing.lower()
        risks = []
        score = 100  # Perfectly safe baseline

        # Hidden sugar detection
        if any(sugar in item for sugar in hidden_sugars):
            risks.append("Hidden Sugar")
            score -= 30

        # Preservatives / additives
        if any(p in item for p in preservatives):
            risks.append("Preservative / Additive")
            score -= 40

        # Allergen check
        if any(a in item for a in allergens):
            risks.append("Allergen Risk")
            score -= 50

        if not risks:
            risks.append("Low Risk")

        analysis.append({
            "ingredient": ing,
            "risks": risks,
            "score": max(0, score)
        })

    return analysis
