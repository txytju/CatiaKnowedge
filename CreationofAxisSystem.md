
# 基于线生成坐标系

## 背景

- 类型：知识工程
- 用途：基于线（curve:c）以及线上的初始点（point:p_ref），生成沿线偏移的一系列点（p）及在这些点处的局部坐标系（A）
- 使用基础
  - 设计表：储存有点（p）相对初始点（p_ref）的偏移距离
- 局部坐标系特征
  - X轴与线在该点处相切
  - Z轴竖直向上
  - 由右手坐标系法则决定Y轴方向
- 需要填写
  - 坐标系数量：num
  - 在设计表中，沿线总偏移量在第几列：num_column
  - 用于存放点和坐标系的几何集合（Geomtry Set）名称：Name_Points, Name_Axis
- 需要指定
  - 曲线：c
  - 参考点：p_ref
  - 设计表：dt
  - 几何集合（Name_Points, Name_Axis）的父级
  - 插入点和坐标系的`list`


## Code

```java
// Points
// Axis

// Define Parameters
let n, num, num_column(Integer)
let p_ref, p(point)
let c(curve)
let dt(DTSheetType)
let Points_Set, Axis_Set(OpenBodyFeature)
let Name_Points, Name_Axis(String)
let D(direction)
let linetangent_p(line)
let V, V_z, V_y(vector)
let A(AxisSystem)


// Design Parameters
//////////////////////////////////////////////////////////////////
set num =
set num_column =
set Name_Points = "_Points"
set Name_Axis = "_Axis"

set c =
set p_ref =
set dt =
set Points_Set = new("OpenBodyFeature", Name_Points, 父对象)
set Axis_Set = new("OpenBodyFeature", Name_Axis, 父对象)
//////////////////////////////////////////////////////////////////


n = 1
for n while n <= num
{
   //////////////////////////////////////////////////////////////////
   p = CreateOrModifyDatum("Point", Points_Set, 点的列表, n)
   A = CreateOrModifyDatum("AxisSystem", Axis_Set, 坐标系的列表, n)
   //////////////////////////////////////////////////////////////////

   //Creat a point on which the Axis will be build
   p = pointoncurve(c, p_ref, dt.CellAsReal(n,num_column), True)

   // Creat a line tangent at the curve on point "p"
   // Get the direction of the line and transfor the direction to a vector
   linetangent_p = linetangent(c, p, 5m, 0m, False)
   D = direction(linetangent_p)
   V = D -> Vector()

   // Vector of Z direction
   V_z = direction(0, 0, 1) -> Vector()
   // Get the V_y using cross product
   V_y = [ ( V.Get(2,1) * V_z.Get(3,1) ) - ( V.Get(3,1) * V_z.Get(2,1) );
   ( V.Get(3,1) * V_z.Get(1,1) ) - ( V.Get(1,1) * V_z.Get(3,1) );
   ( V.Get(1,1) * V_z.Get(2,1) ) - ( V.Get(2,1) * V_z.Get(1,1) )]

   // Creat Axis using 3 directions
   A = axisSystem(p, D, V_y->Direction(), V_z->Direction())

   // Set the Axis name
   A.Name = ToString(n)
 }
```



## 改进
- 父对象和 list 对象集中提前定义

```
// 剥离方式
let father(typeoffather)
set father = '3D shapeXX'
set Points_Set = new("OpenBodyFeature", Name_Points, father)

let Points_list, Axis_list (list)
set Points_list =
set Axis_list =
```


# 在三维道路中心线上创建X轴在平面内的坐标系

- 类型：知识工程
- 用途：在道路中心线上，生成X轴在水平面内的坐标系
- 使用基础
    - 三维道路中心线`c`
    - 道路中心线在水平面内的投影`c_ref`
    - 起始点在平面线的上的投影`p_ref_start`

