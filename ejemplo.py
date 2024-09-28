from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes
from UTN_Heroes_Dataset.utn_funciones.auxiliares import color_text



print(len(matriz_data_heroes))

for dato in matriz_data_heroes[0]:
    print(color_text(dato))