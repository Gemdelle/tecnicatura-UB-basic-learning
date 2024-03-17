import os
import tkinter as tk
from tkinter import scrolledtext

import pygame
import io
import sys

from ui.components.avatar_frame import AvatarFrame
from ui.components.dialog_text import DialogText
from ui.components.frame import Frame

text_to_type_phase_1_1 = "Aprendí hace poco a contar y no sé si me confundí."
text_to_type_phase_1_2 = "- Verificar que la cantidad de hierbas sea la correcta."
text_to_type_phase_1_3 = "- Declarar la variable flores asignándole el valor que corresponde."

typed_text_phase_1_1 = ""
typed_text_phase_1_2 = ""
typed_text_phase_1_3 = ""

# Typing speed (characters per second)
typing_speed = 10

herbs_count = 3
flowers_count = 3

input_text = ('# direction = "north"\n# move = false\nhierbas = 1')
input_active = False

code_text = None

def on_unmap(event, root):
    root.grab_set()

def release_grab(event=None, root=None):
    root.grab_release()


class ConsoleRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)
def execute_code():
    global input_text, input_active
    if code_text is None:
        return

    code_to_execute = code_text.get("1.0", tk.END)
    # Create a StringIO object to capture printed output
    captured_output = io.StringIO()
    # Redirect stdout to the StringIO object
    sys.stdout = captured_output
    # Execute the input code
    try:
        exec(code_to_execute)
    except Exception as e:
        print("Error:", e)
    finally:
        # Restore stdout
        sys.stdout = sys.__stdout__
    # Get the captured output
    output = captured_output.getvalue()
    # Close the StringIO object
    captured_output.close()


def render_field_1(screen, root, go_to_field_2):
    global typed_text_phase_1_1, typed_text_phase_1_2, typed_text_phase_1_3, text_to_type_phase_1_1, text_to_type_phase_1_2, text_to_type_phase_1_3, code_text

    # BACKGROUND #
    background_image = pygame.image.load("assets/background_field_1.png").convert()
    background_rect = background_image.get_rect()
    scaled_image = pygame.transform.scale(background_image, (1920 , 1080))
    screen.blit(scaled_image, background_rect)

    # DIALOG FRAME + AVATAR FRAME #
    frame = Frame(screen, 50, 50, 1750, 300, (100, 100, 100))
    avatar_frame = AvatarFrame(screen, 1700, 100, 10, 370, (0, 0, 0))
    frame.add_element(avatar_frame)

    dialog_text_phase_1_1 = DialogText(screen, 120, 100, 500, 300, typed_text_phase_1_1)
    frame.add_element(dialog_text_phase_1_1)
    dialog_text_phase_1_2 = DialogText(screen, 120, 150, 500, 300, typed_text_phase_1_2)
    frame.add_element(dialog_text_phase_1_2)
    dialog_text_phase_1_3 = DialogText(screen, 120, 200, 500, 300, typed_text_phase_1_3)

    frame.add_element(dialog_text_phase_1_3)

    # Delay for the typing speed
    pygame.time.delay(int(1000 / typing_speed))

    if text_to_type_phase_1_1:
        typed_text_phase_1_1 += text_to_type_phase_1_1[0]
        text_to_type_phase_1_1 = text_to_type_phase_1_1[1:]

    if not text_to_type_phase_1_1:
        if text_to_type_phase_1_2:
            typed_text_phase_1_2 += text_to_type_phase_1_2[0]
            text_to_type_phase_1_2 = text_to_type_phase_1_2[1:]

        if not text_to_type_phase_1_2:
            if text_to_type_phase_1_3:
                typed_text_phase_1_3 += text_to_type_phase_1_3[0]
                text_to_type_phase_1_3 = text_to_type_phase_1_3[1:]
            if not text_to_type_phase_1_3:
                # Make the window transient to prevent focusing issues
                root.attributes("-toolwindow", True)
                root.transient()
                # Set window geometry (size and position)
                root.geometry(f"{600}x{700}+{50}+{350}")
                # Disable window resizing
                root.resizable(False, False)
                # Disable window dragging
                root.overrideredirect(True)

                # Create a scrolled text area for code input
                code_text = scrolledtext.ScrolledText(root, width=500, height=60)
                code_text.pack(padx=10, pady=10)
                # Create a button to run the code
                run_button = tk.Button(root, text="Run Code", command=execute_code)
                run_button.pack(pady=10)
                # Bind events to handle window visibility
                root.bind("<Unmap>", lambda event: on_unmap(event, root))
                root.protocol("WM_DELETE_WINDOW", lambda event: release_grab(event, root))
                # Make the window modal
                root.focus_force()
                # Run the Tkinter event loop
                root.mainloop()
                root.update()
                os.environ['SDL_WINDOWID'] = str(code_text.winfo_id())
                os.environ['SDL_VIDEODRIVER'] = 'windib'
                while True:
                    pygame.display.update()
                    root.update()

    frame.draw()