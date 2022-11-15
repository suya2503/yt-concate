class Seeker:
    def __init__(self, yt, search_caption) -> None:
        self.yt = yt
        self.search_caption = search_caption
        self.seeked_caption_ts = self.seek_for_the_caption()

    def seek_for_the_caption(self):
        if not self.yt.captions:
            print(f'Not captions in this video:{self.yt.video_id}')
            return
        else:
            qualified_time = []
            for caption in self.yt.captions:
                if self.search_caption in caption:
                    print('Found the caption!!')
                    pre_time, post_time = self.yt.captions[caption].split("-->")
                    pre_time = pre_time.strip()
                    post_time = post_time.strip()
                    qualified_time.append((pre_time, post_time))
            return qualified_time
