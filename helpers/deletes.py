import time
import pyautogui


def delete_all():

    repeats = 128
    i = 0
    while i < repeats:
        i = i+1
        # Preencher os campos de texto
        pyautogui.click((1150, 618))
        time.sleep(0.5)

        pyautogui.press('enter')
        time.sleep(0.1)

        try:
            pyautogui.locateOnScreen(
                'images/error.png', grayscale=True, region=(525, 200, 300, 300))
            pyautogui.press('f5')
            print('found')
            time.sleep(2)
        except:
            print('not found')
            pass

        pyautogui.press('enter')
        time.sleep(2)


if __name__ == "__main__":
    time.sleep(2)

    delete_all()
