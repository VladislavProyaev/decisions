url = "https://leetcode.com/problems/integer-to-english-words/description/"


class Solution:
    def numberToWords(self, num: int) -> str:
        ones = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine"
        ]
        tens = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen"
        ]
        twenties = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety"
        ]

        def evaluate(n):
            if n % 100 < 10:
                res = ones[n % 100]
                n //= 100
            elif n % 100 < 20:
                res = tens[n % 10]
                n //= 100
            else:
                res = ones[n % 10]
                n //= 10
                res = twenties[n % 10] + (" " + res if res else "")
                n //= 10
            if n > 0:
                return ones[n] + " Hundred" + ((" " + res) if res else "")
            return res

        if num == 0:
            return "Zero"

        thousands = ["", " Thousand", " Million", " Billion"]
        i = 0
        words = ""

        while num > 0:
            if num % 1000 != 0:
                words = (
                    evaluate(num % 1000)
                    + thousands[i]
                    + (" " + words if words else "")
                )
            num //= 1000
            i += 1

        return words.strip()
