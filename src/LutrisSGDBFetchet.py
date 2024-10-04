from interface.MainWindow import MainWindow
from utils.Config import update_parser

if __name__ == '__main__':
    update_parser()
    app = MainWindow()

    app.mainloop()
