from utils.gemini_client import get_client

def generate_hashtags(post: str) -> str:
    """Generate 5-7 relevant hashtags for LinkedIn post."""
    model = get_client()
    prompt = f"Suggest 5-7 hashtags for this LinkedIn post:\n\n{post}"
    result = model.generate_content(prompt)
    return result.text.strip()