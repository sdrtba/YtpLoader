import yt_dlp

def download(url):
    ydl_opts = {
        'format': 'ba[ext=m4a]', # bestaudio.m4a
        'paths': {'home': 'output'}, # temp and main files in one folder
        'retries': 10,
        'quiet': True, # without logs
        'progress': True, # show progress bar
        'skip_unavailable_fragments': True,

        #'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.download(url)
            print(info)
    except:
        print('Oops... Slomalsya')


if __name__ == '__main__':
    url = input('link: ')
    #url = 'https://www.youtube.com/watch?v=9f_t9QbjyHc&list=PLMevcTN3zskefoCJ_nZzircZDxNL4UIcv&index=2'
    download(url)
