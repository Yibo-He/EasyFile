### 输入格式

字符串 str	字符串，通配符为空串。如果原串是空串，新串也必须是空串

颜色	color	字符串，六位十六进制数 rgb，通配符为空串

字体	typeface 字符串 字体的名称，通配符为空串

字号	size	一个浮点数，表示字号，通配符为0



传入一个dict构成的list，dict两两成组，第一个dict表示需要被替换的元素，第二个字典表示替换的元素

### Example

[

  {"str":"用户","typeface":"等线","size":16,"color":"000000"},
  
  {"str":"我","typeface":"宋体","size":12,"color":"66ccff"},

  {"str":"图","typeface":"","size":0,"color":""},
  
  {"str":"我","typeface":"宋体","size":12,"color":"66ccff"}

]

