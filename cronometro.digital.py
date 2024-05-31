import tkinter as tk

class Stopwatch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cronômetro digital")
        self.configure(background ="white")
        
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.is_running = False
        
        self.time_label = tk.Label(self, text="00:00:00", font=("Helvetica", 100), bg= "white", fg="green")
        self.time_label.pack()
        
        self.start_button = tk.Button(self, text="Iniciar", font=("Helvica", 20), command=self.start_timer, bg="white", fg="green",)
        self.start_button.pack(side=tk.LEFT, padx=180)
        
        self.stop_button = tk.Button(self, text="Parar", font=("Helvica", 20), command=self.stop_timer, bg="white", fg="green")
        self.stop_button.pack(side=tk.LEFT, padx=180)
        
        self.reset_button = tk.Button(self, text="Resetar", font=("Helvica", 20), command=self.reset_timer, bg="white", fg="green")
        self.reset_button.pack(side=tk.LEFT, padx=180)
        
        self.update_time()
    
    def update_time(self):
        if self.is_running:
            self.seconds += 1
            if self.seconds >= 60:
                self.seconds = 0
                self.minutes += 1
                if self.minutes >= 60:
                    self.minutes = 0
                    self.hours += 1
        
        self.update_display()
        self.after(1000, self.update_time)
    
    def update_display(self):
        time_string = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        self.time_label.config(text=time_string)
    
    def start_timer(self):
        self.is_running = True
    
    def stop_timer(self):
        self.is_running = False
    
    def reset_timer(self):
        self.is_running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.update_display()

if __name__ == "__main__":
    app = Stopwatch()
    app.mainloop()

