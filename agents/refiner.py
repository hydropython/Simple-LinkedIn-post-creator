from utils.gemini_client import get_client

def refine_post(draft: str) -> str:
    """Refine LinkedIn post: concise, professional, engaging."""
    model = get_client()
    prompt = f"Polish this LinkedIn post to be concise, professional, and engaging:\n\n{draft}"
    result = model.generate_content(prompt)
    return result.text.strip()