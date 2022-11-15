from yt_concate.settings import CAPTIONS_DIR

import os

class YT:
    def __init__(self, video_link) -> None:
        self.video_link = video_link
        self.video_id = self.get_video_id_from_url(video_link)
        self.caption_fp = self.get_caption_fp()
        self.captions = self.get_captions_from_file()

    
    @staticmethod
    def get_video_id_from_url(url):
        return url.split("watch?v=")[-1]

    def get_caption_fp(self):
        # get video id
        video_id = self.get_video_id_from_url(self.video_link)
        # get caption file name
        caption_fn = f"{video_id}_caption_file.txt"
        # get caption file path 
        caption_fp = os.path.join(CAPTIONS_DIR, caption_fn)
        return caption_fp

    def check_if_caption_file_exists(self):
        return os.path.exists(self.caption_fp) and os.path.getsize(self.caption_fp)
    
    def get_captions_from_file(self):
        if not self.check_if_caption_file_exists():
            print('Not found caption file!!')
            return {}
        
        else:
            with open(self.caption_fp, mode="r", encoding="utf-8") as reader:
                time = None
                time_flag = False
                caption = None
                captions = {}
                for line in reader:
                    if "-->" in line:
                        time = line
                        time_flag = True
                    else:
                        if time_flag:
                            caption = line
                            time_flag = False
                            captions.update({caption:time})
            return captions
            
