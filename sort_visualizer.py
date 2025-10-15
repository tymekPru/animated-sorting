from tkinter import * 
import tkinter as tk 
import random
import insertion_sort

def get_random_numbers() -> list[int]:
    data: list[float] = []
    for n in range(100):
        data.append(n*3)
    random.shuffle(data)
    return data 

class SortVisualizer:
    def __init__(self, alg_type: int):
        self.root = Tk()
        self.root.title("Sorting Visualized")

        window_width = 850
        window_height = 450
        x = int((self.root.winfo_screenwidth() / 2) - (window_width / 2))
        y = int((self.root.winfo_screenheight() / 2) - (window_height / 2))
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.wm_resizable(False,False)

        alg_map = {
            1: [insertion_sort.sort, "Insertion sort"]
        }
        self.sort_func = alg_map[alg_type][0]
        self.label = tk.Label(self.root, text=alg_map[alg_type][1])
        self.label.pack()

        self.canvas_width = 800
        self.canvas_height = 375
        self.canvas = Canvas(self.root, bg="white", height=self.canvas_height, width=self.canvas_width)
        self.canvas.pack()

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.start_button = tk.Button(button_frame, text="Start", command=self.start_sort)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_sort)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self.reset_sort()
    
    def reset_sort(self):
        self.data = get_random_numbers()
        self.draw_bars(self.data, "black")

    def start_sort(self):
        gen = self.sort_func(self.data)
        self.animate(gen)

    def animate(self, generator):
        try:
            data = next(generator)
            self.draw_bars(data)
            self.root.after(25, lambda: self.animate(generator))
        except StopIteration:
            self.draw_bars(self.data, "green")
    
    def draw_bars(self, data, color = 'blue'):
        self.canvas.delete("all")
        bar_width = self.canvas_width/len(data)
        for i, val in enumerate(data):
            x0 = i * bar_width
            y0 = self.canvas_height
            x1 = (i+1) * bar_width
            y1 = self.canvas_height - val
            self.canvas.create_rectangle(x0, y0, x1, y1, fill = color)
        self.root.update_idletasks()

    def start(self):
        mainloop()

