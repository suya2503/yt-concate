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
        for video_link in data:
            # create yt object
            source = YouTube(video_link)
            # get caption -> str
            ch_caption = source.captions.get_by_language_code('en')

            ch_caption_convert_to_srt =(ch_caption.generate_srt_captions())

            print(ch_caption_convert_to_srt)
            #save the caption to a file named Output.txt
            # get caption fp
            caption_fp = utils.get_caption_fp(video_link=video_link)
            
            with open(caption_fp, "w") as text_file:
                text_file.write(ch_caption_convert_to_srt)
            break