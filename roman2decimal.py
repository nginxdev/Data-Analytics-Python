def roman_to_int(input_char_seq):
    roman_decimal_dict = {'m': 1000, 'd': 500, 'c': 100, 'l': 50, 'x': 10, 'v': 5, 'i': 1}
    input_char_seq = input_char_seq.lower()
    roman_decimal_equivalent = []

    if len(input_char_seq) == 1:
        return roman_decimal_dict[input_char_seq]

    for char in input_char_seq:
        val = roman_decimal_dict[char]
        roman_decimal_equivalent.append(val)

    total = 0

    for curr, nex in zip(roman_decimal_equivalent, roman_decimal_equivalent[1:]):
        if curr >= nex:
            total += curr
        else:
            total -= curr
    return total + nex

print(roman_to_int('mcmiv'))
print(roman_to_int('MMCXI'))

list = ['i','iv','v','ix','x','xl','l','xc','c','cd','d','cm','m','mmmmcmxcix']
for roman in list:
    print(roman_to_int(roman))
