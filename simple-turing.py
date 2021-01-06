#!/usr/bin/env python3

# components:
# read/write head
# tape of arbitrary length, not a ring
# state register
# instruction table

# let's start with a Busy Beaver...
# https://en.wikipedia.org/wiki/Busy_Beaver_game

tape = ['B','E','N','T',' ','W','O','O','K','I','E']
pos = 0
state = 'A'
VALID_STATES = ['A','B']
VALID_SYMBOLS = ['0','1']

steps = 0	# this is where we will count total machine operations. It's also
		# easy to impose a bound here to catch unintended
		# non-halting machines.


# scrolling the tape left / right
def tape_move_left():
	global tape, pos, steps
	if pos == 0:
		tape_add_left(tape)
	pos -= 1
	steps += 1

def tape_move_right():
	global tape, pos, steps
	if pos == len(tape):
		tape_add_right(tape)
	pos += 1
	steps += 1


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
	return tape[pos]

def main():
	# constants

	global tape, pos, state


	print("Cool.\n")
	
	# let's try some tape additions
	tape_add_left()
	tape_add_left()
	tape_add_right()
	tape_add_right()
	
	# quick debugging
	for i in range(len(tape)):
		print(head_read())
		tape_move_right()

	# and compare
	print(tape)



if __name__ == "__main__":
	main()

