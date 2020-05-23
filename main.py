from PyQt5 import QtWidgets, uic
import sys
from concurrent.futures import ThreadPoolExecutor
import pathlib
import requests

URL_ALL = 'https://ngosang.github.io/trackerslist/trackers_all.txt'
URL_BEST = 'https://ngosang.github.io/trackerslist/trackers_best.txt'
URL_ALL_IP = 'https://ngosang.github.io/trackerslist/trackers_all_ip.txt'
URL_BEST_IP = 'https://ngosang.github.io/trackerslist/trackers_best_ip.txt'


class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi(str(pathlib.Path(__file__).parent.absolute()) + '\\gui.ui', self)

        self.btnAll = self.findChild(QtWidgets.QPushButton, 'btnAll')
        self.btnBest = self.findChild(QtWidgets.QPushButton, 'btnBest')
        self.btnAllIP = self.findChild(QtWidgets.QPushButton, 'btnAllIP')
        self.btnBestIP = self.findChild(QtWidgets.QPushButton, 'btnBestIP')
        self.edtField = self.findChild(QtWidgets.QTextEdit, 'edtField')

        self.btnAll.clicked.connect(self.getAllTrackers)
        self.btnBest.clicked.connect(self.getBestTrackers)
        self.btnAllIP.clicked.connect(self.getAllTrackersIP)
        self.btnBestIP.clicked.connect(self.getBestTrackersIP)

        self.show()

    def getAllTrackers(self):
        self.exec_in_thread(URL_ALL)

    def getBestTrackers(self):
        self.exec_in_thread(URL_BEST)

    def getAllTrackersIP(self):
        self.exec_in_thread(URL_ALL_IP)

    def getBestTrackersIP(self):
        self.exec_in_thread(URL_BEST_IP)

    @staticmethod
    def thread_function(url):
        print(f'Getting trackers from url {url}...')
        return requests.get(url).text

    def exec_in_thread(self, url):
        with ThreadPoolExecutor() as executor:
            future = executor.submit(GUI.thread_function, url)
            return_value = future.result()
            self.edtField.setText(return_value)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    app.exec_()
