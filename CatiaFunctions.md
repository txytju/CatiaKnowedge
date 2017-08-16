
# 重要说明文档

## `CreateOrModifyDatum`

### 说明

```java
CreateOrModifyDatum (datumType: String, destination: Feature, patternList: List, indexInPatternList: Integer): UndefinedType Information

CreateOrModifyDatum used in a Knowledge Pattern, creates a new Geometric Feature in the destination body and stores it within a list from the Pattern.
Inputs:
- datumType(String): the datum type. Can be either Point, Line, Curve, Surface, VolumeGeo, Circle, Plane
- destination(Feature): a body or geometrical set which will store the created feature
- patternList(List): a Pattern list which will reference the created element
- indexInPatternList(Integer):  an optional index giving the position in which the object must be inserted in the list. Default behavior is to append the result to the list
Returned value:
- UndefinedType: the created geometric feature
```
### Sample

```java
/* Simple pattern creating points along a curve */
let i(Integer)
let currentPoint(Point)
let currentRatio(Real)

for i while i <= NumberOfPoints
{
currentRatio = i / NumberOfPoints
// The first call creates and empty geometric feature
currentPoint = CreateOrModifyDatum("Point",PartBody, `Relations\Knowledge Pattern.1\List.1`)
// The second call fills it with actual geometry
currentPoint = pointoncurveRatio(MyPatternCurve,point(0,0,0), currentRatio, TRUE)
}
```
## `linetangent`

### 说明
```java
linetangent (crv: Curve, pt: Point, start: Length, end: Length, orientation: Boolean): Line
Information
Creates a line tangent to curve at a given point.
```

### Sample
```java
Geometrical Set.1\Line.11 = linetangent (`Geometrical Set.1\Spline.1`, `Geometrical Set.1\Point.6`,0mm, 30mm, true)
```
