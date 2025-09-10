# agents/platform.py
from crewai import Agent, tools
from utils.gemini_client import get_client

def platform_adapt_tool(post: str, platform: str) -> str:
    """
    Adapts a post for the specific social media platform.
    - LinkedIn: professional tone, structured, 100-150 words
    - Telegram: casual, short, engaging, 50-100 words
    - Facebook: friendly, approachable, 80-120 words
    """
    model = get_client()
    prompt = f"""
    Adapt this post for {platform}:

    Post content:
    {post}

    Requirements:
    - Adjust tone and length for {platform}
    - Keep important ideas clear
    - Add small emojis if appropriate
    """
    result = model.generate_content(prompt)
    return result.text.strip()

PlatformTool = tools.tool(platform_adapt_tool)

PlatformAgent = Agent(
    role="Platform Adaptation Specialist",
    goal="Modify social media posts for platform-specific engagement",
    backstory="Expert in LinkedIn, Telegram, and Facebook content strategies",
    tools=[PlatformTool],
    allow_delegation=False
)
