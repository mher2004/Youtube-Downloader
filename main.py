import yt_dlp

# A testing url
URL = 'https://www.youtube.com/watch?v=4afq7e1vPO0'

# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=False)

    # ydl.sanitize_info makes the info json-serializable
    # This prints all the information
    print(f"Hello thank you for requesting the information \n"
          f"Here is some information that you might want to know \n"
          f"ID: {ydl.sanitize_info(info)['id']}\n"
          f"Title: {ydl.sanitize_info(info)['title']}\n"
          f"Duration: {ydl.sanitize_info(info)['duration'] // 60} minutes {ydl.sanitize_info(info)['duration'] % 60} seconds\n"
          f"Channel: {ydl.sanitize_info(info)['channel']}\n"
          f"Resolution: {ydl.sanitize_info(info)['resolution']}\n"
          f"URL: {ydl.sanitize_info(info)['original_url']}\n"
          f"Upload date: {ydl.sanitize_info(info)['upload_date']}\n")
