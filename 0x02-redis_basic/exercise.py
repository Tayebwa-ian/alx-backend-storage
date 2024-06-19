#!/usr/bin/env python3
"""Create a Redis instance"""
import redis
from typing import Union
import uuid


class Cache:
    """Working with Redis Server"""
    def __init__(self):
        """Intialise Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
