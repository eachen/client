#--*coding:utf-8*--

'''
Created on 2016��8��17��

@author: pc  one
'''
import wx
import socket
import threading
class frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, size=(1280, 720), title="自动测试工具".decode('utf-8', 'ignore')) 
        self.myPanel=panel(self)
class panel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,-1,pos=(50,50),size=(100,100))
        self.button=wx.Button(self,-1,label=('test'))
        self.Bind(wx.EVT_BUTTON, self.onclick, self.button)
    def onclick(self,event):
        self.clientSkt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.clientSkt.connect(("127.0.0.1",9999))
        tread=threading.Thread(target=self.recive,args=(self.clientSkt))
        tread.start()
    def recive(self,skt):
        print skt.recv(1024)

class MyApp(wx.App):
    def OnPreInit(self, *args, **kwargs):
        rame = frame()
        rame.Show()
        self.MainLoop()
        return wx.App.OnPreInit(self, *args, **kwargs)
if __name__ == "__main__":
    app = MyApp()