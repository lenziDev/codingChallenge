from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
import re
from nltk.tokenize import sent_tokenize

LANGUAGE = "english"



class Sumy():
    """
    Sumy lib https://github.com/miso-belica/sumy
    """
    def __init__(self, text):
        self.parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
        self.text = text

        # Find the number of statements and the number of sentences of summary
        round_number = round( len(sent_tokenize(self.text)) * 0.5 )

        if not round_number > 0:
            self.sentences_count = 1
        else:
            self.sentences_count = round_number

    def LexRank(self):
        """
        Unsupervised approach to text summarization based on graph-based centrality scoring of sentences.
        """

        return LexRankSummarizer()(self.parser.document, self.sentences_count)
    
    def Luhn(self):
        """
        Based on frequency of most important words
        """
        return LuhnSummarizer()(self.parser.document, self.sentences_count)
    
    def LSA(self):
        """
        Based on term frequency techniques with singular value decomposition to summarize texts
        """
        return LsaSummarizer()(self.parser.document, self.sentences_count)