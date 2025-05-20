#!/usr/bin/python3.11

import os
from decouple import config


def get_env_or_config(key, default=""):
    return os.getenv(key) or config(key, default=default)
