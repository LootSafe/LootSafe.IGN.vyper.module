import pytest

@pytest.fixture
def ign_tester(t):
    from vyper import compiler
    t.languages['vyper'] = compiler.Compiler()
    contract_code = open('IGN.v.py').read()
    t.c = t.s.contract(contract_code, language='vyper', args=[t.accounts[0]])
    return t

def test_register(ign_tester):
    # Check that you can register an IGN
    assert ign_tester.c.register("Matt")
