x = int(input ("Введите число Х, отличное от  0:  "))
y = int(input ("Введите число Y, отличное от  0 :  "))
if x==0  or y==0 : print ("Число не должно быть равно  0")
if x>0 and y>0 : print ("Точка находится в плоскости 1")
if x>0 and y<0 : print ("Точка находится в плоскости 2")
if x<0 and y<0 : print ("Точка находится в плоскости 3")
if x<0 and y>0 : print ("Точка находится в плоскости 4")