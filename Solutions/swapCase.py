def swapcase(s):
    sample = ''
    #s = 'PytHoN'
    for i in s:
        if i.islower():
            sample = sample + i.upper()
        else:
            sample = sample + i.lower()
    return sample
print(swapcase('PytHoN12'))
