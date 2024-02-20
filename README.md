# Lyrics Extractor

Lyrics Extractor is a Python script that extracts lyrics from audio files and exports them to LRC (Lyrics) files.

## Overview

This script scans a specified directory for audio files and extracts the lyrics metadata from them. It supports various audio formats, including FLAC, MP3, and more, using the Mutagen library. The extracted lyrics are then exported to LRC files for easy viewing and synchronization with music players that support LRC format.

## Features

- Extracts lyrics from audio files in various formats
- Supports FLAC, MP3, and other formats through the Mutagen library
- Exports lyrics to LRC files for easy viewing and synchronization

## Usage

1. Install Python on your system if you haven't already.
2. Clone or download the Lyrics Extractor project from GitHub.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Create a CSV file named `lib.csv` listing the directories containing your audio files.
5. Run the script using `python main.py`.

## Requirements

- Python 3.x
- Mutagen library (automatically installed via `requirements.txt`)

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on GitHub or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
