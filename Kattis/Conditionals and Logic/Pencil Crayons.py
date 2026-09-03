num_boxes, num_colors = map(int, input().split())
boxes = []

for _ in range(num_boxes):
    boxes.append(list(map(str, input().split())))

count = 0
for box in boxes:
    count += len(box) - len(set(box))


print(count)
