import re


class Validator:
    def __init__(
        self, command, commands=["add", "edit", "delete", "show", "upload", "index"]
    ):
        self.patternNumber = "\+77[047]\d{8}$"
        self.patternId = "\d+$"
        self.patternName = "[a-zA-Zа-яА-Я]+"
        self.patternFile = ".+\.csv$"
        self.commands = commands
        self.arguments = command
        self.command = command[1] if len(command) > 1 else "index"
        self.error = ""
        self.validate()

    def isNumber(self, string):
        return bool(re.match(self.patternNumber, string))

    def isId(self, string):
        return bool(re.match(self.patternId, string))

    def isName(self, string):
        return bool(re.match(self.patternName, string))

    def isFile(self, string):
        return bool(re.match(self.patternFile, string))

    def validate(self):
        if self.command not in self.commands:
            self.error = "Wrong action argument. Supported only: add, edit, delete, show, index, upload."
            return self

        # add
        if (self.command in self.commands[0]) and len(self.arguments) < 4:
            self.error = "Second argument is required. Example: main.py add NAME NUMBER"
            return self
        if self.command in self.commands[0] and not self.isName(self.arguments[2]):
            self.error = "Second argument should be a correct name"
            return self
        if self.command in self.commands[0] and not self.isNumber(self.arguments[3]):
            self.error = "Third argument should be a correct mobile number +7XXXXXXXXXX"
            return self

        # show
        if (self.command in self.commands[3]) and len(self.arguments) < 3:
            self.error = "Second argument is required for filtering. Should be ID, NAME or PHONE NUMBER"
            return self
        if (self.command in self.commands[3]) and not (
            self.isNumber(self.arguments[2])
            or self.isId(self.arguments[2])
            or self.isName(self.arguments[2])
        ):
            self.error = "Second argument should be a correct ID, NAME or PHONE NUMBER"
            return self

        # delete
        if (self.command in self.commands[2]) and len(self.arguments) < 3:
            self.error = (
                "Second argument is required for delete. Should be ID or PHONE NUMBER"
            )
            return self

        if (self.command in self.commands[2]) and not (
            self.isNumber(self.arguments[2])
            or self.isId(self.arguments[2])
            or self.isName(self.arguments[2])
        ):
            self.error = "Provide ID, Name or correct MOBILE NUMBER"
            return self

        # edit
        if (self.command in self.commands[1]) and len(self.arguments) < 5:
            self.error = "Second, third, fourth arguments are required for editing. edit ID NEW_NAME NEW_NUMBER"
            return self

        if (self.command in self.commands[1]) and not (
            self.isNumber(self.arguments[4])
            or self.isId(self.arguments[2])
            or self.isName(self.arguments[3])
        ):
            self.error = "Invalid arguments. main.py edit ID NEW_NAME NEW_NUMBER. Pass correct mobile number"
            return self

        # upload
        if (self.command in self.commands[4]) and len(self.arguments) < 3:
            self.error = "Second argument is required. Pass path to your csv file"
            return self
        if (self.command in self.commands[4]) and not self.isFile(self.arguments[2]):
            self.error = "Second argument should be a correct CSV file"
            return self
