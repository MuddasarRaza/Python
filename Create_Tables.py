import psycopg2
def create_tables():
	""" create tables in the PostgreSQL database"""
	commands = ("""
		CREATE TABLE Rotation (
				Rot_X_axis INTEGER Not Null,
				Rot_Y_axis INTEGER Not Null,
				Rot_Z_axis INTEGER Not Null,
				timestamp BIGINT Not Null
		)
		""",
                """        
		CREATE TABLE Environment (
				Temperature INTEGER Not Null,
				AirPressure INTEGER Not Null,
				Humidity INTEGER Not Null,
				timestamp BIGINT Not Null
		)
		""",
		"""        
		CREATE TABLE Angular (

				Ang_X_axis INTEGER Not Null,
				Ang_Z_axis INTEGER Not Null,
				Ang_y_axis INTEGER Not Null,
				timestamp BIGINT Not Null
		)
		""",
                """      
		CREATE TABLE Acceleration (
				Acc_X INTEGER NOT NULL,
				Acc_Y INTEGER NOT NULL,
				Acc_Z INTEGER Not Null,
				timestamp BIGINT Not Null
		)
		""")
		
	conn = None
	try:
		# read the connection parameters
		#params = config()
		# connect to the PostgreSQL server
		conn = psycopg2.connect(host="localhost", database="jmif", user="jmifuser", password="eww8s0F4asdf354s")
		cur = conn.cursor()
		# create table one by one
		for command in commands:
			cur.execute(command)
		# close communication with the PostgreSQL database server
		cur.close()
		# commit the changes
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
 
 
if __name__ == '__main__':
	create_tables()
