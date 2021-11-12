import os

import fitz


def pdf2image(pdfPath,imgPath,zoom_x,zoom_y,rotation_angle):
    """
    # 将PDF转化为图片
    pdfPath pdf文件的路径
    imgPath 图像要保存的文件夹
    zoom_x x方向的缩放系数
    zoom_y y方向的缩放系数
    rotation_angle 旋转角度
    """
    # 打开PDF文件
    pdf = fitz.open(pdfPath)
    # 逐页读取PDF
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
        pm = page.get_pixmap(matrix=trans, alpha=False)
        # 开始写图像
        pm.save(imgPath+str(pg)+".png")
    pdf.close()


import camelot
import PyPDF2

def pdf2csv(pdfPath):
    tables = camelot.read_pdf(pdfPath)

    tables.export('test.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
    print(len(tables))
    # tables[0].to_csv('test.csv',encoding='gbk') # to_json, to_excel, to_html, to_markdown, to_sqlite
    return tables


def split_pdf(document,lst):
    """
    切割指定的PDF文件
    """
    ret=[]
    for pages in lst:
        pdfw=PyPDF2.PdfFileWriter()
        for page in pages:
            pdfw.addPage(document.getPage(page))
        ret.append(pdfw)
    return ret

if __name__ == "__main__":
    # pdf2image("test.pdf","test",10,10,0)
    filename="test1.pdf"
    tables=[]
    with open(filename,"rb") as file:
        document=PyPDF2.PdfFileReader(file)
        pdfs=split_pdf(document,[[0,1],[2]])
        for i,x in enumerate(pdfs):
            with open('tmp'+str(i)+'.pdf','wb') as f:
                x.write(f)
            tables+=pdf2csv('tmp'+str(i)+'.pdf')
            print(len(tables))
    print(len(tables))
    for i,x in enumerate(tables):
        print(i)
        x.to_excel('test'+str(i)+'.xlsx')

    #pdf2csv('test.pdf')[0].to_excel('11.xlsx')

