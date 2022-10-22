print((lambda x: 'ra' in x)(input()))
exit()
contains = lambda s, sample='ra': sample in s
s = input()
print(contains(s))