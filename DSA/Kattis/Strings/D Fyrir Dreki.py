a, b, c = int(input()), int(input()), int(input())

num_roots = b**2 - 4 * a * c

print(0 if num_roots < 0 else 1 if num_roots == 0 else 2)
