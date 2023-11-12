import tkinter as tk
import tkinter.messagebox
import chatgpt_integration as chat_api

def initialize_screen():
    root = tk.Tk()
    root.title("Avenge Your Pet")
    root.geometry("800x600")  # Set the size of the window
    return root

def start_game(root, start_button, studio_label):
    studio_label.destroy()  # Remove the studio label
    start_button.destroy()  # Remove the start button
    message_area = create_message_display_area(root)
    entry = create_message_entry(root)
    create_send_button(root, entry, message_area)

def display_start_button(root, studio_label):
    start_button = tk.Button(root, text="Start", command=lambda: start_game(root, start_button, studio_label))
    start_button.pack(pady=10)
    return start_button

def display_studio_name(root):
    label = tk.Label(root, text="Cabinhead Studios Presents", font=("Arial", 24))
    label.pack(pady=20)  # Adding some padding
    return label  # Return the label widget

def create_message_entry(root):
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)
    return entry

def create_send_button(root, entry, message_area):
    def send_message():
        player_message = entry.get()
        update_messages(message_area, "Player: " + player_message)
        clear_entry_box(entry)

        # Direct call to get the narrator's response
        get_narrator_response(player_message, message_area)

    button = tk.Button(root, text="Send", command=send_message)
    button.pack(pady=5)

def get_narrator_response(player_message, message_area):
    # Synchronous call to get ChatGPT response
    narrator_response = chat_api.get_chatgpt_response(player_message)
    update_messages(message_area, "Narrator: " + narrator_response)


def update_messages(text_area, message):
    text_area.config(state=tk.NORMAL)
    text_area.insert(tk.END, message + "\n")
    text_area.config(state=tk.DISABLED)
    text_area.see(tk.END)  # Scroll to the bottom

def clear_entry_box(entry):
    entry.delete(0, tk.END)

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
    studio_label = display_studio_name(root)
    display_start_button(root, studio_label)
    bind_escape_key(root, lambda: on_escape_pressed(root))
    root.mainloop()