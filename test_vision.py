
# Import Pillow and our AI function
from PIL import Image
from vision import analyze_image

# Open a sample image
image = Image.open("sample.jpg")

# Write an instruction for Gemini
prompt = "Identify all the important visible objects. Present your answer as a bullet list."

# Ask Gemini to analyze the image
result = analyze_image(image, prompt)

# Display the AI response
print("\nGemini's response:")
print(result)
