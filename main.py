import yt_dlp

def download():
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s', # output template to name files as <title>.<ext>
        'paths': {'home': 'output'}, # temp and main files in one folder
        'format': 'ba[ext=m4a]', # bestaudio.m4a
        'retries': 4,
        'quiet': True, # without logs
        'progress': True, # show progress bar
        'skip_unavailable_fragments': True,
	    'noincludeunavailablevideos': True,
	    'ignoreerrors': True,
	    'no_warnings': True,
	    'playliststart': skip,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    url = input('link (pass for https://www.youtube.com/playlist?list=PLcLWzrwuuZhP-qE-ttdWn0x8ANgR8xzpC): ')
    url = url if url != '' else "https://www.youtube.com/playlist?list=PLcLWzrwuuZhP-qE-ttdWn0x8ANgR8xzpC"

    skip = input('skip (pass for 0): ')
    skip = skip if skip != '' else 3

    download()
