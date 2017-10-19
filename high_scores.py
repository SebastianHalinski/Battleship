def player_score(score, all_shots, level, name):
    high_score_line = []
    high_score_line.append(score)
    high_score_line.append(all_shots)
    high_score_line.append(level)
    high_score_line.append(name)
    return high_score_line


def export_hall_of_fame(text_file, high_scores_data):
    import csv

    with open(text_file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in high_scores_data:
            writer.writerow(row)


def import_hall_of_fame(text_file, player_score):
    import csv
    high_scores_data = []
    with open(text_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row[0] = int(row[0])
            high_scores_data.append(row)
    high_scores_data = sorted(high_scores_data, key = lambda score: score[0], reverse = True)

    for row in high_scores_data:
        if int(row[0]) <= player_score[0]:
            del high_scores_data[-1]

            high_scores_data.append(player_score)
            break
    high_scores_data = sorted(high_scores_data, key = lambda score: score[0], reverse = True)

    return high_scores_data


def get_highscore_table():
    name_data = []
    level_data = []
    all_shots_data = []
    score_data = []
    index_data = []
    index = 1

    high_scores_data = import_hall_of_fame("high_scores.csv", player_score)

    for i in high_scores_data:
        index_data.append(str(index))
        name_data.append(i[3])
        level_data.append(i[1])
        all_shots_data.append(str(i[2]))
        score_data.append(str(i[0]))
        index += 1

    import texttable as tt
    tab = tt.Texttable()
    headings = ['Idx', 'Score', 'all shots', 'level', 'Name']
    tab.header(headings)

    for row in zip(index_data, score_data, level_data, all_shots_data, name_data):
        tab.add_row(row)

    table = tab.draw()

    return str(table)


# high_score_line = player_score(2379, 42, 'medium', 'plajer')
# player_score = player_score(8999, 12, 'hard', 'plejer')
# print(import_hall_of_fame('high_scores.csv', player_score))
# high_scores_data = import_hall_of_fame('high_scores.csv', player_score)
# print(get_highscore_table())
# export_hall_of_fame('high_scores.csv', high_scores_data)
