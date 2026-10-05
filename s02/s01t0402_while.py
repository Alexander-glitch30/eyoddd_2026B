"""
escribir un programa que calcule
 la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa
calculara la suma del 1 al 100
42 usando un ciclo while
"""
#importar la biblioteca de tiempo
import time
#crear las variables para
#el programa
n=100
the_sum=0
#tomando el t1
timestamp_01=time.time()
#iniciando la suma
while (n>0):
    the_sum=the_sum+n #100+99+98+...+
    n=n-1
#tomando el t2
timestamp_02=time.time()

#imprimimos la solucion
print(f"la suma es{the_sum}")

elapsed_time=round((timestamp_02-timestamp_01)*1e6,2)
print (f"tiempo de ejecucion:{elapsed_time}us")
