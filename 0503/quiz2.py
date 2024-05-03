import RPi.GPIO as GPIO
import time
from ctypes import *
from contextlib import contextmanager
import speech_recognition as sr
from gtts import gTTS

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)


v = 343
TRIGGER_PIN = 16
ECHO_PIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure():
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
    t = pulse_end - pulse_start
    d = t * v
    d = d / 2
    return d * 100

with noalsaerr():
    #obtain audio from the microphone
    r=sr.Recognizer() 

    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...") 
        #listen for 1 seconds and create the ambient noise energy level 
        r.adjust_for_ambient_noise(source, duration=1) 
        print("Say something!")
        audio=r.listen(source)

    # recognize speech using Google Speech Recognition 
    try:
        print("Google Speech Recognition thinks you said:")
        print(r.recognize_google(audio))
        if "start" in r.recognize_google(audio):
            dist = measure()
            tts = gTTS(text='the distance is ' + str(dist) + 'cm', lang='en')
            tts.save('distance.mp3')
            os.system('play distance.mp3 > /dev/null 2>&1')

        GPIO.cleanup()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        GPIO.cleanup()
    except sr.RequestError as e:
        print("No response from Google Speech Recognition service: {0}".format(e))
        GPIO.cleanup()
