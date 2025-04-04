# YouTube Video Summarizer

## Overview
This project is a Flask-based web application that extracts transcripts from YouTube videos and generates concise summaries using Natural Language Processing (NLP).

## Features
- **Transcript Extraction:** Retrieves video transcripts using `youtube_transcript_api`.
- **Text Summarization:** Uses Hugging Face's `transformers` pipeline for summarization.
- **Web Interface:** Users can input a YouTube URL and receive a summarized version of the video's transcript.

## Technologies Used
- **Backend:** Flask
- **NLP:** Hugging Face Transformers (for text summarization)
- **APIs:** YouTube Transcript API
- **Libraries:**
  - `Flask`: Web framework
  - `transformers`: NLP model for summarization
  - `youtube_transcript_api`: Extracts video transcripts

## Installation
### Prerequisites
- Python installed (version 3.7 or later)
- `pip` installed

### Steps to Run the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/youtube-video-summarizer.git
   cd youtube-video-summarizer
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```sh
   python app.py
   ```
4. Open `http://127.0.0.1:5000/` in your browser.

## Usage
1. Enter a YouTube video URL into the web interface.
2. The application fetches the transcript and generates a summary.
3. The summarized text is displayed on the page.

## Folder Structure
```
youtube-video-summarizer/
│── static/
│── templates/
│   └── new.html       # Web UI for summarizer
│── app.py             # Flask application
│── requirements.txt   # Required dependencies
```
