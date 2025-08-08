from qstate.core import *

def self_test():
    state = cnot(hadamard(zero(2), 0), 0, 1)
    p = probabilities(state)
    assert all(abs(a-b)<1e-12 for a,b in zip(p,[.5,0,0,.5]))
    assert abs(sum(p)-1)<1e-12
    assert all(abs(a-b)<1e-12 for a,b in zip(hadamard(hadamard(zero(2),1),1),zero(2)))
    assert cnot(cnot(zero(2),0,1),0,1) == zero(2)
    return p

def test_original_reference_cases():
    self_test()
