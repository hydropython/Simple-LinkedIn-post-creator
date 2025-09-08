import streamlit as st
from agents.draft_writer import draft_post
from agents.refiner import refine_post
from agents.hashtags import generate_hashtags

st.set_page_config(page_title="LinkedIn Post Generator (Gemini)", page_icon="💡")
st.title("💡 Multi-Agent LinkedIn Post Generator with Gemini")

topic = st.text_input("Enter a topic for your LinkedIn post:")

if st.button("Generate Post"):
    if not topic:
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Generating draft..."):
            draft = draft_post(topic)

        with st.spinner("Refining draft..."):
            refined = refine_post(draft)

        with st.spinner("Adding hashtags..."):
            hashtags = generate_hashtags(refined)

        st.subheader("✨ Final LinkedIn Post")
        st.write(refined)
        st.subheader("📌 Suggested Hashtags")
        st.write(hashtags)

