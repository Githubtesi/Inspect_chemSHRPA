# -*- coding: utf-8 -*-
# Created by tesiy at 2022/08/11
import pathlib

PROJECT_DIR = pathlib.Path(__file__).parent
INFO_LOG_FILE = PROJECT_DIR / pathlib.Path("info.log")
ERROR_LOG_FILE = PROJECT_DIR / pathlib.Path("error.log")
TEMP_DIR = PROJECT_DIR / pathlib.Path("temp")
TEST_DIR = PROJECT_DIR / pathlib.Path("test")
UNZIP_TEMP_DIR = PROJECT_DIR / pathlib.Path("unzip_temp")
