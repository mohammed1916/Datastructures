V = 5
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
selected = [False] * V
selected[0] = True
print("Edge : Weight\n")
no_edge = 0

while no_edge < V - 1:
    minimum = float('inf')
    min_row = 0
    min_col = 0
    for row in range(V):
        if selected[row]:
            for col in range(V):
                if not selected[col] and G[row][col]:
                    if minimum > G[row][col]:
                        minimum = G[row][col]
                        min_row, min_col = row, col
    print(f"{min_row}-{min_col}:{G[min_row][min_col]}")
    selected[min_col] = True
    no_edge += 1