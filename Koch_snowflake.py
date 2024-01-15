import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 2 / 3**0.5)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    window.mainloop()


# Запит у користувача числа для побудови Сніжинки Коха
def main():
    user_input = input('Введіть ціле число від 1 до 10: ')
    user_input = int(user_input)
    if user_input > 0 and user_input < 11:
        draw_koch_snowflake(user_input)
    else:
        print('Invalid command.')


if __name__ == "__main__":
    main()