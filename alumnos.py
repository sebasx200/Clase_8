def alumnos():

    alumnos = []
    respuesta = True

    while respuesta:

        alumno = []

        alumno.append(input("ingrese el nombre del alumno: \n"))
        alumno.append(float(input("ingrese la primera nota: \n")))
        alumno.append(float(input("ingrese la segunda nota: \n")))
        alumno.append(float(input("ingrese la tercera nota: \n")))

        alumnos.append(alumno)

        respuesta = input("¿Desea ingresar otro alumno?\nIngrese S para sí\nIngrese cualquier otra cosa para no")
        if respuesta == 's':

            respuesta = True
        else:
            respuesta = False

    if len(alumnos) > 0 :
        print("Listado de las nota de los alumnos")
        print("Nombre \t Nota1\t Nota2\t Nota3")
        for alumno in alumnos:
            print(alumno[0]+"\t" + str(alumno[1])+"\t\t" + str(alumno[2])+"\t\t" + str(alumno[3]))

    if len(alumnos) > 0 :
        print("\nListado de los promedios de los alumnos")
        print("Nombre: \t  Promedio")
        for alumno in alumnos:
            promedio = (alumno[1] + alumno[2] + alumno[3])/3
            print (alumno[0]+"\t" +str(round(promedio, 1)))

    if len(alumnos) > 0 :
        print("\nListado de los alumnos que perdieron la materia")
        print("Nombre: \t  Promedio")
        for alumno in alumnos:
            promedio = (alumno[1] + alumno[2] + alumno[3]) / 3
            if promedio < 3 :
                print(alumno[0]+"\t" + str(round( promedio, 1)))


