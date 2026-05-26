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

        def build_user_interface(self):
            tk.Label(self.main_window, text="FAN 1 STATUS", bg="#0b0c10", fg="#66fcf1", font=("Helvetica", 14, "bold")).pack(pady=(20, 5))
            f1_data = f"Speed: {self.fan1.get_speed()} | Radius: {self.fan1.get_radius()} \nColor: {self.fan1.get_color()} | Power: {'ON' if self.fan1.get_on() else 'OFF'}"
            tk.Label(self.main_window, text=f1_data, bg="#0b0c10", fg="#c5c6c7", font=("Courier", 10)).pack()

            tk.Label(self.main_window, text="FAN 2 STATUS", bg="#0b0c10", fg="#66fcf1", font=("Helvetica", 14, "bold")).pack(pady=(20, 5))
            f2_data = f"Speed: {self.fan2.get_speed()} | Radius: {self.fan2.get_radius()} \nColor: {self.fan2.get_color()} | Power: {'ON' if self.fan2.get_on() else 'OFF'}"
            tk.Label(self.main_window, text=f2_data, bg="#0b0c10", fg="#c5c6c7", font=("Courier", 10)).pack()
        