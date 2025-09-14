import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
import random
import json
import os

class ColorSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Selector Pro")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure custom styles
        self.style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#f0f0f0')
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'), background='#f0f0f0')
        self.style.configure('Custom.TButton', font=('Arial', 10), padding=10)
        self.style.configure('Color.TButton', font=('Arial', 9), padding=5)
        
        # Variables
        self.selected_colors = []
        self.max_colors = tk.IntVar(value=5)
        self.color_history = []
        self.tagged_color_index = None  # Index of the tagged color
        
        # Load saved colors if exists
        self.load_color_history()
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="🎨 Color Selector Pro", style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Number of colors selection
        colors_frame = ttk.LabelFrame(main_frame, text="Settings", padding="10")
        colors_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        
        ttk.Label(colors_frame, text="Number of colors to select:", style='Header.TLabel').grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        
        colors_spinbox = ttk.Spinbox(colors_frame, from_=1, to=20, textvariable=self.max_colors, width=10)
        colors_spinbox.grid(row=0, column=1, sticky=tk.W)
        
        # Control buttons frame
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Add color button
        add_color_btn = ttk.Button(control_frame, text="➕ Add Color", command=self.add_color, style='Custom.TButton')
        add_color_btn.grid(row=0, column=0, padx=(0, 10))
        
        # Random color button
        random_color_btn = ttk.Button(control_frame, text="🎲 Random Color", command=self.add_random_color, style='Custom.TButton')
        random_color_btn.grid(row=0, column=1, padx=(0, 10))
        
        # Clear all button
        clear_btn = ttk.Button(control_frame, text="🗑️ Clear All", command=self.clear_all_colors, style='Custom.TButton')
        clear_btn.grid(row=0, column=2, padx=(0, 10))
        
        # Fill random button
        fill_random_btn = ttk.Button(control_frame, text="🎯 Fill Random", command=self.fill_random_colors, style='Custom.TButton')
        fill_random_btn.grid(row=0, column=3, padx=(0, 10))
        
        # Tag management buttons
        tag_frame = ttk.Frame(control_frame)
        tag_frame.grid(row=1, column=0, columnspan=4, pady=(10, 0))
        
        tag_color_btn = ttk.Button(tag_frame, text="🏷️ Tag Selected", command=self.tag_selected_color, style='Custom.TButton')
        tag_color_btn.grid(row=0, column=0, padx=(0, 10))
        
        clear_tag_btn = ttk.Button(tag_frame, text="❌ Clear Tag", command=self.clear_tag, style='Custom.TButton')
        clear_tag_btn.grid(row=0, column=1, padx=(0, 10))
        
        random_tag_btn = ttk.Button(tag_frame, text="🎲 Random Tag", command=self.random_tag, style='Custom.TButton')
        random_tag_btn.grid(row=0, column=2, padx=(0, 10))
        
        # Selected colors display
        colors_display_frame = ttk.LabelFrame(main_frame, text="Selected Colors", padding="10")
        colors_display_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 20))
        colors_display_frame.columnconfigure(0, weight=1)
        colors_display_frame.rowconfigure(0, weight=1)
        
        # Canvas for color display
        self.colors_canvas = tk.Canvas(colors_display_frame, height=200, bg='white', relief=tk.SUNKEN, bd=2)
        self.colors_canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Scrollbar for canvas
        scrollbar = ttk.Scrollbar(colors_display_frame, orient="horizontal", command=self.colors_canvas.xview)
        scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        self.colors_canvas.configure(xscrollcommand=scrollbar.set)
        
        # Color info frame
        info_frame = ttk.Frame(colors_display_frame)
        info_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))
        
        self.color_info_label = ttk.Label(info_frame, text="No colors selected", style='Header.TLabel')
        self.color_info_label.grid(row=0, column=0, sticky=tk.W)
        
        # Export/Import frame
        export_frame = ttk.LabelFrame(main_frame, text="Export/Import", padding="10")
        export_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        
        export_btn = ttk.Button(export_frame, text="💾 Export Colors", command=self.export_colors, style='Custom.TButton')
        export_btn.grid(row=0, column=0, padx=(0, 10))
        
        import_btn = ttk.Button(export_frame, text="📁 Import Colors", command=self.import_colors, style='Custom.TButton')
        import_btn.grid(row=0, column=1, padx=(0, 10))
        
        # Color history frame
        history_frame = ttk.LabelFrame(main_frame, text="Color History", padding="10")
        history_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        history_frame.columnconfigure(0, weight=1)
        history_frame.rowconfigure(0, weight=1)
        
        # History listbox
        self.history_listbox = tk.Listbox(history_frame, height=6, font=('Arial', 9))
        self.history_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # History scrollbar
        history_scrollbar = ttk.Scrollbar(history_frame, orient="vertical", command=self.history_listbox.yview)
        history_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.history_listbox.configure(yscrollcommand=history_scrollbar.set)
        
        # History buttons
        history_btn_frame = ttk.Frame(history_frame)
        history_btn_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        use_history_btn = ttk.Button(history_btn_frame, text="Use Selected", command=self.use_history_color, style='Custom.TButton')
        use_history_btn.grid(row=0, column=0, padx=(0, 10))
        
        clear_history_btn = ttk.Button(history_btn_frame, text="Clear History", command=self.clear_history, style='Custom.TButton')
        clear_history_btn.grid(row=0, column=1)
        
        # Bind double-click to history listbox
        self.history_listbox.bind('<Double-1>', lambda e: self.use_history_color())
        
        # Update display
        self.update_colors_display()
        self.update_history_display()
        
    def add_color(self):
        if len(self.selected_colors) >= self.max_colors.get():
            messagebox.showwarning("Limit Reached", f"You can only select {self.max_colors.get()} colors!")
            return
            
        color = colorchooser.askcolor(title="Choose a color")
        if color[1]:  # If a color was selected
            hex_color = color[1]
            self.selected_colors.append(hex_color)
            self.add_to_history(hex_color)
            self.update_colors_display()
            
    def add_random_color(self):
        if len(self.selected_colors) >= self.max_colors.get():
            messagebox.showwarning("Limit Reached", f"You can only select {self.max_colors.get()} colors!")
            return
            
        # Generate random color
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        
        self.selected_colors.append(hex_color)
        self.add_to_history(hex_color)
        self.update_colors_display()
        
    def fill_random_colors(self):
        self.clear_all_colors()
        num_colors = self.max_colors.get()
        
        for _ in range(num_colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            hex_color = f"#{r:02x}{g:02x}{b:02x}"
            self.selected_colors.append(hex_color)
            self.add_to_history(hex_color)
            
        self.update_colors_display()
        
    def clear_all_colors(self):
        self.selected_colors.clear()
        self.tagged_color_index = None
        self.update_colors_display()
        
    def update_colors_display(self):
        self.colors_canvas.delete("all")
        
        if not self.selected_colors:
            self.colors_canvas.create_text(400, 100, text="No colors selected", font=('Arial', 14), fill='gray')
            self.color_info_label.config(text="No colors selected")
            return
            
        # Calculate color rectangle dimensions
        canvas_width = self.colors_canvas.winfo_reqwidth() or 400
        color_width = max(60, canvas_width // len(self.selected_colors))
        color_height = 150
        
        # Set canvas scroll region
        total_width = len(self.selected_colors) * color_width
        self.colors_canvas.configure(scrollregion=(0, 0, total_width, color_height))
        
        for i, color in enumerate(self.selected_colors):
            x1 = i * color_width
            x2 = x1 + color_width - 5
            y1 = 10
            y2 = y1 + color_height - 20
            
            # Draw color rectangle
            outline_color = 'red' if i == self.tagged_color_index else 'black'
            outline_width = 4 if i == self.tagged_color_index else 2
            self.colors_canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=outline_color, width=outline_width)
            
            # Draw tag indicator if this is the tagged color
            if i == self.tagged_color_index:
                tag_x = x2 - 15
                tag_y = y1 + 10
                self.colors_canvas.create_text(tag_x, tag_y, text="🏷️", font=('Arial', 12), fill='red')
            
            # Draw color hex code
            text_x = x1 + color_width // 2
            text_y = y2 + 15
            self.colors_canvas.create_text(text_x, text_y, text=color, font=('Arial', 8), fill='black')
            
            # Add click handler for color removal
            self.colors_canvas.tag_bind(f"color_{i}", "<Button-1>", lambda e, idx=i: self.remove_color(idx))
            
        # Update info label
        tag_info = f" | Tagged: {self.selected_colors[self.tagged_color_index] if self.tagged_color_index is not None else 'None'}"
        self.color_info_label.config(text=f"Selected {len(self.selected_colors)}/{self.max_colors.get()} colors{tag_info}")
        
    def remove_color(self, index):
        if 0 <= index < len(self.selected_colors):
            self.selected_colors.pop(index)
            # Adjust tagged color index if necessary
            if self.tagged_color_index is not None:
                if index < self.tagged_color_index:
                    self.tagged_color_index -= 1
                elif index == self.tagged_color_index:
                    self.tagged_color_index = None
                elif self.tagged_color_index >= len(self.selected_colors):
                    self.tagged_color_index = None
            self.update_colors_display()
            
    def add_to_history(self, color):
        if color not in self.color_history:
            self.color_history.insert(0, color)
            # Keep only last 50 colors in history
            if len(self.color_history) > 50:
                self.color_history = self.color_history[:50]
            self.save_color_history()
            self.update_history_display()
            
    def update_history_display(self):
        self.history_listbox.delete(0, tk.END)
        for color in self.color_history:
            self.history_listbox.insert(tk.END, color)
            
    def use_history_color(self):
        selection = self.history_listbox.curselection()
        if selection and len(self.selected_colors) < self.max_colors.get():
            color = self.color_history[selection[0]]
            self.selected_colors.append(color)
            self.update_colors_display()
        elif len(self.selected_colors) >= self.max_colors.get():
            messagebox.showwarning("Limit Reached", f"You can only select {self.max_colors.get()} colors!")
            
    def clear_history(self):
        self.color_history.clear()
        self.save_color_history()
        self.update_history_display()
        
    def export_colors(self):
        if not self.selected_colors:
            messagebox.showwarning("No Colors", "No colors to export!")
            return
            
        from tkinter import filedialog
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                data = {
                    'colors': self.selected_colors,
                    'max_colors': self.max_colors.get(),
                    'history': self.color_history,
                    'tagged_color_index': self.tagged_color_index
                }
                
                if filename.endswith('.json'):
                    with open(filename, 'w') as f:
                        json.dump(data, f, indent=2)
                else:
                    with open(filename, 'w') as f:
                        f.write("Selected Colors:\n")
                        for i, color in enumerate(self.selected_colors):
                            tag_marker = " [TAGGED]" if i == self.tagged_color_index else ""
                            f.write(f"{color}{tag_marker}\n")
                        f.write(f"\nMax Colors: {self.max_colors.get()}\n")
                        f.write(f"Tagged Color Index: {self.tagged_color_index}\n")
                        f.write("\nColor History:\n")
                        for color in self.color_history:
                            f.write(f"{color}\n")
                            
                messagebox.showinfo("Success", f"Colors exported to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")
                
    def import_colors(self):
        from tkinter import filedialog
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                if filename.endswith('.json'):
                    with open(filename, 'r') as f:
                        data = json.load(f)
                    self.selected_colors = data.get('colors', [])
                    self.max_colors.set(data.get('max_colors', 5))
                    self.color_history = data.get('history', [])
                    self.tagged_color_index = data.get('tagged_color_index', None)
                else:
                    with open(filename, 'r') as f:
                        lines = f.readlines()
                    colors = []
                    for line in lines:
                        line = line.strip()
                        if line.startswith('#') and len(line) == 7:
                            colors.append(line)
                    self.selected_colors = colors
                    
                self.update_colors_display()
                self.update_history_display()
                messagebox.showinfo("Success", f"Colors imported from {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import: {str(e)}")
                
    def save_color_history(self):
        try:
            with open('color_history.json', 'w') as f:
                json.dump(self.color_history, f)
        except:
            pass
            
    def load_color_history(self):
        try:
            if os.path.exists('color_history.json'):
                with open('color_history.json', 'r') as f:
                    self.color_history = json.load(f)
        except:
            self.color_history = []
            
    def tag_selected_color(self):
        if not self.selected_colors:
            messagebox.showwarning("No Colors", "Please select some colors first!")
            return
            
        # Create a simple dialog to select which color to tag
        tag_window = tk.Toplevel(self.root)
        tag_window.title("Select Color to Tag")
        tag_window.geometry("400x300")
        tag_window.configure(bg='#f0f0f0')
        tag_window.transient(self.root)
        tag_window.grab_set()
        
        # Center the window
        tag_window.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, self.root.winfo_rooty() + 50))
        
        ttk.Label(tag_window, text="Click on a color to tag it:", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Create a frame for color selection
        color_frame = tk.Frame(tag_window, bg='#f0f0f0')
        color_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Create color buttons
        for i, color in enumerate(self.selected_colors):
            btn = tk.Button(color_frame, text=color, bg=color, fg='white' if self.is_dark_color(color) else 'black',
                          font=('Arial', 10), width=15, height=2,
                          command=lambda idx=i: self.set_tagged_color(idx, tag_window))
            btn.pack(pady=2)
            
        # Cancel button
        ttk.Button(tag_window, text="Cancel", command=tag_window.destroy).pack(pady=10)
        
    def set_tagged_color(self, index, window):
        self.tagged_color_index = index
        self.update_colors_display()
        window.destroy()
        messagebox.showinfo("Tagged", f"Color {self.selected_colors[index]} has been tagged!")
        
    def clear_tag(self):
        self.tagged_color_index = None
        self.update_colors_display()
        messagebox.showinfo("Tag Cleared", "No color is tagged now.")
        
    def random_tag(self):
        if not self.selected_colors:
            messagebox.showwarning("No Colors", "Please select some colors first!")
            return
            
        self.tagged_color_index = random.randint(0, len(self.selected_colors) - 1)
        self.update_colors_display()
        messagebox.showinfo("Random Tag", f"Color {self.selected_colors[self.tagged_color_index]} has been randomly tagged!")
        
    def is_dark_color(self, hex_color):
        """Check if a color is dark (for text color selection)"""
        hex_color = hex_color.lstrip('#')
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        # Calculate luminance
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        return luminance < 0.5

def main():
    root = tk.Tk()
    app = ColorSelectorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
