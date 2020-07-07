import display
import keypad
import lcd
import infologging
import sys
import time
import http

from http.client import HTTPException


def update_meeting_display(LCD, meeting_state):
    infologging.log_message('main.update_meeting_display: ' + str(meeting_state))
    image = display.get_updated_display((128, 128),meeting_state)
    lcd.show_image(LCD, image)

def init():
    infologging.log_message('main.init()')
    infologging.setup_logging()
    keypad.init_gpio()
    return lcd.init()

meeting_state = False

def main_loop(LCD):
    x = keypad.process_input(LCD)
    if x != None:
        meeting_state = x
    meeting_state = keypad.process_input(LCD)
    
    update_meeting_display(LCD, meeting_state)


def main():
    infologging.log_message('main.main()')
    LCD = init()

    counter = 0
    update_meeting_display(LCD, meeting_state)

    while(1):
        main_loop(LCD)
        time.sleep(0.34)

if __name__ == '__main__':
    main()
