import os
import json

def filenameandpath(filenameandpath):
    with open(filenameandpath, "r") as f:
        json.load(f)



