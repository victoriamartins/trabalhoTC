class Transition:
    def __init__(self, transition):
        self.q_from = transition[0]
        self.read_tape1 = transition[1]
        self.read_tape2 = transition[2]
        self.read_tape3 = transition[3]
        self.q_next = transition[4]
        self.write_tape1 = transition[5]
        self.move_tape1 = transition[6]
        self.write_tape2 = transition[7]
        self.move_tape2 = transition[8]
        self.write_tape3 = transition[9]
        self.move_tape3 = transition[10]

