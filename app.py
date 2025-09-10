import streamlit as st
import pandas as pd
from orchestrator import generate_social_post  # updated function name

st.set_page_config(page_title="Social Media Post Generator", page_icon="💡")
st.title("💡 Multi-Agent Social Media Post Generator")

st.write("Choose **one** input method to generate your post:")

# ---------------------------
# Input method
# ---------------------------
input_method = st.radio(
    "Select input type:",
    ("Enter a topic", "Paste your content", "Upload a content file")
)

topic = ""
file_content = ""

if input_method == "Enter a topic":
    topic = st.text_input("Enter your topic:")
elif input_method == "Paste your content":
    file_content = st.text_area("Paste your content here:", placeholder="Copy and paste your content...")
elif input_method == "Upload a content file":
    uploaded_file = st.file_uploader("Upload a TXT or CSV file:", type=["txt", "csv"])
    if uploaded_file:
        if uploaded_file.type == "text/plain":
            file_content = uploaded_file.read().decode("utf-8")
        elif uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file)
            file_content = " ".join(df.select_dtypes(include="object").astype(str).agg(" ".join, axis=1))

# ---------------------------
# Social media selection
# ---------------------------
social_media = st.selectbox(
    "Select target social media:",
    ("LinkedIn", "Telegram", "Facebook")
)

# ---------------------------
# Style selection
# ---------------------------
post_styles = st.multiselect(
    "Select refinement style(s):",
    ["Storytelling, Professional, Engaging", "Bullet + Bold + Emoji"],
    default=["Storytelling, Professional, Engaging"]
)
post_type = st.selectbox(
    "Select the type of your post:",
    [
        "Promotional",
        "Inspirational/Motivational",
        "Educational/Informative",
        "Engagement/Interactive",
        "Behind-the-Scenes / Personal Stories",
        "News/Updates",
        "User-Generated Content / Testimonials",
        "Entertaining/Fun"
    ]
)
# ---------------------------
# Generate button
# ---------------------------
if st.button("Generate Post"):
    if not topic and not file_content:
        st.warning("Please enter a topic, paste content, or upload a content file.")
    else:
        prompt_input = topic if topic else file_content
        
        with st.spinner("🚀 Generating your social media post..."):
            result = generate_social_post(
                content=prompt_input,
                platform=social_media,
                styles=post_styles,
                post_type=post_type  # <-- pass user-selected type
            )

        st.subheader("✨ Refined Post")
        refined_paragraphs = result["refined"].split("\n\n")
        for para in refined_paragraphs:
            st.write(para)

        st.subheader("📌 Hashtags")
        # Format hashtags nicely
        formatted_hashtags = " ".join([f"#{tag}" for tag in result["hashtags"]])
        st.write(formatted_hashtags)

        st.subheader(f"🌐 Final {social_media} Post")
        final_paragraphs = result["platform_post"].split("\n\n")
        for para in final_paragraphs:
            st.write(para)