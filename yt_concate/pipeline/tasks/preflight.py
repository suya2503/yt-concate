from .task import Task

class Preflight(Task):
    def process(self, data, config, utils):
        utils.create_dir()
        return 
