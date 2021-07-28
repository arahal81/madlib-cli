import re

print("""
Welcome to madlib game
Please fill in the gaps by adding words according to what is required to be entered
    """)


def read_template(path):

    try:
        with open(path, 'r') as file:
            file_text = file.read().strip()
            # print(file_text)
            return file_text

    except FileNotFoundError:
        file_text = "file name is wrong or file not found."

    if file_text == "file name is wrong or file not found.":
        raise FileNotFoundError(file_text)

    return file_text


read_template("assets/first_templet.txt")


def parse_template(text):
    usable_parts_temp = re.findall(r"\{.*?\}", text)
    usable_parts = ()

    for i in usable_parts_temp:
        usable_parts = usable_parts + (re.sub(r"\{|\}", "", str(i)),)

    new_text = re.sub(r"\{.*?\}", "{}", text)

    output = [new_text, usable_parts]
    return output
    # return usable_parts


# print(parse_template("It was a {Adjective} and {Adjective} {Noun}."))


def get_user_input(usable_parts):
    user_input = []

    for x in usable_parts:
        u_input = input(f"please enter word for {x} \n ==> ")
        user_input.append(u_input)

    return user_input


useble = parse_template("It was a {Adjective} and {Adjective} {Noun}.")
# print(get_user_input(useble[1]))


def merge(text, user_input):
    fulltext = text.format(*user_input)
    with open('assets/output_file.txt', 'w') as file:
        file.write(fulltext)
    return read_template('assets/output_file.txt')


if __name__ == "__main__":
    text = read_template('assets/first_templet.txt')
    tuble = parse_template(text)
    user_input = get_user_input(tuble[1])
    print(merge(tuble[0], user_input))
