from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes


def mostrar_lista_matriz ():
    cantidad_columnas = len(matriz_data_heroes[0])
    cantidad_filas = len(matriz_data_heroes)
    for indice in range(cantidad_columnas):
        texto = ""
        for sub_indice in range(cantidad_filas):
            
            if type(matriz_data_heroes[sub_indice][indice]) == str:
                
                if len(matriz_data_heroes[sub_indice][indice]) >= 20:
                    texto_original = matriz_data_heroes[sub_indice][indice]
                    texto_saneado = texto_original[:19]
                    texto += f"{texto_saneado:20} | "
                else:
                    texto += f"{matriz_data_heroes[sub_indice][indice]:20} | "
                
            elif type(matriz_data_heroes[sub_indice][indice]) == int:
                texto += f"{matriz_data_heroes[sub_indice][indice]:03} | "
                
            elif type(matriz_data_heroes[sub_indice][indice]) == float:
                texto += f"{matriz_data_heroes[sub_indice][indice]:8.2f} | "
                
            else:
                texto += f"{matriz_data_heroes[sub_indice][indice]} | "
                
                
        texto = texto[0 : -3]
        print(texto)