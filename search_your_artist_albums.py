import requests

def search_artist_albums():
    artist_name = input("Enter Artist name: ").strip()

    if not artist_name:
        print("Artist name cannot be empty.")
        return

    parameters = {
        "term": artist_name,
        "entity": "musicTrack",
        "limit": 200
    }

    try:
        response = requests.get("https://itunes.apple.com/search", params=parameters, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return

    py_data = response.json()

    if "results" not in py_data or len(py_data["results"]) == 0:
        print(f"No results found for artist: {artist_name}")
        return

    albums = {}

    for track in py_data["results"]:
        album = track.get("collectionName")
        date = track.get("releaseDate")

        if not album or not date:
            continue

        if album not in albums:
            albums[album] = date

    if not albums:
        print(f"No albums found for artist: {artist_name}")
        return

    print(f"\n{artist_name.upper()} <{len(albums)}> unique albums found on  iTunes:\n")

    albums = dict(sorted(albums.items(), key=lambda x:x[1], reverse=True))

    for num, album in enumerate(albums.items()):
        print(f"{num + 1:>3}. {album[0]}. \033[90mRelease date: {album[1][:10]}\033[0m")

    print(f"\nThank you for choosing  Apple iTunes")

if __name__ == "__main__":
    search_artist_albums()
