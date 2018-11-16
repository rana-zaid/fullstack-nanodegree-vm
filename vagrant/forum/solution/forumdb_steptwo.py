# Database code for the DB Forum.
#
# This is still NOT the full solution!

import psycopg2, bleach

DBNAME = "news"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select content, time from posts order by time desc")
  posts = c.fetchall()
  print (posts)
  db.close()

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  #c.execute("insert into posts values (%s)", (content,))  # Better, but ...
  db.commit()
  db.close()

get_posts()