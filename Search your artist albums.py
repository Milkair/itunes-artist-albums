import requests

def search_artist_albums():
    artist_name = input("Enter Artist name: ").strip()

    if not artist_name:
        print("❌ Artist name cannot be empty.")
        return

    parameters = {
        "term": artist_name,
        "entity": "musicTrack",
        "limit": 200
    }

    try:
        response = requests.get("https://itunes.apple.com/search", params=parameters, timeout=10)
        response.raise_for_status()  # catches HTTP errors
    except requests.exceptions.RequestException as e:
        print("❌ Network error:", e)
        return

    py_data = response.json()

    if "results" not in py_data or len(py_data["results"]) == 0:
        print(f"❌ No results found for artist: {artist_name}")
        return

    ken_carson_albums = {}

    for track in py_data["results"]:
        album = track.get("collectionName")
        date = track.get("releaseDate")

        if not album or not date:
            continue

        if album not in ken_carson_albums:
            ken_carson_albums[album] = date

    if not ken_carson_albums:
        print(f"❌ No albums found for artist: {artist_name}")
        return

    print(f"\n✅ {artist_name} unique albums found on iTunes:\n")

    ken_carson_albums = dict(sorted(ken_carson_albums.items(), key=lambda x:x[1], reverse=True))

    count = 1
    for album, date in ken_carson_albums.items():
        print(f"{count:>2}. {album} — {date}")
        count += 1

if __name__ == "__main__":
    search_artist_albums()
