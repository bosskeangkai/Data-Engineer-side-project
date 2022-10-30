import psycopg2
import csv
conn = psycopg2.connect("host=localhost user=postgres password=Bossza1234 dbname=fongpae_dataset")
cursor = conn.cursor()

# access and open CSV file
with open('./Dataset/dataset.csv','r',encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader)

    # for loop to access each row in CSV file
    for row in reader:
        cursor.execute(
            "INSERT INTO raw_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row
        )

conn.commit()