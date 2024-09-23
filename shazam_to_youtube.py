import yt_dlp, csv, time, os

def get_unique_songs(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        rows = list(csv.reader(csv_file))[1:]
    unique_songs = {f"{row[2]} by {row[3]}" for row in rows if f"{row[2]} by {row[3]}" != "Title by Artist"}
    return list(unique_songs)

def write_to_file(output_filename, lines):
    with open(output_filename, "w", encoding='utf-8') as file:
        file.writelines(line + "\n" for line in lines)

def get_playlist_video_ids(playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            playlist_data = ydl.extract_info(playlist_url, download=False)
            video_ids = [entry['id'] for entry in playlist_data['entries']]
            return video_ids
    except Exception:
        return []

def search_youtube(query):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_result = ydl.extract_info(f"ytsearch1:{query}", download=False)
        if search_result and 'entries' in search_result:
            return search_result['entries'][0]['id']
    return None

def add_songs_to_playlist(playlist_url, songs):
    existing_video_ids = get_playlist_video_ids(playlist_url)
    if not existing_video_ids:
        return

    songs_to_add_manually = []

    for song in songs:
        song = song.strip()
        video_id = search_youtube(song)

        if not video_id:
            continue

        if video_id in existing_video_ids:
            pass
        else:
            songs_to_add_manually.append(song)

        time.sleep(1)

    if songs_to_add_manually:
        print("\nSongs that can be added manually:")
        for song in songs_to_add_manually:
            print(f"- {song}")
    else:
        print("No songs to be added manually.")

def check_response(response):
    if response.lower() == "yes":
        os.remove("shazamlibrary.csv")
    else:
        pass

if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=PLu8j3ct0xuKGmUbHYL7B48-X_4cOO85k-"
    input_file = "shazamlibrary.csv"
    output_file = "test.txt"
    unique_songs = get_unique_songs(input_file)
    write_to_file(output_file, unique_songs)
    add_songs_to_playlist(playlist_url, unique_songs)
    os.remove("test.txt")
    response = input("Do you want to remove the original csv file? ")
    check_response(response)
