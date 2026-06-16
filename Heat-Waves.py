import sys
from rich import print
from time import sleep
import os

os.system('cls')

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def printLyrics():
    lines = [
        ("\nSometimes, all I think about is you", 0.07), 
        ("Late nights in the middle of June", 0.06), 
        ("Heat waves been fakin' me out", 0.06), 
        ("Can't make you happier now", 0.06), 
    ]

    delays = [0.4, 0.5, 0.4, 0.5]

    hide_cursor()
    try:
        for i, (line, char_delay) in enumerate(lines):
            for char in line:
                print(f"[bold white]{char}[/bold white]", end="")
                sys.stdout.flush()
                sleep(char_delay)
            print()
            if i < len(delays):
                sleep(delays[i])
    finally:
        print("\n[bold red]✨ End of Heat Waves ✨[/bold red]")
        sleep(3)
        show_cursor()


printLyrics()

