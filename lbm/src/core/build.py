import tkinter as tk
from tkinter import ttk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.canvas_width = 1000
        self.canvas_height = 400
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white", bd=3, relief=tk.SUNKEN)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.setup_navbar()
        self.setup_tools()
        self.setup_events()
        self.obstacle = []

    def setup_navbar(self):
        self.navbar = tk.Menu(self.root)
        self.root.config(menu=self.navbar)

        # File menu
        self.file_menu = tk.Menu(self.navbar, tearoff=False)
        self.navbar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Plot Fluid", command=self.plot_fluid)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Edit menu
        self.edit_menu = tk.Menu(self.navbar, tearoff=False)
        self.navbar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.undo)

    def setup_tools(self):
        self.selected_tool = "pen"
        self.colors = ["black"]
        self.selected_color = self.colors[0]
        self.brush_sizes = [10, 14, 18, 24]
        self.selected_size = self.brush_sizes[0]
        self.pen_types = ["round", "square"]
        self.selected_pen_type = self.pen_types[0]

        self.tool_frame = ttk.LabelFrame(self.root, text="Tools")
        self.tool_frame.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.Y)

        self.pen_button = ttk.Button(self.tool_frame, text="Pen", command=self.select_pen_tool)
        self.pen_button.pack(side=tk.TOP, padx=5, pady=5)

        self.brush_size_label = ttk.Label(self.tool_frame, text="Brush Size:")
        self.brush_size_label.pack(side=tk.TOP, padx=5, pady=5)

        self.brush_size_combobox = ttk.Combobox(self.tool_frame, values=self.brush_sizes, state="readonly")
        self.brush_size_combobox.current(0)
        self.brush_size_combobox.pack(side=tk.TOP, padx=5, pady=5)
        self.brush_size_combobox.bind("<<ComboboxSelected>>", lambda event: self.select_size(int(self.brush_size_combobox.get())))

        self.color_label = ttk.Label(self.tool_frame, text="Color:")
        self.color_label.pack(side=tk.TOP, padx=5, pady=5)

        self.color_combobox = ttk.Combobox(self.tool_frame, values=self.colors, state="readonly")
        self.color_combobox.current(0)
        self.color_combobox.pack(side=tk.TOP, padx=5, pady=5)
        self.color_combobox.bind("<<ComboboxSelected>>", lambda event: self.select_color(self.color_combobox.get()))

        self.pen_type_label = ttk.Label(self.tool_frame, text="Pen Type:")
        self.pen_type_label.pack(side=tk.TOP, padx=5, pady=5)

        self.pen_type_combobox = ttk.Combobox(self.tool_frame, values=self.pen_types, state="readonly")
        self.pen_type_combobox.current(0)
        self.pen_type_combobox.pack(side=tk.TOP, padx=5, pady=5)
        self.pen_type_combobox.bind("<<ComboboxSelected>>", lambda event: self.select_pen_type(self.pen_type_combobox.get()))

        self.clear_button = ttk.Button(self.tool_frame, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack(side=tk.TOP, padx=5, pady=5)

    def setup_events(self):
        self.canvas.bind("<Button-1>", self.draw)

    def select_pen_tool(self):
        self.selected_tool = "pen"

    def select_size(self, size):
        self.selected_size = size

    def select_color(self, color):
        self.selected_color = color

    def select_pen_type(self, pen_type):
        self.selected_pen_type = pen_type

    def draw(self, event):
        if self.selected_tool == "pen":
                if self.selected_pen_type == "round":
                    x1 = event.x - self.selected_size
                    y1 = event.y - self.selected_size
                    x2 = event.x + self.selected_size
                    y2 = event.y + self.selected_size
                    self.canvas.create_oval(x1, y1, x2, y2, fill=self.selected_color, outline=self.selected_color)
                    new_y = 0
                    if event.y >= 200:
                        new_y = -(event.y - 200)
                    elif event.y < 200: 
                        new_y = abs(event.y - 200)    
                    self.obstacle.append(['Canvas', 'cylinder', self.selected_size / 50 , [event.x /400 , new_y /400]])
                elif self.selected_pen_type == "square":
                    x1 = event.x - self.selected_size
                    y1 = event.y - self.selected_size
                    x2 = event.x + self.selected_size
                    y2 = event.y + self.selected_size
                    new_y = 0
                    if event.y >= 200:
                        new_y = -(event.y - 200)
                    elif event.y < 200: 
                        new_y = abs(event.y - 200)
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.selected_color, outline=self.selected_color)
                    self.obstacle.append(['Canvas', 'square', self.selected_size / 50, [event.x /400 , new_y /400]])

    def clear_canvas(self):
        self.canvas.delete("all")

    def plot_fluid(self):
        f

        print(self.obstacle)

    def undo(self):
        items = self.canvas.find_all()
        if items:
            self.canvas.delete(items[-1])

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Paint Application")
    app = PaintApp(root)
    root.mainloop()
