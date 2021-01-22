import random
from StateName import StateName


class State:

    def __init__(self, name, diagnoses):
        self.name = name
        self.diagnoses = diagnoses
        self.transitions = dict()

    def addTransition(self, probability, state):
        self.transitions[state] = probability

    def generate(self):
        power = random.uniform(0, 1)
        previous = 0
        if self.name != StateName.initial or self.name != StateName.final:
            self.diagnoses = sorted(self.diagnoses, key=lambda x: x.probability)
            for diagnosis in self.diagnoses:
                if power <= diagnosis.probability + previous:
                    print(diagnosis.name, end=" ")
                    break
                else:
                    previous += diagnosis.probability
            power = random.uniform(0, 1)
            previous = 0

        self.transitions = dict(sorted(self.transitions.items(), key=lambda x: x[1]))
        for state, probability in self.transitions.items():
            if power <= probability + previous:
                state.generate()
                break
            else:
                previous += probability
