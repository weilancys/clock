import tkinter as tk
import time
import threading

class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.title("clock")
        self.minsize(200, 80)
        #self.overrideredirect(True)
        
        self.stringVarForLabel = tk.StringVar()
        self.label = tk.Label(self, textvariable=self.stringVarForLabel, bg='lightblue', font=("Digital-7", 40)) #original font name: "Helvetica"
        self.label.pack(expand=1, fill=tk.BOTH)

        self.updateTimeLoopEnabled = True
        self.timeThread = threading.Thread(target=self.updateTime, args=())
        self.timeThread.daemon = True

        self.protocol("WM_DELETE_WINDOW", self.onWindowClose)

    def updateTime(self):
        while self.updateTimeLoopEnabled:
            self.stringVarForLabel.set(time.strftime("%H:%M:%S"))
            time.sleep(1)

    def onWindowClose(self):        
        self.updateTimeLoopEnabled = False #without this, python raises a runtime error that says "RuntimeError: main thread is not in main loop"
        self.destroy()

    def start(self):
        self.timeThread.start()
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()

