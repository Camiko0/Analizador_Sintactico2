import lexer_rules
import parser_rules

from ply.lex import lex
from ply.yacc import yacc

class Prueba_Completa:
    
    """ ABRIR ARCHIVO POSORDEN"""
    def abrir_archivo(self):
        #Abrir .txt con expresiones aritmeticas
        expresiones = open("expresiones.txt")
        linea = [" "]
        impresion = ''
        while linea != '':
            #Leer linea a linea del .txt
            linea = expresiones.readline().split(' ')
            if (linea == ['']):
                expresiones.close()
                break
            #Ejecutar Lexer y Parse
            lexer = lex(module=lexer_rules)
            parser = yacc(module=parser_rules)
            expression = parser.parse(' '.join(map(str, linea[:-1])).strip('[]'), lexer)
            #Resultado para el archivo
            impresion += "La respuesta para ["+' '.join(map(str, linea[:-1])).strip('[]')+"] es: "+str(expression)+'\n'
        return impresion

    """ AGREGAR EL RESULTADO AL ARCHIVO """   
    def escribir_archivo(self,resultado):
        busquedas = open("resultados.txt", "w")
        busquedas.write(resultado)
        busquedas.close()

prueba = Prueba_Completa()
salida = prueba.abrir_archivo()
prueba.escribir_archivo(salida)
