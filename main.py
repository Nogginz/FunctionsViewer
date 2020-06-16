import numpy as np
from math_rider import MathRider
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import sys
from PyQt5 import QtWidgets
import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):


        super().__init__()
        self.setupUi(self)
        self.graphics_count = 0
        self.count = 0
        self.button_print.clicked.connect(self.print_function)
        self.button_clear.clicked.connect(self.clear)
        self.MplWidget.canvas.axes.grid()
        self.MplWidget.canvas.axes.set_xlabel("x")
        self.MplWidget.canvas.axes.set_ylabel("f(x)")
        #self.MplWidget.canvas.axes.set_aspect('equal')
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

    def clear(self):
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.grid()
        self.count = 0
        self.MplWidget.canvas.draw()
    def print_function(self):
        if self.input_array.text():
            self.input_function.setText('')
            os = self.input_array.text().split('][')
            os[0] = os[0].replace('[', '').replace(']', '').split(',')
            os[1] = os[1] = os[1].replace('[', '').replace(']', '').split(',')
            os[0] = list(map(float, os[0]))
            os[1] = list(map(float, os[1]))
            os_x = os[0]
            os_y = os[1]

        else:
            self.count+=1
            if self.count <=4:
                inp = self.input_function.text().replace(' ','')

                if ';' in inp:
                    inp = inp.split(';')
                    if len(inp) == 3:
                        os_x = np.linspace(float(inp[1]), float(inp[2]), 1000)
                    elif len(inp)==4:
                        os_x = np.linspace(float(inp[1]), float(inp[2]), float(inp[3]))
                    elif len(inp) == 2:
                        os_x = np.linspace(float(inp[1]), 50, 1000)
                    input_func = MathRider(inp[0])
                else:
                    os_x = np.linspace(-50, 50, 1000)
                    input_func = MathRider(inp)

                vfunc = np.vectorize(input_func.interpretotor)

                os_y = vfunc(os_x)

        self.MplWidget.canvas.axes.plot(os_x, os_y)
        self.MplWidget.canvas.axes.set_title('График')


        self.MplWidget.canvas.draw()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()