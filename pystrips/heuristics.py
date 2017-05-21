# Nome: Angelo Gregorio Lovatto
# Numero Usp: 9293435

import util
from state import State

def h_naive(state, planning):
    return 0


def h_add(state, planning):
    '''
    Return heuristic h_add value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    ' YOUR CODE HERE '

    h = {}
    for atom in state:
        h[atom] = 0        
    x = State(state)
    goal = planning.problem.goal
    
    # To keep track of changes to state size
    current = len(x)
    last = 0

    while current != last:
        last = current

        for action in planning.applicable(x):
            effect = action.pos_effect
            x = x.union(effect)

            h_sum = sum(h[atom] for atom in action.precond)

            for atom in effect:
                if atom in h:
                    h[atom] = min(h[atom], 1 + h_sum)
                else:
                    h[atom] = 1 + h_sum

        current = len(x)

    hgoal_sum = 0
    for atom in goal:
        hgoal_sum += h[atom] if atom in h else util.sys.maxsize
    return hgoal_sum

def h_max(state, planning):
    '''
    Return heuristic h_max value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    ' YOUR CODE HERE '

    h = {}
    for atom in state:
        h[atom] = 0
        
    x = State(state)
    goal = planning.problem.goal
    # To keep track of changes to state size
    current = len(x)
    last = 0

    while current != last:
        last = current

        for action in planning.applicable(x):
            effect = action.pos_effect
            x = x.union(effect)

            h_max = max(h[atom] for atom in action.precond)

            for atom in effect:
                if atom in h:
                    h[atom] = min(h[atom], 1 + h_max)
                else:
                    h[atom] = 1 + h_max

        current = len(x)

    for atom in goal:
        if atom not in h:
            h[atom] = util.sys.maxsize
        
    return max(h[atom] for atom in goal)    

def h_ff(state, planning):
    '''
    Return heuristic h_ff value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    util.raiseNotDefined()
    ' YOUR CODE HERE '
