import tkinter as tk


class TopMostWindow(tk.Frame):
    def __init__(self, master=tk.Tk(), color='#202124'):
        super().__init__(master)
        master.withdraw()
        self.tp = tk.Toplevel(master)
        self.tp.overrideredirect(True)
        self.tp.attributes('-topmost', True)
        self.tp.geometry("700x100+500+300")

        self._resizex_widget = tk.Frame(self.tp, cursor='sb_h_double_arrow', bg='#3a3a3a')
        self._resizex_widget.bind("<B1-Motion>", self.resizex)

        self._resizey_widget = tk.Frame(self.tp, cursor='sb_v_double_arrow', bg='#3a3a3a')
        self._resizey_widget.bind("<B1-Motion>", self.resizey)

        cav = tk.Canvas(self.tp, bg=color, highlightthickness=False)

        self._resizex_widget.pack(side=tk.RIGHT, ipadx=1, fill=tk.Y)
        self._resizey_widget.pack(side=tk.BOTTOM, ipady=1, fill=tk.X)

        cav.pack(fill=tk.BOTH, expand=True)

        cav.bind('<Button-1>', self.getMouseClickPos)
        cav.bind('<B1-Motion>', self.moveWindow)
        self.tp.bind("<Escape>", lambda _: self.master.destroy())
        self.tp.protocol("WM_DELETE_WINDOW", self.master.destroy)

    def resizex(self, event):
        xwin = self.tp.winfo_x()
        difference = (event.x_root - xwin) - self.tp.winfo_width()
        if self.tp.winfo_width() > 50:  # 50 is the minimum width for the window
            try:
                self.tp.geometry(f"{self.tp.winfo_width()+difference}x{self.tp.winfo_height()}")
            except:
                pass
        else:
            if difference > 0:  # so the window can't be too small (150x150)
                try:
                    self.tp.geometry(f"{self.tp.winfo_width()+difference}x{self.tp.winfo_height()}")
                except:
                    pass

    def resizey(self, event):
        ywin = self.tp.winfo_y()
        difference = (event.y_root - ywin) - self.tp.winfo_height()
        if self.tp.winfo_height() > 50:  # 50 is the minimum height for the window
            try:
                self.tp.geometry(f"{self.tp.winfo_width()}x{self.tp.winfo_height()+difference}")
            except:
                pass
        else:
            if difference > 0:  # so the window can't be too small (150x150)
                try:
                    self.tp.geometry(f"{self.tp.winfo_width()}x{self.tp.winfo_height()+difference}")
                except:
                    pass

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
