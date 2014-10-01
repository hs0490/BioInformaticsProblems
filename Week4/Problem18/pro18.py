__author__ = 'Umar Quadri'
def long_substr(dnastring_list):
    substr = ''
    if len(dnastring_list) > 1 and len(dnastring_list[0]) > 0:
        for i in range(len(dnastring_list[0])):
            for j in range(len(dnastring_list[0])-i+1):
                if j > len(substr) and all(dnastring_list[0][i:i+j] in x for x in dnastring_list):
                    substr = dnastring_list[0][i:i+j]

    return substr




with open('/media/hs0490/Sharedrive/PycharmWorkspace/CS696/Week4/Problem18/Problem18.txt') as f:
    lines = [line.rstrip('\n') for line in f]
lines=''.join(lines)
lines=lines.split('>Rosalind_')
y=[s[4:] for s in lines]
y.pop(0)
print long_substr(y)



