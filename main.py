from State import State
from Diagnosis import Diagnosis

def main():
    diagnos1 = Diagnosis('DIAGNOSIS 1', 0.8)
    diagnos2 = Diagnosis('DIAGNOSIS 2', 0.2)
    diagnos3 = Diagnosis('DIAGNOSIS 3', 0.1)
    diagnos4 = Diagnosis('DIAGNOSIS 4', 0.3)
    diagnos5 = Diagnosis('DIAGNOSIS 5', 0.5)
    diagnos6 = Diagnosis('DIAGNOSIS 6', 0.7)

    initial = State(1, False, diagnos1, diagnos2)
    state2 = State(1, False, diagnos2, diagnos4, diagnos5)
    state3 = State(1, True, diagnos2, diagnos3, diagnos6)

    initial.addTransition(1, state2)
    state2.addTransition(0.75, initial)
    state2.addTransition(0.25, state3)

    initial.start()

if __name__ == '__main__':
    main()
