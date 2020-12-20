import random

class State(object):
    #https://tostr.pl/blog/implementation-of-finite-state-automata-in-python/
    def __init__(self, probability, final, *diagnoses):
        self.probability = probability
        self.final = final
        self.diagnoses = diagnoses
        self.transitions = {}

    def addTransition(self, probability, state):
        self.transitions[probability] = state

    def start(self):
        self.diagnoses = sorted(self.diagnoses, key=lambda x: x.power)
        power = random.uniform(0,1)
        previous = 0

        for index, diagnosis in enumerate(self.diagnoses):
            if power <= diagnosis.power + previous:
                print(diagnosis.name, ("" if self.final else "->"), end=" ")
                break
            else:
                previous += diagnosis.power

        if not self.final:
            probabilities = sorted(list(self.transitions.keys()))
            prob = random.uniform(0,1)
            previous = 0
            for probability in probabilities:
                if prob < probability + previous:
                    self.transitions[probability].start()
                    break
                else:
                    previous += probability
