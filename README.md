# YouTube Audio Summarizer

This is a simple Gradio app that allows you to input a YouTube URL, download its audio, transcribe it, and generate a summary of the content using the Hugging Face Transformers library.

## Prerequisites

Make sure you have the following dependencies installed:
- `yt_dlp`
- `scipy`
- `numpy`
- `transformers`
- `gradio`


## You can install them using the following command:
```
pip install youtube_dl scipy numpy transformers gradio
```
## How to Use

1. Clone this repository to your local machine:
```
git clone https://github.com/nikhilkoche/youtube_summarizer.git
```

2. Navigate to the cloned repository:
```
cd youtube-audio-summarizer
```
3. Run the Gradio app:
```
python app.py

```

4. Open a web browser and go to http://localhost:7860. You will see an input box where you can enter a YouTube URL.

5. Enter a valid YouTube URL in the input box and press Enter.

6. The app will process the audio, transcribe it, and provide a summary of the content.

