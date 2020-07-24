import turtle
import random

def randeg():
    i = random.randint(15,20)
    yield i
 
def tree(branch_len, t,p_size):
    if branch_len > 5:
        t.pencolor('brown')
        t.forward(branch_len)
        t.pensize(8 - p_size)
        t.right(20)
        tree(branch_len-next(randeg()), t,p_size+2)
        t.left(40)
        t.pensize(8- p_size)
        tree(branch_len-next(randeg()), t,p_size+2)
        t.pencolor('green')
        t.right(20)
        t.backward(branch_len)
def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.pencolor('black')
    t.pensize(9)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75, t,0)
    my_win.exitonclick()
main()


