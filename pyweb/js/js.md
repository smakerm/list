
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

#### DOM对象属性
innerHTML   |   获取 或 设置当前DOM对象的HTML文本值
innerText   |   获取 或 设置当前DOM对象的文本值
value       |   获取 或 设置表单控件对象的值
nodeType    |   获取节点属性  |   1:元素节点 2：属性节点 3：文本节点 8：注释节点 9：文档节点
nodeName    |   获取节点名称  |   元素节点：标签名 文本节点：#text 文档节点：#document 注释节点:#comment

getAttribute(attrName)|获取某元素指定的属性|
setAttribute(attrName,attrValue)|设置某元素指定的属性|
removeAttribute(attrName)|移除某元素的属性|

















