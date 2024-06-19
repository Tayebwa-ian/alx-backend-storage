#!/usr/bin/env python3
"""Create a Redis instance"""
import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts the number of calls to Cache class
    Arg:
      method: the passed method
    return: inner fuunction
    """
    @wraps(method)
    def wrapper(*args, **kwargs) -> str:
        """
        Increments the count by 1 everytime the class cache is called
        """
        args[0]._redis.incr(method.__qualname__)
        return method(*args, **kwargs)
    return wrapper


class Cache:
    """Working with Redis Server"""
    def __init__(self):
        """Intialise Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store input data into the redis sever
        Arg:
          data: the input data to store
        return: key(str) for the stored value
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, int, float]:
        """
        Get a value from the redis database and convert is in the right form
        Arg:
          key: the key to use
          fn: function to convert the retrieved data to the correct format
        return: the value from the redis database
        """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_int(data: bytes) -> int:
        """
        convert bytes to int
        Arg:
          data: the data to convert
        return: the new converted data
        """
        return int(data.decode('utf-8'))

    def get_str(data: bytes) -> str:
        """
        convert bytes to str
        Arg:
          data: the data to convert
        return: the new converted data
        """
        return data.decode('utf-8')
