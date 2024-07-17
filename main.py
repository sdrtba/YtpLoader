import yt_dlp

def download(url):
    ydl_opts = {
        'format': 'ba[ext=m4a]', # bestaudio.m4a
        'paths': {'home': 'output'}, # temp and main files in one folder
        'retries': 10,
        'quiet': True, # without logs
        'progress': True, # show progress bar
        'skip_unavailable_fragments': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
    except:
        print('Oops...')


if __name__ == '__main__':
    #url = input('link: ')
    url = "https://www.youtube.com/playlist?list=PLcLWzrwuuZhNet5VdtPJBV-K0WDcRSvhJ"
    download(url)
