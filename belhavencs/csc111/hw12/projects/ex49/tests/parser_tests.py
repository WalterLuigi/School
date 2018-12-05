from nose.tools import *
import ex49.parser as Parser
from ex49.parser import parse_sentence, parse_subject, parse_verb, parse_noun

def test_sentence():
    assert_equal(Parser.parse_sentence("I'm gonna go hit the bear in his face"), []
    result = lexicon.scan("north south east west up down left right")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east'),
                          ('direction', 'west'),
                          ('direction', 'up'),
                          ('direction', 'down'),
                          ('direction', 'left'),
                          ('direction', 'right')])

def test_errors():
