from PyQt5.QtWidgets import QMainWindow
from view.tela import Ui_MainWindow
import threading
import time
import pygame
import os
from os import system


class ControllerTela(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)
        iniciar = threading.Thread(target=self.testar, daemon=True).start()

    def testar(self):
        while True:
            iniciar = threading.Thread(
                target=self.testarcaixa27, daemon=True).start()
            #iniciar = threading.Thread(target = self.testarcaixa28, daemon = True).start()
            #iniciar = threading.Thread(target = self.testarcaixa29, daemon = True).start()
            #iniciar = threading.Thread(target = self.testaradm1, daemon = True).start()
            #niciar = threading.Thread(target = self.testaradm2, daemon = True).start()
            #iniciar = threading.Thread(target = self.testarcam, daemon = True).start()
            #iniciar = threading.Thread(target = self.testardvr, daemon = True).start()
            #iniciar = threading.Thread(target = self.testarrede, daemon = True).start()
            """self.testarcaixa27()
            self.testarcaixa28()
            self.testarcaixa29()
            self.testaradm1()
            self.testaradm2()
            self.testarcam()
            self.testardvr()
            self.testarrede()"""
            time.sleep(3)

    def testarcaixa27(self):
        try:
            resultado = self.ping("192.168.195.253")
            if resultado == True:
                self.tela.caixa27.setStyleSheet("color:green;")
            else:
                self.tela.caixa27.setStyleSheet("color:red;")
                pygame.mixer.init()
                pygame.mixer.music.load("toque.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue

        except:
            pass
        # system("cls")
        # time.sleep(1)


    def testarcaixa28(self):
        try:
            resultado = self.ping("192.168.195.252")
            if resultado == True:
                self.tela.caixa28.setStyleSheet("color:green;")
            else:
                self.tela.caixa28.setStyleSheet("color:red;")
        except:
            pass

    def testarcaixa29(self):
        try:
            resultado = self.ping("192.168.195.250")
            if resultado == True:
                self.tela.caixa29.setText("v")
                self.tela.caixa29.setStyleSheet("color:green;")
            else:
                self.tela.caixa29.setText("x")
                self.tela.caixa29.setStyleSheet("color:red;")
        except:
            pass

    def testaradm1(self):
        try:
            resultado = self.ping("192.168.195.248")
            if resultado == True:
                self.tela.adm1.setText("v")
                self.tela.adm1.setStyleSheet("color:green;")
            else:
                self.tela.adm1.setText("x")
                self.tela.adm1.setStyleSheet("color:red;")
        except:
            pass

    def testaradm2(self):
        try:
            resultado = self.ping("192.168.195.223")
            if resultado == True:
                self.tela.adm2.setText("v")
                self.tela.adm2.setStyleSheet("color:green;")
            else:
                self.tela.adm2.setText("x")
                self.tela.adm2.setStyleSheet("color:red;")
        except:
            pass

    def testarcam(self):
        try:
            resultado = self.ping("192.168.195.222")
            if resultado == True:
                self.tela.cam.setText("v")
                self.tela.cam.setStyleSheet("color:green;")
            else:
                self.tela.cam.setText("x")
                self.tela.cam.setStyleSheet("color:red;")
        except:
            pass

    def testardvr(self):
        try:
            resultado = self.ping("192.168.195.251")
            if resultado == True:
                self.tela.dvr.setStyleSheet("color:green;")
                # self.tela.frame.setStyleSheet("background-color:green;")

            else:
                self.tela.dvr.setStyleSheet("color:red;")
                # self.tela.frame.setStyleSheet("background-color:red;")
        except:
            pass
        system("cls")
        time.sleep(2)

    def testarrede(self):
        try:
            resultado = self.ping("10.0.10.2")
            if resultado == True:
                self.tela.rede.setText("v")
                self.tela.rede.setStyleSheet("color:green;")
            else:
                self.tela.rede.setText("x")
                self.tela.rede.setStyleSheet("color:red;")
        except:
            pass

    def ping(self, Host):
        """
        Returns True if Host responds to a ping request
        """
        import subprocess
        import platform
        try:
            # Ping parameters as function of OS
            ping_str = "-n 1" if platform.system().lower() == "windows"else "-c "
            args = "ping " + " " + ping_str + " " + Host
            need_sh = False if platform.system().lower() == "windows" else True

            # Ping
            return subprocess.call(args) == 0
        except:
            pass
