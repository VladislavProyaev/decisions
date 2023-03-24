import pytest


@pytest.mark.parametrize(
    "words, expected_result",
    [
        (["bella", "label", "roller"], ["e", "l", "l"]),
        (["cool", "lock", "cook"], ["c", "o"]),
    ]
)
def test_problem(solution, words, expected_result):
    assert solution.commonChars(words) == expected_result


@pytest.mark.parametrize(
    "words, expected_result",
    [
        (["bella", "label", "roller"], ["e", "l"]),
        (["cool", "lock", "cook"], ["c", "o", "o"]),
    ]
)
def test_problem_with_error(solution, words, expected_result):
    with pytest.raises(AssertionError):
        assert solution.commonChars(words) == expected_result
