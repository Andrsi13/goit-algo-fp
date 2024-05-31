import turtle
import math

def draw_pythagoras_tree(t, length, depth, angle):
    if depth == 0:
        return

    # Зберігаємо початкову позицію та напрямок черепашки
    t.forward(length)
    position = t.position()
    heading = t.heading()

    # Позиціонуємо черепашку для малювання лівої гілки
    t.left(angle)
    new_length = length * math.cos(math.radians(angle))
    draw_pythagoras_tree(t, new_length, depth - 1, angle)

    # Повертаємося до початкової позиції та напрямку
    t.setposition(position)
    t.setheading(heading)

    # Позиціонуємо черепашку для малювання правої гілки
    t.right(angle)
    new_length = length * math.sin(math.radians(angle))
    draw_pythagoras_tree(t, new_length, depth - 1, angle)

    # Повертаємося до початкової позиції та напрямку
    t.setposition(position)
    t.setheading(heading)

def main():
    depth = int(input("Введіть рівень рекурсії: "))
    length = 100  # Початкова довжина гілки
    angle = 45    # Кут нахилу гілок

    # Налаштовуємо черепашку
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Повертаємо черепашку вверх
    t.penup()
    t.goto(0, -screen.window_height() // 2 + 50)
    t.pendown()

    # Малюємо оголене дерево Піфагора
    draw_pythagoras_tree(t, length, depth, angle)

    # Завершуємо малювання
    turtle.done()

if __name__ == "__main__":
    main()
