from json import dumps, loads
from typing import Any, Optional

from redis import Redis as RedisClient
REDIS_PARAMS = {"port": 6379, "host": 'localhost'}


class Redist:
    def __init__(self):
        __redis_vars = REDIS_PARAMS
        self.redis_prefix =  ""
        self.redis = RedisClient(**__redis_vars)

    def get_redis_ns(self, name: str) -> str:
        return f"{self.redis_prefix}{name}"

    def execute(self, action: str, *args, **kwargs) -> Optional[bytes]:
        if kwargs.get("name"):
            kwargs["name"] = self.get_redis_ns(kwargs["name"])
        return getattr(self.redis, action)(*args, **kwargs)

    def get(self, name: str) -> Optional[Any]:
        redis_value = self.execute("get", name=name)
        return redis_value if redis_value is None else loads(redis_value.decode())

    def set(self, name: str, value: Any, expiration: Optional[int] = None) -> None:
        self.execute("set", name=name, value=dumps(value), ex=expiration)
        return

    def delete(self, *names) -> None:
        self.execute("delete", *[self.get_redis_ns(name) for name in names])
        return

    def expire(self, name: str, expiration: int) -> None:
        self.execute("expire", name=name, time=expiration)
