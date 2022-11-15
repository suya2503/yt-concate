import urllib.request
import json
import ssl
import sys
sys.path.append('/Users/suya/DS_Suya/Projects/yt-concate')
from yt_concate.settings import API_KEY
from yt_concate.pipeline.tasks.get_vedio_list import GetVedioList
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.tasks.download_captions import DownloadCaptions
from yt_concate.pipeline.tasks.read_captions import ReadCaptions
from yt_concate.pipeline.tasks.search_caption import SearchCaptions
from yt_concate.pipeline.tasks.preflight import Preflight
from yt_concate.pipeline.tasks.postflight import Postflight
from yt_concate.utils import Utils

CHANNEL_ID = "UC9zY_E8mcAo_Oq772LEZq8Q" # the first take channel

def main():
    # read config
    config = {
        "channel_id":CHANNEL_ID,
        "search_caption":"love"
    }

    # all tasks
    tasks_list = [
        Preflight(),
        GetVedioList(),
        DownloadCaptions(),
        ReadCaptions(),
        SearchCaptions(),
        Postflight(),

    ]

    # utils
    utils = Utils()

    # 導管執行一步步任務(每一步都需要output一些檔案)
    pipeline_1 = Pipeline(tasks=tasks_list)
    pipeline_1.run(config=config, utils=utils)



if __name__ == "__main__":
    main()