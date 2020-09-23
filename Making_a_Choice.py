'''
Problem 1 : Making a Choice
You are given two lists of thriller and comedy movies. Your task is to read a string that is a movie/series to check if it
is of thriller and comedy genre and print the following:
It is a thriller [if the string is of thriller genre].
It is a comedy [if the string is of comedy genre].
It's neither comedy nor thriller [ if it neither comedy nor of thriller genre].
Assumptions: both the lists have all the movies/series of their type.

The given two lists are as follows:
thriller=["Dark","Mindhunter","Parasite","Inception","Insidious","Interstellar","Prison Break","Money
Heist","War","Jack Ryan"]
comedy=["Friends","3 Idiots","Brooklyn 99","How I Met Your Mother","Rick And Morty","The Big Bang
Theory","The Office","Space Force"]
Hint: If the String entered belongs/not belongs to anyone of the genre lists, print out their respective print
statements as mentioned above.
'''
def find_genre(thriller,comedy,movie):
    for i in thriller:
        if i.upper() == movie.upper():
            print("It is a thriller")
            return
    for i in comedy:
        if i.upper() == movie.upper():
            print("It is a comedy")
            return
    print("It's neither comedy nor thriller")


thriller=["Dark","Mindhunter","Parasite","Inception","Insidious","Interstellar","Prison Break","Money Heist","War","Jack Ryan"]
comedy=["Friends","3 Idiots","Brooklyn 99","How I Met Your Mother","Rick And Morty","The Big Bang Theory","The Office","Space Force"]
movie = input()
find_genre(thriller,comedy,movie)

'''
the Office
It is a comedy
'''
