import math,random
from .core import zero,hadamard,cnot,gate,probabilities

def execute(n,operations):
    state=zero(n)
    for op in operations:
        kind=op['gate'].lower()
        if kind=='h': state=hadamard(state,int(op['target']))
        elif kind=='x': state=gate(state,int(op['target']),[[0,1],[1,0]])
        elif kind=='ry':
            t=float(op['angle'])/2
            state=gate(state,int(op['target']),[[math.cos(t),-math.sin(t)],[math.sin(t),math.cos(t)]])
        elif kind=='cx': state=cnot(state,int(op['control']),int(op['target']))
        else: raise ValueError('unknown gate: '+kind)
    return state

def expectation_z(state,target):
    if target<0 or (1<<target)>=len(state):raise ValueError('invalid target')
    return sum((-1 if i&(1<<target) else 1)*p for i,p in enumerate(probabilities(state)))

def sample(state,shots,seed=0):
    if not isinstance(shots,int) or shots<0:raise ValueError('shots must be a nonnegative integer')
    probs=probabilities(state)
    if abs(sum(probs)-1)>1e-9:raise ValueError('state must be normalized')
    rng=random.Random(seed);counts={}
    width=(len(state)-1).bit_length()
    for index in rng.choices(range(len(state)),weights=probs,k=shots):
        label=format(index,f'0{width}b');counts[label]=counts.get(label,0)+1
    return counts
