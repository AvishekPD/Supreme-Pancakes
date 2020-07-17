from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
Keyboard = Controller()
import time
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['are you a bot', ['no', 'na', 'no, what makes you think that?']],
    ['my name is (.*)', ['Hello, %1!']],
    ['why u no work', ['idk ask prox he probobly broked it']],
    ['(.*)Who created you?',['M1 is my Creator and he looks after me =)']]
    ]
time.sleep(0.12)
chat = Chat(pairs, reflections)
chat.converse()
































#mouse.position =(687, 728)
#mouse.click(Button.left, 1)


#for char in "IceCream":
 #   Keyboard.press(char)
  #  Keyboard.release(char)
   # time.sleep(0.12)
#Keyboard.press(Key.enter)
#Keyboard.release(Key.enter)

