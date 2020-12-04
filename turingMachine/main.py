from Transition import Transition


def set_tape(arq):
    lines = arq.readlines()[0].split(' ')
    num1 = ['']
    num2 = ['']
    for i in lines[0]:
        num1.append(str(i))
    for i in lines[1]:
        num2.append(str(i))
    num1.append('')
    num2.append('')
    return num1, num2


def read_final_states(tm_lines):
    f_states = tm_lines[5][3:11].split(',')
    return f_states


def read_split_transitions(tm_lines):
    transition_lines = tm_lines[6:44]
    transition_split = []
    for i in transition_lines:
        transition_split.append(i[0:23].split(','))
    return transition_split


def organize_transitions(splited_data):
    local_set = []
    for i in splited_data:
        local_set.append(Transition(i))
    return local_set


arq_input = open('input.txt', 'r')
arq_machine = open('turing_machine.txt', 'r')

content = arq_machine.readlines()

tape1, tape2 = set_tape(arq_input)
final_states = read_final_states(content)

splited_transitions = read_split_transitions(content)
transitions = organize_transitions(splited_transitions)


arq_input.close()
arq_machine.close()

