classrooms, bottles = map(int, input().split())

for i in range(classrooms):
    req = int(input())
    bottles -= req

print("Jebb" if bottles >= 0 else "Neibb")
