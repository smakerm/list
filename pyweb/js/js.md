
### 事件

#### 数组

方法|作用|注意
---|---|---
length|取长|只能统计索引数组的长度
toString()|将数组转换为字符串|
join(seperator)|返回指定连接符连接的字符串|seperator:连接符
concat(arr1,arr2,...)|返回多个数组拼接后的数组|
reverse()|反转|该函数能够直接改变数组|
sort()|排序|会直接改变数组，默认以unicode码进行排序，利用排序函数排序
push()|入栈，返回新数组长度|
pop()|出栈，返回数组尾部元素|
unshift()|向数组头部增加新元素并返回新数组长度|
shift()|删除并返回数组头部元素|


#### 字符串

方法|作用|注意
---|---|---
length|取长|
toUpperCase()|返回大写|
toLowerCase()|返回小写|
charAt(index)|返回指定下标的字符|
charCodeAt(index)|返回指定下标位置处字符的Unicode码(十进制)|
indexOf(value,fromIndex)|返回 查询子字符串在指定字符串值中的起始下标|
lastIndexOf(value,fromIndex)|于上相反|从后往前查
substring(start,end)|返回从start到end-1处的字符串|
split(seperator)|拆分字符串 返回数组|
/正则表达式/修饰符|模式匹配|i:忽略大小写 g：全局匹配 m：允许多行匹配
replace(substr/regexp,replacement)|替换|
match(substr/regexp)|匹配字符串 返回数组|
search(substr/regexp)|返回第一次出现的下标|

#### window对象

对话框

window.alert()|警告框
window.prompt()|输入框
window.confirm()|确认框

定时器
var ret = setInterval(fun,time)|周期性定时器|fun:要执行的操作 time:时间间隔周期（ms） ret:返回已创建好的对象
clearInterval(timer)|清除定时器|
setTimeout(fun,time)|一次性定时器|
clearTimeout(timer)|清楚定时器|



### DOM

查找节点
document.getElementById('id');|通过ID查找|elem对象
document/elme.getElementsByTagName('标签名')|通过标签查询|由指定标签元素返回的列表
document.getElementsByName(name)|通过name查找|由指定name返回的列表
document/elme.getElementsByClassName(classname)||

elem.parentNode|
elem.children|
elem.nextSibling|
elem.nextElementSibling|
elem.previousSibling|
elem.previousElementSibling|

创建节点
document.createElement("元素名");|elem
增加节点
document.body.appendChild(elem)
parentNode.appendChild(elem)
parentNode.insertBefore(newElem,oldElem)


删除节点
删除节点只能由父元素来发起
document.body.removeChild(elem)
parentNode.removeChild(elem)


#### DOM对象属性
innerHTML   |   获取 或 设置当前DOM对象的HTML文本值
innerText   |   获取 或 设置当前DOM对象的文本值
value       |   获取 或 设置表单控件对象的值
nodeType    |   获取节点属性  |   1:元素节点 2：属性节点 3：文本节点 8：注释节点 9：文档节点
nodeName    |   获取节点名称  |   元素节点：标签名 文本节点：#text 文档节点：#document 注释节点:#comment

getAttribute(attrName)|获取某元素指定的属性|
setAttribute(attrName,attrValue)|设置某元素指定的属性|
removeAttribute(attrName)|移除某元素的属性|


#### DOM元素的样式
    1. 使用setAttribute()设置class属性的值
        elem.setAttribute("class","类选择器");
    2. 使用元素的className 属性修改class值
        elem.className='类选择器';
    3. 自定义元素样式
        elem.style.css属性=值;
        注意:
            如果css属性中包含 - 的话,连字符(-)要取消,并且 - 后面的第一个字符要变大写



#### 时间对象的常用属性
事件源 | event.target
offsetX, offsetY | 获取鼠标在元素上的坐标点
clientX, clientY | 获取鼠标在网页上的坐标点
screenX, screenY | 获取鼠标在屏幕上的坐标点

event.key | 得到按下的字符
event.keypress| event.which  获取ASCII码
event.keydown | event.which  获取键位码
event.stopPropagation() | 阻止事件冒泡










