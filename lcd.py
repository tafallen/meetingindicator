import LCD_1in44
import LCD_Config
import infologging

def init():
    infologging.log_message('lcd.init')
    LCD = LCD_1in44.LCD()
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()

    return LCD

def show_image(LCD, image):
    infologging.log_message('lcd.show_image')
    LCD.LCD_ShowImage(image,0,0)