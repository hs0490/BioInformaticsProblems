__author__ = 'parmeet.singh'

my_file = open("codontable.txt", 'r')
string_file = open("problemnine.txt")
table = {}


def convert(string):
    rna_string = string.replace('T', 'U')
    return rna_string


def fill_dic():
    table_data = my_file.read().splitlines()
    for index in range(0, len(table_data)):
        values = table_data[index].split()
        for index2 in range(0, len(values), 2):
            table[values[index2]] = values[index2 + 1]


def complement(st):
    rev_st = ""
    for index in range(0, len(st)):
        if st[index] == 'A':
            rev_st += 'T'

        elif st[index] == 'C':
            rev_st += 'G'

        elif st[index] == 'T':
            rev_st += 'A'

        elif st[index] == 'G':
            rev_st += 'C'
    rev_st = rev_st[::-1]
    return rev_st


def find_proteins(dna_string):
    actual = convert(dna_string)
    rna_string = convert(dna_string)
    list_of_indices = []
    while rna_string.find('AUG') != -1:
        list_of_indices.append(rna_string.find('AUG'))
        rna_string = rna_string.replace('AUG', 'BBB', 1)

    protein = ""
    list_of = []

    for i in range(0, len(list_of_indices)):

        for index in range(list_of_indices[i], len(rna_string)-2, 3):
            key = actual[index] + actual[index + 1] + actual[index + 2]
            if table[key] != 'Stop':
                protein = protein + table[key]
            elif table[key] == 'Stop':
                #print protein
                #list_of.append(protein)
                if not protein in list_of:
                    list_of.append(protein)
                protein = ""
                break
    return list_of


def possible_proteins():
    dna_data = string_file.read().split('>')
    for index in range(0, len(dna_data)):
        if dna_data[index] not in "":
            dna_string = dna_data[index][14:(len(dna_data[index]))].split('\n')
            data = ''.join(dna_string)

            dna_string2 = complement(data)
            list01 = find_proteins(data)
            list02 = find_proteins(dna_string2)
            protein_list = list(set(list01 + list02))
            for i in range(0,len(protein_list)):
                print protein_list[i]


fill_dic()
possible_proteins()