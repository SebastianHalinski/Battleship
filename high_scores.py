def high_scores(name, points, text_file):  # jak obliczamy punkty???
    with open(text_file, "r") as file:
        lines = []
        for line in file:
            line = line.strip()
            line = line.split(",")
            lines.append(line)
    new_score = [name, str(points)]

    for i in range(len(lines)):
        if points > int(lines[i][1]):
            lines.insert(i, new_score)
            lines.pop()
            print(name, ", your score is:", points)
            print("You will be added to the hall of fame!")
            break
    else:
        print(name, ", your score is", points)
        print("You will not be added to hall of fame...")
    input("Press enter to continue: ")


    new_scores = ""
    for line in lines:
        new_scores += ",".join(line)+'\n'
    with open(text_file, "w") as new_file:
        new_file.write(new_scores)


high_scores("BattleSheep2", 1200, "high_scores.txt")

