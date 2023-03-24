from typing import List

url = "https://leetcode.com/problems/find-common-characters/description/"


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        repeated_letters = []
        first_word = words[0]
        letters = {letter: 0 for letter in first_word}

        for letter in first_word:
            is_valid_letter = True
            letters[letter] += 1
            for word in words[1:]:
                if letter not in word or word.count(letter) < letters[letter]:
                    is_valid_letter = False
                    break

            if is_valid_letter:
                repeated_letters.append(letter)

        return repeated_letters
