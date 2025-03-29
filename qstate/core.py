"""Tiny statevector simulator. Qubit zero is the least significant bit."""
import math

def zero(n):
    if not 1 <= n <= 16:
        raise ValueError('qubit count must be between 1 and 16')
    return [1+0j] + [0j] * ((1 << n)-1)

def gate(state, target, matrix):
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise ValueError('expected a 2x2 matrix')
    if target < 0 or (1 << target) >= len(state):
        raise ValueError('target outside register')
    out = state.copy()
    for i in range(len(state)):
        if not i & (1 << target):
            j = i | (1 << target)
            out[i] = matrix[0][0]*state[i] + matrix[0][1]*state[j]
            out[j] = matrix[1][0]*state[i] + matrix[1][1]*state[j]
    return out

def hadamard(state, target):
    s = 1/math.sqrt(2)
    return gate(state, target, [[s,s],[s,-s]])

def cnot(state, control, target):
    if control == target or min(control,target) < 0 or (1 << max(control,target)) >= len(state):
        raise ValueError('invalid control or target')
    out = [0j]*len(state)
    for i, amplitude in enumerate(state):
        j = i ^ (1 << target) if i & (1 << control) else i
        out[j] = amplitude
    return out

def probabilities(state):
    return [abs(a)**2 for a in state]

