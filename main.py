import tkinter as tk
from ui import UI

def main():
    root = tk.Tk()
    root.title("PSR Image Enhancement")
    ui = UI(root)
    root.mainloop()

if __name__ == "__main__":
    main()