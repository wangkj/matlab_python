# coding=utf-8
import wx
import wx.richtext as rt


class CopyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        # 用于点击按钮时保存
        self.msg = ""
        self.initGUI()

    def initGUI(self):
        self.__create_componts()
        self.__set_properties()
        self.__do_layout()

    def __create_componts(self):
        self.leftTxt = rt.RichTextCtrl(self, style=wx.TE_MULTILINE)
        self.rightTxt = rt.RichTextCtrl(self, style=wx.TE_MULTILINE)
        self.funcBtn1 = wx.Button(self, label="Function1")
        self.funcBtn2 = wx.Button(self, label="Function2")
        self.funcBtn3 = wx.Button(self, label="Function3")

        self.Bind(wx.EVT_BUTTON, self.onFunction1Click, self.funcBtn1)
        self.Bind(wx.EVT_BUTTON, self.onFunction2Click, self.funcBtn2)
        self.Bind(wx.EVT_BUTTON, self.onFunction3Click, self.funcBtn3)

    def onFunction1Click(self, evt):
        self.left2right()

    def onFunction2Click(self, evt):
        self.left2right()

    def onFunction3Click(self, evt):
        self.left2right()

    def left2right(self):
        msg = self.leftTxt.GetValue()
        self.msg = msg
        self.rightTxt.SetValue(msg)

    def __set_properties(self):
        pass

    def __do_layout(self):
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(mainSizer)

        leftSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Left Txt"), wx.VERTICAL)
        buttonSizer = wx.BoxSizer(wx.VERTICAL)
        rightSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Right Txt"), wx.VERTICAL)

        mainSizer.Add(leftSizer, 2, wx.EXPAND | wx.ALL, 10)
        mainSizer.Add(buttonSizer, 1, wx.EXPAND | wx.ALL, 10)
        mainSizer.Add(rightSizer, 2, wx.EXPAND | wx.ALL, 10)

        # 左侧文本框
        leftSizer.Add(self.leftTxt, 1, wx.EXPAND | wx.ALL, 10)

        # 中间按钮
        buttonSizer.Add(self.funcBtn1, 0, wx.ALL, 10)
        buttonSizer.Add(self.funcBtn2, 0, wx.ALL, 10)
        buttonSizer.Add(self.funcBtn3, 0, wx.ALL, 10)

        # 右侧文本框
        rightSizer.Add(self.rightTxt, 1, wx.EXPAND | wx.ALL, 10)


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, size=(600, 400))
        self.Center()
        CopyPanel(self)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = TestFrame()
    frame.Show()
    app.MainLoop()