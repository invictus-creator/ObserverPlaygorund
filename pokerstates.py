from enum import Enum, auto

class Street(Enum):
    PREFLOP = auto()
    FlOP = auto()
    TURN = auto()
    RIVER = auto()

class Trigger(Enum):
    # number of black dots indication card is on board
    ZERO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()


if __name__ == '__main__':
    # State Machine
    rules = {
        Street.PREFLOP: [
            (Trigger.THREE, Street.FlOP)
        ],
        Street.FlOP: [
            (Trigger.ZERO, Street.PREFLOP),
            (Trigger.FOUR, Street.TURN)
        ],
        Street.TURN: [
            (Trigger.ZERO, Street.PREFLOP),
            (Trigger.FIVE, Street.RIVER)
        ],
        Street.RIVER: [
            (Trigger.ZERO, Street.PREFLOP)
        ]
    }


    street = Street.PREFLOP

    while True:
        print(f"Street is currently: {street}")

        for i in range(len(rules[street])):
            t = rules[street][i][0]
            print(f"{i}: {t}")

        idx = int(input("Select trigger: "))
        street = rules[street][idx][1]
