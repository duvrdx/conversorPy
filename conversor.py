from PySimpleGUI.PySimpleGUI import Window
import pytube
from pytube import YouTube
from pytube import Playlist
from PySimpleGUI import PySimpleGUI as sg

def main():
    #Layout
    sg.theme('Reddit')
    layout =[
        [sg.Radio('Vídeo',"RAD01", key="v"),sg.Radio('Playlist',"RAD01", key="p")],
        [sg.Text('Link'), sg.Input(key='link')],
        [sg.Radio('MP3', "RAD02", key='m3'),sg.Radio('MP4',"RAD02", key='m4')],
        [sg.Button('Baixar')],
        [sg.Text('', key='status')]
    ]
    #Janela
    janela = sg.Window('YouDownload', layout)

    #Ler os eventos
    c = True

    while c:
        eventos, valores = janela.read()

        if eventos == sg.WINDOW_CLOSED:
            c = False
        if eventos == 'Baixar':
            s = 0
            if valores['link'] != "":
                if valores['v'] == True:
                    link = valores['link']
                    yt = YouTube(link)

                    if valores['m3']:
                        print(f'Downloading: {yt.title}')
                        janela.find_element('status').Update(value=(f'Downloading: {yt.title}'))
                        ys = yt.streams.get_audio_only()
                        ys.download(output_path="audio")
                        janela.find_element('status').update(value=f"Download Concluido: {yt.title}")

                    if valores['m4']:
                        print(f'Downloading: {yt.title}')
                        janela.find_element('status').Update(value=(f'Downloading: {yt.title}'))
                        ys = yt.streams.get_highest_resolution()
                        ys.download(output_path="video")
                        janela.find_element('status').update(value=f"Download Concluido: {yt.title}")

                if valores['p'] == True:
                    link = valores['link']
                    p = Playlist(link)

                    if valores['m3']:
                        print(f'\nDownloading: {p.title}')
                        janela.find_element('status').Update(value=(f'\nDownloading: {p.title}'))
                        for url in p.video_urls:
                            try:
                                yt = YouTube(url)
                            except pytube.exceptions.VideoUnavailable:
                                print(f'\nVideo {url} is unavaialable, skipping.')
                                janela.find_element('status').Update(value=(f'\nVideo {url} is unavaialable, skipping.'))
                            else:
                                yt.streams.get_audio_only().download(output_path="audio")
                                janela.find_element('status').update(value=f"Download Concluido: {p.title}'")

                    if valores['m4']:
                        print(f'\nDownloading: {p.title}')
                        janela.find_element('status').Update(value=(f'\nDownloading: {p.title}'))
                        for url in p.video_urls:
                            try:
                                yt = YouTube(url)
                            except pytube.exceptions.VideoUnavailable:
                                print(f'\nVideo {url} is unavaialable, skipping.')
                                janela.find_element('status').Update(value=(f'\nVideo {url} is unavaialable, skipping.'))
                            else:
                                yt.streams.get_audio_only().download(output_path="video")
                                janela.find_element('status').update(value=f"Download Concluido: {p.title}")  

            else:
                janela.find_element('status').update(value="Insira o Link!")



if __name__ == "__main__":
    main()