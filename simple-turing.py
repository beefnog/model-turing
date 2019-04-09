#!/usr/bin/env python3


# components:
# read/write head
# tape of arbitrary length, not a ring
# state register
# instruction table

# let's start with a Busy Beaver...
# https://en.wikipedia.org/wiki/Busy_Beaver_game

# constants
VALID_STATES = ['A','B']
VALID_SYMBOLS = ['0','1']

# initial machine
tape = ['0']
state = 'A'


# def (TODO: head move, or tape scroll, such that more zero initialized cells are
#	automatically added on the appropriate side of the rw head)

