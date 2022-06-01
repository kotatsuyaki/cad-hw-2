import fileinput

header = input().split(',')
print('|' + '|'.join(header) + '|')
print('|---' * len(header) + '|')

for line in fileinput.input():
    line = line.strip()
    line = ['$' + word + '$' for word in line.split(',')]
    print('|' + '|'.join(line) + '|')
