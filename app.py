
# Import the libraries we need
from image_processor import prepare_image
import streamlit as st
from PIL import Image
from vision import analyze_image

# Configure the Streamlit page
st.set_page_config(
    page_title="AI Image Analyzer",
    page_icon="🔍",
    layout="wide"
)

# Display the application heading
st.title("🔍 AI Image Analyzer")
st.write("Upload an image and let AI understand what is inside it.")

st.divider()

# Let the user upload an image
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png", "webp"]
)

# Continue only if an image has been uploaded
if uploaded_file is not None:

    # Read the uploaded image and convert it to RGB
    original_image = Image.open(uploaded_file)
    image = prepare_image(original_image)
    # Create two columns for the image and its information
    left, right = st.columns(2)

    with left:
        st.subheader("Your Image")
        st.image(image, use_container_width=True)

    with right:
        st.subheader("Image Information")
        st.write(f"Width: {image.width} pixels")
        st.write(f"Height: {image.height} pixels")
        st.write(f"Image format: {uploaded_file.type}")

    st.divider()

    # Let the user select an analysis task
    st.subheader("Choose an Analysis Task")

    task = st.selectbox(
        "What would you like the AI to do?",
        [
            "Image Captioning",
            "Object Identification",
            "Scene Understanding",
            "Visual Question Answering"
        ]
    )

    # Prepare prompts for each task
    prompts = {
        "Image Captioning":
            "Describe this image clearly and accurately.",

        "Object Identification":
            "Identify the main visible objects in this image and explain what they are.",

        "Scene Understanding":
            "Explain what is happening in this image, including the environment and context."
    }

    # Ask for a question if the user selects Visual Question Answering
    if task == "Visual Question Answering":
        question = st.text_input(
            "Ask a question about your image:",
            placeholder="Example: What objects can you see?"
        )
        prompt = question

    else:
        prompt = prompts[task]

    # Start analysis when the button is clicked
    if st.button("Analyze Image", type="primary"):

        if not prompt.strip():
            st.warning("Please enter a question first.")

        else:
            try:
                # Show a loading message while Gemini works
                with st.spinner("AI is analyzing your image..."):

                    result = analyze_image(image, prompt)

                # Display the result
                st.subheader("AI Analysis Result")
                st.success("Analysis completed!")
                st.write(result)

            except Exception as error:
                error_message = str(error)

    if "503" in error_message or "UNAVAILABLE" in error_message:
        st.warning(
            "Gemini is temporarily busy. Please try again shortly."
        )

    elif "429" in error_message:
        st.warning(
            "API request limit reached. Please wait before trying again."
        )

    else:
        st.error(f"Something went wrong: {error_message}")
else:
    st.info("Upload an image to get started.")
