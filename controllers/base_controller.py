from abc import ABC, ABCMeta, abstractmethod


class BaseController(ABC, metaclass=ABCMeta):

    @abstractmethod
    @classmethod
    def find_by_id(cls, id):
        pass

    @abstractmethod
    def save_to_db(self):
        pass
