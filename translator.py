import tkinter as tk
from deep_translator import GoogleTranslator

# Function to translate text
def translate():
    input_text = input_entry.get()
    destination_language = destination_language_var.get()
    translated_text = GoogleTranslator(source='auto', target=destination_language).translate(input_text)
    output_label.config(text="Translated: " + translated_text)

# Create main window
root = tk.Tk()
root.title("Text Translator")

# Input label and entry
input_label = tk.Label(root, text="Enter text to translate:")
input_label.pack()
input_entry = tk.Entry(root, width=50)
input_entry.pack()

# Destination language label and dropdown
destination_language_label = tk.Label(root, text="Select destination language:")
destination_language_label.pack()
destination_language_var = tk.StringVar(root)
destination_language_var.set('en')  # default language
language_dropdown = tk.OptionMenu(root, destination_language_var, 'en', 'es', 'fr', 'de', 'jp', 'ko', 'zh-CN')
language_dropdown.pack()

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack()

# Output label
output_label = tk.Label(root, text="")
output_label.pack()

# Run the Tkinter main loop
root.mainloop()
