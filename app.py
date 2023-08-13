import yt_dlp
import ffmpeg
import gradio as gr
from transformers import pipeline

# Define the download function
def download_from_url(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    ydl.download([url])
    
    info = ydl.extract_info(url, download=False) 
    video_title = info['title']
    video_id = url.split('/')[-1]
    formatted_video_id = f"[{video_id}]"
    # Load the speech-to-text pipeline
    model = "facebook/wav2vec2-large-960h-lv60-self"
    pipe = pipeline(model=model)
    #audio_file_name = audio_file[0]
    stream = ffmpeg.input('output.m4a')
    stream = ffmpeg.output(stream, 'output.wav')
    #ffmpeg.run(stream)

    # Perform speech-to-text
    text = pipe(f"{video_title} {formatted_video_id}.wav", chunk_length_s=10)
    #text = pipe(stream, chunk_length_s=10)
    #transcribed_text = text[0]['text']
    transcribed_text = text['text']
    #pp = pipeline('summarization') # this works
    #output = pp(transcribed_text,max_length = 100, min_length =20,do_sample=False)
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    #tokenizer_kwargs = {'truncation':True,'max_length':512}
    text_summerization = summarizer(transcribed_text, max_length=130, min_length=30, do_sample=False)
    return text_summerization


# Define the input and output interfaces
#input_interface = gr.Interface(fn=transcribe_audio,inputs=gr.inputs.Audio(label="Upload your audio file"),outputs="text")
input_interface = gr.Interface(fn=download_from_url,inputs=gr.inputs.Textbox(label="url here"),outputs="text")

# Run the Gradio interface
if __name__ == "__main__":
    input_interface.launch()