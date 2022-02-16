from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer

LANGUAGE = "english"
SENTENCES_COUNT = 10


class Sumy():
    """
    Sumy lib https://github.com/miso-belica/sumy
    """
    def __init__(self, text):
        self.parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))

    def LexRank(self):
        """
        Unsupervised approach to text summarization based on graph-based centrality scoring of sentences.
        """
        return LexRankSummarizer()(self.parser.document, SENTENCES_COUNT)
    
    def Luhn(self):
        """
        Based on frequency of most important words
        """
        return LuhnSummarizer()(self.parser.document,SENTENCES_COUNT)
    
    def LSA(self):
        """
        Based on term frequency techniques with singular value decomposition to summarize texts
        """
        return LsaSummarizer()(self.parser.document,SENTENCES_COUNT)