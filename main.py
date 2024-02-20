import os
import csv
from mutagen import File

def get_all_file_paths(directory):
    file_paths = []
    try:
        for entry in os.scandir(directory):
            if entry.is_file() and not entry.name.endswith(".lrc"):
                file_paths.append(entry.path)
    except OSError as ex:
        print("Error:", ex)
    return file_paths

def export_lyrics_as_lrc(lyrics, filename):
    try:
        with open(filename, "w") as outfile:
            outfile.write(lyrics)
        print("Lyrics exported to", filename, "successfully.")
    except IOError as ex:
        print("Error:", ex)

def read_csv(filename):
    values = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                values.extend(row)
    except FileNotFoundError:
        print("File doesn't exist. Creating a new file.\nPlace all the directories you want to scan in lib.csv.")
        open(filename, 'a').close()
    except IOError as ex:
        print("Error:", ex)
    return values if values else []

def main():
    lib = read_csv("lib.csv")

    for directory in lib:
        files = get_all_file_paths(directory)
        for file in files:
            filename = file + ".lrc"
            # Use Mutagen to extract metadata tags
            try:
                audio = File(file)
                if "lyrics" in audio:
                    lyrics = audio["lyrics"][0]
                    export_lyrics_as_lrc(lyrics, filename.replace('.flac', ''))
            except Exception as e:
                print(f"Error extracting metadata from {file}: {e}")

if __name__ == "__main__":
    main()
