import yaml
import os
from State import State
from Diagnosis import Diagnosis
from StateName import StateName
from Model import Model


def getDiagnosis(filename):
    with open(filename) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        states = dict()
        name = data['name']

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

        return name, states


def getModel():
    diagnoses = dict()
    for diagnosisFile in os.listdir('diagnoses/'):
        name, state = getDiagnosis('diagnoses/' + diagnosisFile)
        diagnoses[name] = Model(name, state)

    with open('model.yml') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        final = Model(StateName.final, None)

        for diagnosisNames in data['diagnoses']:
            if diagnosisNames in data['transition_probability']:
                for key, value in data['transition_probability'][diagnosisNames].items():
                    diagnoses[diagnosisNames].addTransition(value, diagnoses[key])
            if diagnosisNames in data['final_diagnoses']:
                for key, value in data['final_diagnoses'].items():
                    diagnoses[key].addTransition(value, final)

        initial = Model(StateName.initial, None)
        for key, value in data["start_diagnoses"].items():
            initial.addTransition(value, diagnoses[key])

        return initial
