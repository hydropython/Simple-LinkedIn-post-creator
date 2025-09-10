import os
import openai
from PIL import Image
from io import BytesIO

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt: str, size: str = "512x512") -> Image.Image:
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=size
    )
    image_url = response['data'][0]['url']
    return Image.open(BytesIO(openai.Image.retrieve(image_url).content))