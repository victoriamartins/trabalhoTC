file_in = open('input.txt', 'r')

conteudo = file_in.readline()

inputs = conteudo.split()
entrada1 = inputs[0]
entrada2 = inputs[1]

# processos

file_in.close()

saida = ['1010']

file_out = open('output.txt', 'w')

file_out.writelines(saida)

file_out.close()
