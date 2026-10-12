#arrays
#from array import
import array as arr

#crescion de un arreglo
# 1: entero con signo
# 2: entero sin signo
# f: numero decimal 
# d: numero decimal doble 
# u: caracteres unicos 
my_array=arr.array('i',[10,22,300,3,7,40,35,9,10,340,45])

#iteracion automatica
#for num in my_array:
#    print (num)

#acceso individual a los elementos
#print (my_array[0]) #primer elemento
#print (my_array[1]) #segundo elemento
#print (my_array[3]) #tercer elemento

#tamaño de arreglo
#
#print (len(my_array))

#interacion por indices
for i in range (len(my_array)):
     if my_array [i]%2==0:
        print(f"elemento num {i+1}:{my_array[i]}")