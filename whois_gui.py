#!/usr/bin/python
'''
Description : Program to fetch whois information of a domain name
Author : Magochi James  
Email : james@magochi.net
Credits(whois module): Silver Moon m00n.silv3r@gmail.com
Hosted on github under magochi profile
'''
import kate
import wx
import os
import random
import re
import wx.lib.dialogs
import socket, sys
import dns.resolver
class testgui(wx.Frame):
  def __init__(self, parent, id, title):
       		wx.Frame.__init__(self, parent, id, title, size=(500,230))
        	# Menu stuff
        	menubar =wx.MenuBar()
        	menufile =wx.Menu()
        	menuhelp =wx.Menu()
        	self.SetMenuBar(menubar)
        	menubar.Append(menufile, '&File')
        	menubar.Append(menuhelp, '&Help')
        	exitmenu =menufile.Append(-1, 'Quit', 'Exit Application')
        	about =menuhelp.Append(-1, 'About', 'About us')
        	#panel creation and sizer
        	panel =wx.Panel(self, -1)
        	hbsizer =wx.BoxSizer(wx.VERTICAL)
        	self.orig_text =wx.TextCtrl(panel,-1,size=(470,120),style=wx.TE_MULTILINE)
       #	 self.orig_text =wx.TextCtrl(panel,-1)
       #	Objects
        	self.orig_label =wx.StaticText(panel,-1, 'Paste Your Domain here: ')
        	ok_button =wx.Button(panel,-1,'Domain Expiry')
        	cancel_button =wx.Button(panel,-1,'Clear')
        	format_seq =wx.Button(panel,-1,'View MX')
        	rhead =wx.Button(panel,-1,'View TXT')
        	exit_button=wx.Button(panel,-1,'Exit')
        	disp =wx.StaticText(panel,-1,'')
     		vsizer1 =wx.BoxSizer(wx.HORIZONTAL)
     		vsizer4 =wx.BoxSizer(wx.HORIZONTAL)
     		vsizer5 =wx.BoxSizer(wx.HORIZONTAL)
     		vsizer6 =wx.BoxSizer(wx.HORIZONTAL)
     		vsizer2 =wx.BoxSizer(wx.HORIZONTAL)
     		vsizer1.Add(self.orig_label,1,wx.CENTRE,10)
     		vsizer2.Add(self.orig_text,1,wx.CENTRE,10)
     		vsizer5.Add(rhead,1,wx.RIGHT,1)
     		vsizer5.Add(format_seq,1,wx.RIGHT,1)
     		vsizer5.Add(ok_button,1,wx.RIGHT,1)
     		vsizer5.Add(cancel_button,1,wx.RIGHT,1)
     		vsizer5.Add(exit_button,1,wx.RIGHT,1)
     		vsizer6.Add(disp,1,wx.CENTER,1)
     		hbsizer.Add(vsizer1,0,wx.CENTER|wx.ALL,1)
#    		   hbsizer.Add(self.orig_text,0, wx.CENTER|wx.ALL,1)
     		hbsizer.Add(vsizer2,0, wx.CENTER|wx.ALL,1)
     		hbsizer.Add(vsizer4,0, wx.CENTER|wx.ALL,1)
     		hbsizer.Add(vsizer5,0,wx.ALIGN_RIGHT|wx.RIGHT,1)
     		hbsizer.Add(vsizer6,0,wx.CENTER,1)
		#events
     		self.Bind(wx.EVT_BUTTON,self.executa,ok_button)
     		self.Bind(wx.EVT_BUTTON,self.txt,rhead)
     		self.Bind(wx.EVT_BUTTON,self.mx,format_seq)
     		self.Bind(wx.EVT_MENU, self.soja, exitmenu)
     		self.Bind(wx.EVT_MENU, self.OnAboutBox, about)
     		self.Bind(wx.EVT_BUTTON,self.clear,cancel_button)
     		self.Bind(wx.EVT_BUTTON,self.soja,exit_button)
#pane		l.CreateStatusBar()
     		panel.SetSizer(hbsizer) 
     		self.Centre()
     		self.Show(True)
     	def OnAboutBox(self, e):
        	info = wx.AboutDialogInfo()
        	info.SetIcon(wx.Icon('logo.png', wx.BITMAP_TYPE_PNG))
       		info.SetName('WHOIS Tool')
       	 	info.SetVersion('1.0')
       	 	info.SetDescription("For MTN Business")
       	 	info.SetCopyright('(C) 2013 Magochi James')
       	 	info.SetWebSite('http://www.mtnbusiness.co.ke')
       	 	info.SetLicence("Program to fetch whois information of a domain name, \nAuthor : Magochi James Email : james@magochi.net \nCredits(whois module): Silver Moon m00n.silv3r@gmail.com \nOpen Soure Python Code Hosted on github under magochi profile")
       	 	info.AddDeveloper('james@magochi.net')
       	 	info.AddDocWriter('jameMagochi James')
       	 	info.AddArtist('james@magochi.net')
       	 	info.AddTranslator('james@magochi.net')
        	wx.AboutBox(info)
	
	def clear(self,event=None):
		self.orig_text.SetValue('')
	def format_seq(self,event=None):
		originator=self.orig_text.GetValue()
		comm=re.sub('[ \t\r\n]','',originator)
        	self.orig_text.SetValue(comm)
	def rheader(self,event=None):
		originator=self.orig_text.GetValue()
		comm=re.sub('>.*','>',originator)
        	self.orig_text.SetValue(comm)
	def soja(self, event=None):
    		self.Close(True)
	def txt(self,event=None):
		self.domain_name = self.orig_text.GetValue()
		answers = dns.resolver.query(self.domain_name, 'TXT')
		du = wx.lib.dialogs.ScrolledMessageDialog(self,""+unicode(answers.response), " Entire -DIG  Results -MTN ")
		du.ShowModal()
	def mx(self,event=None):
		self.domain_name = self.orig_text.GetValue()
		answers = dns.resolver.query(self.domain_name, 'MX')
		#print answers.response
		#print "------"
		du = wx.lib.dialogs.ScrolledMessageDialog(self,""+unicode(answers.response), " Entire -DIG  Results -MTN ")
		du.ShowModal()
	def executa(self,event=None):
		recordid=random.randint(20,10055)
	#	originator=self.orig_text.GetValue()
		#os.system('perl /home/obiero/codonopt/codonOpt-test.pl %s' %originator)
        	self.domain_name = self.orig_text.GetValue() 
		#wx.MessageBox('Domain:' +self.domain_name, 'MTN')   
		gal = kate.mtn()
		magochi = gal.get_whois_data(self.domain_name)
        	for line in magochi.split("\n"):
        		if "xpire" in line:
        	      		#print "Domain :"+domain_name, line.strip()
				answer = line.strip()
		#wx.MessageBox(""+self.domain_name+": =>  :"+answer, 'MTN Business(K)  - results') 
		dlg = wx.MessageDialog(self,""+self.domain_name+": =>  :"+answer+"\n\n\nDo you wish to view entire WHOIS result ?",'MTN Business(K)  - results', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		if dlg.ShowModal() == wx.ID_YES:
			du = wx.lib.dialogs.ScrolledMessageDialog(self,''+magochi, " Entire -WHOIS Results ")
			du.ShowModal()
				#wx.MessageBox('Domain: not found!!', 'MTN')    
		#    wx.MessageBox('Download completed', 'Info', wx.OK | wx.ICON_INFORMATION)
app =wx.App()
testgui(None, -1, 'WHOIS - MTN Business Kenya')
app.MainLoop()
