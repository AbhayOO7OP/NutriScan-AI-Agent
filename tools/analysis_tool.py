# ---------------------------------------------------------
# analysis_tool.py
# Wrapper for ingredient risk analysis
# ---------------------------------------------------------

from agents import risk_agent

def run_risk_analysis(ingredients):
    """
    Calls the risk analyzer to classify and score ingredients.
    """
    return risk_agent.analyze_ingredients(ingredients)
