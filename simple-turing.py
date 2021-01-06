#!/usr/bin/env python3

# components:
# read/write head
# tape of arbitrary length, not a ring
# state register
# instruction table

# let's start with a Busy Beaver...
# https://en.wikipedia.org/wiki/Busy_Beaver_game

# tape = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
tape = []

pos = 0
state = 'A'
steps = 0

WORKING_STATES = ['A','B']
HALT_STATE = 'H'
VALID_SYMBOLS = ['0','1']

DECK = {
	'A0': '1RB',
	'A1': '1LB',
	'B0': '1LA',
	'B1': '1RH',
	}
	
# stepping the tape left / right
def tape_step_left():
	global tape, pos, steps
	if pos == 0:
		tape_add_left()
	pos -= 1
	# steps += 1


def tape_step_right():
	global tape, pos, steps
	if pos == len(tape):
		tape_add_right(tape)
	pos += 1
	# steps += 1


# if the tape is not long enough, we need to add more...
# note: busy beaver game cells are always zero when untouched.
def tape_add_left():
	global pos
	tape.insert(0,'0')
	# because lists are zero indexed, we have to move our position counter
	# to account for the new list length
	if pos != 0:
		pos += 1


def tape_add_right():
	tape.append('0')


def head_read():
	global tape, pos
	return tape[pos]


def head_write(symbol):
	global tape, pos
	tape[pos] = symbol


def head_execute():
	
	global state
	# jobs
	
	# 1. read card for current state and symbol
	symbol = head_read()
	todo = DECK[state + symbol]
	print(todo)
	
	# 2. write symbol
	if todo[0] is '1':
		head_write('1')
	else:
		head_write('0')
	
	# 3. move head
	if todo[1] is 'L':
		tape_step_left()
	if todo[1] is 'R':
		tape_step_right()
		
	# 4. declare state
	state = todo[2]


def main():
	# constants

	global tape, pos, state, steps

	# initialize
	tape.append('0')
	
	while state != HALT_STATE:
		print("Step: ", steps)
		# print(tape)
		steps += 1
		# here = head_read()
		head_execute()


if __name__ == "__main__":
	main()

