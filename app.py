from flask import Flask, request, render_template, send_file, abort, make_response
import os
import yt_dlp
import configparser
import logging

# Setup Flask application
app = Flask(__name__)

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')
ffmpeg_path = config.get('Paths', 'ffmpeg_path', fallback=os.path.join(os.getcwd(), 'ffmpeg', 'bin', 'ffmpeg.exe'))

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_youtube_video_as_mp3(youtube_url, output_path):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': ffmpeg_path,
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }
        logging.info(f'Started downloading {youtube_url}')
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=True)
            filename = ydl.prepare_filename(info_dict)
            base, ext = os.path.splitext(filename)
            mp3_file = base + '.mp3'
            if os.path.exists(mp3_file):
                logging.info(f'Successfully converted to MP3: {mp3_file}')
                return mp3_file, os.path.basename(mp3_file), None
            else:
                logging.error(f'Failed to convert to MP3')
                return None, None, "Failed to convert to MP3"
    except Exception as e:
        logging.error(f'Error: {str(e)}')
        return None, None, str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        youtube_url = request.form['youtube_url']
        if not youtube_url.startswith("https://www.youtube.com/watch?v="):
            return render_template('index.html', message="Invalid YouTube URL")

        output_path = './downloads'
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        file_path, filename, error = download_youtube_video_as_mp3(youtube_url, output_path)
        if file_path:
            try:
                response = make_response(send_file(file_path, as_attachment=True))
                response.headers['X-Filename'] = filename
                return response
            except FileNotFoundError:
                abort(404, description="File not found")
        else:
            return render_template('index.html', message=f"Error: {error}")

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # You can add logic to handle form submission here, e.g., send an email or save to a database
        return render_template('contact.html', message="Thank you for your message!")
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(port=5000)