```java
// 基于三维道路中心线在平面上投影线上的点的切线创建坐标系，并在三维中心线上创建坐标系
// Ref_Points
// Points
// Axis

// Define Parameters
//////////////////////////////////////////////////////////////////
let n, num, num_column(Integer)
// c_ref ：三维中心线在平面内的投影
// c : 三维中心线
let c, c_ref(curve)
// p_ref_start ：投影线上的节段点
// p_ref: 在投影线上创建的用于在中心线投影的点
// p : p_ref 在道路中心线上的投影
let p_ref, p_ref_start, p(point)
let dt(DTSheetType)
let Ref_Points_Set, Points_Set, Axis_Set(OpenBodyFeature)
let Name_Points_Ref, Name_Points, Name_Axis(String)
let D(direction)
let linetangent_p_ref(line)
let V, V_z, V_y(vector)
let A(AxisSystem)
//////////////////////////////////////////////////////////////////


// Design Parameters
//////////////////////////////////////////////////////////////////
set num =
set num_column =
set c_ref =  `道路中心线在平面内的投影线`
set c = `道路中心线`
set p_ref_start = `起始点`
set dt = `Relations\抗拔桩坐标系设计表\Sheet`
set Name_Points_Ref = "KBZ_Points_Ref"
set Name_Points = "KBZ_Points"
set Name_Axis = "KBZ_Axis"
set Ref_Points_Set = new("OpenBodyFeature", Name_Points_Ref, `几何 A.1` )
set Points_Set = new("OpenBodyFeature", Name_Points, `几何 A.1` )
set Axis_Set = new("OpenBodyFeature", Name_Axis, `几何 A.1` )
//////////////////////////////////////////////////////////////////


n = 1
for n while n <= num
{
	p_ref = CreateOrModifyDatum("Point", Ref_Points_Set, `Relations\Knowledge Pattern.1\Ref_Points`  , n)
	p = CreateOrModifyDatum("Point", Points_Set, `Relations\Knowledge Pattern.1\Points`   , n)
	A = CreateOrModifyDatum("AxisSystem", Axis_Set, `Relations\Knowledge Pattern.1\Axis`  , n)

	//Creat a point on which the Axis will be build
	p_ref = pointoncurve(c_ref, p_ref_start, dt.CellAsReal(n,num_column), True)
	p = project (p_ref, c, direction(0, 0, 1))
	// Creat a line tangent at the curve on point "p"
	// Get the direction of the line and transfor the direction to a vector
	linetangent_p_ref = linetangent(c_ref, p_ref, 5m, 0m, False)
	D = direction(linetangent_p_ref)
	V = D -> Vector()

	// Vector of Z direction
	V_z = direction(0, 0, 1) -> Vector()
	// Get the V_y using cross product
	V_y = [ ( V.Get(2,1) * V_z.Get(3,1) ) - ( V.Get(3,1) * V_z.Get(2,1) );
	( V.Get(3,1) * V_z.Get(1,1) ) - ( V.Get(1,1) * V_z.Get(3,1) );
	( V.Get(1,1) * V_z.Get(2,1) ) - ( V.Get(2,1) * V_z.Get(1,1) )]

	// Creat Axis using 3 directions
	A = axisSystem(p, D, V_y->Direction(), V_z->Direction())

	// Set the nameS
	p_ref.Name = ToString(n)
	p.Name = ToString(n)
	A.Name = ToString(n)

}

```

# 基于线和线上的已有点生成坐标系

## 背景
- 要做坐标系的线和坐标系的原点已经存在，基于上述线和点创建坐标系。

## Code
```java
//根据点和线，在点上生成坐标系
//该坐标系是和三维线相切的

let n, num(Integer)
let p(point)
let c(curve)
let Points(list)
let Points_Set, Axis_Set(OpenBodyFeature)
let Name_Axis(String)
let linetangent_p(line)
let D(direction)
let V, V_z, V_y(vector)
let A(AxisSystem)

set c = `道路中心线`
set Points_Set = `1st_layer_Points到道路中心线投影点`
set Points = Points_Set ->Query("Point","")
set Name_Axis = "Axis"
set Axis_Set = new("OpenBodyFeature", Name_Axis, `3D Shape00721263 A.1`   )





n = 1
for n while n <= num
{
	p = Points.GetItem(n)
	A = CreateOrModifyDatum("AxisSystem", Axis_Set,`Relations\生成坐标系\Axis` , n)
	// p点处的切线
	linetangent_p = linetangent(c, p, 5m, 0m, False)
	D = direction(linetangent_p)
	// 切线向量
	V = D ->Vector()
	// Z方向
	V_z = direction(0, 0, 1) -> Vector()
	// 差积
	V_y = [ ( V.Get(2,1) * V_z.Get(3,1) ) - ( V.Get(3,1) * V_z.Get(2,1) );
	( V.Get(3,1) * V_z.Get(1,1) ) - ( V.Get(1,1) * V_z.Get(3,1) );
	( V.Get(1,1) * V_z.Get(2,1) ) - ( V.Get(2,1) * V_z.Get(1,1) )]

	A = axisSystem(p, D, V_y ->Direction(), direction(0,0,1))
	A.Name = ToString(n)

}

```
