import pytest


@pytest.mark.parametrize(
    "nums1, nums2, expected_result",
    [
        ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
        ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),
    ]
)
def test_problem(solution, nums1, nums2, expected_result):
    assert solution.findDifference(nums1, nums2) == expected_result


@pytest.mark.parametrize(
    "nums1, nums2, expected_result",
    [
        ([1, 2, 3], [2, 4, 6], [[1], [4, 6]]),
        ([1, 2, 3, 3], [1, 1, 2, 2], [[], [3]]),
    ]
)
def test_problem_with_error(solution, nums1, nums2, expected_result):
    with pytest.raises(AssertionError):
        assert solution.findDifference(nums1, nums2) == expected_result
