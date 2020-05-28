import ctypes
import os
from cropImg import crop_img

class OCR:
    def __init__(self):
        self.dll=None
        self.path=os.getcwd()
        self.setDll()
    def setDll(self):
        #加载DLL
        self.dll=ctypes.CDLL("./OCR.dll")

    def getOCR(self, img: str) -> str:
        """输入dat地址和图片地址
            mcg:
            img:图片路径
        """

        codes=[]
        mcg=os.path.join(self.path,'./12306.dat')
        mcgPath = mcg.encode('utf8')
        mcg = ctypes.create_string_buffer(mcgPath)

        #分割图片
        crop_img(img)


        for i in range(1,9):
            codePath = os.getcwd() + '\\' + 'yzm\\'+str(i)+'.jpg'
            imgPath = codePath.encode('utf8')
            img = ctypes.create_string_buffer(imgPath)

            result=ctypes.string_at(self.dll.getOCR(mcg, img))
            codes.append(result.decode('gb2312'))
        return codes

