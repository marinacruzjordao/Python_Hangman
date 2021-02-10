from PySimpleGUI import PySimpleGUI as sg
import image
from random import randint

class Hangman:

    def __init__(self):
        #layout
        sg.theme('Reddit')
        self.words=['banana','apple', 'learn','teach','software','hardware','computador','music','vacations','everyday' ,'dog','mathematic','vocabulary', 'bus','hollywood', 'table', 'chair','stairs','sky','cloud','sun','sea','beach','sand','tree','car','aeroplane','aeroport','internet','browser','mouse','keyboard','house','bike','ride','sport']

        self.layout=[
            [sg.Button(image_data=image.img)],
            [sg.Button('Play',size=(40,1))],
            [sg.Output(size=(40,15))],
            [sg.Text('Letter? ',size=(18,1)),sg.Input(key='letter',size=(18,1))],
        ]

        self.aux=0
        self.val=0
        self.correct=[]
        self.tries=0

    def start(self):
        #create a window in GUI

        self.w1=sg.Window('HANGMAN GAME').layout(self.layout)

        while True:
            self.event, value=self.w1.read()
            self.letter=value.get('letter')

            if self.event == sg.WINDOW_CLOSED:
                break

            if self.event == 'Play':
                if self.aux==0:
                    c.select_word()
                else:
                    c.validation()
                    
    def select_word(self):
        #select a random word
        self.aux=1
        n=randint(1,len(self.words))
        self.word=self.words[n]

        for i in self.word:
            print(' __ ', end='')
        print()

    def validation(self):
        #verify letter belongs to the word
        if (self.letter in self.word )or (self.letter.lower() in self.word):
            self.correct.append(self.letter)
            self.val=0
            for i in self.word:
                if i in self.correct:
                    print(' ',i,' ', end='')
                    self.val+=1
                else:
                    print(' __ ', end='')
            print()
        else:
            self.tries+=1
            print(f'{self.letter} does not belong to the word. Tries ({self.tries}/10)')
       
        #win or lost validation
        if self.val==len(self.word):
                self.val=0
                self.aux=0
                self.tries=0
                print('Congratulations! You won!')
        elif self.tries==10:
                self.val=0
                self.aux=0
                self.tries=0
                print('You lost!')

c=Hangman()
c.start()