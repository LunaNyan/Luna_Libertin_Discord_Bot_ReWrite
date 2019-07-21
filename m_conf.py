import configparser, m_log, main

filename = "config.ini" #example file name

conf = configparser.ConfigParser()

try:
    conf.read(filename)
    m_log.info("successfully loaded configuration file.")
except Exception as e:
    main.giveup("failed to load configuration file : " + str(e))

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
        m_log.error("failed to writing configuration file : " + str(e))
    with open(filename, 'w') as configfile:
        conf.write(configfile)
