CurveSymmetry-

Save, then Drag 'n' Drop the CurveSymmetry.rvb file over an open Rhino V4 window. This will register an alias

CurveSymmetry that will run the script and auto complete like a regular command.

Usage:

The tool accepts lines, arcs, open polylines and open freeform curves. Select the curve at the end you want to keep, the other end of the curve will be adjusted. 

-If the curve is a freeform curve or polyline, control points will be adjusted so that points which fall on one side (the curve-selection side) of the axis of symmetry are mirrored across the axis.

Symmetry options: Auto, XAuto, YAuto, User, 3Pt

	- All of these options except 3pt create a symmetry plane normal to the current CPlane. 
	
	-Auto: Finds the midpoint of a line between the end points of the curve and mirrors the points on a plane perpendicular to that line at the midpoint. This is probably most useful when the end points on the curve are in the right place but the interior points are not arranged quite symmetrically.
	
	-XAuto:Finds the midpoint of a line between the end points of the curve then mirrors the points on a plane parallel to Cplane X at this midpoint.
	
	-YAuto:Finds the midpoint of a line between the end points of the curve then mirrors the points on a plane parallel to Cplane Y at this midpoint.

	-User: The user sets a vertical mirror plane by picking two points.
	
	-3pt: The user picks 3 points in space to define a symmetry plane.

- If the curve is a line or arc, then the user selects a point on the curve and the  curve is made symmetrical about that point- again, the selected end of the curve determines which end stays put, and which end is changed.

Limitataions that I know of so far:

1. No polycurves other than polylines. 

2. No closed curves. 

3. The result for freeform curves is always a uniform curve at least for right now- non-uniform knot spacing is not respected.