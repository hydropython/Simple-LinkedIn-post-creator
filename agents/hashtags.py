# agents/hashtags.py
from crewai import Agent, tools
from utils.gemini_client import get_client
import re

def generate_hashtags_tool(post: str) -> list:
    """
    Generate relevant hashtags from the post.
    Ensures hashtags are meaningful, multi-word phrases combined in camel case.
    """
    model = get_client()
    try:
        prompt = f"""
        Extract 8-12 relevant hashtags from the following post.
        Each hashtag should start with '#' and use camel case for multi-word phrases.
        Do NOT split letters individually.

        Post:
        {post}
        """
        result = model.generate_content(prompt)
        hashtags = result.text.strip().split()  # split by space
        # Ensure each hashtag starts with #
        hashtags = [ht if ht.startswith("#") else f"#{ht}" for ht in hashtags]
        return hashtags
    except Exception as e:
        return [f"#HashtagGenerationFailed"]

HashtagTool = tools.tool(generate_hashtags_tool)

HashtagAgent = Agent(
    role="Hashtag Generator",
    goal="Generate clean and relevant hashtags for social media posts",
    backstory="Social media expert, focusing on impactful hashtags",
    tools=[HashtagTool],
    allow_delegation=False
)



