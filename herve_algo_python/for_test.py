def getNumber ():
    while type:
        print ('Saisir un nombre: ', end = '')
        getTempNumber=input ()
        try:
            getTempNumber=int(getTempNumber)
        except ValueError:
            print ('"'+  getTempNumber + '"' + ' - pas de nombre')
        else:
            break
       
a = getNumber ()
print (a)

"""
def getNumber ():     # Ввод числа и проверка что число это не текст
     while type:
         print ('Введите число:', end = '')
         getTempNumber=input ()                      # Ввод числа
         try:                                        # Проверка что getTempNumber преобразоваывается в чило без ошибки
             getTempNumber=int(getTempNumber)
         except ValueError:                          # Проверка на ошибку неверного формата (введены буквы)
             print ('"'+  getTempNumber + '"' + ' - не является числом')
         else:                                       # Если getTempNumber преобразован в число без ошибки, выход из цикла while
             break
     return abs (getTempNumber) # возращает модуль getTempNumber (для искл. отрицат. чисел)
 a = getNumber ()
 print (a)
"""