import urllib.request
import json
import ssl
import sys
sys.path.append('/Users/suya/DS_Suya/Projects/yt-concate')
from yt_concate.settings import API_KEY
from yt_concate.tasks.get_vedio_list import GetVedioList

tasks_list = [
    GetVedioList,

]

for task in tasks_list:
    task_obj = task()
    task_obj.process()


if __name__ == "__main__":

    CHANNEL_ID = "UCag5MH_BUo4oJdQyOMSvCRw"

    # video_list = get_all_video_in_channel(channel_id=CHANNEL_ID)
    # print(len(video_list))
    print(API_KEY)