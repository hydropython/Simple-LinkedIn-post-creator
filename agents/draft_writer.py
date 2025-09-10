from crewai import Agent, tools
from utils.gemini_client import get_client

def draft_post_tool(topic: str) -> str:
    """Generates a raw LinkedIn post draft based on the provided topic."""
    model = get_client()
    prompt = f"Write a LinkedIn post about: {topic}"
    result = model.generate_content(prompt)
    return result.text.strip()

DraftPostTool = tools.tool(draft_post_tool)

DraftWriterAgent = Agent(
    role="LinkedIn Draft Writer",
    goal="Generate raw drafts of LinkedIn posts based on topics or uploaded content.",
    backstory="Professional content strategist for LinkedIn posts.",
    tools=[DraftPostTool],
    allow_delegation=False
)






