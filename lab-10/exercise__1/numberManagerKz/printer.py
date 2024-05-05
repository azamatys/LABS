from tqdm import tqdm
from time import sleep
from colorama import Fore


class Printer:

    def __init__(self, length=90):
        self.length = length if (length % 2) == 1 else length + 1

    def logo(self):
        print(
            Fore.WHITE
            + "  ______               __                ________                     __     "
        )
        print(
            " /      \             |  \              |        \                   |  \    "
        )
        print(
            "|  $$$$$$\  _______  _| $$_     ______  | $$$$$$$$______    ______  _| $$_   "
        )
        print(
            "| $$  | $$ /       \|   $$ \   /      \ | $$__   /      \  /      \|   $$ \  "
        )
        print(
            "| $$  | $$|  $$$$$$$ \$$$$$$  |  $$$$$$\| $$  \ |  $$$$$$\|  $$$$$$\\\\$$$$$$  "
        )
        print(
            "| $$  | $$| $$        | $$ __ | $$  | $$| $$$$$ | $$  | $$| $$   \$$ | $$ __ "
        )
        print(
            "| $$__/ $$| $$_____   | $$|  \| $$__/ $$| $$    | $$__/ $$| $$       | $$|  \\"
        )
        print(
            " \$$    $$ \$$     \   \$$  $$ \$$    $$| $$     \$$    $$| $$        \$$  $$"
        )
        print(
            "  \$$$$$$   \$$$$$$$    \$$$$   \$$$$$$  \$$      \$$$$$$  \$$         \$$$$ "
        )
        print("\n")

    def loading(self):
        for i in tqdm(range(100), desc="Loading...", smoothing=0.3):
            sleep(0.007)
        print("\n")

    def verbose(self, message, numbers=None):

        print(Fore.GREEN + f"+" + "-" * self.spacer("++") + "+")
        print(f"| {message}" + " " * (self.spacer(message) - 3) + "|")
        if numbers:
            print(
                "| ID"
                + " " * (int(self.length / 3) - 4)
                + "| Name"
                + " " * (int(self.length / 3) - 6)
                + "| Number"
                + " " * (int(self.length / 3) - 8)
                + "|"
            )
            (
                print(self.content(numbers))
                if type(numbers) is not list
                else [print(self.content(numbers[i])) for i in range(len(numbers))]
            )

        print(f"+" + "-" * self.spacer("++") + "+")

    def error(self, message, error=None):
        print(Fore.RED + f"+" + "-" * self.spacer("++") + "+")
        print(f"| {message}" + " " * (self.spacer(message) - 3) + "|")
        if error:
            print(f"| {error}" + " " * (self.spacer(error) - 3) + "|")
        print(f"+" + "-" * self.spacer("++") + "+")

    def spacer(self, string):
        return self.length - len(string)

    def content(self, number):
        return (
            f"| {number.id}"
            + " " * (int(self.length / 3) - len(str(number.id)) - 2)
            + f"| {number.name}"
            + " " * (int(self.length / 3) - len(number.name) - 2)
            + f"| {number.phone}"
            + " " * (int(self.length / 3) - len(number.phone) - 2)
            + "|"
        )
