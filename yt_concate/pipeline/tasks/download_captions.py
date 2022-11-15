"""
download_caption
"""
# built-in module
import os
# pypi module
from pytube import YouTube

# custom module
from .task import Task, TaskException
from yt_concate.settings import CAPTIONS_DIR

class DownloadCaptions(Task):
    def __init__(self) -> None:
        super().__init__()
    
    def process(self, data, config, utils):
        #download the package by:  pip install pytube
        captions_fp = []
        for video_link in data:
            # get caption fp
            caption_fp = utils.get_caption_fp(video_link=video_link)
            # check if file exist
            if utils.check_if_caption_file_exists(video_link):
                print(f'{video_link} caption file exists!!')
                continue
            
            try:
                # create yt object
                source = YouTube(video_link)
                # get caption -> str
                ch_caption = source.captions.get_by_language_code('en')
                ch_caption_convert_to_srt =(ch_caption.generate_srt_captions())
                #save the caption to a file named Output.txt
                with open(caption_fp, "w") as text_file:
                    text_file.write(ch_caption_convert_to_srt)
            except KeyError as e:
                print(f'KeyError exists when downloading captions for url:{video_link}')
                print(e)
                continue
            except AttributeError as e:
                print(f"AttributeError exists when downloading captions for url:{video_link}")
                print(f"No caption in this video for url:{video_link}")
                print(e)
                continue
            # print(ch_caption_convert_to_srt)

            captions_fp.append(caption_fp)
        return data