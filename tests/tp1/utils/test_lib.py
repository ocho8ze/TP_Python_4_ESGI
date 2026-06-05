from src.tp1.utils.lib import choose_interface

def test_when_choose_interface_then_return_empty_string():
    # When
    result = choose_interface()

    # Then
    assert result == ""
