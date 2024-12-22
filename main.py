from yt_dlp import YoutubeDL

def download(url, skip, cookies):
    current_url = None

    def hook(d):
        nonlocal current_url
        if d['status'] == 'downloading':
            current_url = d.get('info_dict', {}).get('webpage_url')
        if d['status'] == 'finished':
            song_title = d.get('info_dict', {}).get('title', None)
            if song_title:
                with open('songs.txt', 'a', encoding="utf-8") as ds_f:
                    ds_f.write(song_title + '\n')

    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'paths': {'home': 'output'},
        'format': 'ba[ext=m4a]',
        'retries': 4,
        'quiet': False,
        'progress_hooks': [hook],
        'skip_unavailable_fragments': True,
        'no_warnings': True,
        'ignoreerrors': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'playliststart': skip,
        'cookiefile': cookies,
        'download_archive': 'archive.txt',
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        with open('error.txt', 'a', encoding="utf-8") as e_f:
            e_f.write("-----------------------------------------\n")
            e_f.write(f"URL текущей песни: {current_url}\n")
            e_f.write(f"Ошибка: {e}\n")


if __name__ == '__main__':
    url = input('link (pass for https://www.youtube.com/playlist?list=PLcLWzrwuuZhP-qE-ttdWn0x8ANgR8xzpC): ')
    url = url if url != '' else "https://www.youtube.com/playlist?list=PLcLWzrwuuZhP-qE-ttdWn0x8ANgR8xzpC"

    skip = input('skip (pass for 0): ')
    skip = skip if skip != '' else 3

    cookies_path = 'cookies.txt'

    download(url, skip, cookies_path)
