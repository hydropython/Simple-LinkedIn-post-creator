# agents/post_type.py
from crewai import Agent, tools
from utils.gemini_client import get_client

def classify_post_type_tool(post: str) -> str:
    """
    Classifies a social media post into one of the main types:
    - Promotional
    - Inspirational/Motivational
    - Educational/Informative
    - Engagement/Interactive
    - Behind-the-Scenes / Personal Stories
    - News/Updates
    - User-Generated Content / Testimonials
    - Entertaining/Fun
    Returns post type as string.
    """
    model = get_client()
    prompt = f"""
    Analyze this post and classify it into one of these types:
    Promotional, Inspirational/Motivational, Educational/Informative, Engagement/Interactive,
    Behind-the-Scenes / Personal Stories, News/Updates, User-Generated Content / Testimonials, Entertaining/Fun.

    Post content:
    {post}
    """
    result = model.generate_content(prompt)
    return result.text.strip()

PostTypeTool = tools.tool(classify_post_type_tool)

PostTypeAgent = Agent(
    role="Post Type Classifier",
    goal="Determine the type of social media post for better adaptation",
    backstory="Social media analyst specializing in content classification",
    tools=[PostTypeTool],
    allow_delegation=False
)
