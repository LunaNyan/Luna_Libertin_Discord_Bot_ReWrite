import sys
import sqlite3, configparser

#if __name__ == '__main__':
#    sys.exit(1)

db_obj = sqlite3.connect("db_main.dat")
db = db_obj.cursor()

temp_obj = sqlite3.connect(":memory:")
temp = temp_obj.cursor()

temp.execute("CREATE TABLE user_chats_count(id INTEGER NOT NULL, count INTEGER);")
temp.execute("CREATE TABLE guild_chats_count(id INTEGER NOT NULL, count INTEGER);")

def user_count(message):
    try:
        temp.execute("SELECT count FROM user_chats_count WHERE id = ?", (str(message.author.id)))
        count = temp.fetchone()[0]
        temp.execute("UPDATE user_chats_count SET count = ? WHERE id = ?", (str(int(count)+1), str(message.author.id)))
        return int(count)
    except:
        temp.execute("INSERT INTO user_chats_count VALUES(?, ?);", (str(message.author.id)), '1')
        return 1
    temp_obj.commit()

def guild_count(message):
    try:
        temp.execute("SELECT count FROM guild_chats_count WHERE id = ?", (str(message.guild.id)))
        count = temp.fetchone()[0]
        temp.execute("UPDATE guild_chats_count SET count = ? WHERE id = ?", (str(int(count)+1), str(message.guild.id)))
        return int(count)
    except:
        temp.execute("INSERT INTO guild_chats_count VALUES(?, ?);", (str(message.guild.id)), '1')
        return 1
    temp_obj.commit()
