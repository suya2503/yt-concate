import os

from yt_concate.pipeline.tasks.task import Task
from yt_concate.models.yt import YT



class ReadCaptions(Task):
    """
    return object include some video info and captions
    """
    def process(self, data, config, utils):
        return [YT(video_link) for video_link in data]
        # for video_link in data:
            # check if caption file exists
            # if not utils.check_if_caption_file_exists(video_link):
            #     print('Not found caption file!!')
            #     continue

            # with open(utils.get_caption_fp(video_link), mode="r", encoding="utf-8") as reader:
            #     time = None
            #     time_flag = False
            #     caption = None
            #     captions = {}
            #     for line in reader:
            #         if "-->" in line:
            #             time = line
            #             time_flag = True
            #         else:
            #             if time_flag:
            #                 caption = line
            #                 time_flag = False
            #                 captions.update({caption:time}) # 因為還要再帶有該影片的資訊（eg. 影片ID來標注該captions都是該影片的字幕，此時就會讓字典有了兩層的資料結構，對於日後的維護是需要記憶力或時間來回憶的，這就沒有這麼好維護）

