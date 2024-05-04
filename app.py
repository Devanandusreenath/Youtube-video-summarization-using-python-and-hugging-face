from flask import Flask, render_template, request
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if 'youtube.com' in url:
            video_i = extract_youtube_id(url)
            video_id=url.split("=")[1]
            print(video_id)
            from IPython.display import YouTubeVideo
            YouTubeVideo(video_id)

            YouTubeTranscriptApi.get_transcript(video_id)

            transcript=YouTubeTranscriptApi.get_transcript(video_id)
            print(transcript)
            print(transcript[0:5])

            result = ""
            for i in transcript:
                result=result+' '+i['text']
            print(result)
            print(len(result))

            summarizer = pipeline('summarization')

            num_iters = int(len(result)/1000)
            summarized_text=[]

            for i in range(0,num_iters+1):
                start=0
                start=i * 1000
                end = (i + 1)*1000
                out=summarizer(result[start:end])
                out=out[0]
                out=out['summary_text']
                summarized_text.append(out)
    
           #print(summarized_text)
            summary=str(summarized_text)
            return render_template('new.html', video_id=video_i,summary=summary)
        else:
            return 'Invalid video link'
    return render_template('new.html')

def extract_youtube_id(url):
    video_id = url.split('v=')[-1]
    return video_id.split('&')[0]

if __name__ == '__main__':
    app.run(debug=True)