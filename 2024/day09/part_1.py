input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
map = lines[0]

disk_size = sum(int(x) for x in map)
disk = ['.' for _ in range(disk_size)]

write_head = 0

for i in range(len(map)):  # writing out the disk
    if i % 2 == 0:
        id = str(i // 2)

        for j in range(write_head, write_head + int(map[i])):
            disk[j] = id

    write_head += int(map[i])

read_head = disk_size - 1
write_head = 0

while write_head < read_head:  # perform contiguizing
    while disk[write_head] != '.':  # find the next free slot
        write_head += 1

    while disk[read_head] == '.':  # find the next file chunk to move
        read_head -= 1

    if write_head > read_head:
        break

    disk[write_head] = disk[read_head]
    disk[read_head] = '.'

checksum = 0

for i in range(disk_size):
    if disk[i] != '.':
        checksum += i * int(disk[i])

print(checksum)
