import random
l1=["apple","banana","grapes","orange","kiwi"]
word= random.choice(l1).lower()
display=["_"]*len(word)
print("guse the fruit name")
i=6
while "_" in display and i>0:
    gusse=input("enter the letter:").lower()
    if gusse in word:
        for j in range(len(word)):
            if word[j]==gusse:
                display[j]=gusse
    else:
        i-=1
        print("wrong gusse")
        print(f"You still have {i} attempts remaining")
    print(" ".join(display))
if "_" not in display:
    print("Congratulations! You guessed the word:", word)
else:
     print("Game Over!")
     print("The word was:", word)

    
              
         


