import urllib.request
import json
import ssl

def get_all_video_in_channel(channel_id):
    api_key = "AIzaSyDn8tiokD8Iyl-FrM-5egX-N-b2QFi2XKE"

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = f"{base_search_url}key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25"

    video_links = []
    url = first_url
    while True:
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
    return video_links


if __name__ == "__main__":
    CHANNEL_ID = "UCag5MH_BUo4oJdQyOMSvCRw"
    video_list = get_all_video_in_channel(channel_id=CHANNEL_ID)
    print(len(video_list))