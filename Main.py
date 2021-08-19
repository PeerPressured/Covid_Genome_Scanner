def sequenzenfinder(gen, seq):
    copy = gen
    displ = 0
    indizes = []
    while True:
        if seq in copy:
            index = copy.index(seq)
            indizes.append(index+displ)
            copy = copy[index+1:]
            displ += index+1
        else:
            return indizes



filename = 'LongCovid.txt'
file = open(filename,'r')
content = file.read().splitlines()
file.close()
genom = ''.join(content) #inhalt der text-datei beschönigt
basensequenz = input('Fügen Sie hier die Genomsequenz ein').lower()
if basensequenz in genom:
    print(sequenzenfinder(gen = genom, seq = basensequenz))
else:
    print(False)
