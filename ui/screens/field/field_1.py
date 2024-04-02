import io
import sys

import pygame

from core.field_1_character_status import Field1CharacterStatus
from ui.components.avatar_frame import AvatarFrame
from ui.components.button import Button
from ui.components.dialogue_text import DialogueText
from ui.components.frame import Frame
from ui.components.image import Image
from ui.utils.localization_manager import LocalizationManager
from ui.utils.resource_path_util import resource_path
from ui.utils.set_time_out_manager import SetTimeoutManager
from ui.utils.sound_manager import SoundManager

localizationManager = LocalizationManager("en")
localizationManager.load_translations("en", resource_path("assets\\data\\translations_en.json"))

# DIALOGS
# PHASE 1
text_to_type_phase_1_1_backup = localizationManager.translate("field_1_text_to_type_phase_1_1")
text_to_type_phase_1_2_backup = localizationManager.translate("field_1_text_to_type_phase_1_2")
text_to_type_phase_1_3_backup = localizationManager.translate("field_1_text_to_type_phase_1_3")
text_to_type_phase_1_4_backup = localizationManager.translate("field_1_text_to_type_phase_1_4")
text_to_type_phase_1_5_backup = localizationManager.translate("field_1_text_to_type_phase_1_5")
text_to_type_phase_1_6_backup = localizationManager.translate("field_1_text_to_type_phase_1_6")
text_to_type_phase_1_7_backup = localizationManager.translate("field_1_text_to_type_phase_1_7")

text_to_type_phase_1_1 = text_to_type_phase_1_1_backup
text_to_type_phase_1_2 = text_to_type_phase_1_2_backup
text_to_type_phase_1_3 = text_to_type_phase_1_3_backup
text_to_type_phase_1_4 = text_to_type_phase_1_4_backup
text_to_type_phase_1_5 = text_to_type_phase_1_5_backup
text_to_type_phase_1_6 = text_to_type_phase_1_6_backup
text_to_type_phase_1_7 = text_to_type_phase_1_7_backup

typed_text_phase_1_1 = ""
typed_text_phase_1_2 = ""
typed_text_phase_1_3 = ""
typed_text_phase_1_4 = ""
typed_text_phase_1_5 = ""
typed_text_phase_1_6 = ""
typed_text_phase_1_7 = ""

# PHASE 2
text_to_type_phase_2_1_backup = localizationManager.translate("field_1_text_to_type_phase_2_1")
text_to_type_phase_2_2_backup = localizationManager.translate("field_1_text_to_type_phase_2_2")
text_to_type_phase_2_3_backup = localizationManager.translate("field_1_text_to_type_phase_2_3")
text_to_type_phase_2_4_backup = localizationManager.translate("field_1_text_to_type_phase_2_4")
text_to_type_phase_2_5_backup = localizationManager.translate("field_1_text_to_type_phase_2_5")

text_to_type_phase_2_1 = text_to_type_phase_2_1_backup
text_to_type_phase_2_2 = text_to_type_phase_2_2_backup
text_to_type_phase_2_3 = text_to_type_phase_2_3_backup
text_to_type_phase_2_4 = text_to_type_phase_2_4_backup
text_to_type_phase_2_5 = text_to_type_phase_2_5_backup

typed_text_phase_2_1 = ""
typed_text_phase_2_2 = ""
typed_text_phase_2_3 = ""
typed_text_phase_2_4 = ""
typed_text_phase_2_5 = ""

field_1_error_1_backup = localizationManager.translate("field_1_error_1")
field_1_error_2_backup = localizationManager.translate("field_1_error_2")
field_1_error_3_backup = localizationManager.translate("field_1_error_3")
field_1_error_4_backup = localizationManager.translate("field_1_error_4")

text_to_type_error_phase_2_1 = field_1_error_1_backup
text_to_type_error_phase_2_2 = field_1_error_2_backup
text_to_type_error_phase_2_3 = field_1_error_3_backup
text_to_type_error_phase_2_4 = field_1_error_4_backup

