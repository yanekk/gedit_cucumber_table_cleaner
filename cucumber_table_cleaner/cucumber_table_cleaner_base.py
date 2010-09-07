import re

class CucumberTableCleaner:
    @staticmethod
    def clean(string):
        columns = {}
        indentation = None
        result = []
        result_string = ""
        string = string.strip("\n")

        for line in string.split("\n"):
            match = re.search("[\S]", line)
            if not match:
                result_string += line.rstrip() + "\n" # TODO: correct it
            else:
                position = match.start()
                if not indentation:
                    if position > 0:
                        indentation = line[0:position]
                line = line.strip("\t ")

                for index, item in enumerate(line.split("|")):
                    if columns.has_key(index):
                        column_width = columns[index]
                        if len(item) > column_width:
                            columns[index] = len(item)
                    else:
                        columns[index] = len(item) + 2
                result.append(line)

        if not indentation:
            indentation = "\t"

        for line_index, line in enumerate(result):
            line_result = []
            for item_index, item in enumerate(line.split("|")):
                item = item.strip()
                line_result.append(item.center(columns[item_index]))
            result[line_index] = indentation + ("|".join(line_result)).strip()

        result_string += "\n".join(result)
        return result_string
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
if __name__ == "__main__":
    print "Test One:"
    print CucumberTableCleaner.clean(test_one)
    print "Test Two:"
    print CucumberTableCleaner.clean(test_two)

