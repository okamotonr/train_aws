'''test parrot module'''
from sample_pkg.parrot import parrot


def test_parrot():
    '''test parrot module'''
    message = 'Hello'
    expect = 'Hello'
    result = parrot(message)

    assert result == expect
