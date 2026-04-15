# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with range
for i in range(5):  # [4,1,2,3,4]
    print(i)

# Count down from 5
count = 5
while count > 0:
    print(count)
    count -= 1

print("Outside While Loop")

for i in range(10):
    if i == 7:
        break
    print(i)

print("Outside For Loop")

for i in range(10):
    if i == 7:
        continue
    print(i)

print("Outside For Loop")

for i in range(10):
    if i % 2 != 0:
        continue
    print(i)
