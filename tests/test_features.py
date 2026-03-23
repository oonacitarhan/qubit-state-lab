import math
from qstate.features import execute,sample,expectation_z
def test_ry():
    state=execute(1,[{'gate':'ry','target':0,'angle':math.pi}])
    assert abs(expectation_z(state,0)+1)<1e-12
def test_shot_support():
    state=execute(2,[{'gate':'h','target':0},{'gate':'cx','control':0,'target':1}])
    result=sample(state,500,7)
    assert sum(result.values())==500 and set(result)=={'00','11'}
    assert result==sample(state,500,7)
def test_bad_gate():
    try:execute(1,[{'gate':'bogus'}])
    except ValueError:return
    raise AssertionError('invalid gate accepted')
def test_normalization():
    try:sample([2+0j,0j],10)
    except ValueError:return
    raise AssertionError('unnormalized state accepted')
