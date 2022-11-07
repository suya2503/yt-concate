import urllib.request
import json
import ssl
import sys
sys.path.append('/Users/suya/DS_Suya/Projects/yt-concate')
from yt_concate.settings import API_KEY
from yt_concate.pipeline.tasks.get_vedio_list import GetVedioList
from yt_concate.pipeline.tasks.task import TaskException
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = "UCag5MH_BUo4oJdQyOMSvCRw"

def main():
    # read config
    config = {
        "channel_id":CHANNEL_ID
    }

    # all tasks
    tasks_list = [
        GetVedioList(),

    ]

    # 導管執行一步步任務
    pipeline_1 = Pipeline(tasks=tasks_list)
    pipeline_1.run(config=config)



if __name__ == "__main__":
    main()