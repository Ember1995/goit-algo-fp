import turtle
import math

def draw_pythagoras_tree(t, order, size):
    if order == 0:
        t.forward(size)
        t.backward(size)
    else:
        t.forward(size)
        t.left(45)
        draw_pythagoras_tree(t, order - 1, size / math.sqrt(2))
        t.right(90)
        draw_pythagoras_tree(t, order - 1, size / math.sqrt(2))
        t.left(45)
        t.backward(size)

def setup_turtle():
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)

    return t, window

def draw_pythagoras_tree_main(order, size=100):
    t, window = setup_turtle()
    draw_pythagoras_tree(t, order, size)
    window.mainloop()

# Тестування
if __name__ == "__main__":

    # Виклик функції з рівнем рекурсії 5
    draw_pythagoras_tree_main(5)
