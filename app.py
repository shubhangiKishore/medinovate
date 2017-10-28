from flask import Flask
import hashlib
from flask import request
from PIL import Image
import imagehash


def hash_it():
    hash = imagehash.average_hash(Image.open("t"))
    print (hash)
    return hash



hash_it()

