from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.read()

player1_score = 0
player2_score = 0

for line in lines.split("\n"):
    is_valid = True
    id_, event_data = line.split(":")
    balls_by_color = defaultdict(int)

    for event in event_data.split(";"):
        for balls in event.split(","):
            quantity, color = balls.split()
            quantity = int(quantity)

            balls_by_color[color] = max(balls_by_color[color], quantity)

            if quantity > {
                "red": 12,
                "green": 13,
                "blue": 14,
            }.get(color, 0):
                is_valid = False

    score = 1

    for ball_count in balls_by_color.values():
        score *= ball_count

    player2_score += score

    if is_valid:
        player1_score += int(id_.split()[-1])

print(player1_score)
print(player2_score)
