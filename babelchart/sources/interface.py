from abc import ABCMeta, abstractmethod

class BaseSource(metaclass=ABCMeta):

    @abstractmethod
    def get_series(self):
        pass

