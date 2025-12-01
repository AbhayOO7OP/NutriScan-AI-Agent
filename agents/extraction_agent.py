# ---------------------------------------------------------
# extraction_agent.py
# Extract ingredients from food label image using Gemini
# ---------------------------------------------------------

import re
from google import genai

client = genai.Client()

def extract_ingredients(image_bytes):
    """
    Extract text from an image using Gemini Vision and parse ingredients.
    """

    # Step 1: OCR using Gemini
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=["Extract ONLY the ingredient list from this image:", image_bytes]
    )

    raw_text = response.text if response else ""

    # Step 2: Clean & parse ingredients
    ingredients = parse_ingredients(raw_text)
    return ingredients


def parse_ingredients(text):
    """
    Clean OCR text and extract ingredient list properly.
    """
    text = text.lower().replace("\n", " ")

    # Look for "ingredients:" keyword
    match = re.search(r"ingredients[:\-]?\s*(.*)", text)

    if match:
        ingredients_raw = match.group(1)
    else:
        ingredients_raw = text

    # Split by comma
    items = [i.strip() for i in ingredients_raw.split(",") if len(i.strip()) > 1]

    return items
