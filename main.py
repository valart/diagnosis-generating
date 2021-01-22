import Parser
from StateName import StateName


def main():
    HMM = Parser.getModel('configuration1.yml')
    for _ in range(10):
        HMM[StateName.initial].generate()
        print()


if __name__ == '__main__':
    main()
