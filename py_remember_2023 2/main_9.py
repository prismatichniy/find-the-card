import sys
from random import shuffle
from PyQt5.QtCore import Qt, QSize, QTimer
from ruleslist import rules_list
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QPushButton, \
    QGridLayout

theme = 1
game_continue = True
schet = 0

class MainWindow(QMainWindow, QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.resize(640, 480)
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(640, 480))

        #  Окно Главного меню
        self.setGeometry(400, 200, 640, 480)
        self.setWindowTitle('Найди пару')
        self.setStyleSheet("background-color: lightgreen; ")

        #  Текст в Окне "Главное меню"
        self.gl_text = QLabel(self)
        self.gl_text.setText("Найди пару")
        self.gl_text.setGeometry(235, 10, 250, 55)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.gl_text.setFont(font)
        self.gl_text.setObjectName("gl_text")

        #  Кнопка старт, которая привязана к другому классу и открывает новое окно с приложением
        self.button1 = QPushButton("Играть", self)
        self.button1.setGeometry(195, 150, 250, 40)
        self.button1.setStyleSheet("background-color: gray; ")
        self.button1.clicked.connect(self.open_train_window)
        self.button1.clicked.connect(self.closew)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")

        # кнопка смены тем карточек
        self.button2 = QPushButton("Выбрать тему", self)
        self.button2.setGeometry(195, 200, 250, 40)
        self.button2.setStyleSheet("background-color: gray; ")
        self.button2.clicked.connect(self.open_window_for_selection)
        self.button2.clicked.connect(self.closew)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")

        self.button8 = QPushButton("Правила игры", self)
        self.button8.setGeometry(195, 250, 250, 40)
        self.button8.setStyleSheet("background-color: gray; ")
        self.button8.clicked.connect(self.open_rules_window)
        self.button8.clicked.connect(self.closew)

        self.button7 = QPushButton("Выход", self)
        self.button7.setGeometry(195, 300, 250, 40)
        self.button7.setStyleSheet("background-color: gray; ")
        self.button7.clicked.connect(self.closew)

    def open_rules_window(self):
        self.game = rules()
        self.game.show()

    def closew(self):
        self.close()

    def open_train_window(self):
        self.game = App()
        self.game.show()

    def open_window_for_selection(self):
        self.game = gamese()
        self.game.show()

class rules(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 640, 480)
        self.setWindowTitle('правила')
        self.setStyleSheet("background-color: lightgreen; ")

        self.gl_text = QLabel(self)
        self.gl_text.setText(rules_list[0])
        self.gl_text.setGeometry(0, 10, 2500, 55)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)

        self.gl_text.setFont(font)
        self.gl_text.setObjectName("gl_text")

        self.button6 = QPushButton("назад", self)
        self.button6.setGeometry(195, 300, 250, 40)
        self.button6.setStyleSheet("background-color: gray; ")
        self.button6.clicked.connect(self.open_main)
        self.button6.clicked.connect(self.closer)

    def rules(self):
        self.rules = rules_list[0]
        print(self.rules)
        return self.rules

    def open_main(self):
        self.game = MainWindow()
        self.game.show()

    def closer(self):
        self.close()

class winpage(QWidget):
    def __init__(self):
        super().__init__()
        global schet
        schet = 0
        self.setGeometry(400, 200, 640, 480)
        self.setWindowTitle('Вы выиграли')
        self.setStyleSheet("background-color: lightgreen; ")

        self.gl_text = QLabel(self)
        self.gl_text.setText("Вы выиграли!")
        self.gl_text.setGeometry(220, 10, 250, 55)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.gl_text.setFont(font)
        self.gl_text.setObjectName("gl_text")

        self.button11 = QPushButton("Играть заново", self)
        self.button11.setGeometry(195, 150, 250, 40)
        self.button11.setStyleSheet("background-color: gray; ")
        self.button11.clicked.connect(self.open_train_window)
        self.button11.clicked.connect(self.closer)

        self.button13 = QPushButton("В главное меню", self)
        self.button13.setGeometry(195, 200, 250, 40)
        self.button13.setStyleSheet("background-color: gray; ")
        self.button13.clicked.connect(self.open_main)
        self.button13.clicked.connect(self.closer)

    def open_train_window(self):
        self.game = App()
        self.game.show()

    def open_main(self):
        self.game = MainWindow()
        self.game.show()

    def closer(self):
        self.close()

