# import json
import yt_dlp

URL = 'https://www.youtube.com/watch?v=4afq7e1vPO0'

# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=False)

    # ℹ️ ydl.sanitize_info makes the info json-serializable
    # information =
    print(f"Hello thank you for requesting the information \n"
          f"Here is some information that you might want to know \n"
          f"ID: {ydl.sanitize_info(info)['id']}\n"
          f"Title: {ydl.sanitize_info(info)['title']}\n"
          f"Duration: {ydl.sanitize_info(info)['duration']//60} minutes {ydl.sanitize_info(info)['duration']%60} seconds\n"
          f"Channel: {ydl.sanitize_info(info)['channel']}\n"
          f"Resolution: {ydl.sanitize_info(info)['resolution']}\n"
          f"URL: {ydl.sanitize_info(info)['original_url']}\n"
          f"Upload date: {ydl.sanitize_info(info)['upload_date']}\n")

# dict_keys(
#     ['id', 'title', 'formats', 'thumbnails',
#     'thumbnail', 'description', 'channel_id',
#     'channel_url', 'duration',
#      'view_count', 'average_rating', 'age_limit',
#      'webpage_url', 'categories', 'tags', 'playable_in_embed',
#      'live_status', 'media_type', 'release_timestamp',
#      '_format_sort_fields', 'automatic_captions', 'subtitles',
#      'comment_count', 'chapters', 'heatmap', 'like_count',
#      'channel', 'channel_follower_count', 'uploader',
#      'uploader_id', 'uploader_url', 'upload_date',
#      'timestamp', 'availability', 'original_url',
#      'webpage_url_basename', 'webpage_url_domain',
#      'extractor', 'extractor_key', 'playlist', 'playlist_index',
#      'display_id', 'fulltitle', 'duration_string',
#      'release_year', 'is_live', 'was_live', 'requested_subtitles',
#      '_has_drm', 'epoch', 'requested_formats',
#      'format', 'format_id', 'ext', 'protocol',
#      'language', 'format_note',
#      'filesize_approx', 'tbr', 'width', 'height',
#      'resolution', 'fps', 'dynamic_range', 'vcodec', 'vbr',
#      'stretched_ratio', 'aspect_ratio', 'acodec',
#      'abr', 'asr', 'audio_channels', '_type', '_version'])


# import yt_dlp
#
# URLS = ['https://www.youtube.com/watch?v=4afq7e1vPO0']
#
# ydl_opts = {
#     'format': 'm4a/bestaudio/best',
#     # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
#     'postprocessors': [{  # Extract audio using ffmpeg
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'm4a',
#     }]
# }
#
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     error_code = ydl.download(URLS)
