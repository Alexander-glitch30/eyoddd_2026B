# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack','ronway','palestina','carvajal'] # O(n)

def random_function(students):
    first = students[0] #O(1)
    total = 0 # O(1)
    new_list = [] # O(1)

    for student in students:
        print ("se le suma el total")
        total += 1 # O(n)
        new_list.append(student) # O(n)

    print(new_list) # O(1)
    return total # O(1)
print (f"tamaño de lista de alumnos: {len(student_list_01)}")
print(random_function(student_list_01))

# Calcular la complejidad del algoritmo: o(n)+o(1)+o(1)+O(1)+O(n)+O(n)+o(1)+o(1)
