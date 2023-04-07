from PyQt4 import QtGui, QtCore # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication
from PyQt4.QtCore import QThread, SIGNAL
import project # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from ast import literal_eval

counter = 0
def hexdump2(x):

   # x=str(x)
   l = len(x)
   i = 0
   hexpkt=""
   while i < l:
       d = "%04x  " % i
       hexpkt+=d 
       for j in range(16):
           if i+j < l:
               d = "%02X" % ord(x[i+j])
               hexpkt+=d
               
           else:
               d = "  "
               hexpkt+=d
           if j%16 == 7:
               d = ""
               hexpkt+=d
               
       d = "  "
       hexpkt+=d
       d = x[i:i+16]
       hexpkt+=d
       hexpkt+="\n"
       i += 16
   return hexpkt
class SniffThread(QThread):
  
  def __init__(self):
      QThread.__init__(self)

  def __del__(self):
        self.wait()
 
  def capturepackets(self,packet):
        global counter
        counter += 1
        psummary='Packet #{}: {} ==> {}'.format(counter, packet[0][1].src, packet[0][1].dst)
  
        content = str(packet)
        content =repr(content)
        self.emit(QtCore.SIGNAL('settext(QString,QString)'), psummary,content)   
        self.emit(QtCore.SIGNAL('printhexa(QString)'), content)
      

  def run(self):
      # your logic here 
#      pkts= sniff(filter="src", timeout=50, prn=self.capturepackets)
      while 1:
        pkt = sniff(count=1)
        psummary = 'Packet #{}: {} ==> {}'.format(counter, pkt[0][1].src, pkt[0][1].dst)
        print(psummary)
        self.emit(QtCore.SIGNAL('settext(QString)'), psummary)

        # self.settext(psummary)

class ExampleApp(QtGui.QMainWindow, project.Ui_MainWindow):
    hexalist = []
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        self.pushButton.clicked.connect(self.b1_clicked)
        
        self.list_submissions.itemClicked.connect(self.printhexa)
        self.set_filter()
        f = self.filter.text
        self.emit(QtCore.SIGNAL('run(QString)'), f)
        #self.pushButton_2.clicked.connect(self.b2_clicked)
    def printhexa(self, content):
        t = self.list_submissions.currentItem().text()
        t = str(t)
        i = t.find("#")+1
        j = t.find(":")
        index = int(t[i:j])
        self.textEdit.setText(self.hexalist[index])
       
    def settext(self,packettext,content):
        global hexalist
        content = str(content)
        content = literal_eval(content)
        h = hexdump2(content)
        self.hexalist.append(h)
        content = literal_eval(content)
        self.textEdit.append(h)
        self.list_submissions.addItem(packettext)
        hexdump(content[1:-1])

        print ("hello")
        print (content)
        print (hexdump2(content))
        print (hexalist)
		
    def set_filter(self):
        self.filter.text = "src"
    		
    		
    def b1_clicked(self):


        self.get_thread = SniffThread()
        
        self.connect(self.get_thread, SIGNAL("settext(QString,QString)"), self.settext)

        self.connect(self.get_thread, SIGNAL("finished()"), self.done)

        self.get_thread.start()
     
        self.pushButton_2.setEnabled(True)
      
        self.pushButton_2.clicked.connect(self.get_thread.terminate)
       
        self.pushButton.setEnabled(False)

          # 
    def done(self):
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(True)
        self.hexalist=[]
        QtGui.QMessageBox.information(self, "Done!", "Done Capturing Packets!")
		 
def main():
	
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication

  
    form = ExampleApp()                 # We set the form to be our ExampleApp (design) 
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
