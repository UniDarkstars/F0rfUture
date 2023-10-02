import tkinter as tk
import winsound

class TomatoClock:
    def __init__(self, master):
        self.master = master
        master.title("Tomato Clock")

        self.time_left = 1500  # 默认倒计时时间为25分钟
        self.is_running = False

        self.time_label = tk.Label(master, font=("Helvetica", 36), text=self.format_time(self.time_left))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start_timer, font=("Helvetica", 14), bg="black", fg="white")
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_timer, font=("Helvetica", 14), bg="black", fg="white")
        self.pause_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer, font=("Helvetica", 14), bg="black", fg="white")
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.adjust_button = tk.Button(master, text="Adjust", command=self.adjust_timer, font=("Helvetica", 14), bg="black", fg="white")
        self.adjust_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()

    def pause_timer(self):
        if self.is_running:
            self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.time_left = 1500
        self.update_time_label()

    def adjust_timer(self):
        self.pause_timer()
        adjust_window = tk.Toplevel(self.master)
        adjust_window.title("Adjust Time")

        time_label = tk.Label(adjust_window, text="Set time (in minutes):")
        time_label.pack()

        time_entry = tk.Entry(adjust_window)
        time_entry.pack(pady=10)

        confirm_button = tk.Button(adjust_window, text="Confirm", command=lambda: self.confirm_adjustment(adjust_window, time_entry.get()))
        confirm_button.pack()

    def confirm_adjustment(self, adjust_window, time_value):
        try:
            time_value = int(time_value)
            if time_value > 0:
                self.time_left = time_value * 60
                self.update_time_label()
                adjust_window.destroy()
        except ValueError:
            pass

    def update_timer(self):
        if self.is_running and self.time_left > 0:
            self.time_left -= 1
            self.update_time_label()
            self.master.after(1000, self.update_timer)  # 每1000毫秒（1秒）更新一次计时器
        elif self.time_left == 0:
            winsound.Beep(1000, 1000)  # 发出"beep"声音，持续1秒

    def update_time_label(self):
        self.time_label.config(text=self.format_time(self.time_left))

    @staticmethod
    def format_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

root = tk.Tk()
tomato_clock = TomatoClock(root)
root.mainloop()