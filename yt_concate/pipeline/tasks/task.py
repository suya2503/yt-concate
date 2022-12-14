from abc import ABC
from abc import abstractmethod

class Task(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data, config, utils):
        pass

class TaskException(Exception):
    pass