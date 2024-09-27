def fake_bin(x):
    new = []
    for d in x:
        if d == '0' or d == '1' or d == '2' or d == '3' or d == '4':
            new.append('0')
        else:
            new.append('1')
    return ''.join(new)

print (fake_bin('939108'))