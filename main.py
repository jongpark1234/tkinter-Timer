from tkinter import *
from tkinter.messagebox import showinfo
def timerStart():
    global time
    time = int(input1.get()) * 3600 + int(input2.get()) * 60 + int(input3.get())

def getTime(s):
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return list(map(lambda x: str(x).zfill(2), [h, m, s]))

class sampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('타이머')
        self._frame = None
        self.switch_frame(TimerStartPage)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class TimerStartPage(Frame):
    def __init__(self, master):
        global label1, label2, label3, input1, input2, input3, startBtn
        Frame.__init__(self, master)
        label1 = Label(self, text='시')
        label2 = Label(self, text='분')
        label3 = Label(self, text='초')
        input1 = Entry(self, width = 15, border = 1, relief = 'solid')
        input2 = Entry(self, width = 15, border = 1, relief = 'solid')
        input3 = Entry(self, width = 15, border = 1, relief = 'solid')
        startBtn = Button(self, text='타이머 시작', command=lambda: master.switch_frame(TimerPage))
        label1.grid(row = 0, column = 0, padx = 30, pady = 30)
        label2.grid(row = 0, column = 1, padx = 30, pady = 30)
        label3.grid(row = 0, column = 2, padx = 30, pady = 30)
        input1.grid(row = 1, column = 0, padx = 30, pady = 30)
        input2.grid(row = 1, column = 1, padx = 30, pady = 30)
        input3.grid(row = 1, column = 2, padx = 30, pady = 30)
        startBtn.grid(row = 2, column = 1)

class TimerPage(Frame):
    
    def __init__(self, master):
        global time
        Frame.__init__(self, master)
        time = int(input1.get()) * 3600 + int(input2.get()) * 60 + int(input3.get()) + 1
        self.label = Label(self, text=':'.join(getTime(time)), font=('Helvetica', 48))
        self.label.pack()
        Button(self, text='종료', command=lambda: master.switch_frame(TimerStartPage)).pack()
        self.updateClock()

    def updateClock(self):
        global time
        time -= 1
        self.label.configure(text=':'.join(getTime(time)))
        if time <= 0:
            showinfo('타이머 종료', '지정한 시간이 만료되었습니다.')
            self.master.switch_frame(TimerStartPage)
        self.after(1000, self.updateClock)

sampleApp().mainloop()
