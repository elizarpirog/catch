import re

class Parser:

    def words(

        self,

        text

    ):

        return re.findall(

            r"[A-Za-z]+",

            text.lower()

        )
