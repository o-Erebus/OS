available = [3, 3, 2]  # Available instances of resources A, B, C
m = 3
n = 5
max_need = [
        [7, 5, 3],  # P0
        [3, 2, 2],  # P1
        [9, 0, 2],  # P2
        [2, 2, 2],  # P3
        [4, 3, 3]  # P4
]

allocation = [
        [0, 1, 0],  # P0
        [2, 0, 0],  # P1
        [3, 0, 2],  # P2
        [2, 1, 1],  # P3
        [0, 0, 2]  # P4
]

need = [[0 for x in range(m)] for y in range(n)]
safe = []
for i in range(n):
    for j in range(m):
        need[i][j] = max_need[i][j] - allocation[i][j]


done = [0,0,0,0,0]

while len(safe) < n:
    safe_state = False

    for i in range(n):

        if done[i] != 1:
            if all(need[i][j] <= available[j] for j in range(m)):
                for j in range(m):
                    available[j] = available[j] + need[i][j]
                done[i] = 1
                safe.append(i)
                safe_state = True

    if not safe_state:
        print("Not Safe")
        break
    else:
        print("Safe")
print(safe)