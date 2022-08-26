print ("welcome to my computer Quiz")

playing = input("do you want to play? ")

if playing != "yes":
    quit()

print ("okay! let's play! :)")
score = 0

answer = input("is the coding language python, named after a snake? ")
if answer == "no":
    print("correct!")
     
    score =score + 1
else:
    print("incorrect!")

answer = input ("what does CPU stand for?")
if answer == "Central Processing Unit":
    print("correct")
    score =score + 1
else:
    print("incorrect")

answer =input ("what is the full meaning RAM?")
if answer == "Random access memory":
    print("correct!")
    score =score + 1
else:
    print ("incorrect!")
    
print("you got "+ str(score) + " Questions correct!")