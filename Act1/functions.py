TEXTO1 = 'Introdueix un text:  '
TEXTO2 = 'text.txt'

def read_file(fname):
    file = open(fname,'r')
    print(file.read())
    file.close()
    
def write_file(fname):
    maximo = 10
    frase = input(TEXTO1)
    if len(frase) > maxim:
        while len(frase) > maxim:
            frase = input(TEXTO1)
            file = open(fname,'w')
            file.write(frase)
            file.close()
    else:
        file = open(fname,'w')
        file.write(frase)
        file.close()
        
def def_ruta():
    x = TEXTO2
    return x
