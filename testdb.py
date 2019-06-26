import psycopg2
conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="dbPassword")
print "Connected"
cur = conn.cursor()
print "cur"
Postgres_insert = """INSERT INTO sensordata (rot_x_axis,rot_y_axis,rot_z_axis) values (%s,%s,%s)"""
values_rotation = (55,65,55)
cur.execute(Postgres_insert,values_rotation)
print "data inserted"
conn.commit()
