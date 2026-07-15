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
        ("\nJust know that I will find my way ", 0.09), 
        ("From you ", 0.1), 
        ("Like flowers from a tomb", 0.1), 
        ("While you decide who you are", 0.12), 
        ("And I can see right through", 0.09), 
        ("like shadows on the moon", 0.1), 
        ("And it's all bad news", 0.11), 
        ("Yeah, I, I, I ", 0.14), 
        ("Hate that I made you love me ", 0.12), 
    ]

    delays = [0.2, 0.2, 0.2, 0.2, 1, 0.2, 0.5, 0.4, 0.8]

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
        sleep(3)
        show_cursor()


printLyrics()

