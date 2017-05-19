import util
from state import State


def validate(problem, solution):
    '''
    Return true if `solution` is a valid plan for `problem`.
    Otherwise, return false.

    OBSERVATION: you should check action applicability,
    next-state generation and if final state is indeed a goal state.
    It should give you some indication of the correctness of your planner,
    mainly for debugging purposes.
    '''
    ' YOUR CODE HERE '
    state = State(problem.init)
    for action in solution:
        if not action.precond <= state:
            print("Action not applicable!!!")
            return False
        state = state.difference(action.neg_effect).union(action.pos_effect)

    return problem.goal <= state
