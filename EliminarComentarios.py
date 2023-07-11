# Ramiro Abadie - Programacion I - 1-6

def EliminarComentarios(NombreProg, NombreProgNuevo):
    '''Elimina los comentarios de un codigo'''
    try:
        Programa = open(NombreProg, "rt")
        Nuevo = open(NombreProgNuevo, "wt")
        MultiLinea = False
        
        for Linea in Programa:
            i = 0
            ComillasAbiertas = False
            Comentario = False
            LargoLinea = len(Linea)
            while i < LargoLinea:
                if Linea[i] != "\n":
                    if Linea[i] != '"' and not ComillasAbiertas:
                        if Linea[i] == "#":
                            Comentario = True
                        elif Linea[i] == "'":
                            CantComillas = 1
                            for c in range(i + 1, LargoLinea):
                                if Linea[c] == "'":
                                    CantComillas += 1
                                else:
                                    break
                            if CantComillas >= 3 and not MultiLinea:
                                MultiLinea = True
                                i = c - 1
                            elif CantComillas >= 3 and MultiLinea:
                                MultiLinea = False
                                i = c
                            elif CantComillas < 3 and not MultiLinea:
                                ComillasAbiertas = True
                    elif Linea[i] == '"' and not ComillasAbiertas:
                        ComillasAbiertas = True
                    elif (Linea[i]=='"' or Linea[i]=="'") and ComillasAbiertas:
                        ComillasAbiertas = False
                    
                    if not Comentario and not MultiLinea:
                        Nuevo.write(Linea[i])
                else:
                    Nuevo.write(Linea[i])
                i += 1
        
    except FileNotFoundError as Error:
        print(f"No se puede abrir el archivo: {Error}")
    except OSError as Error:
        print(f"No se puede abrir el archivo: {Error}")
    finally:
        try:
            Programa.close()
            Nuevo.close()
        except NameError:
            pass
    

def main():
    NombreProg = "Prog.txt"
    NombreProgNuevo = "Prog-SinComentarios.txt"
    
    EliminarComentarios(NombreProg, NombreProgNuevo)
    print("----Finalizado con exito----")
    
main()