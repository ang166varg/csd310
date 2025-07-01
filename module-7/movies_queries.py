import mysql.connector
from mysql.connector import errorcode

# Connect to MySQL
try:
    db = mysql.connector.connect(
        user="movies_user",          # replace with your MySQL username
        password="popcorn",  # replace with your MySQL password
        host="127.0.0.1",
        database="movies"
    )

    cursor = db.cursor()

    # Query 1: Display all Studio records
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    print("\n-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}\n")

    # Query 2: Display all Genre records
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}\n")

    # Query 3: Display movies with runtime less than 120
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    short_films = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for film in short_films:
        print(f"Film Name: {film[0]}")
        print(f"Runtime: {film[1]}\n")

    # Query 4: Display film names and directors, ordered by director
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    directors = cursor.fetchall()
    print("-- DISPLAYING Director RECORDS in Order --")
    for film in directors:
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}\n")

    db.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)