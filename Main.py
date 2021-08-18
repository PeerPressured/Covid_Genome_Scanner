filename = 'Genome.txt'
file = open(filename,'r')
content = file.read().splitlines()
file.close()
genom = ''.join(content)
basensequenz = input('Fügen Sie hier die Genomsequenz ein').lower()
if basensequenz in genom:
    pass
else:
    print(False)
