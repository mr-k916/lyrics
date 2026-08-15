import sys
import time
import os

def print_lyrics():
    lines = [
        ("\nSomethings you just can't refuse", 0.07),
        ("She wanna ride me like a cruise", 0.07),
        ("And I'm not", 0.1), 
        ("Trayna lose", 0.1),
        ("Then you're left in the dust", 0.07), 
        ("Unless I stuck by ya", 0.09),
        ("You're the sunflower", 0.09),
        ("I think your love would be too much", 0.03),
        ("Or you'll be left in the dust", 0.09),
        ("Unless I stuck by ya", 0.09),
        ("You're the sunflower", 0.09),
        ("You're the sunflower", 0.09),
    ]

    delays = [0.3, 0.4, 0.02, 2.0, 0.4, 0.8, 0.8, 1.0, 0.4, 0.8, 0.8, 0.5]

    os.system('cls' if os.name == 'nt' else 'clear')

    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        BOLD_WHITE = "\033[1;37m"
        RESET = "\033[0m"

        for i, (line, char_delay) in enumerate(lines):
            sys.stdout.write(BOLD_WHITE)
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(char_delay)
            sys.stdout.write(RESET + "\n")
            sys.stdout.flush()

            if i < len(delays):
                time.sleep(delays[i])
    finally:
        time.sleep(1)
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

if __name__ == "__main__":
    print_lyrics()
