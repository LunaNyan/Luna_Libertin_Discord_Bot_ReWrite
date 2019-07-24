import datetime, sys

print_log = True

def writedown(text):
    writedown_str = str(datetime.datetime.now()) + text
    with open("log.txt", "a") as f:
        f.write(writedown_str + "\n")
    if print_log:
        print(writedown_str)

def error(text):
    writedown(" : E : " + text)

def warn(text):
    writedown(" : W : " + text)

def info(text):
    writedown(" : I : " + text)

def giveup(text):
    error("Giving Up. Reason : " + text)
    sys.exit()