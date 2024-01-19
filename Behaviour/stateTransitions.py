from transitions import Machine
import random

class Estudante(object):
    states = ['Acordando', 'Estudando', 'Tomando cafe', 'Jogando', 'Dormindo']

    def __init__(self, name):
        self.name = name
        self.period = 3
        self.machine = Machine(model=self, states = Estudante.states, initial='Dormindo')
        self.machine.add_transition(trigger='acordar', source='Dormindo', dest='Acordando')
        self.machine.add_transition('cafeinado', 'Tomando cafe', 'Estudando')
        self.machine.add_transition('estudado', 'Estudando', 'Jogando')
        self.machine.add_transition('dormir', 'Jogando', 'Dormindo')
        self.machine.add_transition('cafeina', 'Acordando', 'Tomando cafe')

eu = Estudante('Pedro')
print(eu.state)

eu.acordar()
print(eu.state)
eu.cafeina()
print(eu.state)
eu.cafeinado()
print(eu.state)
eu.estudado()
print(eu.state)
eu.dormir()
print(eu.state)


