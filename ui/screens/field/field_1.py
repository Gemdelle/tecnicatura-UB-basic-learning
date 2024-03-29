import os

import pygame
import io
import sys

from core.field_1_character_status import Field1CharacterStatus
from ui.components.avatar_frame import AvatarFrame
from ui.components.button import Button
from ui.components.dialogue_text import DialogueText
from ui.components.frame import Frame

text_to_type_phase_1_1_backup = "Aprendí hace poco a contar y no sé si me confundí."
text_to_type_phase_1_2_backup = "- Verificar que la cantidad de hierbas sea la correcta."
text_to_type_phase_1_3_backup = "- Declarar la variable flores asignándole el valor que corresponde."

text_to_type_phase_1_1 = "Aprendí hace poco a contar y no sé si me confundí."
text_to_type_phase_1_2 = "- Verificar que la cantidad de hierbas sea la correcta."
text_to_type_phase_1_3 = "- Declarar la variable flores asignándole el valor que corresponde."

typed_text_phase_1_1 = ""
typed_text_phase_1_2 = ""
typed_text_phase_1_3 = ""

text_to_type_sad_phase_1_1_backup = "No te equivoques kpo por favor"
text_to_type_sad_phase_1_1 = "No te equivoques kpo por favor"
typed_text_sad_phase_1_1 = ""

text_to_type_happy_phase_1_1_backup = "Bien ahi maquina, pasaste la prueba"
text_to_type_happy_phase_1_1 = "Bien ahi maquina, pasaste la prueba"
typed_text_happy_phase_1_1 = ""

# Typing speed (characters per second)
typing_speed = 10

herbs_count = 3
flowers_count = 3

code_text = [
    'hierbas = 1'
]
validation_code_text = ['print(hierbas == 3)']

cursor = 0
active = True
field_1_character_status = Field1CharacterStatus.DEFAULT

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def execute_code():
    global code_text, field_1_character_status
    if code_text == "":
        return
    code_to_validate = code_text.copy()
    for code in validation_code_text:
        code_to_validate.append(code)

    code_to_execute = "\n".join(code_to_validate)
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
    output = captured_output.getvalue().replace("\n", "")
    # Close the StringIO object
    captured_output.close()
    if output == "True":
        field_1_character_status = Field1CharacterStatus.HAPPY
        #go_to_field_2()
    else:
        field_1_character_status = Field1CharacterStatus.SAD

def save_code(text):
    global code_text
    code_text[-1] += text

def erase_code():
    global code_text
    code_text[-1] = code_text[-1][:-1]
    if len(code_text[-1]) == 0:
        if len(code_text) > 1:
            code_text = code_text[:-1]

def line_break():
    code_text.append("")

