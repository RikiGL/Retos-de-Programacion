'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''
def funcionAnagrama (p1, p2):
    if p1 == p2:
        return False
    elif len(p1) == len (p2):
        if sorted(p1.lower()) == sorted(p2.lower()):
            return True
    return False    

palabra1 = input ("Escriba una palabra: ")
palabra2 = input ("Escriba otra palabra: ")        

if funcionAnagrama (palabra1, palabra2):
    print("Son anagramas")
else:
    print("No son anagramas")




