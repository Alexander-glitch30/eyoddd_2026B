
"""
NOTAS:
1. Identifco el tamaño de la entrada "n"
El tamaño de la entrada es el numero
de estudiantes.

2. Es ver cuanto crece el numero de
operaciones en mi algoritmo conforme
creece el tamaño de la entrada
Agrego las bigO identificadas
Teniendo en cuenta la Cota superior asintotica
O(n) + O(4) = O(n+4) = O(n)
""" 
#creando una lista de estudiantes
student_list_01=['jordan','pipen','curry','shack']
student_list_01=['mike','sant','walker','lesay']


#verificando precencia de estudiante
def check_student(input_student, student_list):
    for student in student_list:
        if input_student==student: #o(n)
            print("estudiante encontrado👍")#o(1)
            return student#o(1)
    #si no encuentro al estudiante 
    print ("estuante nno encontrado❌")#o(1)
    return None#o(1)

#probando algoritmo
check_student("walter", student_list_01)#o(1)
