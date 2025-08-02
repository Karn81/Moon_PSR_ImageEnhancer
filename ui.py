# import tkinter as tk
# from tkinter import filedialog, ttk
# from image_processing import ImageProcessing

# class UI:
#     def __init__(self, root):
#         self.root = root
#         self.image_processing = ImageProcessing("input_images", "outer_images")

#         # Create a main frame to hold all the widgets
#         self.main_frame = ttk.Frame(self.root, padding="10")
#         self.main_frame.pack(fill="both", expand=True)

#         # Create a style object to configure the font
#         self.style = ttk.Style()
#         self.style.configure("MyFont.TButton", font=("Segoe UI", 12))
#         self.style.configure("MyFont.TLabel", font=("Segoe UI", 12))
#         self.style.configure("MyFont.TEntry", font=("Segoe UI", 12))

#         # Create a header frame with a logo and title
#         self.header_frame = ttk.Frame(self.main_frame, padding="10")
#         self.header_frame.pack(fill="x")
#         self.logo_label = ttk.Label(self.header_frame, text="PSR Image Enhancement", style="MyFont.TLabel")
#         self.logo_label.pack(side="left", padx=10)
#         self.title_label = ttk.Label(self.header_frame, text="With Reduction", style="MyFont.TLabel")
#         self.title_label.pack(side="left", padx=10)

#         # Create a content frame to hold the input and output widgets
#         self.content_frame = ttk.Frame(self.main_frame, padding="10")
#         self.content_frame.pack(fill="both", expand=True)

#         # Create an input frame to hold the input widgets
#         self.input_frame = ttk.Frame(self.content_frame, padding="10")
#         self.input_frame.pack(fill="x")

#         # Create input frame widgets
#         self.input_label = ttk.Label(self.input_frame, text="Input Image:", style="MyFont.TLabel")
#         self.input_label.pack(pady=5)
#         self.input_entry = ttk.Entry(self.input_frame, width=40, style="MyFont.TEntry")
#         self.input_entry.pack(pady=5)
#         self.browse_button = ttk.Button(self.input_frame, text="Browse", command=self.browse_image, style="MyFont.TButton")
#         self.browse_button.pack(pady=5)

#         # Create a separator between input and output frames
#         self.separator = ttk.Separator(self.content_frame, orient="horizontal")
#         self.separator.pack(fill="x", padx=5, pady=5)

#         # Create an output frame to hold the output widgets
#         self.output_frame = ttk.Frame(self.content_frame, padding="10")
#         self.output_frame.pack(fill="x")

#         # Create output frame widgets
#         self.output_label = ttk.Label(self.output_frame, text="Enhanced Image:", style="MyFont.TLabel")
#         self.output_label.pack(pady=5)
#         self.output_entry = ttk.Entry(self.output_frame, width=40, style="MyFont.TEntry")
#         self.output_entry.pack(pady=5)
#         self.reduced_output_label = ttk.Label(self.output_frame, text="Reduced Image:", style="MyFont.TLabel")
#         self.reduced_output_label.pack(pady=5)
#         self.reduced_output_entry = ttk.Entry(self.output_frame, width=40, style="MyFont.TEntry")
#         self.reduced_output_entry.pack(pady=5)
#         self.enhance_button = ttk.Button(self.output_frame, text="Enhance", command=self.enhance_image, style="MyFont.TButton")
#         self.enhance_button.pack(pady=5)

#         # Create a status bar to display messages
#         self.status_bar = ttk.Label(self.main_frame, text="", relief="sunken", anchor="w", style="MyFont.TLabel")
#         self.status_bar.pack(fill="x")

#     def browse_image(self):
#         image_path = filedialog.askopenfilename()
#         self.input_entry.delete(0, tk.END)
#         self.input_entry.insert(0, image_path)

#     def enhance_image(self):
#         image_path = self.input_entry.get()
#         enhanced_image_path, reduced_image_path = self.image_processing.enhance_image(image_path)
#         if enhanced_image_path and reduced_image_path:
#             self.output_entry.delete(0, tk.END)
#             self.output_entry.insert(0, enhanced_image_path)
#             self.reduced_output_entry.delete(0, tk.END)
#             self.reduced_output_entry.insert(0, reduced_image_path)
#             self.status_bar.config(text="Image enhanced and reduced successfully!")
#         else:
#             self.status_bar.config(text="Failed to enhance or reduce the image.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("PSR Image Enhancement")
#     root.geometry("600x500")  # Increased size to accommodate new widgets
#     root.resizable(False, False)
#     my_gui = UI(root)
#     root.mainloop()
# import tkinter as tk
# from tkinter import filedialog, ttk
# from image_processing import ImageProcessing

# class UI:
#     def __init__(self, root):
#         self.root = root
#         self.image_processing = ImageProcessing("input_images", "outer_images")

#         # Configure the root window
#         self.root.title("PSR Image Enhancement")
#         self.root.geometry("700x600")
#         self.root.resizable(True, True)

