# ---------------------------------------------------------------------
# Name:   selectfile.py [you should select the office .txt|.py file[only for txt]]
#
# Author:    Sharedelin
#
# Created:   2012/12/21
# Copyright: (C) fudelin 2012
# Licence:
# Reference: http://www.blog.pythonlibrary.org/2011/02/10/wxpython-showing-2-filetypes-in-wx-filedialog/
#
# Run environment: python-2.7.3 &&wxPython2.8-win32-unicode-2.8.12.1-py27
# you can get the software:http://www.wxpython.org/
# ---------------------------------------------------------------------

# import wx,sys,os,win32ui
import wx

########################################################################
# set the file filter
wildcard1 = "All files (*.*)|*.*|" \
            "Python source (*.py; *.pyc)|*.py;*.pyc"
wildcard2 = "Python source (*.py; *.pyc)|*.py;*.pyc|" \
            "All files (*.*)|*.*"


########################################################################
class MyForm(wx.Frame):
    # -------------------------------------------------------------------
    # set the window layout
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,"Multi-file type wx.FileDialog Tutorial",pos=(0, 0), size=(410, 335))
        # def the global variance
        global TxtCfn, Contents
        # layout the Frame
        panel = wx.Panel(self, wx.ID_ANY)
        TxtCfn = wx.TextCtrl(panel, pos=(15, 5), size=(200, 25))
        btnO = wx.Button(panel, label="Open", pos=(225, 5), size=(70, 25))
        btnS = wx.Button(panel, label="Save", pos=(300, 5), size=(70, 25))
        Contents = wx.TextCtrl(panel, pos=(15, 35), size=(360, 260),
                               style=wx.TE_MULTILINE | wx.HSCROLL)
        # bind the button event
        btnO.Bind(wx.EVT_BUTTON, self.onOpenFile)
        btnS.Bind(wx.EVT_BUTTON, self.onSaveFile)
        # -------------------------------------------------------------------
        # def [onOpenFile] function of the label [open]button

    def onOpenFile(self, event):
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard=wildcard1,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            tmp = ""
            # paths = dlg.GetPaths()
            paths = dlg.GetPaths()
            # print "You chose the following file(s):"
            for path in paths:
                tmp = tmp + path
            # set the value of TextCtrl[filename]
            TxtCfn.SetValue(tmp)
            # set the value to the TextCtrl[contents]
            file = open(TxtCfn.GetValue())
            Contents.SetValue(file.read())
            file.close()
        dlg.Destroy()
        # def onSaveFile function

    def onSaveFile(self, event):
        """
        Create and show the Save FileDialog
        """
        dlg = wx.FileDialog(self,
                            message="select the Save file style",
                            defaultFile="",
                            wildcard=wildcard2,
                            style=wx.SAVE
                            )
        if dlg.ShowModal() == wx.ID_OK:
            filename = ""
            paths = dlg.GetPaths()
            # split the paths
            for path in paths:
                filename = filename + path
            # write the contents of the TextCtrl[Contents] into the file
            file = open(filename, 'w')
            file.write(Contents.GetValue())
            file.close()
            # show the save file path
            TxtCfn.SetValue(filename)
        dlg.Destroy()
        # -----------------------------------------------------------------------


##########################################################################
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()