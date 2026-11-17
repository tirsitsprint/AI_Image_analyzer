# AI Image Analyzer

## Overview

AI Image Analyzer is a Python-based application that uses Google's Gemini Vision API to analyze images.

Users can upload images, generate descriptions, identify visible objects, understand scenes, and ask questions about uploaded images.

## Features

- Image upload and preview
- Image captioning
- Object identification
- Scene understanding
- Visual question answering
- Image preprocessing using Pillow
- AI-powered analysis using Gemini

## Technologies

- Python
- Streamlit
- Google Gemini API
- Pillow
- python-dotenv

## Project Structure

```text
aimage/
│
├── app.py
├── vision.py
├── image_processor.py
├── test_vision.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository.
2. Create a virtual environment.
3. Install the dependencies.
4. Configure your Gemini API key.

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Never publish your real API key.

## Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal.

## Learning Objectives

This project demonstrates:

- Image processing with Python
- Working with APIs
- Multimodal AI
- Prompt engineering
- Environment variables
- Building interfaces with Streamlit

## Future Improvements

- Object detection with bounding boxes
- Downloadable analysis reports
- Analysis history
- Support for additional AI models

## Author

Developed as a practical learning project in Python and Vision AI.