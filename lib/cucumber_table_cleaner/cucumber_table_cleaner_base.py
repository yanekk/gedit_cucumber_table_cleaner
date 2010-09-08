import re

class CucumberTableCleaner:
    def __init__(self, string):
        self.__string         = string.strip("\n")
        self.__columns        = {}
        self.__indentation    = None
        self.__lines          = self.__string.split("\n")

    def do_clean(self):
        for i in self.__lines:
            self.__set_indentation()
            self.__set_widths(i)
        return self.__render()

    def __set_indentation(self):
        line  = self.__lines[0]
        match = self.__line_is_valuable(line)
        if match:
            position = match.start()
            if not self.__indentation:
                if position > 0:
                    self.__indentation = line[0:position]
                else:
                    self.__indentation = "   "


    def __set_widths(self, line):
        if self.__line_is_valuable(line):
            for index, word in enumerate(line.split("|")):
                if self.__columns.has_key(index):
                    column_width = self.__columns[index]
                    if len(word) >= column_width:
                        self.__columns[index] = len(word)

                        if len(word) == len(word.strip()):
                            self.__columns[index] += 2

                else:
                    self.__columns[index] = len(word)
                    if len(word) == len(word.strip()):
                        self.__columns[index] += 2

    def __line_is_valuable(self, line):
        match = re.search("[\S]", line)
        return match

    def __render(self):
        return_string = ""
        for line in self.__lines:
            if self.__line_is_valuable(line):
                line_result = []
                for item_index, item in enumerate(line.split("|")):
                    item = item.strip()
                    line_result.append(item.center(self.__columns[item_index]))
                return_string += self.__indentation + ("|".join(line_result)).strip() + "\n"
            else:
                return_string += line + "\n"
        return return_string

    @staticmethod
    def clean(string):
        c = CucumberTableCleaner(string)
        return c.do_clean()

"""
*** test area
"""

test_one = """
    Examples:
    | first_arg | second_arg | please | dont | hurt | me|
    | i | am | just | a | simple | man |
    |bleah|i|drop|this|shit|
|indentation|fail|will|crush|you|
"""

test_two = """
        | this | should | stay | indented |
        | i | am | a | moron |
"""
test_three = """|there | is | no | line-end | signs |
| what | should | i | do | now | """
if __name__ == "__main__":
    print "Test One:"
    print CucumberTableCleaner.clean(test_one)
    print "Test Two:"
    print CucumberTableCleaner.clean(test_two)
    print "Test Three:"
    print CucumberTableCleaner.clean(test_three)

