from Summarizer import Summarizer
from Reader import Reader
from pprint import pprint
from QuestionGenerator import QGenerator




reader = Reader("exempledef.pdf")

print(reader.returnPaperContent(1,2))

summarizer = Summarizer()
summarizer.detect_language(reader.returnPaperContent())

print(summarizer.summarize(reader.returnPaperContent(1,2)))

