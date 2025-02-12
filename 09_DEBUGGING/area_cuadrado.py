def calcular_area_cuadrado(lado):
    """Calcula el area de un cuadrado al recibir el lado como parametro"""
    area = lado * lado
    return area


lado_cuadrados = [2, 3, 4, 5, 6, 7, 8, 9, 10]
area_cuadrados = []
for lado in lado_cuadrados:
    area = calcular_area_cuadrado(lado)
    area_cuadrados.append(area)
    
    """python -m pdb area_cuadrado.py """
    
    """
    python -m pdb area_cuadrado.py 
> e:\practicas\cursoinlearnig\09_debugging\area_cuadrado.py(1)<module>()
-> def calcular_area_cuadrado(lado):
(Pdb) break 8
Breakpoint 1 at e:\practicas\cursoinlearnig\09_debugging\area_cuadrado.py:8
(Pdb) l
  1  -> def calcular_area_cuadrado(lado):
  2         Calcula el area de un cuadrado al recibir el lado como parametro
  3         area = lado * lado
  4         return area
  5
  6
  7     lado_cuadrados = [2, 3, 4, 5, 6, 7, 8, 9, 10]
  8 B   area_cuadrados = []
  9     for lado in lado_cuadrados:
 10         area = calcular_area_cuadrado(lado)
 11         area_cuadrados.append(area)
(Pdb) continue
> e:\practicas\cursoinlearnig\09_debugging\area_cuadrado.py(8)<module>()
-> area_cuadrados = []
(Pdb) next
> e:\practicas\cursoinlearnig\09_debugging\area_cuadrado.py(9)<module>()
-> for lado in lado_cuadrados:
(Pdb)
    """