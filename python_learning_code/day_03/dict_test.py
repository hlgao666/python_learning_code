corr_letters = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

phone = input('phone: ')

output = ''

for item in phone:
    output += corr_letters.get(item, '!') + " "
print(output)
