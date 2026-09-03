# get cost of sowing per square meter
c = float(input())

# get the number of lawns to sow
n = int(input())
total = 0

for i in range(n):
    # get the length and width of each lawn
    x, y = map(float, input().split())
    # add all the area of the lawns
    total += x * y

# display the total cost of sowing
print(total * c)
