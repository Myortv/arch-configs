ignore = {
    '/dev/sda6',
}
output = ''
with open('/etc/mtab') as file:
    for line in file:
        if not line.startswith('/'):
            continue
        line = line.split()
        if not (set(line) & ignore):
            words = [word for word in line if word.startswith('/')]
            output += f'  --{words[0]}\t{words[1]}\n'

print(output)
