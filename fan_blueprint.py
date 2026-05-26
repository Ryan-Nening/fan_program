import tkinter as tk

class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def get_speed(self): return self.__speed
    def get_radius(self): return self.__radius
    def get_color(self): return self.__color
    def get_on(self): return self.__on

    def set_speed(self, speed): self.__speed = speed
    def set_radius(self, radius): self.__radius = radius
    def set_color(self, color): self.__color = color
    def set_on(self, on): self.__on = on

    class FanDashboard:
        def __init__(self):
            self.main_window = tk.Tk()
            self.main_window.title("Fan Test")
            self.main_window.geometry("400x300")
            self.main_window.configure(bg="#0b0c10")
            self.fan1 = Fan(Fan.FAST, 10.0, "yellow", True)
            self.fan2 = Fan(Fan.MEDIUM, 5.0, "blue", False)