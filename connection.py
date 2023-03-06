import psycopg2

conn  = None

try:
        # Establish a connection to the database
        conn = psycopg2.connect(database="demot", user="postgres", password="Aruba_pgadmin@123", host="localhost", port="5433")

except Exception as e:
        print(e)