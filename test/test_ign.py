import pytest

from ethereum.abi import ValueOutOfBounds
from ethereum.tools import tester

@pytest.fixture
def ign_tester(t):
    from vyper import compiler
    t.languages['vyper'] = compiler.Compiler()
    contract_code = open('IGN.v.py').read()
    t.c = t.s.contract(contract_code, language='vyper', args=[t.accounts[0]])
    return t
