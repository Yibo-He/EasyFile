# This is a sample Python script.
from .process import process

def formatter(document, requirements):
    # print("OK")
    for requirement in requirements:
        document=process(document,requirement)
    return document
