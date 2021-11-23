from pdftable import *


if __name__ == "__main__":
    # pdf2image("test.pdf","test",10,10,0)
    filename="EasyFile面向对象设计文档.pdf"
    x=open(filename,"rb")
    pdf=x.read()
    ret=process(pdf,rules=["2,3","3-4"],format='excel',ext="xlsx",debug=True)
    with open('out'+".zip","wb") as f:
        f.write(ret)