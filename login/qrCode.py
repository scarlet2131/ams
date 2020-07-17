
import time
import pyqrcode
import datetime
from pyqrcode import QRCode
import os

class qrCode:
    def __init__(self, s):
        self.obj = s
    def genUniqueId(self):
        self.t = str(datetime.datetime.now().time()).split('.')[0]
        self.t = self.t.replace(':','')
        uniqueId = self.obj + self.t
        print("UniqueId: ",uniqueId)
        return uniqueId
    def genQR(self):
        uniqueId = self.genUniqueId()
        # Generate QR code 
        url = pyqrcode.create("http://ams12345.herokuapp.com/imageRec/") 
        # Create and save the png file naming "myqr.png" 
        path = 'login/static/QR'
        fileName = self.obj + '_' + self.t +'.svg'
        fullPath = os.path.join(path, fileName)
        print(fullPath)
        url.svg(fullPath, scale = 8) 
        return 'QR/'+fileName