with open('input.txt') as f:
    input_lines = f.readlines()

# Part 1
valid_count = 0
for line in input_lines:
    line = line.rstrip()
    parts = line.split(' ')
    letter_lower_bound, letter_upper_bound = parts[0].split('-')
    letter_lower_bound = int(letter_lower_bound)
    letter_upper_bound = int(letter_upper_bound)
    letter = parts[1].rstrip(':')
    password = parts[2]
    letter_count = password.count(letter)
    if (letter_count >= letter_lower_bound) and (letter_count <= letter_upper_bound):
        print(letter_lower_bound, letter_upper_bound, letter, password)
        valid_count += 1
print(valid_count)

# Part 2
valid_count = 0
for line in input_lines:
    line = line.rstrip()
    parts = line.split(' ')
    letter_pos_1, letter_pos_2 = parts[0].split('-')
    letter_pos_1 = int(letter_pos_1)-1
    letter_pos_2 = int(letter_pos_2)-1
    letter = parts[1].rstrip(':')
    password = parts[2]
    match_1 = password[letter_pos_1:(letter_pos_1+1)] == letter
    match_2 = password[letter_pos_2:(letter_pos_2+1)] == letter
    if (match_1 and not match_2) or (match_2 and not match_1):
        valid_count += 1
print(valid_count)
