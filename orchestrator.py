# orchestrator.py
from agents.draft_writer import DraftWriterAgent
from agents.refiner import RefinerAgent
from agents.hashtags import HashtagAgent
from agents.post_type import PostTypeAgent
from agents.platform import PlatformAgent
from agents.social_media import SocialMediaAgent

def generate_social_post(
    content: str,
    platform: str = "LinkedIn",
    styles=["Storytelling, Professional, Engaging"],
    post_type: str = None  # optional user-selected post type
):
    """
    Orchestrates multiple agents to generate a polished social media post.
    """
    # 1️⃣ Draft
    draft = DraftWriterAgent.tools[0].func(content)

    # 2️⃣ Refine
    refined = RefinerAgent.tools[0].func(draft, styles)

    # 3️⃣ Hashtags
    hashtags = HashtagAgent.tools[0].func(refined)

    # 4️⃣ Post type (use user-selected if provided)
    if not post_type:
        post_type = PostTypeAgent.tools[0].func(refined)

    # 5️⃣ Platform adaptation
    platform_post = PlatformAgent.tools[0].func(refined, platform)

    # 6️⃣ Meta-review by SocialMediaAgent
    final_post = SocialMediaAgent.tools[0].func(platform_post, hashtags, post_type, platform)

    return {
        "draft": draft,
        "refined": refined,
        "hashtags": hashtags,
        "post_type": post_type,
        "platform_post": platform_post,
        "final_post": final_post
    }













