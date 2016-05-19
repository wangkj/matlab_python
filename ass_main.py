#!/usr/bin/env python
#coding=utf-8

import wx
import os
import re
import gl
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import ass_slicer


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Ass_main")

        self.InitUI()
        self.SetSize((950, 600))

    # --------------------------------------------------------------------------------------------------
    def InitUI(self):
        panel = wx.Panel(self)

        # this functions to build menu
        self.createMenuBar()  # 简化的init方法

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        #1 First create the controls
        topLbl = wx.StaticText(panel, -1, "ASS 2.5D",size=(1000,-1),style= wx.ALIGN_CENTER)  # 1 创建窗口部件
        topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        down_topLbl = wx.StaticText(panel, -1, "Autofokus Sensor Simulator",size=(1000,-1),style= wx.ALIGN_CENTER)
        down_topLbl.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

        #2 staticBox_up_Sizer

        # 2.1 define
        profile_Static = wx.StaticText(panel, -1, "Profile",size=(100,-1),
                                       style= wx.ALIGN_CENTER)
        self.profile_Text = wx.TextCtrl(panel, -1, "unigit_input.txt",size=(300,-1))
        profile_Load = wx.Button(panel, -1, "Load")
        profile_Save = wx.Button(panel, -1, "Save")
        profile_Edit = wx.Button(panel, -1, "Edit")
        profile_Slice = wx.Button(panel, -1, "Slice")
        profile_Show = wx.Button(panel, -1, "Show")

        nzk_Static = wx.StaticText(panel, -1, "NZK", size=(100,-1),
                                        style= wx.ALIGN_CENTER)
        nzk_Text = wx.TextCtrl(panel, -1, "nzk_ill.txt",size=(300,-1))
        nzk_Load = wx.Button(panel, -1, "Load")
        nzk_Save = wx.Button(panel, -1, "Save")
        nzk_Edit = wx.Button(panel, -1, "Edit")

        staticBox_up = wx.StaticBox(panel, label= 'Document')
        staticBox_up_Sizer = wx.StaticBoxSizer(staticBox_up, orient= wx.VERTICAL)

        # 2.2 Bind
        self.Bind(wx.EVT_BUTTON, self.Load_FileDialog_profile, profile_Load)
        self.Bind(wx.EVT_BUTTON, self.Save_FileDialog_profile, profile_Save)
        self.Bind(wx.EVT_BUTTON, self.Edit_FileDialog_profile, profile_Edit)
        self.Bind(wx.EVT_BUTTON, self.Slice_FileDialog_profile, profile_Slice)
        self.Bind(wx.EVT_BUTTON, self.Show_FileDialog_profile, profile_Show)

        self.Bind(wx.EVT_BUTTON, self.Load_FileDialog_profile, nzk_Load)
        self.Bind(wx.EVT_BUTTON, self.Edit_FileDialog_profile, nzk_Edit)

        # 2.3 BoxSizer
        # Profile
        hbox_up_profile = wx.BoxSizer(wx.HORIZONTAL)
        hbox_up_profile.Add(profile_Static)
        hbox_up_profile.Add(self.profile_Text)
        hbox_up_profile.Add((10, 10), 1)
        hbox_up_profile.Add(profile_Load)
        hbox_up_profile.Add((10, 10), 1)
        hbox_up_profile.Add(profile_Save)
        hbox_up_profile.Add((10, 10), 1)
        hbox_up_profile.Add(profile_Edit)
        hbox_up_profile.Add((10, 10), 1)
        hbox_up_profile.Add(profile_Slice)
        hbox_up_profile.Add((10, 10), 1)
        hbox_up_profile.Add(profile_Show)
        staticBox_up_Sizer.Add(hbox_up_profile)

        # NZK
        hbox_up_nzk = wx.BoxSizer(wx.HORIZONTAL)
        hbox_up_nzk.Add(nzk_Static)
        hbox_up_nzk.Add(nzk_Text)
        hbox_up_nzk.Add((10, 10), 1)
        hbox_up_nzk.Add(nzk_Load)
        hbox_up_nzk.Add((10, 10), 1)
        hbox_up_nzk.Add(nzk_Save)
        hbox_up_nzk.Add((10, 10), 1)
        hbox_up_nzk.Add(nzk_Edit)
        staticBox_up_Sizer.Add(hbox_up_nzk)

        # 3 staticBox_left_Sizer

        # staticBox_left_up_Sizer
        RadioButton_left_up = ['Natural', 'Linear_TE', 'Polar', 'Linear_TM', 'Circular']

        radioButton_left_up = wx.RadioBox(panel, -1, "Polarisation",size= wx.DefaultSize,
                    choices=RadioButton_left_up, majorDimension=3, style =wx.RA_SPECIFY_COLS | wx.NO_BORDER)


        # staticBox_left_down_Sizer
        radioButton_left_down_Gauss = wx.RadioButton(panel, -1, "Gauss", style = wx.RB_GROUP)
        radioButton_left_down_Circular = wx.RadioButton(panel, -1, "Circular",)
        intensity_Static_NA_i = wx.StaticText(panel, -1, "NA_i",
                                       style=wx.ALIGN_CENTER)
        intensity_Text_NA_i = wx.TextCtrl(panel, -1, "0.0")
        intensity_Static_NA_a = wx.StaticText(panel, -1, "NA_a",
                                              style=wx.ALIGN_CENTER)
        intensity_Text_NA_a = wx.TextCtrl(panel, -1, "0.7")

        staticBox_left_down = wx.StaticBox(panel, label='Intensity')
        staticBox_left_down_Sizer = wx.StaticBoxSizer(staticBox_left_down, orient=wx.VERTICAL)

        staticBox_left_down_Sizer.Add(radioButton_left_down_Gauss)

        hbox_left_down = wx.BoxSizer(wx.HORIZONTAL)
        hbox_left_down.Add(radioButton_left_down_Circular)
        hbox_left_down.Add((20, 20), 1)
        hbox_left_down.Add(intensity_Static_NA_i)
        hbox_left_down.Add((10, 10), 1)
        hbox_left_down.Add(intensity_Text_NA_i)
        hbox_left_down.Add((10, 10), 1)
        hbox_left_down.Add(intensity_Static_NA_a)
        hbox_left_down.Add((10, 10), 1)
        hbox_left_down.Add(intensity_Text_NA_a)

        staticBox_left_down_Sizer.Add((20, 20), 1)
        staticBox_left_down_Sizer.Add(hbox_left_down)

        staticBox_left = wx.StaticBox(panel, label='Illumination')
        staticBox_left_Sizer = wx.StaticBoxSizer(staticBox_left, orient=wx.VERTICAL)
        staticBox_left_Sizer.Add(radioButton_left_up)
        staticBox_left_Sizer.Add(staticBox_left_down_Sizer)

        # 4 staticBox_right_Sizer

        # staticBox_right_up_Sizer
        RadioButton_right_up = ['Natural', 'Linear_TE', 'Polar', 'Linear_TM', 'Circular']

        radioButton_right_up = wx.RadioBox(panel, -1, "Polarisation", size=wx.DefaultSize,
                                          choices=RadioButton_right_up, majorDimension=3,
                                          style=wx.RA_SPECIFY_COLS | wx.NO_BORDER)

        # staticBox_right_down_Sizer
        radioButton_right_down_Gauss = wx.RadioButton(panel, -1, "Gauss", style=wx.RB_GROUP)
        radioButton_right_down_Circular = wx.RadioButton(panel, -1, "Circular", )

        intensity_right_Static_NA_ratio = wx.StaticText(panel, -1, "NA-ratio",
                                              style=wx.ALIGN_CENTER)
        intensity_right_Text_NA_ratio = wx.TextCtrl(panel, -1, "0.5")

        intensity_right_Static_NA_i = wx.StaticText(panel, -1, "NA_i",
                                              style=wx.ALIGN_CENTER)
        intensity_right_Text_NA_i = wx.TextCtrl(panel, -1, "0.0")
        intensity_right_Static_NA_a = wx.StaticText(panel, -1, "NA_a",
                                              style=wx.ALIGN_CENTER)
        intensity_right_Text_NA_a = wx.TextCtrl(panel, -1, "0.7")

        staticBox_right_down = wx.StaticBox(panel, label='Intensity')
        staticBox_right_down_Sizer = wx.StaticBoxSizer(staticBox_right_down, orient=wx.VERTICAL)

        hbox_right_down_1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_right_down_1.Add(radioButton_right_down_Gauss)
        hbox_right_down_1.Add((20, 20), 1)
        hbox_right_down_1.Add(intensity_right_Static_NA_ratio )
        hbox_right_down_1.Add((10, 10), 1)
        hbox_right_down_1.Add(intensity_right_Text_NA_ratio)

        staticBox_right_down_Sizer.Add(hbox_right_down_1)

        hbox_right_down_2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_right_down_2.Add(radioButton_right_down_Circular)
        hbox_right_down_2.Add((20, 20), 1)
        hbox_right_down_2.Add(intensity_right_Static_NA_i)
        hbox_right_down_2.Add((10, 10), 1)
        hbox_right_down_2.Add(intensity_right_Text_NA_i)
        hbox_right_down_2.Add((10, 10), 1)
        hbox_right_down_2.Add(intensity_right_Static_NA_a)
        hbox_right_down_2.Add((10, 10), 1)
        hbox_right_down_2.Add(intensity_right_Text_NA_a)

        staticBox_right_down_Sizer.Add((10, 10), 1)
        staticBox_right_down_Sizer.Add(hbox_right_down_2)

        staticBox_right = wx.StaticBox(panel, label='Illumination')
        staticBox_right_Sizer = wx.StaticBoxSizer(staticBox_right, orient=wx.VERTICAL)
        staticBox_right_Sizer.Add(radioButton_right_up)
        staticBox_right_Sizer.Add(staticBox_right_down_Sizer)

        # 5 BoxSizer_middle
        hbox_middle = wx.BoxSizer(wx.HORIZONTAL)
        hbox_middle.Add(staticBox_left_Sizer)
        hbox_middle.Add((20,20),1)
        hbox_middle.Add(staticBox_right_Sizer)

        # 6 staticBox_down_Sizer
        diffraction_Matrix_Static = wx.StaticText(panel, -1, "Diffraction_Matrix", size=(100, -1),
                                       style=wx.ALIGN_CENTER)
        diffraction_Matrix_Text = wx.TextCtrl(panel, -1, "diffmat.txt", size=(300, -1))
        diffraction_Matrix_Load = wx.Button(panel, -1, "Load")
        diffraction_Matrix_Edit = wx.Button(panel, -1, "Edit")

        calibration_Table_Static = wx.StaticText(panel, -1, "Calibration_Table", size=(100, -1),
                               style=wx.ALIGN_CENTER)
        calibration_Table_Text = wx.TextCtrl(panel, -1, "calibrate.txt", size=(300, -1))
        calibration_Table_Load = wx.Button(panel, -1, "Load")
        calibration_Table_Edit = wx.Button(panel, -1, "Edit")
        calibration_Table_Plot = wx.Button(panel, -1, "Plot")

        scan_Signal_Static = wx.StaticText(panel, -1, "Scan_Signal", size=(100, -1),
                                                 style=wx.ALIGN_CENTER)
        scan_Signal_Text = wx.TextCtrl(panel, -1, "scan_signal.txt", size=(300, -1))
        scan_Signal_Load = wx.Button(panel, -1, "Load")
        scan_Signal_Edit = wx.Button(panel, -1, "Edit")
        scan_Signal_Plot = wx.Button(panel, -1, "Plot")

        staticBox_down = wx.StaticBox(panel, label='')
        staticBox_down_Sizer = wx.StaticBoxSizer(staticBox_down, orient=wx.VERTICAL)
        staticBox_down_Sizer.Add((10, 10), 1)

        # diffraction_Matrix
        hbox_down_diffraction_Matrix = wx.BoxSizer(wx.HORIZONTAL)
        hbox_down_diffraction_Matrix.Add(diffraction_Matrix_Static)
        hbox_down_diffraction_Matrix.Add((20, 20), 1)
        hbox_down_diffraction_Matrix.Add(diffraction_Matrix_Text)
        hbox_down_diffraction_Matrix.Add((20, 20), 1)
        hbox_down_diffraction_Matrix.Add(diffraction_Matrix_Load)
        hbox_down_diffraction_Matrix.Add((20, 20), 1)
        hbox_down_diffraction_Matrix.Add(diffraction_Matrix_Edit)
        staticBox_down_Sizer.Add(hbox_down_diffraction_Matrix)

        # calibration_Table
        hbox_down_calibration_Table = wx.BoxSizer(wx.HORIZONTAL)
        hbox_down_calibration_Table.Add(calibration_Table_Static)
        hbox_down_calibration_Table.Add((20, 20), 1)
        hbox_down_calibration_Table.Add(calibration_Table_Text)
        hbox_down_calibration_Table.Add((20, 20), 1)
        hbox_down_calibration_Table.Add(calibration_Table_Load)
        hbox_down_calibration_Table.Add((20, 20), 1)
        hbox_down_calibration_Table.Add(calibration_Table_Edit)
        hbox_down_calibration_Table.Add((20, 20), 1)
        hbox_down_calibration_Table.Add(calibration_Table_Plot)
        staticBox_down_Sizer.Add(hbox_down_calibration_Table)

        # scan_Signal
        hbox_down_scan_Signal = wx.BoxSizer(wx.HORIZONTAL)
        hbox_down_scan_Signal.Add(scan_Signal_Static)
        hbox_down_scan_Signal.Add((20, 20), 1)
        hbox_down_scan_Signal.Add(scan_Signal_Text)
        hbox_down_scan_Signal.Add((20, 20), 1)
        hbox_down_scan_Signal.Add(scan_Signal_Load)
        hbox_down_scan_Signal.Add((20, 20), 1)
        hbox_down_scan_Signal.Add(scan_Signal_Edit)
        hbox_down_scan_Signal.Add((20, 20), 1)
        hbox_down_scan_Signal.Add(scan_Signal_Plot)
        staticBox_down_Sizer.Add(hbox_down_scan_Signal)

        # 7 end buttons

        end_CheckBox_Parallel = wx.CheckBox(panel, -1, "Parallel")
        end_CheckBox_Use_BCs = wx.CheckBox(panel, -1, "Use BC's")
        end_Button_Set_BCs = wx.Button(panel, -1, "Set BC's")
        end_Button_Converge = wx.Button(panel, -1, "Converge")
        end_Button_Diffract = wx.Button(panel, -1, "Diffract")
        end_Button_Prepare = wx.Button(panel, -1, "Prepare")
        end_Button_Calibration = wx.Button(panel, -1, "Calibration")
        end_Button_Intensity = wx.Button(panel, -1, "Intensity")
        end_Button_Scan = wx.Button(panel, -1, "Scan")
        end_Button_Batch = wx.Button(panel, -1, "Batch")

        hbox_end_Button = wx.BoxSizer(wx.HORIZONTAL)
        hbox_end_Button.Add(end_CheckBox_Parallel)
        hbox_end_Button.Add(end_CheckBox_Use_BCs)
        hbox_end_Button.Add(end_Button_Set_BCs)
        hbox_end_Button.Add(end_Button_Converge)
        hbox_end_Button.Add(end_Button_Diffract)
        hbox_end_Button.Add(end_Button_Prepare)
        hbox_end_Button.Add(end_Button_Calibration)
        hbox_end_Button.Add(end_Button_Intensity)
        hbox_end_Button.Add(end_Button_Scan)
        hbox_end_Button.Add(end_Button_Batch)

        # end main
        mainSizer.Add(topLbl, 0, wx.ALL, 5)
        mainSizer.Add(down_topLbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        mainSizer.Add(staticBox_up_Sizer, 0, wx.ALL, 5)
        mainSizer.Add(hbox_middle, 0, wx.ALL, 5)
        mainSizer.Add(staticBox_down_Sizer, 0, wx.ALL, 5)
        mainSizer.Add(hbox_end_Button, 0, wx.ALL, 5)

        panel.SetSizer(mainSizer)



    #--------------------------------------------------------------------------------------------------
    # 创建菜单部分
    def menuData(self):  # 菜单数据
        return (
                ("Functions",
                 ("Diffraction Computation", "", self.OnCloseWindow),
                 ("Intensity Computation", "", self.OnCloseWindow),
                 ("Scan Computation", "", self.OnCloseWindow),
                 ("Calibration", "", self.OnCloseWindow),
                 ("Set BC's", "", self.OnCloseWindow)),
                ("Options",
                 ("Show Aux Plots", "", self.OnCloseWindow),
                 ("", "", ""),
                 ("About","", self.OnCloseWindow),
                 ("Exit","", self.OnCloseWindow)))

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1:]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachLabel, eachStatus, eachHandler in menuData:
            if not eachLabel:
                menu.AppendSeparator()
                continue
            menuItem = menu.Append(-1, eachLabel, eachStatus)
            self.Bind(wx.EVT_MENU, eachHandler, menuItem)
        return menu
    # 创建菜单结束--------------------------------------------------------------------------------------


    # --------------------------------------------------------------------------------------------------
    # 使用到的函数
    # used functions

    # profile functions
    def Load_FileDialog_profile(self, event):
        dialog = wx.FileDialog(self, message="Choose a file",
            defaultFile="unigit_input.txt",
            wildcard=gl.wildcard,
            style= wx.OPEN | wx.CHANGE_DIR)
        if dialog.ShowModal() == wx.ID_OK:
            self.profile_path = dialog.GetPath()
            self.profile_Text.SetValue(self.profile_path)
            file = open(self.profile_Text.GetValue())
            self.profile_file = file.read()
            gl.t_line = map(lambda x: re.findall(r"\d+\.?\d*", x), self.profile_file.split('\n'))
            file.close()
        #dialog.ShowModal()
        dialog.Destroy()

    def Save_FileDialog_profile(self, event):
        dlg = wx.FileDialog(self,
                            message="Save file",
                            defaultFile="unigit_input_sliced.txt",
                            wildcard=gl.wildcard_save,
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
            file.write(self.profile_file)
            file.close()
        dlg.Destroy()

    def Edit_FileDialog_profile(self, event):
        path = self.profile_Text.GetValue()
        os.system('notepad %s' %  path )

    def Slice_FileDialog_profile(self, event):
        dialog = ass_slicer.SubclassDialog()
        result = dialog.ShowModal()

    def Show_FileDialog_profile(self, event):
        plt.xlabel('Lateral Distance in microns')
        plt.ylabel('Height in nm')

        h0 = 0
        h1 = 0
        #t_line = self.profile_file.split('\n')

        pitch = float(gl.t_line[4][0])
        NoL = int(gl.t_line[6][0])
        n0 = int(gl.t_line[7][2])
        num = 8
        operator = {0: 'white', 1: 'red', 2: 'blue', 3: 'grey', 4: 'yellow', 5: 'c'}
        currentAxis = plt.gca()
        for n in range(NoL):
            id = int(gl.t_line[num][0])
            if (id == 1):
                #here have problem , maybe 1 or 2 and wait
                n1 = int(gl.t_line[num+1][2])
                h = int(gl.t_line[num+2][0])
                h1 = h0 + h
                plt.bar(left = 0 , height = pitch/1000, width = pitch/1000 )

                #X = [0 pitch pitch 0]/1000
                #Y = [h0 h0 h1 h1]
                #switch n1:
            else:
                np = int(gl.t_line[num+1][0])
                xx = map(int, gl.t_line[num+2])
                # this not good , maybe we must use numpy
                xm = len(xx)
                xn = 1
                # define
                num_eps = 0
                eps = [[0, 0], [0, 0]]
                for i1 in range(2):
                    for i2 in range(2):
                        eps[i1][i2] = float(gl.t_line[num+3][num_eps])
                        num_eps = num_eps + 1
                nx = [int(gl.t_line[num+3][4]),int(gl.t_line[num+3][5])]
                h = float(gl.t_line[num+4][0])
                h1 = h0 + h
                x0 = 0
                if xx[np-1] != pitch:
                    xx.append(pitch)
                    nx.append(nx[0])
                for m in range(len(xx)):
                    x1 = xx[m-1]
                    currentAxis.add_patch(Rectangle( (x0/1000,h0), (x1-x0)/1000, h1-h0, facecolor=operator.get(nx[m - 1]) ))
                    x0 = x1
                h0 = h1

                #operator.get(int(nx[m - 1]))
                print nx
                print xx
                print xm
                print xn
                print eps
                print nx
            num = num + 5
        fak = 0.2
        currentAxis.add_patch(Rectangle(( 0,-fak * h1), pitch/1000, fak * h1, facecolor=operator.get(int(n0)) ))
        plt.axis([0, pitch/1000, -fak*h1, h0])
        plt.show()

        #for m in range(xm)
        print n0
        print gl.t_line

    def OnCloseWindow(self, event):
        self.Destroy()

    # --------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()