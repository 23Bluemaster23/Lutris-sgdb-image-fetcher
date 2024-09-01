from interface.MainWindow import MainWindow
from utils.Config import update_parser

update_parser()
app = MainWindow()

app.mainloop()
