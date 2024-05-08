from turtle import *

axiom = 'F--F--F'
rules = 'F+F--F+F'
angle = 60


def koch_snowflake(txt, n):
    if n < 0:
        return ''
    elif n == 0:
        return txt
    else:
        return koch_snowflake(''.join(rules if i == 'F' else i for i in txt), n - 1)


def draw(txt):
    penup()
    goto(-280, -150)
    pendown()
    pensize(5)
    bgcolor('black')
    color('blue', 'lightblue')
    speed(10)
    begin_fill()
    for item in txt:
        if item == '-':
            left(angle)
        elif item == '+':
            right(angle)
        else:
            forward(7)
    end_fill()
    done()


txt = koch_snowflake(axiom, 4)
draw(txt)
