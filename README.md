#安装


除了安装requirements中的包，还需要手动安装ghostscript(不能用pip安装)

#提取表格

调用process(file,rules,format,ext)

file是pdf文件的二进制串
返回一个zip压缩包的二进制串

`file = fitz.open(filename)`

rules形如
`[“0,1,2”，“3”，“3-5”]`
，默认为["all"]

format可选 csv, json, excel, html , sqlite，默认为csv,ext为文件扩展名

提取跨越多页的表格还存在问题

