from detector import PalindromeDetector

class Analyzer:

    def analyze(

        self,

        words

    ):

        detector =

            PalindromeDetector()

        found =

            detector.find(

                words

            )

        return {

            "all": found,

            "unique": sorted(

                set(found)

            )

        }
