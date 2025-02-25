#! /usr/bin/env python3

# Idea: implement a Busy Beaver Turing machine for fun
#
# components:
# read/write head
# tape of arbitrary length, implemented as a dict in this case
# state register
# instruction table

# ref: https://en.wikipedia.org/wiki/Busy_Beaver_game

class TuringMachine:
    def __init__(self):
        self.pos = 0
        self.state = 'A'
        self.steps = 0

        self.tape = dict() # {<pos_num>: 'contents'}
        self.head_write('0')
        print("Machine created.")
    
    def head_read(self):
        return self.tape[self.pos]
    
    def head_write(self, value):
        self.tape[self.pos] = value
    
    def head_left(self):
        self.pos -= 1

        # Is this a valid position? If not, extend the tape.
        try:
            self.tape[self.pos]
        except KeyError:
            self.tape[self.pos] = 0
        
        return
    
    def head_right(self):
        self.pos += 1

        # Is this a valid posltion? If not, extend the tape.
        try:
            self.tape[self.pos]
        except KeyError:
            self.tape[self.pos] = 0
        
        return
    

    def execute(self, deck):
        self.contents = self.head_read()
        combined = self.state + str(self.contents) # e.g. A0
        card_value = deck[combined]

        # 'A0' -> '1RB'
        #
        # If A0, then...
        # write '1'
        # move head right
        # set state to 'B'

        print(combined, card_value)

        self.head_write(card_value[0])

        if 'R' == card_value[1]:
            print("moving right")
            self.head_right()
        if 'L' == card_value[1]:
            print("moving left")
            self.head_left()
        
        self.state = card_value[2]

        self.steps += 1
        return




def get_deck():
    predefined_deck = {
        'A0': '1RB',
        'A1': '1LB',
        'B0': '1LA',
        'B1': '0LC',
        'C0': '1RH',
        'C1': '1LD',
        'D0': '1RD',
        'D1': '0RA'
    }
    # predefined_deck = {
    #     'A0': '1RB',
    #     'A1': '1LB',
    #     'B0': '1LA',
    #     'B1': '1RH'
    # }
    return predefined_deck


def main():
    
    deck = get_deck() # for now we have a hard-code deck returned from the function
    if not type(deck) is dict:
        print("get_deck() failed to parse the provided deck. Halting...")
        print(type(deck))
        return

    tm = TuringMachine()
    print(tm)
    print("Step:", tm.steps, "State:", tm.state, "Pos:", tm.pos)
    while tm.state != 'H':
        tm.execute(deck)
        print("Step:", tm.steps, "State:", tm.state, "Pos:", tm.pos)
        for k in sorted(tm.tape):
            print(k, tm.tape[k])
        # input("\npush for go")
    
    print("\n\n\nHALT state reached.")
    print("Final tape:")
    for k in sorted(tm.tape):
        print(k, tm.tape[k])
    print("")


if __name__ == "__main__":
    main()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
