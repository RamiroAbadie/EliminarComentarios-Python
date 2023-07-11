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
                print("-"*25 + f"i = {i}" + "-"*25)
                if Linea[i] != "\n":
                    if Linea[i] != '"' and not ComillasAbiertas:
                        if Linea[i] == "#":
                            Comentario = True
                        elif Linea[i] == "'":
                            print("-"*25)
                            print(f"{Linea}")
                            print(f"i == {i}")
                            print('Linea[i] == "\'"')
                            CantComillas = 1
                            print(f"CantComillas == {CantComillas}")
                            for c in range(i + 1, LargoLinea):
                                print("----Ciclo for----")
                                print(f"c == {c}")
                                print(f"Linea[c] == {Linea[c]}")
                                if Linea[c] == "'":
                                    print("Entro al if")
                                    CantComillas += 1
                                    print(f"CantComillas + 1 == {CantComillas}")
                                else:
                                    print("----BREAK----")
                                    break
                            if CantComillas >= 3 and not MultiLinea:
                                print("-MULTILINEA-")
                                print(f"CantComillas == {CantComillas}")
                                MultiLinea = True
                                print(f"MultiLinea == {MultiLinea}")
                                i = c - 1
                                print(f"(i = c) -> i == {i} -> c - 1 == {c}")
                            elif CantComillas >= 3 and MultiLinea:
                                print("-!!NO MULTILINEA!!-")
                                MultiLinea = False
                                print(f"MultiLinea == {MultiLinea}")
                                i = c
                                print(f"(i = c) -> i == {i} -> c - 1 == {c}")
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