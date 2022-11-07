"""
utilities
散落於各個function, class中都會用到的function
因為都會用到所以寫在utils.py中, 以利其他class或function做使用
"""
import os

from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_DIR


class Utils:
    def __init__(self) -> None:
        pass


    def create_dir(self):
        # check if DIR exists
        if not os.path.exists(CAPTIONS_DIR):
            os.makedirs(CAPTIONS_DIR)
        if not os.path.exists(VIDEOS_DIR):
            os.makedirs(VIDEOS_DIR)
    
    
    @staticmethod
    def get_video_id_from_url(url):
        return url.split("watch?v=")[-1]
    
    
    def get_caption_fp(self, video_link):
        # get video id
        video_id = self.get_video_id_from_url(video_link)
        # get caption file name
        caption_fn = f"{video_id}_caption_file.txt"
        # get caption file path 
        caption_fp = os.path.join(CAPTIONS_DIR, caption_fn)
        return caption_fp
    