# Nirel Marie M. Ibarra
# 192468
# March 15, 2021

# I have not discussed the Python language code in my program
# with anyone other than my instructor or the teaching assistants
# assigned to this course

# I have not used Python language code obatained from another student
# or any other unauthorized source, either modified or unmodified

# If any Python language code or documentation used in my program 
# was obtained from another source, such as a textbook or website,
# that has clearly noted with a proper ciration in the comments
# of my program

#closest answer
#infinitely asks prompt unless number is outside the range

def create_story(artist, food, emotion, name, organ, song):
    story = "\n\nThe Majestic " + artist + "\n\nOnce upon a time, in a far away kingdom, there lived a ruler known as The Majestic " + artist + ". Beloved by all people, The Majestic " + artist + " was always quite unique, always wearing a crown made of " + food + " and " + emotion + ". \n\nBut one day, the evil villain " + name +" broke into the palace to kidnap The Majestic " + artist + ".\nThankfully, the beloved ruler was skilled in martial arts. One swift kick to " +name + "'s " + organ + " sent the evildoer flying across the room yelling " + song + "!" + "\n\nThe end."
    return story

while True:
    artist = input()
    if artist == "stop":
        break
    else:
        food = input()
        emotion = input()
        name = input()
        organ = input()
        song = input()
    
    print(create_story(artist, food, emotion, name, organ, song))