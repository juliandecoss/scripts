from threading import local

from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()
base_thread = local()


class BaseModel(base):
    __abstract__ = True
    shard_thread = base_thread
    shard_thread.shard = "konfio"

    @classmethod
    def get_shard(cls):
        return cls.shard_thread.shard


class KonfioModel(BaseModel):
    __abstract__ = True
    __table_args__ = {"schema": "KONFIO"}