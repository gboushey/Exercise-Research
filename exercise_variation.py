daily_exercise_log = [30, 30, 45, 0, 0, 30, 25]

delta = []

for i in range(1, len(daily_exercise_log)):
    diff = daily_exercise_log[i] - daily_exercise_log[i-1]
    delta.append(diff)

print(delta)