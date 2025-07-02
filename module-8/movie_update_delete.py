import mysql.connector
print("This Python script connects to the movies database and shows how to add,"
"change, and remove records from the film table using SQL commands. It includes a "
"function called show_films that joins the film, genre, and studio tables to display helpful film information."
 "The output shows the list of films before and after each change, so you can see that the updates worked correctly.")
# connect to the movies database
db = mysql.connector.connect(
user="movies_user",
password="popcorn",
host="127.0.0.1",
database="movies"
)

cursor = db.cursor()

# define the function to display films
def show_films(cursor, title):
    # Execute an inner join to gather film details
    cursor.execute("""
        SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, 
               studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """)

    films = cursor.fetchall()

    print("\n  -- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(
            film[0], film[1], film[2], film[3]
        ))

# 1. Display initial films
show_films(cursor, "DISPLAYING FILMS")

# 2. Insert a new film (e.g., 'Gladiator')
cursor.execute("""
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES ('Gladiator', '2000', '155', 'Ridley Scott', 1, 1)
""")
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# 3. Update film 'Alien' to Horror genre (assuming Horror genre_id is 1)
cursor.execute("""
    UPDATE film
    SET genre_id = 1
    WHERE film_name = 'Alien'
""")
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE– Changed Alien to Horror")

# 4. Delete the film Gladiator
cursor.execute("""
    DELETE FROM film
    WHERE film_name = 'Gladiator'
""")
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Close the connection
cursor.close()
db.close()