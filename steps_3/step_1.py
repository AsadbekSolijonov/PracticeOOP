# YouTube Downloader
# pip install pytube

from pytube import YouTube


class Downloader:

    @staticmethod
    def youtube_downloader(video_url, output_url):
        try:
            yt = YouTube(video_url)
            video = yt.streams.get_highest_resolution()
            print(f'Dowmloading: {yt.title}')
            video.download(output_path=output_url)
            print(f'Download complate!')
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    yt_url = 'https://youtu.be/WcDaZ67TVRo?si=ca1YOXYxyvc1iAT5'
    saved_url = '/videos/'
    Downloader.youtube_downloader(video_url=yt_url, output_url=saved_url)
