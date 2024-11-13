words = []
wordcount = 1
count = 0
newwords = []

for x in range(10):
    enter = str(input(f"Enter Word #{wordcount}: "))    
    words.append(enter)
    wordcount += 1

lettercount = int(input("Enter number of Letters: "))

for i in range(10):
    if len(words[count]) >= lettercount:
        newwords.append(words[count])
    count += 1

print(f"Words with letters above or equal to {lettercount}: ")
print(newwords)