#importando funcion array
#del modulo array 
#como arr
from array import array as arr

#importando una funcion de otro
#archivo
from s02t0102_1d import print_array 

my_array=arr('i',[2,10,15,20])

print ("-----antes de la insercion-----")
print_array(my_array)

#insercion 
my_array.insert(1,90)
print ("-----despues de la insercion-----")
print_array(my_array)

print ("-----despues de un append-----")
my_array.append(1000)
print_array(my_array)

print ("-----simular un append con insert-----")
my_array.insert(len(my_array),90000)
print_array(my_array)