#         # Create a main frame to hold all the widgets
#         self.main_frame = ttk.Frame(self.root, padding="15", style="Main.TFrame")
#         self.main_frame.pack(fill="both", expand=True)

#         # Create a style object to configure the font and colors
#         self.style = ttk.Style()
#         self.style.configure("Main.TFrame", background="#f0f0f0")
#         self.style.configure("MyFont.TButton", font=("Segoe UI", 12), padding=6)
#         self.style.configure("MyFont.TLabel", font=("Segoe UI", 12), background="#f0f0f0")
#         self.style.configure("MyFont.TEntry", font=("Segoe UI", 12))
#         self.style.configure("MyFont.TSeparator", background="#dcdcdc")
#         self.style.configure("MyFont.TFrame", background="#f0f0f0")
#         self.style.configure("MyFont.TLabel", background="#f0f0f0")
#         self.style.configure("MyFont.TButton", background="#007bff", foreground="white")
#         self.style.map("MyFont.TButton", background=[("active", "#0056b3")])

#         # Create a header frame with a logo and title
#         self.header_frame = ttk.Frame(self.main_frame, padding="10", style="MyFont.TFrame")
#         self.header_frame.pack(fill="x")
#         self.logo_label = ttk.Label(self.header_frame, text="Image Enhancement Project", style="MyFont.TLabel")
#         self.logo_label.pack(side="left", padx=10)
#         self.title_label = ttk.Label(self.header_frame, text="Enhance and Reduce Your Images", style="MyFont.TLabel")
#         self.title_label.pack(side="left", padx=10)

#         # Create a content frame to hold the input and output widgets
#         self.content_frame = ttk.Frame(self.main_frame, padding="15", style="MyFont.TFrame")
#         self.content_frame.pack(fill="both", expand=True)

#         # Create an input frame to hold the input widgets
#         self.input_frame = ttk.Frame(self.content_frame, padding="10", style="MyFont.TFrame")
#         self.input_frame.pack(fill="x")

#         # Create input frame widgets
#         self.input_label = ttk.Label(self.input_frame, text="Input Image:", style="MyFont.TLabel")
#         self.input_label.pack(pady=5)
#         self.input_entry = ttk.Entry(self.input_frame, width=50, style="MyFont.TEntry")
#         self.input_entry.pack(pady=5)
#         self.browse_button = ttk.Button(self.input_frame, text="Browse", command=self.browse_image, style="MyFont.TButton")
#         self.browse_button.pack(pady=5)

#         # Create a separator between input and output frames
#         self.separator = ttk.Separator(self.content_frame, orient="horizontal", style="MyFont.TSeparator")
#         self.separator.pack(fill="x", padx=5, pady=10)

#         # Create an output frame to hold the output widgets
#         self.output_frame = ttk.Frame(self.content_frame, padding="10", style="MyFont.TFrame")
#         self.output_frame.pack(fill="x")

#         # Create output frame widgets
#         self.output_label = ttk.Label(self.output_frame, text="Enhanced Image:", style="MyFont.TLabel")
#         self.output_label.pack(pady=5)
#         self.output_entry = ttk.Entry(self.output_frame, width=50, style="MyFont.TEntry")
#         self.output_entry.pack(pady=5)
#         self.reduced_output_label = ttk.Label(self.output_frame, text="Reduced Image:", style="MyFont.TLabel")
#         self.reduced_output_label.pack(pady=5)
#         self.reduced_output_entry = ttk.Entry(self.output_frame, width=50, style="MyFont.TEntry")
#         self.reduced_output_entry.pack(pady=5)
#         self.enhance_button = ttk.Button(self.output_frame, text="Enhance", command=self.enhance_image, style="MyFont.TButton")
#         self.enhance_button.pack(pady=10)

#         # Create a status bar to display messages
#         self.status_bar = ttk.Label(self.main_frame, text="", relief="sunken", anchor="w", style="MyFont.TLabel")
#         self.status_bar.pack(fill="x", pady=5)

#     def browse_image(self):
#         image_path = filedialog.askopenfilename()
#         self.input_entry.delete(0, tk.END)
#         self.input_entry.insert(0, image_path)

#     def enhance_image(self):
#         image_path = self.input_entry.get()
#         enhanced_image_path, reduced_image_path = self.image_processing.enhance_image(image_path)
#         if enhanced_image_path and reduced_image_path:
#             self.output_entry.delete(0, tk.END)
#             self.output_entry.insert(0, enhanced_image_path)
#             self.reduced_output_entry.delete(0, tk.END)
#             self.reduced_output_entry.insert(0, reduced_image_path)
#             self.status_bar.config(text="Image enhanced and reduced successfully!")
#         else:
#             self.status_bar.config(text="Failed to enhance or reduce the image.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     my_gui = UI(root)
#     root.mainloop()
import tkinter as tk
from tkinter import filedialog, ttk
from image_processing import ImageProcessing

