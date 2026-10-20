#importando funcion array
#del modulo array 
#como arr
from array import array as arr

#importando una funcion de otro
#archivo
from s02t0102_1d import print_array 

my_array=arr('i',[2,10,15,20])

print ("-----antes de la eliminiacion-----")
print_array(my_array)

#eliminacion
try:
    my_array.remove(100)
except:
    print (f"no se encuentra en el arreglo")    

print ("-----despues de la eliminacion-----")
print_array(my_array)
  



