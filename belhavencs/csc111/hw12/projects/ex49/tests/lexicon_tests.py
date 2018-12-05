#!/usr/bin/env python
from nose.tools import *
import ex49.lexicon as Lexicon
from ex49.lexicon import scan


def test_directions():
    assert_equal(Lexicon.scan("north"), [('direction', 'north')])
    result = Lexicon.scan("north south east west up down left right")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east'),
                          ('direction', 'west'),
                          ('direction', 'up'),
                          ('direction', 'down'),
                          ('direction', 'left'),
                          ('direction', 'right')])

def test_verbs():
    assert_equal(Lexicon.scan("go"), [('verb', 'go')])
    result = Lexicon.scan("go kill eat stop")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat'),
                          ('verb', 'stop')])


def test_stops():
    assert_equal(Lexicon.scan("the"), [('stop', 'the')])
    result = Lexicon.scan("the in of from at")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of'),
                          ('stop', 'from'),
                          ('stop', 'at')])


def test_nouns():
    assert_equal(Lexicon.scan("bear"), [('noun', 'bear')])
    result = Lexicon.scan("bear princess door cabinet")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess'),
                          ('noun', 'door'),
                          ('noun', 'cabinet')])

def test_numbers():
    assert_equal(Lexicon.scan("1234"), [('number', 1234)])
    result = Lexicon.scan("3 91234 123456")
    assert_equal(result, [('number', 3),
                          ('number', 91234),
                          ('number', 123456)])


def test_errors():
    assert_equal(Lexicon.scan("ASDFADFASDF"),
                 [('error', 'asdfadfasdf')])
    result = Lexicon.scan("bear IAS princess fooyoutoo door")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'ias'),
                          ('noun', 'princess'),
                          ('error', 'fooyoutoo'),
                          ('noun', 'door')])