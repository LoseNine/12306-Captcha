from ocr import OCR

if __name__ == '__main__':
    ocr=OCR()
    img="D:/codes/fuck12306/红枣_茶蛊_铃铛_铃铛_红枣_热水袋_茶蛊_红枣.jpg"
    print('result:', ocr.getOCR(img))