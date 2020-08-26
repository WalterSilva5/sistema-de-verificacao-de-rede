def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Programa Titulo"))
 
        class Sinais(QtCore.QObject):
            sinal = QtCore.pyqtSignal()
            def __init__(self):
                QtCore.QObject.__init__(self)
        sinal = Sinais()
        def mudarCor():
            MainWindow.setStyleSheet("background-color: #{};".format(random.randint(100000,999999)))
            print("a")
        sinal.sinal.connect(mudarCor)
        def enviarSInal():
            while True:
                print('x')
                time.sleep(1)
                sinal.sinal.emit()
 
        iniciar = threading.Thread(target = enviarSInal, daemon = True).start()