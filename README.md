# Tube2Tune - YouTube to MP3 Downloader

## Introduction
Tube2Tune is a web application that allows users to download YouTube videos as MP3 files. It features a simple and user-friendly interface, making it easy to convert and download audio from YouTube videos.

## Features
- Convert YouTube videos to MP3
- Download MP3 files with a single click
- Responsive design
- SEO optimized

## Requirements
- Flask
- Python 3.x
- `yt-dlp`
- `ffmpeg` 


Note:
To download FFmpeg: https://github.com/BtbN/FFmpeg-Builds/releases
1- Download the ffmpeg-master-latest-win64-gpl-shared.zip file for Windows, or select the appropriate build for your operating system.
2- Unzip the downloaded file.
3- Place the extracted FFmpeg folder inside your project directory.
    
## Installation

1. Clone the repository:
    ```bash
    cd tube2tune
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    flask run
    ```

5. Open your browser and go to `http://127.0.0.1:5000/`

## Usage
- Enter the YouTube video URL in the input field.
- Click "Download" to start the conversion process.
- Once the MP3 file is ready, click "Download Ready!" to save the file to your device.

## Troubleshooting
- If you encounter any issues, make sure all dependencies are installed correctly.
- Check the console for error messages and refer to the documentation.

## Changelog
- **v1.0**: Initial release

## License
This project is licensed under the MIT License - see the LICENSE file for details.
