from textwrap import fill
import tkinter as tk


class TopMostWindow(tk.Frame):
    def __init__(self, master=tk.Tk(), color='#202124', minW=50, minH=50):
        super().__init__(master)

        self.minW = minW
        self.minH = minH
        master.withdraw()
        self.tp = tk.Toplevel(master)
        self.tp.overrideredirect(True)
        self.tp.attributes('-topmost', True)
        self.tp.geometry("50x50+500+300")

        resizeR_widget = tk.Frame(self.tp, cursor='sb_h_double_arrow', bg='#3a3a3a')
        resizeR_widget.bind("<B1-Motion>",
                            lambda event: self.resize(event, 'Right'))

        resizeL_widget = tk.Frame(self.tp, cursor='sb_h_double_arrow', bg='#3a3a3a')
        resizeL_widget.bind("<B1-Motion>",
                            lambda event: self.resize(event, 'Left'))

        resizeT_widget = tk.Frame(self.tp, cursor='sb_v_double_arrow', bg='#3a3a3a')
        resizeT_widget.bind("<B1-Motion>",
                            lambda event: self.resize(event, 'Top'))

        resizeD_widget = tk.Frame(self.tp, cursor='sb_v_double_arrow', bg='#3a3a3a')
        resizeD_widget.bind("<B1-Motion>",
                            lambda event: self.resize(event, 'Bottom'))

        test = tk.Frame(self.tp, cursor='fleur', bg='#3a3a3a')

        cav = tk.Canvas(self.tp, bg=color, cursor='fleur', highlightthickness=False)

        resizeR_widget.pack(side=tk.RIGHT, ipadx=1, fill=tk.Y)
        resizeL_widget.pack(side=tk.LEFT, ipadx=1, fill=tk.Y)
        resizeT_widget.pack(side=tk.TOP, ipady=1, fill=tk.X)
        resizeD_widget.pack(side=tk.BOTTOM, ipady=1, fill=tk.X)
        # test.grid(column=0, row=0, sticky=tk.SE)
        cav.pack(fill=tk.BOTH, expand=True)

        cav.bind('<Button-1>', self.getMouseClickPos)
        cav.bind('<B1-Motion>', self.moveWindow)
        self.tp.bind("<Escape>", lambda _: self.master.destroy())
        self.tp.protocol("WM_DELETE_WINDOW", self.master.destroy)

    def resize(self, event, direction):
        try:
            winX = self.tp.winfo_x()  # 取得視窗目前的X座標
            winY = self.tp.winfo_y()  # 取得視窗目前的Y座標
            winW = self.tp.winfo_width()  # 取得視窗目前的寬度
            winH = self.tp.winfo_height()  # 取得視窗目前的高度
            newX, newY, newW, newH = winX, winY, winW, winH
            nowX = event.x_root  # 取得滑鼠按下時的X座標
            nowY = event.y_root  # 取得滑鼠按下時的Y座標

            if direction == 'Left':
                difference = winX - nowX
            if direction == 'Right':
                difference = (nowX - winX) - winW
            if direction == 'Top':
                difference = winY - nowY
            if direction == 'Bottom':
                difference = (nowY - winY) - winH

            if direction in ('Left', 'Right') and (winW > self.minW or difference > 0):  # 視窗寬度不能小於50
                newW = winW+difference
                if direction == 'Left':
                    newX = nowX
            if direction in ('Top', 'Bottom') and (winH > self.minH or difference > 0):  # 視窗高度不能小於50
                newH = winH+difference
                if direction == 'Top':
                    newY = nowY

            if winW < self.minW:
                newW = self.minW
            if winH < self.minW:
                newH = self.minH

            self.tp.geometry(f'{newW}x{newH}+{newX}+{newY}')
        except Exception as e:
            print(e)

    def getMouseClickPos(self, event):
        self.clickX = event.x_root
        self.clickY = event.y_root

        self.winX = self.tp.winfo_x()
        self.winY = self.tp.winfo_y()

    def moveWindow(self, event):
        nowX = event.x_root
        nowY = event.y_root

        moveX = (nowX - self.clickX)
        moveY = (nowY - self.clickY)

        self.tp.geometry(f'+{self.winX+moveX}+{self.winY+moveY}')


if __name__ == '__main__':
    win = TopMostWindow()
    win.mainloop()
