"""
Lab for theme authomats 
"""
import random


class State:
    """
    Presents the state of system
    """

    STATES = ["Tired", "Exused", "Moody", "Inactive", "Satisfied"]
    HAPPY = True
    SAD = False
    EVENTS = [
        "Wake up",
        "Air Allert",
        "Exam",
        "Lunch",
        "Have a walk",
        "Go to pub",
        "Go sleep",
    ]

    def __init__(self):
        self.state_ind = 0
        self.event_ind = 0
        self.energy = 0
        self.time = 0
        self.hungry = False
        self.prob = 0.3
        if self.energy != 0:
            self.prob = 1 / self.energy

    def change_state(self):
        """
        Changes the state of system
        """
        self.state_ind = (self.state_ind + 1) % len(self.STATES)
        if random.uniform(0, 1) > self.prob:
            self.state_ind = random.randint(0, len(self.STATES))

    def isHungry(self):
        """
        Checks if system is hungry
        """
        if self.hungry is True:
            self.hungry = False
        else:
            self.hungry = True

    def change_event(self):
        """
        Changes the event of system
        """
        self.event_ind = (self.event_ind + 1) % len(self.EVENTS)


def run(time: int, state):
    """
    Runs the authomat
    """
    for i in range(1):
        if time == 8:
            print(f"I just {state.EVENTS[0]}, snd I'm already {state.STATES[1]}")
            state.change_event()
            state.change_state()
            state.energy = 20
        elif time == 9:
            print("I want to lay down some more time, but i should go(")
        elif time == 10:
            print("I should go to my uni to write an exam.")
        elif time == 11:
            print(f"{state.EVENTS[1]}. Again.")
            state.change_event()
            state.change_state()
        elif time == 12:
            print(f"I'm going to have my exam now. I'm not even had a breakfast.")
            state.hungry = True
            state.change_event()
            state.change_state()
        elif time in range(13, 15):
            print("I'm still at my exam.")
            state.energy -= int(random.randint(0, 2))
            if time == 15:
                state.change_event()
        elif time == 16:
            print("I'm going to have lunch")
            state.isHungry()
            state.energy += int(random.randint(0, 15))
            if state.energy >= 25:
                print("I'm going to have a walk with my friends")
                state.change_event()
                state.change_state()

            else:
                print("I'm going to go home and sleep")
                return False

        if time in range(19, 21):
            print("We decided to go to pub.")
            state.change_event()
            state.change_state()
            state.energy += random.randint(0, 5)
            if state.energy > 30:
                print("We decided to continue our party at me friends home. Bye!")
                return False
            elif state.energy < 30:
                print("We decided to go home and sleep")
                return False
        return True


def main():
    state = State()
    for i in range(8, 21):
        if not run(i, state):
            break
        i += 1


main()