typed_text_error_phase_2_1 = ""
typed_text_error_phase_2_2 = ""
typed_text_error_phase_2_3 = ""
typed_text_error_phase_2_4 = ""

field_1_text_to_type_phase_3_1_backup = localizationManager.translate("field_1_text_to_type_phase_3_1")
field_1_text_to_type_phase_3_2_backup = localizationManager.translate("field_1_text_to_type_phase_3_2")

text_to_type_correct_phase_3_1 = field_1_text_to_type_phase_3_1_backup
text_to_type_correct_phase_3_2 = field_1_text_to_type_phase_3_2_backup

typed_text_correct_phase_3_1 = ""
typed_text_correct_phase_3_2 = ""

# TOOLTIP
tooltip_text_1 = localizationManager.translate("field_1_tooltip_text_1")
tooltip_text_2 = localizationManager.translate("field_1_tooltip_text_2")
tooltip_text_3 = localizationManager.translate("field_1_tooltip_text_3")
tooltip_text_4 = localizationManager.translate("field_1_tooltip_text_4")
tooltip_text_5 = localizationManager.translate("field_1_tooltip_text_5")
tooltip_text_6 = localizationManager.translate("field_1_tooltip_text_6")
tooltip_text_7 = localizationManager.translate("field_1_tooltip_text_7")
tooltip_text_8 = localizationManager.translate("field_1_tooltip_text_8")
tooltip_text_9 = localizationManager.translate("field_1_tooltip_text_9")

typing_speed = 30

herbs_count = 3
flowers_count = 3

code_text_1 = [
    '# direction = "north"',
    '# move = false',
    'herbs = 1'
]
validation_code_text_1 = ['print(herbs == 0)']
validation_code_text_2 = ['print(flowers == 4)']

cursor = 0
active = True
field_1_character_status = Field1CharacterStatus.DEFAULT
is_tooltip_active = False
should_give_next_level_feedback = False
field_1_music_has_not_been_played = False
is_changing_to_default = False

current_phase = 1

def execute_code():
    global code_text_1, field_1_character_status
    if code_text_1 == "":
        return
    code_to_validate = code_text_1.copy()
    for code in validation_code_text_1:
        code_to_validate.append(code)

    code_to_execute = "\n".join(code_to_validate)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        exec(code_to_execute)

        output = captured_output.getvalue().replace("\n", "")
        if output == "True":
            code_to_validate = code_text_1.copy()
            for code in validation_code_text_2:
                code_to_validate.append(code)

            code_to_execute = "\n".join(code_to_validate)
            captured_output = io.StringIO()
            sys.stdout = captured_output
            exec(code_to_execute)
            output = captured_output.getvalue().replace("\n", "")

            if output == "True":
                play_correct_sound()
                field_1_character_status = Field1CharacterStatus.HAPPY
            else:
                play_wrong_sound()
                field_1_character_status = Field1CharacterStatus.SAD_2
        else:
            play_wrong_sound()
            field_1_character_status = Field1CharacterStatus.SAD_1
    except Exception as e:
        play_wrong_sound()
        if e.args[0] == "name 'flowers' is not defined":
            field_1_character_status = Field1CharacterStatus.SAD_4
        else:
            field_1_character_status = Field1CharacterStatus.SAD_3
        print("Error:", e)
    finally:
        sys.stdout = sys.__stdout__

    captured_output.close()


def save_code(text):
    global code_text_1
    if not field_1_character_status == Field1CharacterStatus.HAPPY:
        code_text_1[-1] += text

def erase_code():
    global code_text_1
    if not field_1_character_status == Field1CharacterStatus.HAPPY:
        code_text_1[-1] = code_text_1[-1][:-1]
        if len(code_text_1[-1]) == 0:
            if len(code_text_1) > 1:
                code_text_1 = code_text_1[:-1]

def line_break():
    if not field_1_character_status == Field1CharacterStatus.HAPPY:
        code_text_1.append("")

def toggle_tooltip():
    global is_tooltip_active
    is_tooltip_active = not is_tooltip_active

def stop_all_music():
    sound_manager = SoundManager()
    sound_manager.stop_all_sounds()

