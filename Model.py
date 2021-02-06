import random
from StateName import StateName


class Model:

    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.transitions = dict()

    def addTransition(self, probability, diagnosis):
         self.transitions[diagnosis] = probability

    def generate(self):
        power = random.uniform(0, 1)
        previous = 0
        self.transitions = dict(sorted(self.transitions.items(), key=lambda x: x[1]))

        for hmm, probability in self.transitions.items():
            if power <= probability + previous:
                if hmm.state is not None:
                    hmm.state[StateName.initial].generate()
                hmm.generate()
                break
            else:
                previous += probability
