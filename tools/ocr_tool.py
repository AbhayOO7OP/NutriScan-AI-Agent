# ---------------------------------------------------------
# ocr_tool.py
# Wrapper for Gemini OCR / Vision extraction
# ---------------------------------------------------------

from agents import extraction_agent

def run_ocr(image_bytes):
    """
    Calls the extraction agent to extract ingredients from image.
    """
    return extraction_agent.extract_ingredients(image_bytes)
