from abc import ABC, ABCMeta, abstractmethod


class BaseMapping(ABC, metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def sql_to_proto(sql):
        pass

    @staticmethod
    @abstractmethod
    def proto_to_sql(proto):
        pass
