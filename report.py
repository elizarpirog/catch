class Report:

    def print(

        self,

        document,

        stats,

        data

    ):

        print(

            "Loaded text\n"

        )

        print(

            document.name

        )

        print()

        print(

            "Words scanned\n"

        )

        print(

            stats["words"]

        )

        print()

        print(

            "Palindromes found\n"

        )

        for word in data["unique"]:

            print(word)

        print()

        print(

            "Longest\n"

        )

        print(

            stats["longest"]

        )

        print()

        print(

            "Total unique\n"

        )

        print(

            stats["unique"]

        )
