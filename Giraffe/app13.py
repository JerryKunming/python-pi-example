def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Please input the words or sentences you need to translate: ")))

# This is the end of program for translation.

'''
This is the comment area for 
multiple lines.
If you like writing something
important for programming. It
is the right area for you.


'''