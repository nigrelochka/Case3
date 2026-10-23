"""Главное меню фрактальной мастерской (роль 4)."""
import turtle
from fractals.basic import draw_binary_tree, draw_branch
from fractals.koch import koch, koch_snowflake, minkowski
from fractals.complex import ice_fractal_1, ice_fractal_2, levy, dragon

FRACTALS = {
    "1": ("Двоичное дерево", draw_binary_tree),
    "2": ("Ветка", draw_branch),
    "3": ("Кривая Коха", koch),
    "4": ("Снежинка Коха", koch_snowflake),
    "5": ("Кривая Минковского", minkowski),
    "6": ("Ледяной фрактал №1", ice_fractal_1),
    "7": ("Ледяной фрактал №2", ice_fractal_2),
    "8": ("Кривая Леви", levy),
    "9": ("Дракон Хартера–Хейтуэя", dragon),
}

def show_menu() -> None:
    print("\n=== ФРАКТАЛЬНАЯ МАСТЕРСКАЯ ===")
    for key, (name, _) in FRACTALS.items():
        print(f"{key}. {name}")
    print("10. Выход")

def main() -> None:
    screen = turtle.Screen()
    screen.title("Фрактальная мастерская")
    pen = turtle.Turtle()
    pen.speed(0)
    while True:
        show_menu()
        choice = input("Выберите пункт меню: ").strip()
        if choice == "10":
            break
        if choice not in FRACTALS:
            print("Нет такого пункта меню.")
            continue
        try:
            order = int(input("Глубина рекурсии (0–6): "))
            size = float(input("Размер (> 0): "))
            if not 0 <= order <= 6 or size <= 0:
                raise ValueError
            angle = float(input("Угол (0–90): ")) if choice == "1" else None
            if angle is not None and not 0 < angle <= 90:
                raise ValueError
        except ValueError:
            print("Некорректные параметры. Попробуйте снова.")
            continue
        pen.clear()
        pen.penup()
        pen.home()
        pen.pendown()
        _, draw = FRACTALS[choice]
        # Функции пока заглушки; реализация — задача участников.
        if angle is not None:
            draw(order, size, angle)
        else:
            draw(order, size)
        print("Функция вызвана. Нажмите Enter для возврата в меню.")
        input()
    screen.bye()

if __name__ == "__main__":
    main()
