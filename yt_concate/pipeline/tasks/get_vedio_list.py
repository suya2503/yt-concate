import sys
import os
sys.path.append('/Users/suya/DS_Suya/Projects/yt-concate')
import urllib.request
import json
import ssl
from yt_concate.settings import API_KEY
from yt_concate.pipeline.tasks.task import Task, TaskException
from yt_concate.settings import VIDEOS_LINK_DIR


class GetVedioList(Task):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data, config, utils):

        channel_id = config['channel_id']

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = f"{base_search_url}key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25"
        video_links = []
        # check if video link exists
        if utils.check_if_video_link_file_exists(channel_id) and os.path.getsize(os.path.join(VIDEOS_LINK_DIR, f"{channel_id}.txt")) > 0:
            print(f'Found the video link file for channel id:{channel_id}')
            return utils.read_video_link_file(channel_id)

        url = first_url
        while True:
            # 這裡也有是最有可能出錯的地方 -> 但不知道有哪些錯誤
            context = ssl._create_unverified_context()
            inp = urllib.request.urlopen(url, context=context)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = f"{first_url}&pageToken={next_page_token}"
            except:
                break
        print(len(video_links), video_links)

        # save the video link to file
        utils.write_video_link_to_file(channel_id, video_links)

        return video_links


if __name__ == "__main__":
    config = {
        'channel_id': 'UCag5MH_BUo4oJdQyOMSvCRw'
    }

    obj = GetVedioList()
    video_list = obj.process(config=config)
    print(video_list)
