with open('input.txt') as f:
    lines = [line.rstrip() for line in f.readlines()]
line_length = len(lines[0])

# Part 1
current_x = 0
tree_hits = 0
for line in lines:
    symbol = line[current_x % line_length]
    if symbol == '#':
        tree_hits += 1
    current_x += 3
print(tree_hits)

# Part 2
product = 1
for (delta_x, delta_y) in (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
):
    current_x = 0
    tree_hits = 0
    for line_index in range(0, len(lines), delta_y):
        line = lines[line_index]
        symbol = line[current_x % line_length]
        if symbol == '#':
            tree_hits += 1
        current_x += delta_x
    product *= tree_hits
    print((delta_x, delta_y), tree_hits)
print(product)
