import tkinter as tk
import random


# Snow animation
def snow_animation(canvas, width, height):
    snowflakes = []
    
    def create_snowflake():
        x = random.randint(0, width)
        y = 0
        size = random.uniform(0.1, 110.5)
        speed = random.uniform(1, 3)
        
        snowflake = canvas.create_oval((x, y, x + size, y + size), fill="red")
        snowflakes.append((snowflake, x, y, speed))
    
    # функц движения снежинок
    def move_snowflakes():
        for snowflake in snowflakes:
            snowflake_id, x, y, speed = snowflake
            canvas.move(snowflake_id, 0, speed)
            
            # если снежинка достигла нижней границы окна , она начинает падать снова сверху
            if x >= height:
                canvas.move(snowflake_id, -x, -height)
    
    # создаем снежинки
    for _ in range(100):
        create_snowflake()
    
    # запускаем анимацию
    def animate():
        move_snowflakes()
        window.after(50, animate)
    
    animate()


# создаем окно
window = tk.Tk()
window.title("Новый год 2024!")
window.geometry("450x350")

# создаем холст
canvas = tk.Canvas(window, width=450, height=350, bg="black")
canvas.pack()

# добавляем надпись
label = tk.Label(canvas, text="С наступающим НОВЫМ годом 2024!", font=("Arial", 19), bg="black", fg="white")
label.place(relx=0.5, rely=0.5, anchor="center")

# запускаем анимацию снега
snow_animation(canvas, 400, 300)

# запускаем главный цикл окна
window.mainloop()