def play_background_music():
    sound_manager = SoundManager()
    sound_manager.set_volume("background_music", 0.3)
    sound_manager.play_sound("background_music")

def play_correct_sound():
    sound_manager = SoundManager()
    sound_manager.set_volume("correct", 0.3)
    sound_manager.play_sound("correct")

def play_wrong_sound():
    sound_manager = SoundManager()
    sound_manager.set_volume("wrong", 0.3)
    sound_manager.play_sound("wrong")

def play_next_level_sound():
    sound_manager = SoundManager()
    sound_manager.set_volume("next-level", 0.3)
    sound_manager.play_sound("next-level")

def change_to_default():
    global field_1_character_status, typed_text_phase_1_1, typed_text_phase_1_2, typed_text_phase_1_3, typed_text_phase_1_4, typed_text_phase_1_5,typed_text_phase_1_6,\
        typed_text_phase_1_7, typed_text_phase_2_1, typed_text_phase_2_2, typed_text_phase_2_3, typed_text_phase_2_4, typed_text_phase_2_5, is_changing_to_default,\
        text_to_type_error_phase_2_1, text_to_type_error_phase_2_2, text_to_type_error_phase_2_3, typed_text_error_phase_2_1, typed_text_error_phase_2_2, typed_text_error_phase_2_3

    typed_text_phase_2_1 = text_to_type_phase_2_1_backup
    typed_text_phase_2_2 = text_to_type_phase_2_2_backup
    typed_text_phase_2_3 = text_to_type_phase_2_3_backup
    typed_text_phase_2_4 = text_to_type_phase_2_4_backup
    typed_text_phase_2_5 = text_to_type_phase_2_5_backup

    field_1_character_status = Field1CharacterStatus.DEFAULT
    is_changing_to_default = False


