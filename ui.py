import tkinter as tk

def initialize_screen():
    root = tk.Tk()
    root.title("Avenge Your Pet")
    root.geometry("1024x768")  # Set the size of the window
    return root

def display_studio_name(root):
    label = tk.Label(root, text="Cabinhead Studios", font=("Arial", 24))
    label.pack(pady=20)  # Adding some padding

def display_start_button(root, start_callback):
    start_button = tk.Button(root, text="Start", command=start_callback)
    start_button.pack(pady=10)

def create_message_entry(root, send_message_callback):
    entry = tk.Entry(root, width=50)
    entry.bind("<Return>", lambda event: send_message_callback(entry.get()))
    entry.pack(pady=5)
    return entry

def create_send_button(root, send_message_callback, entry):
    button = tk.Button(root, text="Send", command=lambda: send_message_callback(entry.get()))
    button.pack(pady=5)

def create_message_display_area(root):
    text_area = tk.Text(root, height=20, width=80)
    text_area.pack(pady=5)
    text_area.config(state=tk.DISABLED)  # Make the text area read-only
    return text_area

def bind_escape_key(root, escape_callback):
    root.bind("<Escape>", lambda event: escape_callback())

def on_escape_pressed(root):
    response = tk.messagebox.askquestion("Exit Game", "Do you want to exit the game?")
    if response == "yes":
        root.quit()  # Exit the game
    # If the response is "no", the function will simply end, and the game will continue

def update_messages(text_area, message):
    text_area.config(state=tk.NORMAL)
    text_area.insert(tk.END, message + "\n")
    text_area.config(state=tk.DISABLED)
    text_area.see(tk.END)  # Scroll to the bottom

def clear_entry_box(entry):
    entry.delete(0, tk.END)

def run_ui():
    root = initialize_screen()
    display_studio_name(root)
    display_start_button(root, start_callback=lambda: print("Game Started!"))
    bind_escape_key(root, lambda: on_escape_pressed(root))
    root.mainloop()