import functions

def main():
    ruta = functions.def_ruta()
    functions.write_file(ruta)
    functions.read_file(ruta)
    
if __name__ == '__main__':
    main
