import yaml
from State import State
from Diagnosis import Diagnosis
from StateName import StateName


def getModel(filename):
    with open(filename) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        states = dict()
        for state in data['states']:
            diagnoses = []
            for key, value in data['diagnoses'][state].items():
                diagnoses.append(Diagnosis(key, value))
            states[state] = State(state, diagnoses)

        for state in data['states']:
            if state in data['transition_probability']:
                for key, value in data['transition_probability'][state].items():
                    states[state].addTransition(value, states[key])

        initial = State(StateName.initial, [])
        for key, value in data["start_states"].items():
            initial.addTransition(value, states[key])
        states[StateName.initial] = initial

        final = State(StateName.final, [])
        for key, value in data["final_states"].items():
            final.addTransition(value, states[key])
        states[StateName.final] = final

        return states
