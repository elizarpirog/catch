from config import MIN_LENGTH

class PalindromeDetector:

    def find(

        self,

        words

    ):

        result = []

        for word in words:

            if (

                len(word) >= MIN_LENGTH

                and

                word == word[::-1]

            ):

                result.append(

                    word

                )

        return result
