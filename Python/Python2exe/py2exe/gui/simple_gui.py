import os
import tkinter as tk

def main():
    def display_text():
        entered_text = entry_field.get()
        result_label.config(text=f"You entered: {entered_text}")

    # Create the main window
    root = tk.Tk()
    root.title("Simple Tkinter App")

    # Create and pack the widgets
    label = tk.Label(root, text="Enter something:")
    label.pack(pady=10)

    entry_field = tk.Entry(root)
    entry_field.pack(pady=10)

    submit_button = tk.Button(root, text="Submit", command=display_text)
    submit_button.pack(pady=10)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
