from main1 import *
test1 = [
    "* тест 1",
    "(def a 10);",
    "(def b 2);",
    "",
    "(def c $a + b - 3 + pow(2,3)$);"
]
obr(test1)
test2 = [
    "{# this is",
    "test 2 #}",
    "(def a 10)",
    "wdfwdfwef",
    "(def b [ 1 1 [ 2 2 ] 1 ]);"
]
obr(test2)

