import json
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from rich import print

class RoomObject:
    def __init__(self, title, description, enemies=list()):
        self.title = title
        self.description = description
        self.enemies = enemies
    
    def print_room(self):
        s_width = 90
        print(f"[bold red]{self.title.center(s_width, "-")}[/bold red]")
        print(f"| {self.description.ljust(s_width - 4)} |")
        print("|" + "-"*(s_width - 2) + "|")
        #print(f"| You See: {you_see.ljust(s_width + 2)} |")
        for enemy in self.enemies:
            print(f"| {enemy.name.ljust(s_width - 4)} |")
        print("|" + "-"*(s_width - 2) + "|")
        print(f"| What do you do?".ljust(s_width - 1) + "|")
        print(f"| {"1. Attack".ljust(s_width - 5)}  |")
        print(f"| {"2. Heal".ljust(s_width - 5)}  |")
        #print(f"| {option3.ljust(s_width - 4)} |")
        print("|" + "-"*(s_width - 2) + "|")
        #print(f"| Log: {log.ljust(s_width - 9)} |")
        #print("|" + "-"*(s_width - 2) + "|")
        
        choice = Prompt.ask(f"[magenta]What Action?[/magenta]")

        return choice
    def __str__(self):
        return f"Room: {self.title}"



if __name__ == "__main__":
    entryway = RoomObject("Entryway", "You see big doors")
    print(f"{entryway}")