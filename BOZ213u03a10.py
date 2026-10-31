blocks = int(input("Enter the number of blocks: "))

height = 0
needed_blocks = 1

while blocks >= needed_blocks:
    blocks -= needed_blocks
    height += 1
    needed_blocks += 1

print("The height of the pyramid:", height)
