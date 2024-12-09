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

def write_over(source, dest, length):
    for i in range(length):
        disk[dest + i] = disk[source + i]
        disk[source + i] = '.'

while read_head > -1:  # perform contiguizing
    while disk[read_head] == '.':  # find the next file chunk to move
        read_head -= 1

    end = read_head
    id = disk[read_head]

    while disk[read_head] == id:  # find the beginning of the file chunk
        read_head -= 1

    length = end - read_head
    write_head = 0
    start = 0
    is_free = False

    while write_head < disk_size:  # looking for a big enough free space

        while disk[write_head] != '.':
            write_head += 1

        if write_head > read_head:
            break

        start = write_head

        while disk[write_head] == '.':
            write_head += 1

        if write_head - start >= length:
            is_free = True
            break

    if is_free:
        write_over(read_head + 1, start, length)


checksum = 0

for i in range(disk_size):
    if disk[i] != '.':
        checksum += i * int(disk[i])

print(checksum)
