__author__ = 'hs0490'


class CountingNucleotide:
    def countnucleotide(dnastring):
        print dnastring.count('A'),
        print dnastring.count('C'),
        print dnastring.count('G'),
        print dnastring.count('T')
    dnastring = 'GTGATCTCGGTATAACGCATACACCCCTGAACTCACATGGAATATCATCCAGGTGCTAGAATTTCAAGCAAGTGCAACGCCCAGGCGCCGAACGTCGGGGTCGAACGTACTAAATTGAATGGTGGATGCATCGACGGACAAAGATTGACAGGTCCTTATCGATGTTGTTGTATGTAGTCACTCGCTGTTATTGTGAAACTGGCCTCCCAAGCAGCGGCCAACGATGTTACCGCCTCAACATGTCACACGTCTCTGTCTGTCGGCACAATCCATCGTTCTAAAGTCCAAATGATTTTCCTCTTTATTGTACGGGTGGGGGTAGGGGACGCTCGTGAATCCGCCCGGAATCAATAGGGGGCGACTAACCGTTAGAGTGCCCTATACTCGCATACGCTGGATACTTGCATAAGGTGTGTGTCGGAACATCTACGTCGGAATCGGAGATAAGGTGAGCGATGGCCCCGACCCAGGTGTTCTAAACCATAGCTACGTCATCAGGGATTCGGATACTGTCCGGCCGAAGCAATCTAGCCGGGGATCGGTCCGTTTAAAATAGTCGGAGTAAGCGCCCGGCCTACATGTATAGTTGACCTCGTTTAATCGCAACGCCCTGAGCCACGAGGGAGAGAGCCGAGGGAGCATAGTTCGCCTTCAGGCCGGTTGGACATTTTGTGTCGAAAAGCGAGCAGGAATGGCCTGGGTGATTTCAGACAGAAGGCTGGAGGGATGCCTAGGAGTTGGGGTCTGGATGTGGAATAGGTAGGTTCAACAAATGAATTCTACACTATTTACGTCGCGTACTATTGCTTCAGTCCATCTAGCGGCATTGACTGACCCACT'
    countnucleotide(dnastring)


