tran={}
tran['1'] = '`'
tran['2'] = '1'
tran['3'] = '2'
tran['4'] = '3'
tran['5'] = '4'
tran['6'] = '5'
tran['7'] = '6'
tran['8'] = '7'
tran['9'] = '8'
tran['0'] = '9'
tran['-'] = '0'
tran['='] = '-'
tran['W'] = 'Q'
tran['E'] = 'W'
tran['R'] = 'E'
tran['T'] = 'R'
tran['Y'] = 'T'
tran['U'] = 'Y'
tran['I'] = 'U'
tran['O'] = 'I'
tran['P'] = 'O'
tran['['] = 'P'
tran[']'] = '['
tran['\\'] = ']'
tran['S'] = 'A'
tran['D'] = 'S'
tran['F'] = 'D'
tran['G'] = 'F'
tran['H'] = 'G'
tran['J'] = 'H'
tran['K'] = 'J'
tran['L'] = 'K'
tran[';'] = 'L'
tran['\''] = ';'
tran['X'] = 'Z'
tran['C'] = 'X'
tran['V'] = 'C'
tran['B'] = 'V'
tran['N'] = 'B'
tran['M'] = 'N'
tran[','] = 'M'
tran['.'] = ','
tran['/'] = '.'
tran[' '] = ' '


input_line = input()
for x in input_line:
    if x in tran:
        print(tran[x], end='')
    else:
        print(x, end='')
print('')