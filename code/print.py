for line in open("file.txt"):
    for word in line.split():
        if word.endswith("ing"):
            print word
