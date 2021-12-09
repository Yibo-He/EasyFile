# This is a sample Python script.
from .process import process
from .translate import translate


def formatter(document, requirements):
    # print("OK")
    for requirement in requirements:
        document = process(document, requirement)
    return document


def translater(document, fromLang='auto', toLang='zh'):
    translate(document, fromLang, toLang)
