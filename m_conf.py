import configparser

filename = "config.ini" #example file name

conf = configparser.ConfigParser()
conf.read(filename)

def read(key, id):
    try:
        return conf.get(key, id)
    except:
        return False

def write(key, id, value):
    global filename
    try:
        conf.set(key, id, value)
        return True
    except:
        return False
    with open(filename, 'w') as configfile:
        conf.write(configfile)
