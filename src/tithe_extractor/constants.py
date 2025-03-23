"""This file contains constants used in the package."""
# import os

# API Constants
SCRYFALL_BULK_DATA_URL = "https://api.scryfall.com/bulk-data"
HEADERS = {"user-agent": "tithe-extractor/0.1.0", "Accept": "application/json"}
TIMEOUT = 10
FORCE = False
DATA_CACHE_DIR = "data/cache/"
RAW_DATA_DIR = "data/raw/"
# Constants - not sure if this pathing will be correct - may need to be specified by user/project
# MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
# sp_dir = os.path.split(MODULE_DIR)[0]
# PROJECT_DIR = os.path.split(sp_dir)[0]
# DATA_DIR = os.path.join(PROJECT_DIR, "data")
# CACHE_DIR = os.path.join(DATA_DIR, "cache")
# BULK_METADATA_PATH = os.path.join(CACHE_DIR, "bulk-data.json")
# Should automate headers using package info
