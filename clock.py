import tkinter as tk
from math import cos, sin, pi
from datetime import datetime

class AnalogClock(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(bg='black', highlightthickness=0)
        self.size = min(self.winfo_reqwidth(), self.winfo_reqheight())
        self.center = self.size / 2
        self.radius = self.size * 0.4

    def draw_clock_face(self):
        self.create_oval(self.center - self.radius, self.center - self.radius,
                         self.center + self.radius, self.center + self.radius,
                         outline='white', width=4)

    def draw_numbers(self):
        for i in range(1, 13):
            angle = -90 + (i / 12) * 360
            angle_rad = angle * pi / 180
            x = self.center + 0.8 * self.radius * cos(angle_rad)
            y = self.center + 0.8 * self.radius * sin(angle_rad)
            self.create_text(x, y, text=str(i), fill='white', font=('Arial', 12, 'bold'))

    def draw_hands(self):
        now = datetime.now()
        second_angle = (now.second / 60) * 360 - 90
        minute_angle = ((now.minute + now.second / 60) / 60) * 360 - 90
        hour_angle = ((now.hour % 12 + now.minute / 60) / 12) * 360 - 90

        self.delete('second_hand')
        self.draw_hand(second_angle, self.radius * 0.9, 'red', width=1, tag='second_hand')
        self.draw_hand(minute_angle, self.radius * 0.7, 'white', width=2)
        self.draw_hand(hour_angle, self.radius * 0.5, 'white', width=4)

    def draw_hand(self, angle, length, color, width, tag=None):
        angle_rad = angle * pi / 180
        x = self.center + length * cos(angle_rad)
        y = self.center + length * sin(angle_rad)
        self.create_line(self.center, self.center, x, y, fill=color, width=width, tag=tag)

    def update_clock(self):
        self.delete('hands')
        self.draw_clock_face()
        self.draw_numbers()
        self.draw_hands()
        self.after(1000, self.update_clock)

root = tk.Tk()
root.title("Wall Clock")
root.geometry("300x300")
root.configure(bg='black')

clock = AnalogClock(root, width=300, height=300)
clock.pack(expand=True, fill='both')

clock.update_clock()

root.mainloop()
