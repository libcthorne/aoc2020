all_numbers = set()
with open('intro_input.txt') as f:
    for n_str in f.readlines():
        n = int(n_str.strip())
        all_numbers.add(n)

for n in all_numbers:
    diff = 2020-n
    for n2 in all_numbers:
        diff2 = diff-n2
        if diff2 in all_numbers:
            print(n, n2, diff2, n*n2*diff2)
            break
