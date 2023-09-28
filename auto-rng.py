import wx
import random
import threading
import time

class RandomNumberFrame(wx.Frame):
    def __init__(self, parent, title):
        super(RandomNumberFrame, self).__init__(
            parent,
            title=title,
            size=(100, 100),
            style=wx.STAY_ON_TOP | wx.CLOSE_BOX
        )

        # Create a panel with a black background
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.BLACK)

        # Create the TextCtrl (text box) with a black background, white text, centered, and with a bigger font
        self.text_ctrl = wx.TextCtrl(
            self.panel,
            value="",
            style=wx.TE_READONLY | wx.TE_CENTER | wx.BORDER_NONE
        )
        self.text_ctrl.SetBackgroundColour(wx.BLACK)
        self.text_ctrl.SetForegroundColour(wx.WHITE)

        font = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.text_ctrl.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer()
        sizer.Add(self.text_ctrl, 1, flag=wx.EXPAND | wx.ALL, border=10)
        sizer.AddStretchSpacer()
        self.panel.SetSizer(sizer)

        # Start the thread to update the number
        self.update_number()

        self.Centre()
        self.Show()

    def update_number(self):
        threading.Thread(target=self.number_changer_thread).start()

    def number_changer_thread(self):
        while True:
            random_number = str(random.randint(0, 100))
            wx.CallAfter(self.text_ctrl.SetValue, random_number)
            time.sleep(10)

if __name__ == "__main__":
    app = wx.App(False)
    frame = RandomNumberFrame(None, "")
    app.MainLoop()
