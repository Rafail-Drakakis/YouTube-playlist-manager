## YouTube Playlist Manager

### Description:
This Python script helps you manage your YouTube playlist by processing songs from a CSV file (like a Shazam library) and checking whether they already exist in a specified YouTube playlist. It extracts unique songs from the CSV file, checks whether they are present in the YouTube playlist, and outputs a list of songs that need to be manually added to the playlist. It also includes an option to delete the original CSV file after processing.

### Features:
- Extracts unique songs from a CSV file.
- Checks for duplicate entries in a given YouTube playlist.
- Outputs songs that need to be manually added to the playlist.
- Provides an option to delete the CSV file after processing.

### Prerequisites:
To run this project, you'll need to install the following Python packages:
- `yt-dlp`
- `csv`
- `os`
- `time`

To install `yt-dlp`, use:
```bash
pip install yt-dlp
```

### Installation:
1. Clone this repository or download the script file.
2. Ensure you have Python 3 installed.
3. Install the required package `yt-dlp` using pip:
   ```bash
   pip install yt-dlp
   ```

### How to Use:
1. **Prepare a CSV file**: The CSV file (`shazamlibrary.csv`) should have songs listed with their title and artist information. Ensure it's formatted correctly, with the song title in the third column and the artist name in the fourth column.

2. **Specify the Playlist URL**: Replace the `playlist_url` in the script with the URL of your YouTube playlist.

3. **Run the Script**:
   Run the script using:
   ```bash
   python script_name.py
   ```
   This will:
   - Extract unique songs from the CSV.
   - Check the songs against the YouTube playlist.
   - Output any songs that need to be manually added.

4. **Delete the CSV file (optional)**:
   After processing, you will be asked if you want to delete the original CSV file:
   ```bash
   Do you want to remove the original csv file? [yes/no]
   ```

### Example:
1. You have a CSV file named `shazamlibrary.csv` with the following format:
   | Column 1 | Column 2 | **Title** | **Artist** |
   |----------|-----------|-----------|------------|
   | ...      | ...       | Song1     | Artist1    |
   | ...      | ...       | Song2     | Artist2    |

2. The script processes this CSV and checks the songs against the YouTube playlist provided in `playlist_url`.

3. If a song is not in the playlist, it will be listed under "Songs that can be added manually."

### Script Components:
- **get_unique_songs(file_path)**: Extracts unique song titles and artists from the CSV file.
- **write_to_file(output_filename, lines)**: Writes the list of unique songs to an output file.
- **get_playlist_video_ids(playlist_url)**: Retrieves all video IDs from the specified YouTube playlist.
- **search_youtube(query)**: Searches for the song on YouTube and returns the first video ID.
- **add_songs_to_playlist(playlist_url, songs)**: Checks if songs are already in the playlist and outputs a list of those that need to be manually added.
- **check_response(response)**: Deletes the CSV file based on user input.

### Notes:
- This script does **not** automatically add songs to the YouTube playlist. Instead, it lists songs that should be manually added.
- The script uses `yt-dlp` to interact with YouTube and search for songs, so ensure that `yt-dlp` is installed and working correctly.

### License:
This project is open-source and free to use.

