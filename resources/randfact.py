from random import choice
import os
import sys


def resource_path(relative_path):
    """
    PyInstaller compatibility
    See https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(resource_path(dir_path), "facts.txt")) as f:
    facts = [fact.rstrip('\r\n ') for fact in f.readlines() if fact != '']


def get_fact():
    return choice(facts)
