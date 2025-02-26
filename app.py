from tkinter import *
from tkinter import scrolledtext
from generate_response import generate_response

window = Tk()
window.title('AI Assistant')
window.geometry('800x700')
window.resizable(True, True)
window.config(bg='#2E3B4E')

def on_generate():
    """
    Handles the button click event to generate a response.
    """
    user_prompt = prompt_entry.get("1.0", END).strip()
    if not user_prompt:
        result_text.delete(1.0, END)
        result_text.insert(END, "Please enter a prompt first")
        return

    result_text.delete(1.0, END)
    result_text.insert(END, "Processing your request...\n\n")
    window.update()

    response = generate_response(user_prompt)
    result_text.delete(1.0, END)
    result_text.insert(END, response)

title_label = Label(window, text="AI Assistant", fg='white', bg='#2E3B4E', font=("Helvetica", 24, 'bold'))
title_label.pack(pady=15)

result_label = Label(window, text="AI Response:", fg='white', bg='#2E3B4E', font=("Helvetica", 14))
result_label.pack(anchor=W, padx=20)

result_text = scrolledtext.ScrolledText(
    window,
    wrap=WORD,
    width=80,
    height=15,
    font=("Helvetica", 12),
    bg='#EFF0F1'
)
result_text.pack(fill=BOTH, expand=True, padx=20, pady=10)
result_text.insert(END, "AI response will appear here...")

prompt_label = Label(window, text="Your Prompt:", fg='white', bg='#2E3B4E', font=("Helvetica", 14))
prompt_label.pack(anchor=W, padx=20, pady=(10, 0))

prompt_entry = Text(
    window,
    wrap=WORD,
    width=80,
    height=8,
    font=("Helvetica", 12),
    bg='#F0F0F0'
)
prompt_entry.pack(fill=X, padx=20, pady=10)

generate_button = Button(
    window,
    text="Generate Response",
    command=on_generate,
    bg='#4CAF50',
    fg='white',
    font=("Helvetica", 14, 'bold'),
    width=20,
    height=2
)
generate_button.pack(pady=20)

window.mainloop()
