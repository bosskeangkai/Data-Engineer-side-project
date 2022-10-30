import psycopg2;
conn = psycopg2.connect("host=localhost dbname=fongpae_dataset user=postgres password=Bossza1234") #return value of the connect() method is a Connection object.

# the connection object creates a client session with database server 
# create another object called Cursor object for execute our commands.
cursor=conn.cursor()
# create table in fondpae_dataset database 
cursor.execute("""
        CREATE TABLE raw_data(
            province text,
            cultivated_areas INT,
            harvested_area INT,
            product INT,
            rain float,
            fertilizer_price float,
            oil_price float,
            year INT,
            type text
        )
""")
conn.commit()