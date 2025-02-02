from sqlalchemy import *
engine = create_engine('sqlite:///urls.db') 
metadata = MetaData()
cursor = engine.connect()
urls = Table('urls', metadata,
	Column('id', Integer(), primary_key=True),
	Column('url', String(255)))
metadata.create_all(engine)

def add_url(url):
    try:
        cursor.execute(urls.insert().values(url=url))
        cursor.commit()
        return int(cursor.execute(urls.select()).fetchall()[-1][0])  # Return the last inserted ID
    except Exception as e:
        return str(e)  

def get_url_for_id(id):
    try:
        return cursor.execute(urls.select().where(urls.c.id == id)).fetchone()[1]
    except TypeError:
        return 'Нет такой ссылки'