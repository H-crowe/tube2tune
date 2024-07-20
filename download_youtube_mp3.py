import os
from pytube import YouTube

def download_youtube_video_as_mp3(youtube_url, output_path):
    try:
        # Ensure output path exists
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        yt = YouTube(youtube_url)
        video = yt.streams.filter(only_audio=True).first()
        
        if not video:
            print("No audio stream available")
            return
        
        out_file = video.download(output_path=output_path)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        
        # Check if the new file already exists
        if os.path.exists(new_file):
            print(f"File {new_file} already exists.")
            return
        
        os.rename(out_file, new_file)
        print(f"Downloaded and converted to MP3: {new_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    youtube_url = input("Enter the YouTube URL: ").strip()
    output_path = input("Enter the output path: ").strip()
    
    if not youtube_url:
        print("YouTube URL cannot be empty.")
    elif not output_path:
        print("Output path cannot be empty.")
    else:
        download_youtube_video_as_mp3(youtube_url, output_path)
