[toc]

### 背景属性

|作用|属性|取值|注意事项|
|:---:|:---|---|:---:|
|背景颜色|`background-color`|合法的颜色值|背景颜色是从border位置处就开始绘制的|
|背景图像|`background-image`|url(图像路径)||
|背景图像平铺|`background-repeat`|repeat/norepeat/repeat-x/repeat-y|
|背景图片尺寸|`background-size`|width height<br>px xx%||
|背景图片位置|`background-position`|x:水平偏移位置 y:垂直偏移位置<br>x% y%<br>left/right/center||
|背景属性|`backgorund`|color url() repeat position||


### 文本格式化属性
#### 字体属性

|作用|属性|取值|
|---|---|---|
|指定字体|`font-family`|使用,隔开的字体值列表|
|指定字体大小|`font-size`|以px pt为单位的数值|
|字体加粗|`font-weight`|1.normal:正常<br>2.bold:加粗<br>3.value|
|字体样式-斜体|`font-style`|1.normal<br>2.italic|
|小型大写字母|`font-variant`|1.normal<br>2.small-caps|
|字体属性|`font`|style variant weight size family||

#### 文本属性

|作用|属性|取值|
|---|---|---|
|文本颜色|`color`|合法的颜色值|
|文本的排列方式|`text-align`|left/center/right/justify|
|文字的修饰|`text-decoration`|none/underline/overline/line-through|
|行高|`line-height`|px <br>数值:当前文字大小的倍数|
|首行文本缩进|`text-indent`|px|
|文本的阴影|`text-shadow`|h-shadow v-shadow blur color|

### 表格属性

|作用|属性|
|---|---|
|尺寸|`width height`|
|边框属性|`border`|
|文本格式化属性|`font-* text-*`|
|背景属性||
|框模型属性||
|vertical-align||

|作用|属性|取值|
|---|---|---|
|边框合并|`border-collapse`|1.separate<br>2.collapse|
|边框边距|`border-spacing`|1.指定一个值<br>2.两个值|

### 过渡属性

|作用|属性|
|---|---|
|指定属性|`transition-property`|
|指定时长|`transition-duration`|
|指定速率|`transition-timing-function`|
|指定过渡延迟|`transition-delay`|
|简写|`tansition:property duration timeing-function delay`|


## 定位

### 普通流定位
又称为“文档流定位”，是页面布局中所有元素的迷人定位方式。

特点：
1. 每个元素在页面中都有自己的位置，并占据一定的页面空间
2. 每个元素都是在其父元素的左上角开始排列
3. 每个元素基本上都是按照从上到下，从左到右的方式进行排列的
    * 块级元素：从上到下排列
    * 行内元素&行内块：从左到右排列，只有一行显示不下的时候才换行
### 浮动定位
1. 浮动定位
    1. 浮动元素会被排除在文档流之外-脱离文档流，元素将不再占据页面空间
    2. 未浮动的元素们会上前占位
    3. 浮动元素会停靠在父元素的左边或右边或其他已浮动元素的边缘上
    4. 浮动只能在当前 行 浮动
    5. 浮动解决的问题-让多个块级元素在一行内显示

### 相对定位
### 绝对定位
### 固定定位



































