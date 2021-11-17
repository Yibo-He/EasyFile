### 输入格式

字符串 str	字符串，通配符为空串。如果原串是空串，新串也必须是空串

颜色	color	字符串，六位十六进制数 rgb，通配符为空串

字体	typeface 字符串 字体的名称，通配符为空串

字号	size	一个浮点数，表示字号，通配符为0

一组替换规则被保存在一个字典中。被替换元素和替换元素分别在对应元素的key前面加上src\_和dst\_
最终输入为若个字典的列表

### Example

[

  {"src_str":"用户","src_typeface":"等线","src_size":16,"src_color":"000000",

"dst_str":"我","dst_typeface":"宋体","dst_size":12,"dst_color":"66ccff"},

  {"src_str":"图","src_typeface":"","src_size":0,"src_color":"",

  "dst_str":"我","dst_typeface":"宋体","dst_size":12,"dst_color":"66ccff"}

]

### 一些限制

src_str为空，dst_str必须为空

...
