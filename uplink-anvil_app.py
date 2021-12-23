import anvil.server
import sqlite3 

anvil.server.connect("FAAT4YRG5GDBNFK2W7ZRCMWS-5K2JKQ5FSX4GNAMV")


con = sqlite3.connect("first.db", check_same_thread=False)
cur = con.cursor()


@anvil.server.callable
def get_items():
  cur.execute('SELECT * FROM TaskList')
  items = cur.fetchall()
  return [
    {'id': item[3], 'name': item[0], 'quantity': item[2]}
    for item in items
  ]

print(get_items())
anvil.server.wait_forever()