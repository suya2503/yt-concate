from .tasks.task import TaskException, Task
class Pipeline:
    def __init__(self, tasks) -> None:
        self.tasks = tasks
    
    def run(self, config, utils):
        data = None
        for task in self.tasks:
            try:
                data = task.process(data, config=config, utils=utils) # 接收處理完的資料，並傳到下一個Task中
            except TaskException as e:
                print(f'Exception Happened:{e}')
                break