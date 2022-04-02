def soma_1(numero):
    return int(numero) + 1


def test_soma_1():
    assert soma_1(41) == 42


def test_soma_1_numero_como_string():
    assert soma_1("41") == 42
