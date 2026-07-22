from repository import Repository
from parser import Parser
from analyzer import Analyzer
from statistics import Statistics
from report import Report

repository = Repository()

document = repository.load()

parser = Parser()

words = parser.words(

    document.content

)

analysis = Analyzer().analyze(

    words

)

stats = Statistics().build(

    words,

    analysis

)

Report().print(

    document,

    stats,

    analysis

)
