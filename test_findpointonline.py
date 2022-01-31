# test for function "find point on line"

def test_calculate_y():
    from findpointonline import calculate_y
    answer = calculate_y((1, 2), (2, 4), 8)
    assert answer == 16


def test_determine_point():
    from findpointonline import determine_point
    answer = determine_point((1, 2), (2, 4), (8, 16))
    assert answer == True
