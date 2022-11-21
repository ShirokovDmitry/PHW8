import random

def shuffle_file(file):
    reader = open(file, 'r', encoding="utf-8")
    text = reader.readlines()
    random.shuffle(text)
    for line in text:
        print(line)