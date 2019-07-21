import datetime

def writedown(text):
    with open("log.txt", "a") as f:
        f.write(datetime.datetime.now() + text + "\n")

def error(text):
    writedown(" : E : " + text)

def warn(text):
    writedown(" : W : " + text)

def info(text):
    writedown(" : I : " + text)
