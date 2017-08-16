- Knowedege pattern 的 list是什么？有什么作用？
  - list 主要用于存放在知识工程中的迭代对象。当在知识工程中使用迭代对象（比如使用一个循环）时，需要在知识工程内部创建 list。

- 如何在Catia中查看一个对象的类型
  - 打开语言浏览器，将光标放在对象栏，选中树结构中的对象，对象栏下方即反馈对象的类型。


# 常见错误
## `Input`定义错误
1. `The fuction EndModifyTemplate failed.It may be because there are inputs missing, or because some of these inputs are invalid.`
    - 可能原因：在Action中对于模版的`输入（Inputs）`的名字输入不正确，如模版有一个`Input`叫做`TopSurface`，然后在Action中输入时写成了`Surface`，即输入了`temp. SetAttributeDimension("Surface", dt.CellAsReal(n,3), "LENGTH")`，则可能导致这种情况。
