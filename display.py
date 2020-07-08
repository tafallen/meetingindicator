import infologging

from PIL import Image,ImageDraw,ImageFont,ImageColor

def __draw_meeting_display(panel_size, meeting_state):
    infologging.log_message('__draw_meeting_display: ' + str(meeting_state))
    if meeting_state == 1:
        return Image.new("RGB", panel_size, 'Red')
    elif meeting_state == 0:
        return Image.new("RGB", panel_size, 'Green')

    return Image.new("RGB", panel_size, 'Amber')

def get_updated_display(panel_size, meeting_state):
    infologging.log_message('get_updated_display: ' + str(meeting_state))
    return __draw_meeting_display(panel_size,meeting_state) 