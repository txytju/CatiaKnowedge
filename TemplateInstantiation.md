# 实例化

## 背景
- 类型：`Action`
- 用途：用于模版的实例化，模版的特点是其输入条件（`Inputs`）为两个坐标系。
- 使用基础
  - 输入参数设计表：dt
  - 输出设计表：dt_out
  - 桩号表：dt_ZH
  - 资源表：Resource
  - 父对象：pro
  - 引导线（Guideline）：InputCurve
  - 坐标系集合父对象：AxisSet
- 模版的`Input`
  - 一端坐标系：Axis1
  - 另外一端坐标系：Axis2
  - 引导线：Curve
- 需要填写
  -
- 需要指定
  -
- 疑问
  - 查`InstantiateTemplate`的说明，Resource的类型是什么？是不是String？
  - 查`SetAttributeDimension`的说明，"Thinkness"的类型是什么？
## Code

```java
// Input : pro 被改名字的对象的父级
// Input : InputCurve
// Input : AxisSet

/* 创建变量 */
let i, column_ZH, ZH, column_QDZH, column_ZDZH(Integer)
let temp(VPMInstance)
let tempInsRef(VPMReference)
let Axis1,Axis2(AxisSystem)
let AxisList(list)
let c(Curve)
let dt, dt_out, dt_ZH(DTSheetType)
let name(String)
let qdzh, zdzh(String)
let Resource(String)
let Thinkness(String)

set AxisList = AxisSet -> Query("AxisSystem","")
set c = InputCurve

//////////////////////////////////////////////////////////////////
set dt =
set dt_out =
set dt_ZH =

// 桩号参数在设计表中的第几列
set column_ZH =
// 起始桩号在输出设计表中的第几列
// 终点桩号在输出设计表中的第几列
set column_QDZH =
set column_ZDZH =

set Resource =
set name = dt.CellAsString(i, ) +
//////////////////////////////////////////////////////////////////

i = 1
for i while i <= AxisList.Size()-1
{
	// 指定使用什么模板
	temp=InstantiateTemplate(Resource, pro.Reference)
	// 指定模版的 Inputs
	Axis1 = AxisList[i]
	Axis2 = AxisList[i+1]
	temp->SetAttributeObject("Axis1", Axis1)
	temp->SetAttributeObject("Axis2", Axis2)
	temp->SetAttributeObject("Curve",c)
	// 实例的命名
	temp.Name = name
	temp.Reference.Name= name

  //////////////////////////////////////////////////////////////////
  // 实例参数赋值
	temp -> SetAttributeDimension("Attribute", dt.CellAsReal(i, X),"LENGTH")
  // 写入表格
  dt_out.SetCell(i+1, X, X)
  //////////////////////////////////////////////////////////////////

  // 关于节段号的部分
  ZH = dt.CellAsReal(i, column_ZH)
  qdzh = dt_ZH.CellAsString(ZH, column_QDZH)
  zdzh = dt_ZH.CellAsString(ZH, column_ZDZH)

  EndModifyTemplate(temp)
}

```
