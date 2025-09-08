from utils.gemini_client import get_client

def draft_post(topic: str) -> str:
    """Generate raw LinkedIn post draft on a given topic."""
    model = get_client()
    prompt = f"Write a LinkedIn post about: {topic}"
    result = model.generate_content(prompt)
    return result.text.strip()