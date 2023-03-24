url = "https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/"


class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        prefix = self._get_prefix(s)
        suffix = self._get_suffix(s)
        is_valid_string = prefix[0] == suffix[0]

        while is_valid_string:
            s = s[len(prefix):-len(suffix)]
            if len(s) <= 1:
                break
            prefix = self._get_prefix(s)
            suffix = self._get_suffix(s)

            if prefix[0] != suffix[0]:
                is_valid_string = False

        return len(s)

    @staticmethod
    def _get_prefix(s: str) -> str:
        prefix = s[0]
        for string in s[1:]:
            if string == prefix[0]:
                prefix += string
            else:
                break
        return prefix

    @staticmethod
    def _get_suffix(s: str) -> str:
        suffix = s[-1]
        for string in s[::-1][1:]:
            if string == suffix[0]:
                suffix += string
            else:
                break
        return suffix


if __name__ == "__main__":
    a = (
        Solution().minimumLength(
            "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
        )
    )
