import re
import sys
import string

def input():
    f = open('i_am_need_toml.txt', 'r')
    all_commands = []
    for line in f:
        line = line.strip()
        all_commands.append(line)
    return all_commands


def obr(list):
    constants = {}
    f = 0
    for line in list:
        try:
            if line.startswith("{#"):
                print("#" + line[2:])
                f = 1;
                continue

            if f:
                if line.endswith("#}"):
                    print("# " + line[:-2])
                    f = 0
                    continue
                else:
                    if not line.strip():
                        print()
                        continue
                    else:
                        print("# " + line)
                        continue

            if line.startswith("*"):
                print("#" + line[1:])

            elif re.match(r"\(def (\w+) (\d+)\);", line):
                match = re.match(r"\(def (\w+) (\d+)\);", line)
                name, expression = match.groups()  # Извлекаем имя константы и выражение
                constants[name] = expression
                print(name + " = " + expression)

            elif re.match(r"\(def (\w+) (\$[^$]+\$)\);", line):
                match = re.match(r"\(def (\w+) (\$[^$]+\$)\);", line)
                name, expression = match.groups()
                constants[name] = calculate(expression, constants)
                print(name + " = " + calculate(expression, constants))

            elif re.match(r"\(def (\w+) (\[.+\])\);", line):
                match = re.match(r"\(def (\w+) (\[.+\])\);", line)
                name, expression = match.groups()
                constants[name] = list_is_list(expression)
                print(name + " = " + constants[name])

            elif not line:
                print()

            else:
                print("Неверный синтаксис")
        except:
            print("Неверный ввод")

def calculate(str, constans):
    str = str[1:-1]
    str = str.split()
    i = -1
    answ = ""
    for element in str:
        i += 1


        try:
            str[i] = constans[element]
        except:
            continue
    for element in str:
        answ = answ + element
    return f"{eval(answ)}"

def list_is_list(str_list):
    my_list = str_list.split()
    answ = ""
    f = 0
    o = 0
    for i in my_list:
        if i == "[":
            answ = answ + i + " "
            f = 0
            o += 1
        elif i == "]":
            if f:
                if o != 1:
                    answ = answ[:-2] + " ], "
                else:
                    answ = answ[:-2] + " ] "
                continue
            if o != 1:
                answ = answ[:-2] + " ], "
                f = 1
            else:
                answ = answ[:-2] + " ]"
            o -= 1
        else:
            answ = answ + i + ", "
            f = 0
    return answ


def main():
    commands = input()

    # Формирование вывода в формате TOML
    obr(commands)
    #obr(["(def a 10);", "(def b $a - 1$);"])
    #print(calculate("$a + 1$", {"a": "10"}))
    #calculate("$ab + 1$", {"ab": "10"})

if __name__ == "__main__":
    main()
