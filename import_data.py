import psycopg2;
conn = psycopg2.connect("host=localhost dbname=fongpae_dataset user=postgres password=Bossza1234") #return value of the connect() method is a Connection object.

# the connection object creates a client session with database server 
# create another object called Cursor object for execute our commands.
cursor=conn.cursor()
# create table in fondpae_dataset database 
cursor.execute("""
        CREATE TABLE raw_data(
            province text,
            cultivated_areas text,
            harvested_area text,
            product text,
            rain text,
            fertilizer_price text,
            oil_price text,
            plant_price text,
            year text,
            type text
        ) 
""")
conn.commit()