import matplotlib
import numpy as np
import pyabf
import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
matplotlib.use('WXAgg')

class plotPanel(wx.Panel):
    def __init__(self, parent, abfFile, *args, **kwargs):
        wx.Panel.__init__(self, parent, abfFile)
        self.figure = Figure()
        self.axes1 = self.figure.add_subplot(211)
        self.axes2 = self.figure.add_subplot(212)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        abf = pyabf.ABF(f"${abfFile}.abf")
        for sweep in abf.sweepList:
            try:
                abf.setSweep(sweep, channel=2)
                x = abf.sweepX
                y = abf.sweepY
                self.axes1.plot(x,y)
            except:
                abf.setSweep(sweep, channel=0)
                x = abf.sweepX
                y = abf.sweepY
                self.axes1.plot(x,y)
            abf.setSweep(sweep, channel=0)
            x2 = abf.sweepC
            y2 = abf.sweepY
            self.axes2.plot(x,y)

