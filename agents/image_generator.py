import os
import requests
from PIL import Image
from io import BytesIO
import base64

API_KEY = os.getenv("GEN_API_KEY")  # make sure your .env has GEN_API_KEY

def generate_image(prompt: str, size: str = "512x512") -> Image.Image:
    """
    Generate an AI image based on the refined LinkedIn post content.
    """

    url = "https://generativelanguage.googleapis.com/v1beta2/images:generate"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {
        "model": "image-bison-001",
        "prompt": prompt,
        "size": size
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    img_b64 = response.json()["data"][0]["b64_json"]
    img_bytes = base64.b64decode(img_b64)
    return Image.open(BytesIO(img_bytes))



