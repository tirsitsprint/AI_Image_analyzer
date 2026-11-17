import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

def analyze_image(image, prompt):
    # Check that the API key exists
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API key is missing.")

    # Connect to Gemini
    client = genai.Client(api_key=api_key)

    # Try the request up to 3 times
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=[prompt, image]
            )

            return response.text

        except Exception as error:
            # Retry only when the server is temporarily unavailable
            if "503" in str(error) and attempt < 2:
                time.sleep(5)
            else:
                raise