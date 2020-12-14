from Transition import Transition
import sys
from collections import Counter


def set_tape(arq):
    lines = arq.readlines()
    if '#' in lines[0] and '0' in lines[0] and '1' in lines[0]:
        lines = lines[0].split('#')
        num1 = [' ']
        num2 = [' ']
        for b in lines[0]:
            num1.append(str(b))
        for b in lines[1]:
            num2.append(str(b))
        num1.append(' ')
        num2.append(' ')
        return num1, num2
    else:
        print('Entrada inválida.')
        sys.exit()


def read_split_transitions(tm_lines):
    transition_lines = tm_lines[6:41]
    transition_split = []
    for i in transition_lines:
        transition_split.append(i[0:23].split(','))
    return transition_split


def organize_transitions(splited_data):
    local_set = []
    for s in splited_data:
        local_set.append(Transition(s))
    return local_set


def search_transition(current, read1, read2, read3, set_transitions):
    for i in set_transitions:
        if current == i.q_from and read1 == i.read_tape1 and read2 == i.read_tape2 and read3 == i.read_tape3:
            return i
    return False


def move_settings(move, index):
    if move == 'R':
        return index+1
    elif move == 'L':
        return index-1
    elif move == 'S':
        return index


def write_out(vet_read):
    num = Counter(vet_read)
    if '1' in num:
        if num['1'] == 0 or num['1'] == 2:
            return '0'
        else:
            return '1'
    else:
        return '0'


arq_input = open('input.txt', 'r')
arq_machine = open('turing_machine.txt', 'r')
arq_output = open('output.txt', 'w')

content = arq_machine.readlines()

tape1, tape2 = set_tape(arq_input)
final_states = content[5][3:5]
current_state = content[3][3:5]

splited_transitions = read_split_transitions(content)
transitions = organize_transitions(splited_transitions)

tape3 = [' ']
flag_accepted = False
out = []

index_tape1 = 1
index_tape2 = 1
index_tape3 = 0

while True:
    res = search_transition(current_state, tape1[index_tape1], tape2[index_tape2], tape3[index_tape3], transitions)
    if not res:
        arq_output.write('Input rejected!')
        break
    else:
        if res.q_next == 'q6':
            flag_accepted = True
            break
        else:
            tape1[index_tape1] = res.write_tape1
            tape2[index_tape2] = res.write_tape2
            tape3[index_tape3] = res.write_tape3
            index_tape1 = move_settings(res.move_tape1, index_tape1)
            index_tape2 = move_settings(res.move_tape2, index_tape2)
            index_tape3 = move_settings(res.move_tape3, index_tape3)
            if current_state == 'q5':
                out.append(write_out([res.read_tape1, res.read_tape2, res.read_tape3]))
            current_state = res.q_next

if flag_accepted:
    out = out[::-1]
    for i in out:
        arq_output.write(i)
else:
    arq_output.write("Input rejected!")

arq_input.close()
arq_machine.close()
arq_output.close()
