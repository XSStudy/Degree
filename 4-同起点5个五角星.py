import turtle
def draw_fiveStart(leng):
    conut = 1
    while conut <= 5:
        turtle.forward(leng)
        turtle.right(144)
        conut += 1
    leng += 10
    if leng <= 100:
        draw_fiveStart(leng)
def main():
    turtle.penup()
    turtle.backward(100)
    turtle.down()
    turtle.pensize(2)
    turtle.pencolor('red')
    segment = 50
    draw_fiveStart(segment)
    turtle.exitonclick()

if __name__ == '__main__':
    main()