class gamese(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 200, 640, 480)
        self.setWindowTitle('выберите тему')
        self.setStyleSheet("background-color: lightgreen; ")

        self.button3 = QPushButton("Фрукты", self)
        self.button3.setGeometry(195, 150, 250, 40)
        self.button3.setStyleSheet("background-color: gray; ")
        self.button3.clicked.connect(lambda: self.set_theme(1))

        self.button4 = QPushButton("Овощи", self)
        self.button4.setGeometry(195, 200, 250, 40)
        self.button4.setStyleSheet("background-color: gray; ")
        self.button4.clicked.connect(lambda: self.set_theme(2))

        self.button5 = QPushButton("Карты", self)
        self.button5.setGeometry(195, 250, 250, 40)
        self.button5.setStyleSheet("background-color: gray; ")
        self.button5.clicked.connect(lambda: self.set_theme(3))

        self.button6 = QPushButton("назад", self)
        self.button6.setGeometry(195, 300, 250, 40)
        self.button6.setStyleSheet("background-color: gray; ")
        self.button6.clicked.connect(self.open_main)
        self.button6.clicked.connect(self.closem)

    def closem(self):
        self.close()

    def open_main(self):
        self.game = MainWindow()
        self.game.show()

    def set_theme(self, theme_name):
        global theme
        theme = theme_name
        print(theme)

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.game = None
        self.timer = None
        self.picture = None
        self.new_widget_vbox = None
        self.new_vertical_box = None
        self.pictures_dict = None
        self.image_1 = None
        self.image_2 = None
        self.setWindowTitle('Image')
        self.setGeometry(300, 50, 800, 800)

        self.click = 1

        self.pictures_list = self.random_cards()
        print(self.pictures_list)

        self.create_images_dict()

        self.vertical_box = self.create_field_game()
        self.widget_vbox = QWidget()
        self.widget_vbox.setLayout(self.vertical_box)
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.widget_vbox)

        self.setLayout(self.main_layout)

    def create_field_game(self):
        z = 0
        vertical_box = QGridLayout(self)
        for y in range(4):
            for x in range(4):
                self.picture = QLabel(self)
                self.picture.setObjectName(str(z))
                self.picture.resize(150, 150)
                if self.pictures_dict[int(self.pictures_list[z])] == 'close':
                    self.picture.setStyleSheet('width: 150px; height: 150px; color: #000; '
                                               'background-image: none; background: lightgreen')
                else:
                    self.picture.setStyleSheet(f'width: 150px; height: 150px; color: #000;'
                                               f'background-image: url(images/{theme}/{self.pictures_list[z]}.jpg')
                self.picture.installEventFilter(self)
                vertical_box.addWidget(self.picture, y, x)
                z = z + 1
        return vertical_box

    def create_images_dict(self):
        self.pictures_dict = {}
        for i in range(16):
            self.pictures_dict[self.pictures_list[i]] = 'close'
        print(self.pictures_dict)

    def get_field_game(self):
        print('get_field')
        self.new_vertical_box = self.create_field_game()
        self.new_widget_vbox = QWidget()
        self.new_widget_vbox.setLayout(self.new_vertical_box)
        item = self.main_layout.itemAt(0)
        self.main_layout.removeItem(item)
        self.main_layout.addWidget(self.new_widget_vbox)
        self.timer.stop()
        global game_continue
        game_continue = True

    def closer(self):
        self.close()

    def check_images(self, image_1, image_2):
        print('функция проверки картинок на пару')
        if int(image_1) == int(image_2):
            print(f'yees {image_1} {image_2}')
            self.pictures_dict[image_1] = 'open'
            print(self.pictures_dict)
            global schet
            schet += 1
            print(schet, 'пар найдено')
            if schet == 8:
                self.closer()
                self.winpag()
        else:
            global game_continue
            game_continue = False
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.get_field_game)
            self.timer.start(1300)

    def winpag(self):
        print('youwin')
        self.game = winpage()
        self.game.show()

    def eventFilter(self, obj, event):
        if event.type() == 2:
            print(obj.objectName())
            print(self.pictures_list[int(obj.objectName())])
            if game_continue == True:
                if self.pictures_dict[int(self.pictures_list[int(obj.objectName())])] == 'close':
                    print('гадаем картинки')
                    if self.click == 1:
                        print('первый клик')
                        self.image_1 = self.pictures_list[int(obj.objectName())]
                        print(self.image_1)

                        obj.setStyleSheet(f'background-image: url(images/{theme}/{self.image_1}.jpg);'
                                          f'background-position: center;'
                                          f'color: #000')
                        self.click = 2
                    else:
                        print('второй клик')
                        self.image_2 = self.pictures_list[int(obj.objectName())]
                        print(self.image_2)
                        obj.setStyleSheet(f'background-image: url(images/{theme}/{self.image_2}.jpg);'
                                          f'background-position: center;'
                                          f'color: #000')
                        self.check_images(self.image_1, self.image_2)
                        self.click = 1
        return super(QWidget, self).eventFilter(obj, event)
    def mainwin(self):
        self.game = MainWindow()
        self.game.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
            self.mainwin()

    def random_cards(self):
        self.numbers = []
        for i in range(2):
            nums = list(range(1, 9))
            shuffle(nums)
            self.numbers = self.numbers + nums
        return self.numbers


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
