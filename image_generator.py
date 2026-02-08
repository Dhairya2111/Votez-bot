import requests
import os
import sys

def generate_image(prompt, filename="priya_stunning.png"):
    """
    This script uses the Stability AI API (or similar) to generate the requested image.
    Note: You need an API key from stability.ai to run this.
    """
    api_host = "https://api.stability.ai"
    api_key = os.getenv("STABILITY_API_KEY")

    if not api_key:
        print("Error: STABILITY_API_KEY environment variable not set.")
        return

    print(f"Generating image for prompt: {prompt[:50]}...")

    response = requests.post(
        f"{api_host}/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "text_prompts": [
                {
                    "text": prompt,
                    "weight": 1
                },
                {
                    "text": "blurry, distorted, low quality, cartoon, drawing, anime",
                    "weight": -1
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )

    if response.status_code != 200:
        print(f"Error from API: {response.text}")
        return

    data = response.json()

    for i, image in enumerate(data["artifacts"]):
        with open(filename, "wb") as f:
            import base64
            f.write(base64.b64decode(image["base64"]))
    
    print(f"Success! Image saved as {filename}")

if __name__ == "__main__":
    target_prompt = "A beautiful, bold, and stunning Indian girl with long wavy hair, wearing a deep neck red saree with a sleeveless blouse, sitting on a bed in a dimly lit bedroom. She has a seductive expression, looking directly at the camera, biting her lower lip slightly. High quality, realistic, cinematic lighting, 4k."
    generate_image(target_prompt)