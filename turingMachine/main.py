def setTape(arq):
    linhas = arq.readlines()[0].split(' ')
    num1 = ['']
    num2 = ['']
    for i in linhas[0]:
        num1.append(str(i))
    for i in linhas[1]:
        num2.append(str(i))
    num1.append('')
    num2.append('')
    arq.close()
    return num1, num2


arq_input = open('input.txt', 'r')
tape1, tape2 = setTape(arq_input)