def render_field_1(screen, go_to_field_2, go_to_region_selection):
    global field_1_music_has_not_been_played, should_give_next_level_feedback, text_to_type_happy_phase_1_1,typed_text_happy_phase_1_1,field_1_character_status,\
        text_to_type_sad_phase_1_1, typed_text_phase_1_1, typed_text_phase_1_2, typed_text_phase_1_3, text_to_type_phase_1_1, text_to_type_phase_1_2, text_to_type_phase_1_3,\
        code_text_1, active,cursor, typed_text_sad_phase_1_1, typed_text_phase_1_4, typed_text_phase_1_5, typed_text_phase_1_6, typed_text_phase_1_7, typed_text_phase_2_1, typed_text_phase_2_2,\
        typed_text_phase_2_3, typed_text_phase_2_4, typed_text_phase_2_5, text_to_type_phase_1_4, text_to_type_phase_1_5, text_to_type_phase_1_6, text_to_type_phase_1_7, text_to_type_phase_2_1,\
        text_to_type_phase_2_2, text_to_type_phase_2_3, text_to_type_phase_2_4, text_to_type_phase_2_5, current_phase, text_to_type_error_phase_2_1, text_to_type_error_phase_2_2,\
        text_to_type_error_phase_2_3, typed_text_error_phase_2_1, typed_text_error_phase_2_2, typed_text_error_phase_2_3, is_changing_to_default,\
        typed_text_error_phase_2_4, text_to_type_error_phase_2_4, tooltip_text_1, tooltip_text_2, tooltip_text_3, tooltip_text_4, tooltip_text_5, tooltip_text_6, \
        tooltip_text_7, tooltip_text_8, tooltip_text_9, text_to_type_correct_phase_3_1, text_to_type_correct_phase_3_2, typed_text_correct_phase_3_1, typed_text_correct_phase_3_2

    code_area = pygame.image.load(resource_path("assets\\fields\\coding-area.png")).convert_alpha()
    code_frame = Frame(screen, 82, 335, 700, 700, (100, 100, 100), code_area)

    if not field_1_music_has_not_been_played:
        field_1_music_has_not_been_played = True
        play_background_music()

    if field_1_character_status == Field1CharacterStatus.HAPPY and should_give_next_level_feedback:
        code_button = Button(screen, 380, 920, 100, 60, "Next", (0, 0, 0), "White", lambda: go_to_field_2())
        code_button.check_click()
        code_frame.add_element(code_button)
    elif not field_1_character_status == Field1CharacterStatus.HAPPY:
        code_button = Button(screen, 380, 920, 100,60, "Run", (0, 0, 0),"White", lambda: execute_code())
        code_button.check_click()
        code_frame.add_element(code_button)


    if cursor % 4 == 0 and active and code_text_1[-1] and not field_1_character_status == Field1CharacterStatus.HAPPY:
        code_text_1[-1] += "|"
    cursor += 1
    for row, line in enumerate(code_text_1):
        code_text_component = DialogueText(screen, 145, 400 + (row * 40), 500, 600, line, 30, resource_path('font\\MSMincho.ttf'))
        code_frame.add_element(code_text_component)

    # BACKGROUND #
    background_image = pygame.image.load(resource_path("assets\\fields\\00-home.png")).convert_alpha()
    background_rect = background_image.get_rect()
    scaled_image = pygame.transform.scale(background_image, (1920 , 1080))
    screen.blit(scaled_image, background_rect)

    # DIALOGUE FRAME + AVATAR FRAME #
    dialogue_frame = pygame.image.load(resource_path("assets\\fields\\instructions.png")).convert_alpha()
    frame = Frame(screen, 50, 30, 1770, 266, (100, 100, 100), dialogue_frame)

    avatar_frame_img = pygame.image.load(resource_path("assets\\fields\\face-frame.png")).convert_alpha()
    avatar_frame = AvatarFrame(screen, 1570, 10, 300, 300, (0, 0, 0), avatar_frame_img)
    frame.add_element(avatar_frame)

    if field_1_character_status == Field1CharacterStatus.HAPPY:
        avatar_img = pygame.image.load(resource_path("assets\\characters\\01-fields\\01-field-happy.png")).convert_alpha()
        avatar_img_frame = AvatarFrame(screen, 1580, 25, 250, 250, (0, 0, 0), avatar_img)
        frame.add_element(avatar_img_frame)
    elif field_1_character_status == Field1CharacterStatus.SAD_1 or field_1_character_status == Field1CharacterStatus.SAD_2 or field_1_character_status == Field1CharacterStatus.SAD_3  or field_1_character_status == Field1CharacterStatus.SAD_4:
        avatar_img = pygame.image.load(resource_path("assets\\characters\\01-fields\\01-field-sad.png")).convert_alpha()
        avatar_img_frame = AvatarFrame(screen, 1580, 25, 250, 250, (0, 0, 0), avatar_img)
        frame.add_element(avatar_img_frame)
    else:
        avatar_img = pygame.image.load(resource_path("assets\\characters\\01-fields\\01-field-default.png")).convert_alpha()
        avatar_img_frame = AvatarFrame(screen, 1580, 25, 250, 250, (0, 0, 0), avatar_img)
        frame.add_element(avatar_img_frame)

    info_img = Image(screen, avatar_frame.rect.x + (avatar_frame.rect.width / 2),avatar_frame.rect.y + avatar_frame.rect.height + 20, 100,100, "assets\\common\\info_icon.png", lambda: toggle_tooltip())
    frame.add_element(info_img)
    info_img.check_click()

    go_to_map_img = Image(screen, info_img.rect.x , info_img.rect.y + info_img.rect.height + 20, 100, 100, "assets\\common\\map_icon.png", lambda: (stop_all_music(), go_to_region_selection()))
    frame.add_element(go_to_map_img)
    go_to_map_img.check_click()

    dialogue_text_phase_1_1 = DialogueText(screen, 125, 50, 500, 300, typed_text_phase_1_1, 30)
    frame.add_element(dialogue_text_phase_1_1)
    dialogue_text_phase_1_2 = DialogueText(screen, 125, 80, 500, 300, typed_text_phase_1_2, 30)
    frame.add_element(dialogue_text_phase_1_2)
    dialogue_text_phase_1_3 = DialogueText(screen, 125, 110, 500, 300, typed_text_phase_1_3, 30)
    frame.add_element(dialogue_text_phase_1_3)
    dialogue_text_phase_1_4 = DialogueText(screen, 125, 140, 500, 300, typed_text_phase_1_4, 30)
    frame.add_element(dialogue_text_phase_1_4)
    dialogue_text_phase_1_5 = DialogueText(screen, 125, 170, 500, 300, typed_text_phase_1_5, 30)
    frame.add_element(dialogue_text_phase_1_5)
    dialogue_text_phase_1_6 = DialogueText(screen, 125, 200, 500, 300, typed_text_phase_1_6, 30)
    frame.add_element(dialogue_text_phase_1_6)
    dialogue_text_phase_1_7 = DialogueText(screen, 125, 230, 500, 300, typed_text_phase_1_7, 30)
    frame.add_element(dialogue_text_phase_1_7)

    dialogue_text_phase_2_1 = DialogueText(screen, 125, 80, 500, 300, typed_text_phase_2_1, 30)
    frame.add_element(dialogue_text_phase_2_1)
    dialogue_text_phase_2_2 = DialogueText(screen, 125, 130, 500, 300, typed_text_phase_2_2, 30)
    frame.add_element(dialogue_text_phase_2_2)
    dialogue_text_phase_2_3 = DialogueText(screen, 125, 170, 500, 300, typed_text_phase_2_3, 30)
    frame.add_element(dialogue_text_phase_2_3)
    dialogue_text_phase_2_4 = DialogueText(screen, 800, 130, 500, 300, typed_text_phase_2_4, 30)
    frame.add_element(dialogue_text_phase_2_4)
    dialogue_text_phase_2_5 = DialogueText(screen, 800, 170, 500, 300, typed_text_phase_2_5, 30)
    frame.add_element(dialogue_text_phase_2_5)

    dialogue_text_sad_phase_1_1 = DialogueText(screen, 125, 150, 500, 300, typed_text_error_phase_2_1, 30)
    frame.add_element(dialogue_text_sad_phase_1_1)
    dialogue_text_sad_phase_1_2 = DialogueText(screen, 125, 150, 500, 300, typed_text_error_phase_2_2, 30)
    frame.add_element(dialogue_text_sad_phase_1_2)
    dialogue_text_sad_phase_1_3 = DialogueText(screen, 125, 150, 500, 300, typed_text_error_phase_2_3,30)
    frame.add_element(dialogue_text_sad_phase_1_3)
    dialogue_text_sad_phase_1_4 = DialogueText(screen, 125, 150, 500, 300, typed_text_error_phase_2_4, 30)
    frame.add_element(dialogue_text_sad_phase_1_4)

    dialogue_text_happy_phase_1_1 = DialogueText(screen, 125, 80, 500, 300, typed_text_correct_phase_3_1, 30)
    frame.add_element(dialogue_text_happy_phase_1_1)
    dialogue_text_happy_phase_2_1 = DialogueText(screen, 125, 130, 500, 300, typed_text_correct_phase_3_2, 30)
    frame.add_element(dialogue_text_happy_phase_2_1)

    # Delay for the typing speed
    pygame.time.delay(int(1000 / typing_speed))

    if field_1_character_status == Field1CharacterStatus.SAD_1:
        typed_text_phase_1_1 = ""
        typed_text_phase_1_2 = ""
        typed_text_phase_1_3 = ""
        typed_text_phase_1_4 = ""
        typed_text_phase_1_5 = ""
        typed_text_phase_1_6 = ""
        typed_text_phase_1_7 = ""

        text_to_type_phase_1_1 = ""
        text_to_type_phase_1_2 = ""
        text_to_type_phase_1_3 = ""
        text_to_type_phase_1_4 = ""
        text_to_type_phase_1_5 = ""
        text_to_type_phase_1_6 = ""
        text_to_type_phase_1_7 = ""

        typed_text_phase_2_1 = ""
        typed_text_phase_2_2 = ""
        typed_text_phase_2_3 = ""
        typed_text_phase_2_4 = ""
        typed_text_phase_2_5 = ""

        text_to_type_phase_2_1 = ""
        text_to_type_phase_2_2 = ""
        text_to_type_phase_2_3 = ""
        text_to_type_phase_2_4 = ""
        text_to_type_phase_2_5 = ""

        if text_to_type_error_phase_2_1:
            typed_text_error_phase_2_1 += text_to_type_error_phase_2_1[0]
            text_to_type_error_phase_2_1 = text_to_type_error_phase_2_1[1:]
        if not text_to_type_error_phase_2_1 and not is_changing_to_default:
            is_changing_to_default = True
            typed_text_error_phase_2_1 = field_1_error_1_backup
            timeout_manager = SetTimeoutManager()
            timeout_manager.setTimeout(change_to_default, 3)

    elif field_1_character_status == Field1CharacterStatus.SAD_2:
        typed_text_phase_1_1 = ""
        typed_text_phase_1_2 = ""
        typed_text_phase_1_3 = ""
        typed_text_phase_1_4 = ""
        typed_text_phase_1_5 = ""
        typed_text_phase_1_6 = ""
        typed_text_phase_1_7 = ""

        text_to_type_phase_1_1 = ""
        text_to_type_phase_1_2 = ""
        text_to_type_phase_1_3 = ""
        text_to_type_phase_1_4 = ""
        text_to_type_phase_1_5 = ""
        text_to_type_phase_1_6 = ""
        text_to_type_phase_1_7 = ""

        typed_text_phase_2_1 = ""
        typed_text_phase_2_2 = ""
        typed_text_phase_2_3 = ""
        typed_text_phase_2_4 = ""
        typed_text_phase_2_5 = ""

        text_to_type_phase_2_1 = ""
        text_to_type_phase_2_2 = ""
        text_to_type_phase_2_3 = ""
        text_to_type_phase_2_4 = ""
        text_to_type_phase_2_5 = ""

        if text_to_type_error_phase_2_2:
            typed_text_error_phase_2_2 += text_to_type_error_phase_2_2[0]
            text_to_type_error_phase_2_2 = text_to_type_error_phase_2_2[1:]
        if not text_to_type_error_phase_2_2 and not is_changing_to_default:
            is_changing_to_default = True
            typed_text_error_phase_2_2 = field_1_error_2_backup
            timeout_manager = SetTimeoutManager()
            timeout_manager.setTimeout(change_to_default, 3)

    elif field_1_character_status == Field1CharacterStatus.SAD_3:
        typed_text_phase_1_1 = ""
        typed_text_phase_1_2 = ""
        typed_text_phase_1_3 = ""
        typed_text_phase_1_4 = ""
        typed_text_phase_1_5 = ""
        typed_text_phase_1_6 = ""
        typed_text_phase_1_7 = ""

        text_to_type_phase_1_1 = ""
        text_to_type_phase_1_2 = ""
        text_to_type_phase_1_3 = ""
        text_to_type_phase_1_4 = ""
        text_to_type_phase_1_5 = ""
        text_to_type_phase_1_6 = ""
        text_to_type_phase_1_7 = ""

        typed_text_phase_2_1 = ""
        typed_text_phase_2_2 = ""
        typed_text_phase_2_3 = ""
        typed_text_phase_2_4 = ""
        typed_text_phase_2_5 = ""

        text_to_type_phase_2_1 = ""
        text_to_type_phase_2_2 = ""
        text_to_type_phase_2_3 = ""
        text_to_type_phase_2_4 = ""
        text_to_type_phase_2_5 = ""

        if text_to_type_error_phase_2_3:
            typed_text_error_phase_2_3 += text_to_type_error_phase_2_3[0]
            text_to_type_error_phase_2_3 = text_to_type_error_phase_2_3[1:]
        if not text_to_type_error_phase_2_3 and not is_changing_to_default:
            is_changing_to_default = True
            typed_text_error_phase_2_3 = field_1_error_3_backup
            timeout_manager = SetTimeoutManager()
            timeout_manager.setTimeout(change_to_default, 3)

    elif field_1_character_status == Field1CharacterStatus.SAD_4:
        typed_text_phase_1_1 = ""
        typed_text_phase_1_2 = ""
        typed_text_phase_1_3 = ""
        typed_text_phase_1_4 = ""
        typed_text_phase_1_5 = ""
        typed_text_phase_1_6 = ""
        typed_text_phase_1_7 = ""

        text_to_type_phase_1_1 = ""
        text_to_type_phase_1_2 = ""
        text_to_type_phase_1_3 = ""
        text_to_type_phase_1_4 = ""
        text_to_type_phase_1_5 = ""
        text_to_type_phase_1_6 = ""
        text_to_type_phase_1_7 = ""

        typed_text_phase_2_1 = ""
        typed_text_phase_2_2 = ""
        typed_text_phase_2_3 = ""
        typed_text_phase_2_4 = ""
        typed_text_phase_2_5 = ""

        text_to_type_phase_2_1 = ""
        text_to_type_phase_2_2 = ""
        text_to_type_phase_2_3 = ""
        text_to_type_phase_2_4 = ""
        text_to_type_phase_2_5 = ""

        if text_to_type_error_phase_2_4:
            typed_text_error_phase_2_4 += text_to_type_error_phase_2_4[0]
            text_to_type_error_phase_2_4 = text_to_type_error_phase_2_4[1:]
        if not text_to_type_error_phase_2_4 and not is_changing_to_default:
            is_changing_to_default = True
            typed_text_error_phase_2_4 = field_1_error_4_backup
            timeout_manager = SetTimeoutManager()
            timeout_manager.setTimeout(change_to_default, 3)

    elif field_1_character_status == Field1CharacterStatus.HAPPY:
        typed_text_phase_1_1 = ""
        typed_text_phase_1_2 = ""
        typed_text_phase_1_3 = ""
        text_to_type_phase_1_1 = text_to_type_phase_1_1_backup
        text_to_type_phase_1_2 = text_to_type_phase_1_2_backup
        text_to_type_phase_1_3 = text_to_type_phase_1_3_backup
        typed_text_sad_phase_1_1 = ""
        text_to_type_sad_phase_1_1 = field_1_error_1_backup

        if text_to_type_correct_phase_3_1:
            typed_text_correct_phase_3_1 += text_to_type_correct_phase_3_1[0]
            text_to_type_correct_phase_3_1 = text_to_type_correct_phase_3_1[1:]
        if not text_to_type_correct_phase_3_1:
            if text_to_type_correct_phase_3_2:
                typed_text_correct_phase_3_2 += text_to_type_correct_phase_3_2[0]
                text_to_type_correct_phase_3_2 = text_to_type_correct_phase_3_2[1:]
            if not text_to_type_correct_phase_3_2 and not should_give_next_level_feedback:
                play_next_level_sound()
                should_give_next_level_feedback = True

    elif current_phase == 1:
        typed_text_sad_phase_1_1 = ""
        text_to_type_sad_phase_1_1 = field_1_error_1_backup

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
                    if text_to_type_phase_1_4:
                        typed_text_phase_1_4 += text_to_type_phase_1_4[0]
                        text_to_type_phase_1_4 = text_to_type_phase_1_4[1:]
                    if not text_to_type_phase_1_4:
                        if text_to_type_phase_1_5:
                            typed_text_phase_1_5 += text_to_type_phase_1_5[0]
                            text_to_type_phase_1_5 = text_to_type_phase_1_5[1:]
                        if not text_to_type_phase_1_5:
                            if text_to_type_phase_1_6:
                                typed_text_phase_1_6 += text_to_type_phase_1_6[0]
                                text_to_type_phase_1_6 = text_to_type_phase_1_6[1:]
                            if not text_to_type_phase_1_6:
                                if text_to_type_phase_1_7:
                                    typed_text_phase_1_7 += text_to_type_phase_1_7[0]
                                    text_to_type_phase_1_7 = text_to_type_phase_1_7[1:]
                                if not text_to_type_phase_1_7:
                                    current_phase = 2
    else:
        typed_text_phase_1_1 = ""
        typed_text_phase_1_2 = ""
        typed_text_phase_1_3 = ""
        typed_text_phase_1_4 = ""
        typed_text_phase_1_5 = ""
        typed_text_phase_1_6 = ""
        typed_text_phase_1_7 = ""

        typed_text_error_phase_2_1 = ""
        typed_text_error_phase_2_2 = ""
        typed_text_error_phase_2_3 = ""
        typed_text_error_phase_2_4 = ""

        if text_to_type_phase_2_1:
            typed_text_phase_2_1 += text_to_type_phase_2_1[0]
            text_to_type_phase_2_1 = text_to_type_phase_2_1[1:]

        if not text_to_type_phase_2_1:
            if text_to_type_phase_2_2:
                typed_text_phase_2_2 += text_to_type_phase_2_2[0]
                text_to_type_phase_2_2 = text_to_type_phase_2_2[1:]

            if not text_to_type_phase_2_2:
                if text_to_type_phase_2_3:
                    typed_text_phase_2_3 += text_to_type_phase_2_3[0]
                    text_to_type_phase_2_3 = text_to_type_phase_2_3[1:]
                if not text_to_type_phase_2_3:
                    if text_to_type_phase_2_4:
                        typed_text_phase_2_4 += text_to_type_phase_2_4[0]
                        text_to_type_phase_2_4 = text_to_type_phase_2_4[1:]
                    if not text_to_type_phase_2_4:
                        if text_to_type_phase_2_5:
                            typed_text_phase_2_5 += text_to_type_phase_2_5[0]
                            text_to_type_phase_2_5 = text_to_type_phase_2_5[1:]
                        if not text_to_type_phase_2_5:
                            pass



    if is_tooltip_active:
        tooltip_img = pygame.image.load(resource_path("assets\\fields\\coding-area.png")).convert_alpha()
        tooltip_img_frame = Frame(screen, info_img.rect.x - 550, info_img.rect.y, 550, 350, (100, 100, 100), tooltip_img)
        frame.add_element(tooltip_img_frame)
        tooltip_1 = DialogueText(screen, tooltip_img_frame.rect.x + 30, tooltip_img_frame.rect.y + 10,550, 20, tooltip_text_1, 30)
        tooltip_2 = DialogueText(screen, tooltip_img_frame.rect.x + 30, tooltip_img_frame.rect.y + 40,550, 20, tooltip_text_2, 30)
        tooltip_3 = DialogueText(screen, tooltip_img_frame.rect.x + 30, tooltip_img_frame.rect.y + 70,550, 20, tooltip_text_3, 30)
        tooltip_4 = DialogueText(screen, tooltip_img_frame.rect.x + 30, tooltip_img_frame.rect.y + 100,550, 20, tooltip_text_4, 30)
        tooltip_5 = DialogueText(screen, tooltip_img_frame.rect.x + 30, tooltip_img_frame.rect.y + 150,550, 20, tooltip_text_5, 30)
        tooltip_6 = DialogueText(screen, tooltip_img_frame.rect.x + 30, tooltip_img_frame.rect.y + 180,550, 20, tooltip_text_6, 30)
        tooltip_7 = DialogueText(screen, tooltip_img_frame.rect.x + 30, tooltip_img_frame.rect.y + 230,550, 20, tooltip_text_7, 30)
        tooltip_8 = DialogueText(screen, tooltip_img_frame.rect.x + 30, tooltip_img_frame.rect.y + 260,550, 20, tooltip_text_8, 30)
        tooltip_9 = DialogueText(screen, tooltip_img_frame.rect.x + 30, tooltip_img_frame.rect.y + 290,550, 20, tooltip_text_9, 30)
        frame.add_element(tooltip_1)
        frame.add_element(tooltip_2)
        frame.add_element(tooltip_3)
        frame.add_element(tooltip_4)
        frame.add_element(tooltip_5)
        frame.add_element(tooltip_6)
        frame.add_element(tooltip_7)
        frame.add_element(tooltip_8)
        frame.add_element(tooltip_9)
    frame.draw()
    code_frame.draw()

    try:
        if code_text_1[-1][-1] == "|":
            code_text_1[-1] = code_text_1[-1][:-1]
    except:
        pass