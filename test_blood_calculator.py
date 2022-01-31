import pytest


@pytest.mark.parametrize("input_HDL, expected", [
    [70, "Normal"],
    [50, "Borderline Low"],
    [30, "Low"]
    ])
def test_check_HDL(input_HDL, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input_HDL)
    assert answer == expected


def test_check_HDL_2():
    from blood_calculator import check_HDL
    answer = check_HDL(50)
    assert answer == "Borderline Low"


def test_check_HDL_3():
    from blood_calculator import check_HDL
    answer = check_HDL(30)
    assert answer == "Low"
