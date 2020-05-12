# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import pymysql.cursors  

def realizarConsulta(consulta, terminacion):
    consulta = consulta + terminacion
    print(consulta)
 
    # Connect to the database.
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password ='adrianseguraortiz1999',
                                 db='farmacos_bd',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
     
    try:
        
        with connection.cursor() as cursor:

            cursor.execute(consulta)
            print()
            for row in cursor:
                print (row)   
            print()
            
    finally:
    # Close connection.
        connection.close()

def llegamosAHoja(consulta, terminacion):
    fase4 = False
    fin = False
    while not fase4:
        print(''' ¿Qué desea hacer? 
              - Consultar ya: Consultar
              - Añadir otra condición: Añadir''')
        palabra = input('Escribe opción: ')
        if palabra == 'Consultar':
            realizarConsulta(consulta, terminacion)
            fase4 = True
            fin = True
        elif palabra == 'Añadir':
            fase4 = True
    return fin
        
    
consulta = 'SELECT * FROM '
fase1 = False
cambioTabla = False
while not fase1 :
    
    if not cambioTabla: 
        print('''¿Qué desea buscar? 
          - Medicamentos: Med 
          - Principios activos: PrinAct
          - Salir y abandonar la búsqueda: Salir''')
        palabra = input('Escribe clave: ')
    
    if palabra == 'Med':
        consulta = consulta + 'Medicamentos WHERE '
        fase2 = False
        while not fase2 :
            if not cambioTabla:
                
                print('''Elija el atributo del que quiera concretar información 
                      - Código nacional: Cod 
                      - Nombre: Nom 
                      - Vía de administración: Via 
                      - Presentación: Pres 
                      - Formato: For 
                      - Clase de medicamento: CMed
                      - Indicaciones: Ind
                      - Comercialización: Com
                      - Prescripción médica: PMed
                      - PVP: PVP
                      - Añadir condiciones a cumplir por alguno de
                      sus principios activos: CPin
                      - Realizar consulta sin condiciones: CSinCon
                      - Atrás: Atras
                      - Salir y abandonar la búsqueda: Salir''')
            else:
                
                print('''Elija el atributo del que quiera concretar información 
                      - Código nacional: Cod 
                      - Nombre: Nom 
                      - Vía de administración: Via 
                      - Presentación: Pres 
                      - Formato: For 
                      - Clase de medicamento: CMed
                      - Indicaciones: Ind
                      - Comercialización: Com
                      - Prescripción médica: PMed
                      - PVP: PVP
                      - Salir y abandonar la búsqueda: Salir''')
                  
            palabra = input('Escribe clave: ')
            
            if palabra == 'Cod':
                consulta = consulta + 'codigoNacional '
                fase3 = False
                while not fase3:
                    codigo = input('Escribe código a buscar:')
                    consulta = consulta + '= ' + codigo + ' ';
                    if cambioTabla: terminacion = '));'
                    else: terminacion = ';'
                    fin = llegamosAHoja(consulta, terminacion)
                    if not fin: consulta = consulta + 'AND '
                    fase3 = True
                    fase2 = fin
                    fase1 = fin
            elif palabra == 'Nom':
                consulta = consulta + 'nombre '
                fase3 = False
                while not fase3:
                    nombre = input('Escribe nombre a buscar:')
                    consulta = consulta + '= ' +'"'+ nombre +'"' + ' ';
                    if cambioTabla: terminacion = '));'
                    else: terminacion = ';'
                    fin = llegamosAHoja(consulta, terminacion)
                    if not fin: consulta = consulta + 'AND '
                    fase3 = True
                    fase2 = fin
                    fase1 = fin
            elif palabra == 'Via':
                consulta = consulta + 'viaAdministracion '   
                fase3 = False
                while not fase3:
                    via = input('Escribe via de administración a buscar:')
                    consulta = consulta + '= ' +'"'+ via+ '"' + ' ';
                    if cambioTabla: terminacion = '));'
                    else: terminacion = ';'
                    fin = llegamosAHoja(consulta, terminacion)
                    if not fin: consulta = consulta + 'AND '
                    fase3 = True
                    fase2 = fin
                    fase1 = fin                
            elif palabra == 'Pres':
                consulta = consulta + 'presentacion '
                fase3 = False
                while not fase3:
                    presen = input('Escribe presentación a buscar:')
                    consulta = consulta + '= ' +'"'+ presen + '"' + ' ';
                    if cambioTabla: terminacion = '));'
                    else: terminacion = ';'
                    fin = llegamosAHoja(consulta, terminacion)
                    if not fin: consulta = consulta + 'AND '
                    fase3 = True
                    fase2 = fin
                    fase1 = fin
            elif palabra == 'For':
                consulta = consulta + 'formato '
                fase3 = False
                while not fase3:
                    forma = input('Escribe formato a buscar:')
                    consulta = consulta + 'LIKE ' +'"%'+ forma + '%"' + ' ';
                    if cambioTabla: terminacion = '));'
                    else: terminacion = ';'
                    fin = llegamosAHoja(consulta, terminacion)
                    if not fin: consulta = consulta + 'AND '
                    fase3 = True
                    fase2 = fin
                    fase1 = fin
            elif palabra == 'CMed':
                consulta = consulta + 'claseMedicamento '
                fase3 = False
                while not fase3:
                    clase = input('Escribe la clase de medicamento a buscar:')
                    consulta = consulta + 'LIKE ' +'"%'+ clase + '%"' + ' ';
                    if cambioTabla: terminacion = '));'
                    else: terminacion = ';'
                    fin = llegamosAHoja(consulta, terminacion)
                    if not fin: consulta = consulta + 'AND '
                    fase3 = True
                    fase2 = fin
                    fase1 = fin
            elif palabra == 'Ind':
                consulta = consulta + 'indicaciones '
                fase3 = False
                while not fase3:
                    indi = input('Escribe un sintoma a buscar:')
                    consulta = consulta + 'LIKE ' +'"%'+ indi + '%"' + ' ';
                    if cambioTabla: terminacion = '));'
                    else: terminacion = ';'
                    fin = llegamosAHoja(consulta, terminacion)
                    if not fin: consulta = consulta + 'AND '
                    fase3 = True
                    fase2 = fin
                    fase1 = fin
            elif palabra == 'Com':
                consulta = consulta + 'comerzializacion '
                fase3 = False
                while not fase3:
                    comer = input('Escribe si el medicamento esta en el mercado (True o False):')
                    consulta = consulta + '= ' +'"'+ comer + '"' + ' ';
                    if cambioTabla: terminacion = '));'
                    else: terminacion = ';'
                    fin = llegamosAHoja(consulta, terminacion)
                    if not fin: consulta = consulta + 'AND '
                    fase3 = True
                    fase2 = fin
                    fase1 = fin
            elif palabra == 'PMed':
                consulta = consulta + 'prescripcionMedica '
                fase3 = False
                while not fase3:
                    presc = input('Escribe si necesita prescipción(True o False):')
                    consulta = consulta + '= ' + presc  + ' ';
                    if cambioTabla: terminacion = '));'
                    else: terminacion = ';'
                    fin = llegamosAHoja(consulta, terminacion)
                    if not fin: consulta = consulta + 'AND '
                    fase3 = True
                    fase2 = fin
                    fase1 = fin
            elif palabra == 'PVP':
                consulta = consulta + 'pvp '
                fase3 = False
                while not fase3:
                    print('''Seleccione la condición de búsqueda
                          Mayor que: >
                          Mayor o igual que: >=
                          Menor que: <
                          Menor o igual que: <=''')
                    condicion = input('Escribe condición:')
                    precio = input('Indique el precio: ')
                    consulta = consulta + ' ' + condicion + ' ' + precio + ' ';
                    if cambioTabla: terminacion = '));'
                    else: terminacion = ';'
                    fin = llegamosAHoja(consulta, terminacion)
                    if not fin: consulta = consulta + 'AND '
                    fase3 = True
                    fase2 = fin
                    fase1 = fin
            elif palabra == 'CPin' and not cambioTabla:
                consulta = consulta + 'codigoNacional IN (SELECT MEDICAMENTOS_codigoNacional FROM med_tienen_pa  WHERE PRINCIPIOSACTIVOS_nombre IN (SELECT Nombre FROM '		                             									                                  
                fase2 = True 
                cambioTabla = True  
                palabra = 'PrinAct'                                                                               
            elif palabra == 'CSinCon' and not cambioTabla:
                consulta = 'SELECT * FROM Medicamentos'
                realizarConsulta(consulta, ';')
                fase1 = True
                fase2 = True
            elif palabra == 'Atras' and not cambioTabla:
                consulta = 'SELECT * FROM '
                fase2 = True
            elif palabra == 'Salir':
                fase1 = True
                fase2 = True
            
    elif palabra == 'PrinAct':
        consulta = consulta + 'principios_activos WHERE '
        fase2 = False
        while not fase2 :
            if not cambioTabla:  
                print('''Elija el atributo del que quiera concretar información  
                      - Nombre principio activo: Nom
                      - Peso molecular: Peso
                      - Fórmula molecular: Form
                      - Realizar consulta sin condiciones: CSinCon
                      - Añadir condiciones a cumplir por alguno 
                      de sus medicamentos: CMed
                      - Atrás: Atras
                      - Salir y abandonar la búsqueda: Salir''')
            else:
                print('''Elija el atributo del que quiera concretar información  
                      - Nombre principio activo: Nom
                      - Peso molecular: Peso
                      - Fórmula molecular: Form
                      - Salir y abandonar la búsqueda: Salir''')
                  
            palabra = input('Escribe clave: ')
            
            if palabra == 'Nom':
                consulta = consulta + 'Nombre '
                fase3 = False
                while not fase3:
                    nombre = input('Escribe el principio activo a buscar:')
                    consulta = consulta + '= ' + '"'+ nombre + '"'  + ' ';
                    if cambioTabla: terminacion = '));'
                    else: terminacion = ';'
                    fin = llegamosAHoja(consulta, terminacion)
                    if not fin: consulta = consulta + 'AND '
                    fase3 = True
                    fase2 = fin
                    fase1 = fin
            elif palabra == 'Peso':
                consulta = consulta + 'pesoMolecular'
                fase3 = False
                while not fase3:
                    print('''Seleccione la condición de búsqueda
                          Mayor que: >
                          Mayor o igual que: >=
                          Menor que: <
                          Menor o igual que: <=''')
                    condicion = input('Escribe condición:')
                    peso = input('Escribe el peso molecular a buscar:')
                    consulta = consulta + ' ' + condicion + ' ' + peso + ' ';
                    if cambioTabla: terminacion = '));'
                    else: terminacion = ';'
                    fin = llegamosAHoja(consulta, terminacion)
                    if not fin: consulta = consulta + 'AND '
                    fase3 = True
                    fase2 = fin
                    fase1 = fin
            elif palabra == 'Form':
                consulta = consulta + 'formulaMolecular '
                fase3 = False
                while not fase3:
                    formula = input('Escribe un elemento quimico de la formula a buscar:')
                    consulta = consulta + 'LIKE ' + '"%'+ formula + '%"'  + ' ';
                    if cambioTabla: terminacion = '));'
                    else: terminacion = ';'
                    fin = llegamosAHoja(consulta, terminacion)
                    if not fin: consulta = consulta + 'AND '
                    fase3 = True
                    fase2 = fin
                    fase1 = fin
            elif palabra == 'CMed' and not cambioTabla:
                consulta = consulta + 'nombre IN (SELECT PRINCIPIOSACTIVOS_nombre FROM med_tienen_pa  WHERE MEDICAMENTOS_codigoNacional IN (SELECT codigoNacional FROM '		                             									                                  
                fase2 = True 
                cambioTabla = True  
                palabra = 'Med'

            elif palabra == 'CSinCon' and not cambioTabla:
                consulta = 'SELECT * FROM principios_activos'
                realizarConsulta(consulta, ';')
                fase1 = True
                fase2 = True
            elif palabra == 'Atras' and not cambioTabla:
                consulta = 'SELECT * FROM '
                fase2 = True
            elif palabra == 'Salir':
                fase1 = True
                fase2 = True
    
    
        
    elif palabra == 'Salir':
        fase1 = True
    
                
