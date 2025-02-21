fh = ["hey whats up my dude","bro you are my dude","I am the danger"]

lst = []
for line in fh:
    words = line.split()
    index = 0
    for word in words:
        if not lst:
            lst.append(word)
            continue
        while true:
            if index == len(lst):
                break
            if word 
print(lst)