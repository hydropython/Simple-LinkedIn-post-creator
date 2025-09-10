# agents/social_media.py
from crewai import Agent, tools
from utils.gemini_client import get_client

def social_media_review_tool(platform_post: str, hashtags: list, post_type: str, platform: str) -> str:
    """
    Reviews all previous agent outputs and provides final adjustments.
    - Ensures spacing between ideas
    - Bold important words
    - Adds emojis where appropriate
    - Adds hashtags at the end
    """
    model = get_client()
    prompt = f"""
    Review this post for platform '{platform}' and post type '{post_type}':
    Post content:
    {platform_post}

    Hashtags:
    {' '.join(hashtags)}

    Requirements:
    - Separate ideas with line breaks
    - Bold important words only
    - Add relevant emojis
    - Make it ready-to-publish
    """
    result = model.generate_content(prompt)
    return result.text.strip()

SocialMediaTool = tools.tool(social_media_review_tool)

SocialMediaAgent = Agent(
    role="Social Media Meta Reviewer",
    goal="Review and finalize social media posts after all agents have worked",
    backstory="Expert social media strategist and content reviewer",
    tools=[SocialMediaTool],
    allow_delegation=False
)

