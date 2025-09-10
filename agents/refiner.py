from crewai import Agent, tools
from utils.gemini_client import get_client

def refine_post_tool(draft: str, styles: list = ["Storytelling, Professional, Engaging"]) -> str:
    """
    Refines a LinkedIn/social media post to be highly engaging:
    - Paragraph breaks between ideas
    - Bold only key words/phrases
    - 1-2 relevant emojis per paragraph
    - Maintain professional storytelling style
    """
    model = get_client()
    try:
        prompts = []
        if "Storytelling, Professional, Engaging" in styles:
            prompts.append(
                "Refine this draft into a professional LinkedIn post, 100-150 words. "
                "Separate each main idea into its own paragraph. "
                "Bold only the most important words/phrases. "
                "Add 1–2 relevant emojis per paragraph matching the idea. "
                "Make it highly engaging, readable, and persuasive."
            )
        if "Bullet + Bold + Emoji" in styles:
            prompts.append(
                "Rewrite the draft using bullets, bold key points, and 1–2 emojis per bullet."
            )

        combined_prompt = f"Original draft:\n{draft}\n\n" + "\n\n".join(prompts)
        result = model.generate_content(combined_prompt)

        # Ensure paragraph breaks are preserved
        refined_text = "\n\n".join([p.strip() for p in result.text.split("\n") if p.strip()])
        return refined_text
    except Exception as e:
        return f"Refinement failed: {e}"

RefinePostTool = tools.tool(refine_post_tool)

RefinerAgent = Agent(
    role="LinkedIn Post Refiner",
    goal="Polish and style LinkedIn posts to 10/10 quality.",
    backstory="Expert LinkedIn editor focused on readability, impact, and engagement.",
    tools=[RefinePostTool],
    allow_delegation=False
)










