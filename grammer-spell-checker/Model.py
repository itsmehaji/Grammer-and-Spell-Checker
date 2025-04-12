from textblob import TextBlob
from language_tool_python import LanguageTool, utils

class SpellCheckerModule:
    def __init__(self):
        self.grammar_check = LanguageTool('en-US')

    def correct_spell(self, text):
        blob = TextBlob(text)
        corrected = blob.correct()
        return str(corrected)

    def correct_grammar(self, text):
        matches = self.grammar_check.check(text)
        corrected_text = utils.correct(text, matches)
        return corrected_text, len(matches)
