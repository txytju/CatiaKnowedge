
# 实例化对象的操作


## 改名称

```java
// Input : pro 被改名字的对象的父级

// Define Parameters

let i, num_column(Integer)
// instantiatedObjects: 由选中的父对象的子集构成的一个 list
let instantiatedObjects(List)
// destinationref: 父级的 ref
// tmpRef: 子对象的 ref
let destinationref,tmpRef(VPMReference)
// 循环中使用的子集名称
let instantiatedAssyInst(VPMInstance)
let name(String)
let dt(DTSheetType)

//////////////////////////////////////////////////////////////////
set dt =
set num_column =
//////////////////////////////////////////////////////////////////

// 找到父级的 Ref
destinationref = pro.Reference
// 找到父级的所有子集，形成一个 list
instantiatedObjects = destinationref.Children

i = 1
for i while i < pro.Children.Size()
{
	name = dt.CellAsReal(i,num_column)
	instantiatedAssyInst = instantiatedObjects[i]
  tmpRef = instantiatedAssyInst.Reference

  //名称
	instantiatedAssyInst.Name = name
	tmpRef.Name = name
}
```

## 实例化对象参数提取与参数修改

```java
// Input : pro 对象的父级


let destinationref(VPMreference)
let dt(DTSheetType)
let instantiatedObjects, prdPartFeatures(List)
let prdPartFeature(PartFeature)
let prd(Product)
let i, num_column_name, num_column_target(Integer)
let prd_name, FeatureName(String)

// target 可以是实数，也可以是字符串
let target(Real)
/* let target(String) */

//////////////////////////////////////////////////////////////////
set dt =
set FeatureName =
set num_column_name =
set num_column_target =
//////////////////////////////////////////////////////////////////

destinationref = pro.Reference
instantiatedObjects = destinationref.Children

i = 1
for i while i < instantiatedObjects.Size()
{

	prd = instantiatedObjects[i]
	prdPartFeatures = prd.Query("PartFeature","")
	prdPartFeature = prdPartFeatures[1]

	prd_name = prd.Name
	target = prdPartFeature.GetAttributeReal("FeatureName")

  // 输出信息
  dt.SetCell(i+1, num_column_name, prd_name)
	dt.SetCell(i+1, num_column_target, target)

  //修改参数
  prdPartFeature.SetAttributeReal("FeatureName", someValue)
}

- 参数的提取同样可以批量实现
```java
i = 1
for i while i < instantiatedObjects.Size()
{

	prd = instantiatedObjects[i]
	prdPartFeatures = prd.Query("PartFeature","")
	prdPartFeature = prdPartFeatures[1]

	prd_name = prd.Name
	dt.SetCell(i+1, num_column_name, prd_name)
	j = 2
	for Feature inside Features
	{
		target = prdPartFeature.GetAttributeString(Feature)
		num_column_target = j
		dt.SetCell(i+1, num_column_target, target)
    j = j + 1
	}
}
```


## 实例化对象中的点的坐标提取

```java
let destinationref(VPMreference)
let dt(DTSheetType)
let instantiatedObjects, prdPartFeatures(List)
let prdPartFeature(PartFeature)
let prd(Product)
let i, num_column_name, num_column_target(Integer)
let prd_name, FeatureName(String)
let x,y,z(Real)
// target
let targets(list)
let target(Point)


//////////////////////////////////////////////////////////////////
set dt =
set num_column_name = 1
set num_column_target = 2
//////////////////////////////////////////////////////////////////

destinationref = pro.Reference
instantiatedObjects = destinationref.Children

i = 1
for i while i < instantiatedObjects.Size()
{

	prd = instantiatedObjects[i]
	prdPartFeatures = prd.Query("PartFeature","")
	prdPartFeature = prdPartFeatures[1]

	prd_name = prd.Name
	targets = prdPartFeature.Query("Point","x.Name==\"Point\"")
	target=targets[1]
  // x = target.coord(1)
  // y = target.coord(2)
	z = target.coord(3)

	/*子对象名称也可以不输出*/
	dt.SetCell(i+1, num_column_name, prd_name)
	dt.SetCell(i+1, num_column_target, z)
}
```
