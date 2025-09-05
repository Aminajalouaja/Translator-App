import pygame
import csv
from googletrans import Translator


def load_languages(file_path="languages.csv"):
    languages = {}
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                languages[row['code'].strip().lower()] = row['language'].strip()
    except FileNotFoundError:
        print("Error: 'languages.csv' file not found, try again.")
        exit()
    return languages

# Initialize the Translator from googletrans
translator = Translator()


def translate_text(text, src_lang="auto", dest_lang="auto"):
    try:
        
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated.text  
    except Exception as e:
        return f"Translation error: {str(e)}"  

#------Pygame----------------------------------------------------------------------------------------
pygame.init()

# Screen 
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Translator")

# Colors
PINK = (255, 192, 203)
WHITE = (255, 255, 255)
LIGHT_GRAY = (230, 230, 230)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Input boxes
input_box_src_lang = pygame.Rect(50, 100, 200, 40)
input_box_dest_lang = pygame.Rect(50, 180, 200, 40)
input_box_text = pygame.Rect(50, 260, 700, 40)
output_box = pygame.Rect(50, 400, 700, 100)

# Buttons
button_yes = pygame.Rect(250, 520, 100, 40)
button_no = pygame.Rect(450, 520, 100, 40)

# Variables to track input
src_lang_text = ''
dest_lang_text = ''
input_text = ''
output_text = ''
continue_translation = True  

# Flags for active input
active_src = False
active_dest = False
active_text = False

# Load available languages
languages = load_languages()

running = True
while running:
    screen.fill(PINK)  
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box_src_lang.collidepoint(event.pos):
                active_src = True
                active_dest = active_text = False
            elif input_box_dest_lang.collidepoint(event.pos):
                active_dest = True
                active_src = active_text = False
            elif input_box_text.collidepoint(event.pos):
                active_text = True
                active_src = active_dest = False
            elif button_yes.collidepoint(event.pos):  # Yes button clicked
                src_lang_text = ''
                dest_lang_text = ''
                input_text = ''
                output_text = ''
            elif button_no.collidepoint(event.pos):  # No button clicked
                running = False
            else:
                active_src = active_dest = active_text = False

      
        if event.type == pygame.KEYDOWN:
            if active_src:
                if event.key == pygame.K_BACKSPACE:
                    src_lang_text = src_lang_text[:-1]
                else:
                    src_lang_text += event.unicode
            elif active_dest:
                if event.key == pygame.K_BACKSPACE:
                    dest_lang_text = dest_lang_text[:-1]
                else:
                    dest_lang_text += event.unicode
            elif active_text:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

     
            if event.key == pygame.K_RETURN and input_text:
                try:
                   
                    src_lang_text_clean = src_lang_text.strip().lower()
                    dest_lang_text_clean = dest_lang_text.strip().lower()
                    
                    if src_lang_text_clean in languages and dest_lang_text_clean in languages:
                        output_text = translate_text(input_text, src_lang_text_clean, dest_lang_text_clean)
                    else:
                        output_text = "Invalid language code. Check available languages."
                except Exception as e:
                    output_text = f"Error: {e}"

    # Draw input boxes
    pygame.draw.rect(screen, LIGHT_GRAY if active_src else WHITE, input_box_src_lang)
    pygame.draw.rect(screen, LIGHT_GRAY if active_dest else WHITE, input_box_dest_lang)
    pygame.draw.rect(screen, LIGHT_GRAY if active_text else WHITE, input_box_text)
    pygame.draw.rect(screen, WHITE, output_box)

  # input boxes
    src_lang_surface = font.render(src_lang_text, True, BLACK)
    dest_lang_surface = font.render(dest_lang_text, True, BLACK)
    input_surface = font.render(input_text, True, BLACK)
    output_surface = small_font.render(output_text, True, BLACK)

  
    screen.blit(src_lang_surface, (input_box_src_lang.x + 5, input_box_src_lang.y + 5))
    screen.blit(dest_lang_surface, (input_box_dest_lang.x + 5, input_box_dest_lang.y + 5))
    screen.blit(input_surface, (input_box_text.x + 5, input_box_text.y + 5))
    screen.blit(output_surface, (output_box.x + 5, output_box.y + 5))

    # Draw labels
    src_label = font.render("Source Language Code:", True, BLACK)
    dest_label = font.render("Destination Language Code:", True, BLACK)
    text_label = font.render("Text to Translate:", True, BLACK)
    output_label = font.render("Translated Text:", True, BLACK)
    screen.blit(src_label, (50, 70))
    screen.blit(dest_label, (50, 150))
    screen.blit(text_label, (50, 230))
    screen.blit(output_label, (50, 370))

    # buttons
    pygame.draw.rect(screen, LIGHT_GRAY, button_yes)
    pygame.draw.rect(screen, LIGHT_GRAY, button_no)

    #  button 
    yes_text = font.render("Yes", True, BLACK)
    no_text = font.render("No", True, BLACK)
    screen.blit(yes_text, (button_yes.x + 25, button_yes.y + 5))
    screen.blit(no_text, (button_no.x + 25, button_no.y + 5))

    # Ask the user
    question_text = font.render("Do you want to translate something else?", True, BLACK)
    screen.blit(question_text, (200, 480))

    pygame.display.flip()

pygame.quit()
