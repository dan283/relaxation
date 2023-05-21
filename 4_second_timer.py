import tkinter as tk
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")

        self.timer_label = tk.Label(root, text="0.0", font=("Arial", 24))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.is_running = False
        self.start_time = 0

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time()
            self.update_timer()

            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_timer(self):
        if self.is_running:
            self.is_running = False

            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.is_running:
            elapsed_time = time.time() - self.start_time
            if elapsed_time < 4:
                self.timer_label.config(text=f"{elapsed_time:.1f}")
                self.root.after(100, self.update_timer)  # Update every 100 milliseconds
            else:
                self.start_time = time.time()  # Reset the start time
                self.timer_label.config(text="0.0")
                self.update_timer()

root = tk.Tk()
app = TimerApp(root)
root.mainloop()
