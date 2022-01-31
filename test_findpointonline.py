# test for function "find point on line"

def test_find_y():
    from findpointonline import find_y
    answer = find_y((1, 2), (2, 4), 8)
    assert answer == 16
