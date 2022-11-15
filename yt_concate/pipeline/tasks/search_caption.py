from yt_concate.pipeline.tasks.task import Task
from yt_concate.models.seeker import Seeker

class SearchCaptions(Task):
    """
    return object include timestamp of qualified caption
    """
    def process(self, data, config, utils):
        return [Seeker(yt_object, config['search_caption']) for yt_object in data]
            

