# 12306-Captcha
训练模型识别12306图片，最大的问题还是数据集啊

```python
pip install PIL
```


# 入口main
```python
from ocr import OCR

if __name__ == '__main__':
    ocr=OCR()
    #图片路径
    img="D:/codes/fuck12306/红枣_茶蛊_铃铛_铃铛_红枣_热水袋_茶蛊_红枣.jpg"
    print('result:', ocr.getOCR(img))
```

测试图片

![](https://github.com/LoseNine/12306-Captcha/blob/master/img/2.png)

识别结果

![](https://github.com/LoseNine/12306-Captcha/blob/master/img/1.PNG)