class UI:
    def __init__(self, root):
        self.root = root
        self.image_processing = ImageProcessing("input_images", "outer_images")

        # Configure the root window
        self.root.title("PSR Image Enhancement")
        self.root.geometry("700x600")
        self.root.resizable(True, True)

        # Create a style object to configure the font and colors
        self.style = ttk.Style()
        self.style.configure("Main.TFrame", background="#f0f0f0")
        self.style.configure("MyFont.TButton", font=("Segoe UI", 12), padding=6)
        self.style.configure("MyFont.TLabel", font=("Segoe UI", 12), background="#f0f0f0")
        self.style.configure("MyFont.TEntry", font=("Segoe UI", 12))
        self.style.configure("MyFont.TSeparator", background="#dcdcdc")
        self.style.configure("MyFont.TFrame", background="#f0f0f0")
        self.style.configure("MyFont.TLabel", background="#f0f0f0")
        self.style.configure("MyFont.TButton", background="#007bff", foreground="white")
        self.style.map("MyFont.TButton", background=[("active", "#0056b3")])

        # Create a main frame to hold all the widgets
        self.main_frame = ttk.Frame(self.root, padding="15", style="Main.TFrame")
        self.main_frame.pack(fill="both", expand=True)

        # Create a header frame for the logo and title
        self.header_frame = ttk.Frame(self.main_frame, padding="10", style="MyFont.TFrame")
        self.header_frame.pack(fill="x")

        # Create the logo label with Marathi text
        self.logo_label = tk.Label(self.header_frame, text="वासवी शक्ती", font=("Noto Sans Devanagari", 24, "bold"), bg="#f0f0f0", fg="#FFA500")
        self.logo_label.pack(pady=10, padx=10, anchor="center")

        # Create a sub-frame for the title
        self.title_frame = ttk.Frame(self.main_frame, padding="10", style="MyFont.TFrame")
        self.title_frame.pack(fill="x")
        self.title_label = ttk.Label(self.title_frame, text="Enhance and Reduce Your Images", style="MyFont.TLabel")
        self.title_label.pack(side="left", padx=10)

        # Create a content frame to hold the input and output widgets
        self.content_frame = ttk.Frame(self.main_frame, padding="15", style="MyFont.TFrame")
        self.content_frame.pack(fill="both", expand=True)

        # Create an input frame to hold the input widgets
        self.input_frame = ttk.Frame(self.content_frame, padding="10", style="MyFont.TFrame")
        self.input_frame.pack(fill="x")

        # Create input frame widgets
        self.input_label = ttk.Label(self.input_frame, text="Input Image:", style="MyFont.TLabel")
        self.input_label.pack(pady=5)
        self.input_entry = ttk.Entry(self.input_frame, width=50, style="MyFont.TEntry")
        self.input_entry.pack(pady=5)
        self.browse_button = ttk.Button(self.input_frame, text="Browse", command=self.browse_image, style="MyFont.TButton")
        self.browse_button.pack(pady=5)

        # Create a separator between input and output frames
        self.separator = ttk.Separator(self.content_frame, orient="horizontal", style="MyFont.TSeparator")
        self.separator.pack(fill="x", padx=5, pady=10)

        # Create an output frame to hold the output widgets
        self.output_frame = ttk.Frame(self.content_frame, padding="10", style="MyFont.TFrame")
        self.output_frame.pack(fill="x")

        # Create output frame widgets
        self.output_label = ttk.Label(self.output_frame, text="Enhanced Image:", style="MyFont.TLabel")
        self.output_label.pack(pady=5)
        self.output_entry = ttk.Entry(self.output_frame, width=50, style="MyFont.TEntry")
        self.output_entry.pack(pady=5)
        self.reduced_output_label = ttk.Label(self.output_frame, text="Reduced Image:", style="MyFont.TLabel")
        self.reduced_output_label.pack(pady=5)
        self.reduced_output_entry = ttk.Entry(self.output_frame, width=50, style="MyFont.TEntry")
        self.reduced_output_entry.pack(pady=5)
        self.enhance_button = ttk.Button(self.output_frame, text="Enhance", command=self.enhance_image, style="MyFont.TButton")
        self.enhance_button.pack(pady=10)

        # Create a status bar to display messages
        self.status_bar = ttk.Label(self.main_frame, text="", relief="sunken", anchor="w", style="MyFont.TLabel")
        self.status_bar.pack(fill="x", pady=5)

    def browse_image(self):
        image_path = filedialog.askopenfilename()
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, image_path)

    def enhance_image(self):
        image_path = self.input_entry.get()
        enhanced_image_path, reduced_image_path = self.image_processing.enhance_image(image_path)
        if enhanced_image_path and reduced_image_path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, enhanced_image_path)
            self.reduced_output_entry.delete(0, tk.END)
            self.reduced_output_entry.insert(0, reduced_image_path)
            self.status_bar.config(text="Image enhanced and reduced successfully!")
        else:
            self.status_bar.config(text="Failed to enhance or reduce the image.")

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = UI(root)
    root.mainloop()
