#!/usr/bin/env python
#coding=utf-8
import wx
import gl
import math

class SubclassDialog(wx.Dialog):
    def __init__(self):#初始化对话框
        wx.Dialog.__init__(self, None, -1, 'ass_slicer', size=(600, 400))
        self.InitUI()

    #-------------------------------------------------------------------------------------------
    def InitUI(self):
        panel = wx.Panel(self)

        topLbl = wx.StaticText(panel, -1, "ASS Slicer", size=(600, -1), style=wx.ALIGN_CENTER)  # 1 创建窗口部件
        topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        # 1 left

        left_Static_slope = wx.StaticText(panel, -1, "slope/~",style=wx.ALIGN_CENTER)
        self.left_Text_slope = wx.TextCtrl(panel, -1, "80.0")
        left_Static_radius_top = wx.StaticText(panel, -1, "radius_top/nm", style=wx.ALIGN_CENTER)
        self.left_Text_radius_top = wx.TextCtrl(panel, -1, "20")
        left_Static_radius_bot = wx.StaticText(panel, -1, "radius_bot/nm", style=wx.ALIGN_CENTER)
        self.left_Text_radius_bot = wx.TextCtrl(panel, -1, "30.0")
        left_Static_x_pos = wx.StaticText(panel, -1, "x_pos/nm", style=wx.ALIGN_CENTER)
        self.left_Text_x_pos = wx.TextCtrl(panel, -1, "5000")

        staticBox_left = wx.StaticBox(panel, label='left')
        staticBox_left_Sizer = wx.StaticBoxSizer(staticBox_left, orient=wx.HORIZONTAL)

        hbox_left_1 = wx.BoxSizer(wx.VERTICAL)
        hbox_left_1.Add((20, 15), 1)
        hbox_left_1.Add(left_Static_slope)
        hbox_left_1.Add((20, 15), 1)
        hbox_left_1.Add(left_Static_radius_top)
        hbox_left_1.Add((20, 15), 1)
        hbox_left_1.Add(left_Static_radius_bot)
        hbox_left_1.Add((20, 15), 1)
        hbox_left_1.Add(left_Static_x_pos)
        hbox_left_1.Add((20, 15), 1)
        staticBox_left_Sizer.Add((5, 5), 1)
        staticBox_left_Sizer.Add(hbox_left_1)
        staticBox_left_Sizer.Add((20, 20), 1)

        hbox_left_2 = wx.BoxSizer(wx.VERTICAL)
        hbox_left_2.Add((10, 10), 1)
        hbox_left_2.Add(self.left_Text_slope)
        hbox_left_2.Add((10, 10), 1)
        hbox_left_2.Add(self.left_Text_radius_top)
        hbox_left_2.Add((10, 10), 1)
        hbox_left_2.Add(self.left_Text_radius_bot)
        hbox_left_2.Add((10, 10), 1)
        hbox_left_2.Add(self.left_Text_x_pos)
        hbox_left_2.Add((10, 10), 1)
        staticBox_left_Sizer.Add(hbox_left_2)
        staticBox_left_Sizer.Add((5, 5), 1)

        # 2 right

        right_Static_slope = wx.StaticText(panel, -1, "slope/~", style=wx.ALIGN_CENTER)
        self.right_Text_slope = wx.TextCtrl(panel, -1, "70.0")
        right_Static_radius_top = wx.StaticText(panel, -1, "radius_top/nm", style=wx.ALIGN_CENTER)
        self.right_Text_radius_top = wx.TextCtrl(panel, -1, "30")
        right_Static_radius_bot = wx.StaticText(panel, -1, "radius_bot/nm", style=wx.ALIGN_CENTER)
        self.right_Text_radius_bot = wx.TextCtrl(panel, -1, "20.0")
        right_Static_x_pos = wx.StaticText(panel, -1, "x_pos/nm", style=wx.ALIGN_CENTER)
        self.right_Text_x_pos = wx.TextCtrl(panel, -1, "15000")

        staticBox_right = wx.StaticBox(panel, label='right')
        staticBox_right_Sizer = wx.StaticBoxSizer(staticBox_right, orient=wx.HORIZONTAL)

        hbox_right_1 = wx.BoxSizer(wx.VERTICAL)
        hbox_right_1.Add((20, 15), 1)
        hbox_right_1.Add(right_Static_slope)
        hbox_right_1.Add((20, 15), 1)
        hbox_right_1.Add(right_Static_radius_top)
        hbox_right_1.Add((20, 15), 1)
        hbox_right_1.Add(right_Static_radius_bot)
        hbox_right_1.Add((20, 15), 1)
        hbox_right_1.Add(right_Static_x_pos)
        hbox_right_1.Add((20, 15), 1)
        staticBox_right_Sizer.Add((5, 5), 1)
        staticBox_right_Sizer.Add(hbox_right_1)
        staticBox_right_Sizer.Add((20, 20), 1)

        hbox_right_2 = wx.BoxSizer(wx.VERTICAL)
        hbox_right_2.Add((10, 10), 1)
        hbox_right_2.Add(self.right_Text_slope)
        hbox_right_2.Add((10, 10), 1)
        hbox_right_2.Add(self.right_Text_radius_top)
        hbox_right_2.Add((10, 10), 1)
        hbox_right_2.Add(self.right_Text_radius_bot)
        hbox_right_2.Add((10, 10), 1)
        hbox_right_2.Add(self.right_Text_x_pos)
        hbox_right_2.Add((10, 10), 1)
        staticBox_right_Sizer.Add(hbox_right_2)
        staticBox_right_Sizer.Add((5, 5), 1)

        hbox_1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_1.Add(staticBox_left_Sizer)
        hbox_1.Add((50,50 ),1)
        hbox_1.Add(staticBox_right_Sizer)

        # 2

        Static_height = wx.StaticText(panel, -1, "height/nm", style=wx.ALIGN_CENTER)
        self.Text_height = wx.TextCtrl(panel, -1, "100.6")
        Static_pitch = wx.StaticText(panel, -1, "pitch/nm", style=wx.ALIGN_CENTER)
        self.Text_pitch = wx.TextCtrl(panel, -1, "20000")
        Static_lambda = wx.StaticText(panel, -1, "lambda/nm", style=wx.ALIGN_CENTER)
        self.Text_lambda = wx.TextCtrl(panel, -1, "633")

        hbox_2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_2.Add(Static_height)
        hbox_2.Add((5, 5), 1)
        hbox_2.Add(self.Text_height)
        hbox_2.Add((20,10),1)
        hbox_2.Add(Static_pitch)
        hbox_2.Add((5, 5), 1)
        hbox_2.Add(self.Text_pitch)
        hbox_2.Add((20, 10), 1)
        hbox_2.Add(Static_lambda)
        hbox_2.Add((5, 5), 1)
        hbox_2.Add(self.Text_lambda)

        # 3
        Static_truncation = wx.StaticText(panel, -1, "truncation", style=wx.ALIGN_CENTER)
        self.Text_truncation = wx.TextCtrl(panel, -1, "40")
        Static_slices = wx.StaticText(panel, -1, "slices", style=wx.ALIGN_CENTER)
        self.Text_slices = wx.TextCtrl(panel, -1, "30")
        Static_slices_round = wx.StaticText(panel, -1, "slices_round", style=wx.ALIGN_CENTER)
        self.Text_slices_round = wx.TextCtrl(panel, -1, "10")

        hbox_3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_3.Add(Static_truncation)
        hbox_3.Add((5, 5), 1)
        hbox_3.Add(self.Text_truncation)
        hbox_3.Add((20, 10), 1)
        hbox_3.Add(Static_slices)
        hbox_3.Add((5, 5), 1)
        hbox_3.Add(self.Text_slices)
        hbox_3.Add((20, 10), 1)
        hbox_3.Add(Static_slices_round)
        hbox_3.Add((5, 5), 1)
        hbox_3.Add(self.Text_slices_round)

        # 4
        Check_plot = wx.CheckBox(panel, -1, "Plot")
        Static_n_fill = wx.StaticText(panel, -1, "n_fill", style=wx.ALIGN_CENTER)
        self.Text_n_fill_1 = wx.TextCtrl(panel, -1, "1.0")
        self.Text_n_fill_2 = wx.TextCtrl(panel, -1, "0")
        Button_cancel = wx.Button(panel, -1, "Cancel")

        hbox_4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_4.Add(Check_plot)
        hbox_4.Add((5, 5), 1)
        hbox_4.Add(Static_n_fill)
        hbox_4.Add((5, 5), 1)
        hbox_4.Add(self.Text_n_fill_1)
        hbox_4.Add(self.Text_n_fill_2)
        hbox_4.Add((5, 5), 1)
        hbox_4.Add(Button_cancel)

        # 5
        self.Check_inverse = wx.CheckBox(panel, -1, "Inverse")
        Static_n_sub = wx.StaticText(panel, -1, "n_sub", style=wx.ALIGN_CENTER)
        self.Text_n_sub_1 = wx.TextCtrl(panel, -1, "1.5")
        self.Text_n_sub_2 = wx.TextCtrl(panel, -1, "0")
        Button_slice = wx.Button(panel, -1, "Slice")

        hbox_5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_5.Add(self.Check_inverse)
        hbox_5.Add((5, 5), 1)
        hbox_5.Add(Static_n_sub)
        hbox_5.Add((5, 5), 1)
        hbox_5.Add(self.Text_n_sub_1)
        hbox_5.Add(self.Text_n_sub_2)
        hbox_5.Add((5, 5), 1)
        hbox_5.Add(Button_slice)

        #Bind
        self.Bind(wx.EVT_BUTTON, self.OnCloseWindow, Button_cancel)
        self.Bind(wx.EVT_BUTTON, self.Slice, Button_slice)

        # end main
        mainSizer.Add(topLbl, 0, wx.ALL, 5)
        mainSizer.Add(hbox_1, 0, wx.ALL, 5)
        mainSizer.Add((5,5),1)
        mainSizer.Add(hbox_2, 0, wx.ALL, 5)
        mainSizer.Add(hbox_3, 0, wx.ALL, 5)
        mainSizer.Add((5, 5), 1)
        mainSizer.Add(hbox_4, 0, wx.ALL, 5)
        mainSizer.Add(hbox_5, 0, wx.ALL, 5)
        #mainSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        panel.SetSizer(mainSizer)

    #-------------------------------------------------------------------------------------------

    def OnCloseWindow(self, event):
        self.Destroy()

    def Slice(self, event):
        document = gl.t_line

        sll = float(self.left_Text_slope.GetValue())
        slr = float(self.right_Text_slope.GetValue())
        rtl = float(self.left_Text_radius_top.GetValue())
        rtr = float(self.right_Text_radius_top.GetValue())
        rbl = float(self.left_Text_radius_bot.GetValue())
        rbr = float(self.right_Text_radius_bot.GetValue())
        x0l = float(self.left_Text_x_pos.GetValue())
        x0r = float(self.right_Text_x_pos.GetValue())
        hgt = float(self.Text_height.GetValue())
        slc = float(self.Text_slices.GetValue())
        slcr = float(self.Text_slices_round.GetValue())
        num_lambda  = float(self.Text_lambda.GetValue())
        pitch = float(self.Text_pitch.GetValue())
        ord =float(self.Text_truncation.GetValue())
        nk0r = float(self.Text_n_sub_1.GetValue())
        nk0i = float(self.Text_n_sub_2.GetValue())
        nkar = float(self.Text_n_fill_1.GetValue())
        nkai = float(self.Text_n_fill_2.GetValue())
        b_invert = self.Check_inverse.GetValue()

        hsl = hgt - rtl - rbl
        hsr = hgt - rtr - rbr

        col = math.cos(sll/180*math.pi)
        cor = math.cos(slr/180*math.pi)
        sil = math.sin(sll/180*math.pi)
        sir = math.sin(slr/180*math.pi)
        tal = math.tan(sll/180*math.pi)
        tar = math.tan(slr/180*math.pi)

        # deviation from circle center in y - direction
        stl = col * rtl
        str = cor * rtr
        sbl = col * rbl
        sbr = cor * rbr
        # deviation from circle center in x - direction
        ttl = sil * rtl
        ttr = sir * rtr
        tbl = sil * rbl
        tbr = sir * rbr
        # tangent points
        ytl = hgt - rtl + stl
        ytr = hgt - rtr + str
        ybl = rbl - sbl
        ybr = rbr - sbr
        h2 = hgt / 2
        xtl = x0l + (ytl - h2) / tal
        xtr = x0r - (ytr - h2) / tar
        xbl = x0l + (ybl - h2) / tal
        xbr = x0r - (ybr - h2) / tar
        # circle center coordinates
        yctl = hgt - rtl
        ycbl = rbl
        yctr = hgt - rtr
        ycbr = rbr
        xctl = xtl + ttl
        xcbl = xbl - tbl
        xctr = xtr - ttr
        xcbr = xbr + tbr

        part = 2
        ltype = 4
        theta = 0.0
        phi = 0.0

        dlg = wx.FileDialog(self,
                            message="Save file",
                            defaultFile="unigit_input_sliced.txt",
                            wildcard=gl.wildcard_save,
                            style=wx.SAVE
                            )

        if dlg.ShowModal() == wx.ID_OK:
            #filename = ""
            #paths = dlg.GetPaths()
            # split the paths
            #for path in paths:

            #   filename = filename + path
                # write the contents of the TextCtrl[Contents] into the file
            #    file = open(filename, 'w')
            #    file.write(self.profile_file)
            #    file.close()
            filename = ""
            paths = dlg.GetPaths()
            for path in paths:
                filename = filename + path
            file = open(filename,'w')
            file.write('%9.3f          //AOI \n' % theta)
            file.write('%9.3f          //PHI \n' % phi)
            file.write('%d             //Truncation \n' % ord)
            file.write('%d             //Partitions \n' % part)
            file.write('%9.3f      //Pitch \n' % pitch)
            file.write('%9.3f      //Lambda \n' % num_lambda)
            file.write('%d             //Slices \n' % int(slc+2*slcr))
            file.write('( %6.3f , %6.3f )      //2 Index Substrate \n' % (nk0r,nk0i))


            file.close()

        dlg.Destroy()
        self.Destroy()

        print document
        print b_invert
        print hsl
        print hsr
        print col
        print tar



