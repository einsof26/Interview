import pytest

from balancer import main

fixture = [('(((([{}]))))', 'Balanced'),
           ('[([])((([[[]]])))]{()}', 'Balanced'),
           ('}{}', 'Unbalanced'),
           ('{{[(])]}}', 'Unbalanced'),
]

@pytest.mark.parametrize("string, expected_result", fixture)
def test_main(string, expected_result):
    result = main(string)
    assert result == expected_result