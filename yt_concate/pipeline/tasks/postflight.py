from .task import Task

class Postflight(Task):
    def process(self, data, config, utils):
        utils.create_dir()
        return 