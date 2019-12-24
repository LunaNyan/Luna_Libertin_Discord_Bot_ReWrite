import sys, os.path
import sqlite3, configparser

if __name__ == '__main__':
    sys.exit(1)

db_path = "db/db_main.dat"

if os.path.isfile(db_path):
    db_obj = sqlite3.connect(db_path)
    db = db_obj.cursor()
else:
    print("WARNING : DB file not found, creating new one")
    db_obj = sqlite3.connect(db_path)
    db = db_obj.cursor()
    db.execute("CREATE TABLE user(id INTEGER NOT NULL, name TEXT, bio TEXT, createdat DATETIME, level INTEGER, disclosure_createdat INTEGER, disclosure_joinedat INTEGER, user_passive_available INTEGER);")
    db.execute("CREATE TABLE guild(id INTEGER NOT NULL, name TEXT, bio TEXT, createdat DATETIME, disclosure_guild INTEGER, disclosure_user_joinedat INTEGER, user_passive_available INTEGER, guild_passive_available INTEGER, custom_head TEXT, custom_guild_passive_text TEXT, news_channel INTEGER, welcome_message_cid INTEGER welcome_message_text TEXT, farewell_message_cid INTEGER, farewell_message_text TEXT);")
    db_execute("CREATE TABLE guild_custom_commands(gid INTEGER, command TEXT NOT NULL, reply TEXT NOT NULL, writed INTEGER NOT NULL);")

temp_obj = sqlite3.connect(":memory:")
temp = temp_obj.cursor()

temp.execute("CREATE TABLE user_chats_count(id INTEGER NOT NULL, count INTEGER);")
temp.execute("CREATE TABLE guild_chats_count(id INTEGER NOT NULL, count INTEGER);")

def user_count(message):
    try:
        temp.execute("SELECT count FROM user_chats_count WHERE id = ?", (str(message.author.id)))
        count = temp.fetchone()[0]
        temp.execute("UPDATE user_chats_count SET count = ? WHERE id = ?", (str(int(count)+1), str(message.author.id)))
        return int(count+1)
    except:
        temp.execute("INSERT INTO user_chats_count VALUES(?, ?);", (str(message.author.id)), '1')
        return 1
    temp_obj.commit()

def guild_count(message):
    try:
        temp.execute("SELECT count FROM guild_chats_count WHERE id = ?", (str(message.guild.id)))
        count = temp.fetchone()[0]
        temp.execute("UPDATE guild_chats_count SET count = ? WHERE id = ?", (str(int(count)+1), str(message.guild.id)))
        return int(count+1)
    except:
        temp.execute("INSERT INTO guild_chats_count VALUES(?, ?);", (str(message.guild.id)), '1')
        return 1
    temp_obj.commit()

def purge_counts():
    temp.execute("DELETE FROM user_chats_count")
    temp.execute("DELETE FROM guild_chats_count")
