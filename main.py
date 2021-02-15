#!/usr/bin/env python3

# plotviz.py

import wx
from plotPanel import plotPanel

APP_EXIT = 1

class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example,self).__init__(*args, **kwargs)

        panel = wx.SplitterWindow(self)
        cpanel = plotPanel(panel, abfFile)
        #cpanel.draw()

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()
        viewMenu = wx.Menu()

        self.shst = viewMenu.Append(wx.ID_ANY, 'Show statusbar', 'Show Statusbar', kind=wx.ITEM_CHECK)

        viewMenu.Check(self.shst.GetId(), True)
        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import new .abf file...')
        imp.Append(wx.ID_ANY, 'Next...') 
        imp.Append(wx.ID_ANY, 'Previous...')

        fileMenu.AppendSubMenu(imp, 'I&mport')

        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize((950, 950))
        self.Centre()
        self.SetTitle('PyABF Viz')

        menubar.Append(viewMenu, '&View')
        self.SetMenuBar(menubar)

        abfPicker = wx.FilePickerCtrl(self, wx.ID_ANY, message='Please choose your ABF file', wildcard='*.abf')
        btnSizer.Add(abfPicker, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        btnSizer.AddStretchSpacer(3)

   
    def OnQuit(self, e):
        self.Close()
    
    def ToggleStatusBar(self, e):

        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()
    

def main():

    app = wx.App()
    ex = Example(None, title='Sizing')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