def render_field_1(screen, go_to_field_2):
    global text_to_type_happy_phase_1_1,typed_text_happy_phase_1_1,field_1_character_status, text_to_type_sad_phase_1_1, typed_text_phase_1_1, typed_text_phase_1_2, typed_text_phase_1_3, text_to_type_phase_1_1, text_to_type_phase_1_2, text_to_type_phase_1_3, code_text, active,cursor, typed_text_sad_phase_1_1
    code_area = pygame.image.load(resource_path("assets\\fields\\coding-area.png")).convert_alpha()
    code_frame = Frame(screen, 50, 350, 600, 700, (100, 100, 100), code_area)

    if field_1_character_status == Field1CharacterStatus.HAPPY:
        code_button = Button(screen, 300, 950, 100, 60, "Next", (0, 0, 0), "White", lambda: go_to_field_2())
        code_button.check_click()
        code_frame.add_element(code_button)
    else:
        code_button = Button(screen, 300, 950, 100,60, "Run", (0, 0, 0),"White", lambda: execute_code())
        code_button.check_click()
        code_frame.add_element(code_button)


    if cursor % 4 == 0 and active and code_text[-1] and not field_1_character_status == Field1CharacterStatus.HAPPY:
        code_text[-1] += "|"
    cursor += 1
    for row, line in enumerate(code_text):
        code_text_component = DialogueText(screen, 60, 360 + (row * 40), 500, 600, line)
        code_frame.add_element(code_text_component)

    # BACKGROUND #
    background_image = pygame.image.load(resource_path("assets\\fields\\00-home.png")).convert_alpha()
    background_rect = background_image.get_rect()
    scaled_image = pygame.transform.scale(background_image, (1920 , 1080))
    screen.blit(scaled_image, background_rect)

    # DIALOGUE FRAME + AVATAR FRAME #
    dialogue_frame = pygame.image.load(resource_path("assets\\fields\\instructions.png")).convert_alpha()
    frame = Frame(screen, 50, 30, 1756, 266, (100, 100, 100), dialogue_frame)

    avatar_frame_img = pygame.image.load(resource_path("assets\\fields\\face-frame.png")).convert_alpha()
    avatar_frame = AvatarFrame(screen, 1500, 30, 367, 384, (0, 0, 0), avatar_frame_img)
    frame.add_element(avatar_frame)

    if field_1_character_status == Field1CharacterStatus.HAPPY:
        avatar_img = pygame.image.load(resource_path("assets\\characters\\01-fields-default-happy-character.png")).convert_alpha()
        avatar_img_frame = AvatarFrame(screen, 1500, 30, 367, 384, (0, 0, 0), avatar_img)
        frame.add_element(avatar_img_frame)
    elif field_1_character_status == Field1CharacterStatus.SAD:
        avatar_img = pygame.image.load(resource_path("assets\\characters\\01-fields-default-sad-character.png")).convert_alpha()
        avatar_img_frame = AvatarFrame(screen, 1500, 30, 367, 384, (0, 0, 0), avatar_img)
        frame.add_element(avatar_img_frame)
    else:
        avatar_img = pygame.image.load(resource_path("assets\\characters\\01-fields-default-character.png")).convert_alpha()
        avatar_img_frame = AvatarFrame(screen, 1500, 30, 367, 384, (0, 0, 0), avatar_img)
        frame.add_element(avatar_img_frame)

    dialog_text_phase_1_1 = DialogText(screen, 120, 100, 500, 300, typed_text_phase_1_1)
    frame.add_element(dialog_text_phase_1_1)
    dialog_text_phase_1_2 = DialogText(screen, 120, 150, 500, 300, typed_text_phase_1_2)
    frame.add_element(dialog_text_phase_1_2)
    dialog_text_phase_1_3 = DialogText(screen, 120, 200, 500, 300, typed_text_phase_1_3)

    dialog_text_sad_phase_1_1 = DialogText(screen, 120, 150, 500, 300, typed_text_sad_phase_1_1)
    frame.add_element(dialog_text_sad_phase_1_1)

    dialog_text_happy_phase_1_1 = DialogText(screen, 120, 150, 500, 300, typed_text_happy_phase_1_1)
    frame.add_element(dialog_text_happy_phase_1_1)

    frame.add_element(dialogue_text_phase_1_3)

    # Delay for the typing speed
    pygame.time.delay(int(1000 / typing_speed))

    if field_1_character_status == Field1CharacterStatus.SAD:
        typed_text_phase_1_1 = ""
        typed_text_phase_1_2 = ""
        typed_text_phase_1_3 = ""
        text_to_type_phase_1_1 = text_to_type_phase_1_1_backup
        text_to_type_phase_1_2 = text_to_type_phase_1_2_backup
        text_to_type_phase_1_3 = text_to_type_phase_1_3_backup

        if text_to_type_sad_phase_1_1:
            typed_text_sad_phase_1_1 += text_to_type_sad_phase_1_1[0]
            text_to_type_sad_phase_1_1 = text_to_type_sad_phase_1_1[1:]
        if not text_to_type_sad_phase_1_1:
            field_1_character_status = Field1CharacterStatus.DEFAULT

    elif field_1_character_status == Field1CharacterStatus.HAPPY:
        typed_text_phase_1_1 = ""
        typed_text_phase_1_2 = ""
        typed_text_phase_1_3 = ""
        text_to_type_phase_1_1 = text_to_type_phase_1_1_backup
        text_to_type_phase_1_2 = text_to_type_phase_1_2_backup
        text_to_type_phase_1_3 = text_to_type_phase_1_3_backup
        typed_text_sad_phase_1_1 = ""
        text_to_type_sad_phase_1_1 = text_to_type_sad_phase_1_1_backup

        if text_to_type_happy_phase_1_1:
            typed_text_happy_phase_1_1 += text_to_type_happy_phase_1_1[0]
            text_to_type_happy_phase_1_1 = text_to_type_happy_phase_1_1[1:]
        if not text_to_type_happy_phase_1_1:
            pass
    else:
        typed_text_sad_phase_1_1 = ""
        text_to_type_sad_phase_1_1 = text_to_type_sad_phase_1_1_backup

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
                    pass

    frame.draw()
    code_frame.draw()
    try:
        if code_text[-1][-1] == "|":
            code_text[-1] = code_text[-1][:-1]
    except:
        pass