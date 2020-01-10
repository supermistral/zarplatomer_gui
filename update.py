import requests, base64, os, shelve
from PyQt5 import QtCore, QtGui, QtWidgets
#import g

'''def main():
    file_id = ""
    re = drive_services.files().get_media(fileId = file_id)
    fg = '''

class Dialog(QtWidgets.QDialog):
    def __init__(self, name, parent = None):
        QtWidgets.QDialog.__init__(self, parent = None)
        #Main_Window = QtWidgets.QMainWindow(self)
        self.resize(200, 60)
        self.setFixedSize(self.size())
        self.label_err = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_err.setFont(font)
        self.label_err.setText("Доступно новое обновление")
        self.label_err.move(20, 5)
        self.button = QtWidgets.QPushButton("Установить", self)
        self.button.move(60, 30)
        self.button2 = QtWidgets.QPushButton("Отмена", self)
        self.button2.move(120, 30)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

class Function():
    def __init__(self):
        self.main("version")
        self.update()
    
    def main(self, name):
    #    file_path = "update.txt"
        url = "https://api.github.com/repos/supermistral/updates_for_zarplatomer/contents/%s.txt?ref=master" %name
        file_response = requests.get(url)
        print(file_response)
#        print(base64.b64decode(file_response.json()['content']).decode('utf-8'))
        self.file_content = base64.b64decode(file_response.json()['content']).decode('utf-8')
        return self.file_content

    def update(self):
        with shelve.open("temporary") as file:
            cont = self.file_content.split('\n')
            print(cont[0].split()[1])
            '''try:
                ver_pyqt = file["version_pyqt"]
                ver_design = file["version_design"]
                ver_classes = file["version_classes"]
                print(ver_pyqt)
                if cont[0].split()[1] != ver_pyqt:                                                      #СДЕЛАТЬ ЦИКЛ ПО ДОБАВЛЯЕМЫМ ФАЙЛАМ ДЛЯ УСТАНОВКИ ДОП ФАЙЛОВ
                    self.name = "pyqt"
                    self.open_window()
                    file["version_pyqt"] = cont[0].split()[1]
                if cont[1].split()[1] != ver_design:
                    self.name = "design"
                    self.open_window()
                    file["version_design"] = cont[1].split()[1]
                if cont[2].split()[1] != ver_classes:
                    self.name = "classes"
                    self.open_window()
                    file["version_classes"] = cont[2].split()[1]
                if        
            except:
                file["version_pyqt"] = cont[0].split()[1]
                file["version_design"] = cont[1].split()[1]
                file["version_classes"] = cont[2].split()[1]'''
            
            for cont_one in cont:
                val0, val1 = cont_one.split()[0], cont_one.split()[1]
                if "image" in val0:
                    final_img = requests.get(val1)
                    out = open("images\\" + cont_one.split()[2], "wb")                           #Для картинок запрос вида "image <ссылка на картинку> <название картинки>"
                    out.write(final_img.content)                                                #Сделать чек соединения с интернетом
                    out.close()
                    continue
                try:
                    ver = file["version_" + val0]
                    if val1 != ver:
                        self.name = val0
                        self.open_window()
                        file["version_" + val0] = val1
                except:
                    self.name = val0
                    self.open_window()
                    file["version_" + val0] = val1

        os.system("pyqt.py")

    def open_file(self):
        with open(self.name + '.py', "w", encoding = "utf-8") as file_inside:
            file_inside.write(self.main(self.name))
        self.delete_dialog()

    def open_window(self):
        import sys
        self.myapp = QtWidgets.QApplication(sys.argv)
        self.ui = Dialog(self.name)
        self.ui.button.clicked.connect(lambda: self.open_file())
        self.ui.button2.clicked.connect(lambda: self.delete_dialog())
        self.ui.show()
        sys.exit(self.myapp.exec_())

    def delete_dialog(self):
        self.ui.close()
        del self.ui
        del self.myapp

if __name__ == "__main__":
    a = Function()



