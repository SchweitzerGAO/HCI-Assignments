import datetime
import sys
import time
from threading import Thread

import keyboard
import speech_recognition as sr
import win32api
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel
from speech_recognition import WaitTimeoutError

from asrInterface import Ui_MainWindow


class MySignal(QObject):
    gif_change = pyqtSignal(QLabel, QLabel)
    text_change = pyqtSignal(str)


global_signal = MySignal()


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.myCommand = ""
        self.ui = Ui_MainWindow(self)
        self.ui.setupUi(self)
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone(device_index=0)
        global_signal.text_change.connect(self.change_text)
        global_signal.gif_change.connect(self.change_gif)

    def change_text(self, text):
        self.ui.label_5.setText(text)

    def change_gif(self, label_1,label_2):
        label_1.setVisible(False)
        label_2.setVisible(True)

    def listen_and_execute(self):
        while True:
            keyboard.wait(' ')
            try:
                global_signal.gif_change.emit(self.ui.voiceFig,self.ui.playFig)
                global_signal.text_change.emit('Listening...')
                # print('Listening...')
                with self.mic as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=3)
                sentence = self.recognizer.recognize_sphinx(audio)
                # print(sentence)
                global_signal.gif_change.emit(self.ui.playFig, self.ui.voiceFig)
                if sentence.__contains__('pad') or sentence.__contains__('note') or sentence.__contains__('pa'):
                    global_signal.text_change.emit('Opening notepad...')
                    # print('notepad')
                    time.sleep(1)
                    win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 1)
                elif sentence.__contains__('play') or sentence.__contains__('playing') or sentence.__contains__(
                        'music'):
                    global_signal.text_change.emit('Enjoy some music!')
                    # print('music')
                    time.sleep(1)
                    win32api.ShellExecute(0, 'open', 'C:\\Users\\CharlesGao\\Music\\canon6.mp3', '', '', 1)

                elif sentence.__contains__('time') or sentence.__contains__('ti'):
                    now = datetime.datetime.now()
                    # print('time')
                    global_signal.text_change.emit('Now:\n' + now.strftime("%Y-%m-%d %H:%M:%S"))
                    time.sleep(5)
                    # print(now.strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    global_signal.text_change.emit('Sorry I didn\'t catch that, try again!')
                    # print('not recognized')
                    time.sleep(1.5)
                global_signal.text_change.emit('Press space key and then say something!')
            except WaitTimeoutError:
                global_signal.text_change.emit('No audio input, terminating...')
                break
            except Exception as e:
                print(e)

    def run(self):
        self.show()
        thread = Thread(target=self.listen_and_execute)
        thread.setDaemon(True)
        thread.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('./icon/phone.png'))
    application = MyWindow()
    application.run()
    sys.exit(app.exec_())
