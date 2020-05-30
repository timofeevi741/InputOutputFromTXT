forinput=open('input.txt', 'r') # r - read - для считывания из файла
foroutput=open('output.txt', 'w') # w - write - для вывода от начала
a=int(forinput.readline())
b=int(forinput.readline())
foroutput.write(str(a+b))
