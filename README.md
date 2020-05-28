# 12306-Captcha
训练模型识别12306图片，自己存了2万张图，识别率保持了80%，因为笔记本电脑跑不动


测试图片

![](https://github.com/LoseNine/12306-Captcha/blob/master/img/2.png)

识别结果

![](https://github.com/LoseNine/12306-Captcha/blob/master/img/1.png)


#入口main
```python
from ocr import OCR

if __name__ == '__main__':
    ocr=OCR()
    #图片路径
    img="D:/codes/fuck12306/红枣_茶蛊_铃铛_铃铛_红枣_热水袋_茶蛊_红枣.jpg"
    print('result:', ocr.getOCR(img))
```
