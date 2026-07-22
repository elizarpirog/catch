from collections import Counter

class Statistics:

    def build(

        self,

        words,

        palindromes

    ):

        counter = Counter(

            palindromes["all"]

        )

        longest = max(

            palindromes["unique"],

            key=len,

            default=""

        )

        return {

            "words": len(words),

            "counter": counter,

            "longest": longest,

            "unique": len(

                palindromes["unique"]

            )

        }
