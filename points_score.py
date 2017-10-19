all_shots = []
"""punkty do maina"""

def high_score(level, points):
    total_shots = len(points)
    all_ships_lenght = 17
    if level == 'easy':
        level_multiplier = 100
    elif level == 'medium':
        level_multiplier = 200
    elif level == 'hard':
        level_multiplier = 400
    score = level_multiplier * all_ships_lenght / total_shots
    return score

def add_shot(points):
    all_shots.append(1)
    return points
