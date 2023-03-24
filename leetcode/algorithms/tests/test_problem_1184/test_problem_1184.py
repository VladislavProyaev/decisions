import pytest


@pytest.mark.parametrize(
    "distance, start, destination, expected_result",
    [
        ([1, 2, 3, 4], 0, 1, 1),
        ([1, 2, 3, 4], 0, 2, 3),
        ([1, 2, 3, 4], 0, 3, 4),
    ]
)
def test_problem(solution, distance, start, destination, expected_result):
    result = solution.distanceBetweenBusStops(distance, start, destination)
    assert result == expected_result


@pytest.mark.parametrize(
    "distance, start, destination, expected_result",
    [
        ([1, 2, 3, 4], 0, 1, 2),
        ([1, 2, 3, 4], 0, 2, 7),
    ]
)
def test_problem_with_error(
    solution, distance, start, destination, expected_result
):
    with pytest.raises(AssertionError):
        result = solution.distanceBetweenBusStops(distance, start, destination)
        assert result == expected_result
