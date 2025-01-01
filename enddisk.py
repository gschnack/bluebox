import Part, FreeCAD, math
from FreeCAD import Base
from math import *


# battery holder 78x 21
# two battery holder 78 x 42

# DC converter_big  21 x 44 height 14
# DC converter_small 12 x 22 height 3.5


centerx=0
centery=0
inner_radius = 40.   #95
outer_radius = 55    #110
middle_radius = (inner_radius +outer_radius)/2.  
hole_radius = 2.0
pocket_radius = 4.0

thick_plate = 6.5
deltax = 5.
alpha1 = 30 # angle defining the outer thickness
alpha2 = 0
alpha3 = 0


# in calc_angle
deltax2 =0
width_plate =0



plate_left_upper = Base.Vector(0.,0.,0. )
plate_left_lower = Base.Vector(0.,0.,0. )
plate_right_upper = Base.Vector(0.,0.,0. )
plate_right_lower = Base.Vector(0.,0.,0. )


deltay = outer_radius * sin ( alpha1 /180 *pi )

def arcrect( centerx,centery,width,height,radius ):
	
	halfheightr= height /2-radius;
	halfwidthr=width/2-radius;
	halfheight= height /2;
	halfwidth=width/2;


#      v1   v2
#   v8          v3
# 			   
#   v7          v4
#      v6    v5

	v1=Base.Vector(centerx- halfwidthr,centery+halfheight )
	v2=Base.Vector(centerx+ halfwidthr,centery+halfheight )
    
	v3=Base.Vector(centerx+ halfwidth,centery+halfheightr )
	v4=Base.Vector(centerx+ halfwidth,centery-halfheightr )
    
    
	v5=Base.Vector(centerx+ halfwidthr,centery-halfheight )
	v6=Base.Vector(centerx- halfwidthr,centery-halfheight )
    
    
	v7=Base.Vector(centerx-halfwidth,centery-halfheightr )
	v8=Base.Vector(centerx- halfwidth,centery+halfheightr )


	l1=Part.LineSegment(v1,v2 )
	l2=Part.LineSegment(v3,v4 )
	l3=Part.LineSegment(v5,v6 )
	l4=Part.LineSegment(v7,v8 )

	circle = Part.Circle(Base.Vector(centerx+ halfwidthr,centery+halfheightr,0),Base.Vector(0,0,1),radius)
	arc1 = Part.Arc(circle,0,pi/2 )

	circle = Part.Circle(Base.Vector(centerx+ halfwidthr,centery-halfheightr,0),Base.Vector(0,0,1),radius)
	arc2 = Part.Arc(circle,-pi/2,0 )

	circle = Part.Circle(Base.Vector(centerx- halfwidthr,centery-halfheightr,0),Base.Vector(0,0,1),radius)
	arc3 = Part.Arc(circle,pi,-pi/2 )

	circle = Part.Circle(Base.Vector(centerx- halfwidthr,centery+halfheightr,0),Base.Vector(0,0,1),radius)
	arc4 = Part.Arc(circle,pi/2,pi )

	#S1 = Part.Shape([l1,arc1,l2,arc2,l3,arc3,l4,arc4 ])

	l1s=l1.toShape();
	l2s=l2.toShape();
	l3s=l3.toShape();
	l4s=l4.toShape();

	arc1s=arc1.toShape();
	arc2s=arc2.toShape();
	arc3s=arc3.toShape();
	arc4s=arc4.toShape();


	W1 = Part.Wire([l1s,arc1s,l2s,arc2s,l3s,arc3s,l4s,arc4s ])
	#W1 = Part.Wire([l1s,arc1s])
	
	return ( W1 )


def end_disk():
	
	
	global centerx
	global centery
	global inner_radius   #95
	global outer_radius     #110
	global middle_radius  
	global hole_radius 
	global pocket_radius



	outer_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),outer_radius)
	inner_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),inner_radius)
	
	
	
	hole = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	pocket= Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),pocket_radius)
	
	
	
	hole_wire1 = Part.Wire([ hole.toShape() ] )
	hole_wire1.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 20. )
	
	pocket_wire1 = Part.Wire([ pocket.toShape() ] )
	pocket_wire1.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 20. )
	
	
	
	hole_wire2 = Part.Wire([ hole.toShape() ] )
	hole_wire2.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 160. )
	
	pocket_wire2 = Part.Wire([ pocket.toShape() ] )
	pocket_wire2.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 160 )
	
	
	
	hole_wire3 = Part.Wire([ hole.toShape() ] )
	hole_wire3.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), -90. )
	
	pocket_wire3 = Part.Wire([ pocket.toShape() ] )
	pocket_wire3.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), -90 )
	
	
	Part.show( inner_circle.toShape() )
	Part.show( outer_circle.toShape() )
	
	Part.show( hole_wire1)
	Part.show( hole_wire2)
	Part.show( hole_wire3)
	
	Part.show( pocket_wire1)
	Part.show( pocket_wire2)
	Part.show( pocket_wire3)

	screw1 = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	screw1w = Part.Wire([ screw1.toShape() ] )
	screw1w.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 0* 72. )
	Part.show( screw1w )
	
	screw2 = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	screw2w = Part.Wire([ screw2.toShape() ] )
	screw2w.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 1* 72. )
	Part.show( screw2w )
	

	screw3 = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	screw3w = Part.Wire([ screw3.toShape() ] )
	screw3w.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 2* 72. )
	Part.show( screw3w )
	

	screw4 = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	screw4w = Part.Wire([ screw4.toShape() ] )
	screw4w.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 3* 72. )
	Part.show( screw4w )

	screw5 = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	screw5w = Part.Wire([ screw5.toShape() ] )
	screw5w.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 4* 72. )
	Part.show( screw5w )




#                   arc
#           v1       v0 
#
#   v4      v2       	
#   arc


#arc
# v9        v8
#           v7        v6
#                     arc


def speaker_disk(show):
	global thick_plate
	global deltax		

	global plate_left_upper
	global plate_left_lower
	global plate_right_upper
	global plate_right_lower





	
	inner_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),inner_radius)
	arc2 = Part.Arc(inner_circle, (180 -alpha2) /180. *pi,alpha2/180. *pi  )
	
	arc2s=arc2.toShape()

	outer_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),outer_radius)
#	arc1 = Part.Arc(outer_circle, 150/180. *pi,30/180. *pi  )
	arc1 = Part.Arc(outer_circle, (180 -alpha1) /180. *pi,alpha1/180. *pi  )
	
	#Part.show(arc1.toShape())
	
	arc1s = arc1.toShape()

	v0=arc1.EndPoint
	 	
	v1 = Base.Vector(v0.x - deltax , v0.y,0.  )
	v2 = Base.Vector(v1.x , v1.y - thick_plate ,0.  )
	v3 = arc2.EndPoint

	plate_right_upper = v2
	plate_right_lower = v1


	v9=arc1.StartPoint
	v8=Base.Vector(v9.x + deltax , v9.y,0.  )	
	v7 = Base.Vector(v8.x , v8.y - thick_plate ,0.  )
	v6 = arc2.StartPoint
	

	plate_left_upper = v7
	plate_left_lower = v8

	#v8 = Base.Vector(v9.x +deltax, v9.y,0.  )
	#v7 = Base.Vector(v8.x, v8.y -thick_plate ,0.  )
	
	l1=Part.LineSegment(v0,v1 )
	l1s=l1.toShape();

	l2=Part.LineSegment(v1,v2 )
	l2s=l2.toShape();
	
	l3=Part.LineSegment(v2,v3 )
	l3s=l3.toShape();

	l9=Part.LineSegment(v9,v8 )
	l9s=l9.toShape();

	l8=Part.LineSegment(v8,v7 )
	l8s=l8.toShape();

	l7=Part.LineSegment(v7,v6 )
	l7s=l7.toShape();



	W1 = Part.Wire([l9s, l8s,l7s,arc1s, l1s, l2s,l3s, arc2s ] )
	#W2 = Part.Wire([l9s, l8s,l7s ] )


	#Part.show( W2)



	hole = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	pocket= Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),pocket_radius)
	
	
	
	hole_wire1 = Part.Wire([ hole.toShape() ] )
	hole_wire1.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 20. )
	hole_wire2 = Part.Wire([ hole.toShape() ] )
	hole_wire2.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 160. )
	hole_wire3 = Part.Wire([ hole.toShape() ] )
	hole_wire3.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), -90. )
		
	#Part.show( inner_circle.toShape() )
	#Part.show( outer_circle.toShape() )
	

	if ( show == 1 ):
		Part.show( W1)
		
		#Part.show( arc2.toShape() )
		
		Part.show( hole_wire1)
		Part.show( hole_wire2)
		Part.show( hole_wire3)
		






def speaker_disk_protect():
	global thick_plate
	global deltax		
	
	global plate_left_upper
	global plate_left_lower
	global plate_right_upper
	global plate_right_lower


	inner_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),inner_radius)
	arc2 = Part.Arc(inner_circle, (180 -alpha2) /180. *pi,alpha2/180. *pi  )
	
	arc3 = Part.Arc(inner_circle,alpha3/180. *pi, (180 -alpha3) /180. *pi  )
	
	arc3s = arc3.toShape()
	arc2s = arc2.toShape()




	outer_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),outer_radius)
#	arc1 = Part.Arc(outer_circle, 150/180. *pi,30/180. *pi  )
	arc1 = Part.Arc(outer_circle, (180 -alpha1) /180. *pi,alpha1/180. *pi  )
	
	#Part.show(arc1.toShape())
	
	arc1s = arc1.toShape()

	v0=arc3.StartPoint


	
	 
	v2 = plate_right_upper
	v1 = plate_right_lower
	




	#v1 = Base.Vector(v0.x + deltax , v0.y,0.  )
	#v2 = Base.Vector(v1.x , v1.y - thick_plate ,0.  )
	v3 = arc2.EndPoint

	v9=arc3.EndPoint
	#v8=Base.Vector(v9.x + deltax , v9.y,0.  )	
	#v7 = Base.Vector(v8.x , v8.y - thick_plate ,0.  )
	v7 = plate_left_upper 
	v8=  plate_left_lower 
	


	v6 = arc2.StartPoint
	
	#v8 = Base.Vector(v9.x +deltax, v9.y,0.  )
	#v7 = Base.Vector(v8.x, v8.y -thick_plate ,0.  )
	#plate_left_upper
	#global plate_left_lower
		



	l1=Part.LineSegment(v0,v1 )
	l1s=l1.toShape();

	l2=Part.LineSegment(v1,v2 )
	l2s=l2.toShape();
	
	l3=Part.LineSegment(v2,v3 )
	l3s=l3.toShape();

	l9=Part.LineSegment(v9,v8 )
	l9s=l9.toShape();

	l8=Part.LineSegment(v8,v7 )
	l8s=l8.toShape();

	l7=Part.LineSegment(v7,v6 )
	l7s=l7.toShape();

	#Part.show( arc2.toShape() )
	#Part.show( arc3s )

	W1 = Part.Wire([l9s, l8s,l7s, arc3s, l1s, l2s,l3s, arc2s] )
	#W2 = Part.Wire([ ] )


	Part.show( W1)
	#Part.show( W2)



	hole = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	pocket= Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),pocket_radius)
	
	
	
	hole_wire1 = Part.Wire([ hole.toShape() ] )
	hole_wire1.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 20. )
	hole_wire2 = Part.Wire([ hole.toShape() ] )
	hole_wire2.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 160. )
	hole_wire3 = Part.Wire([ hole.toShape() ] )
	hole_wire3.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), -90. )
		
	#Part.show( inner_circle.toShape() )
	Part.show( outer_circle.toShape() )
	
	
	

	Part.show( hole_wire1)
	Part.show( hole_wire2)
	Part.show( hole_wire3)
	









def calcalpha():
	global alpha1
	global alpha2	
	global alpha3
	global deltax2	
	global deltax
	global width_plate	


	deltay1 = outer_radius * sin ( alpha1 /180 *pi )
	alpha2 = 180/pi * asin( (deltay1 -thick_plate ) / inner_radius )
	deltay2 = inner_radius * sin ( alpha2 /180 *pi )
	alpha3 = 	180/pi * asin( (deltay2 + thick_plate ) / inner_radius )

	deltax2 = 	outer_radius * cos( alpha1 /180 *pi )- inner_radius * cos( alpha2 /180 *pi ) - deltax
	

	width_plate = 2* (deltax2 +inner_radius * cos( alpha2 /180 *pi )) 

def rect( centerx,centery,width,height ):
	
	halfheight= height /2;
	halfwidth=width/2;




#      v1   v2
#
#      v4   v3

	v1=Base.Vector(centerx- halfwidth,centery+halfheight )
	v2=Base.Vector(centerx+ halfwidth,centery+halfheight )

    
	v3=Base.Vector(centerx+ halfwidth,centery-halfheight )
	v4=Base.Vector(centerx- halfwidth,centery-halfheight )
	


	l1=Part.LineSegment(v1,v2 )

	l2=Part.LineSegment(v2,v3 )
	l3=Part.LineSegment(v3,v4 )
	l4=Part.LineSegment(v4,v1 )

	l1s=l1.toShape();
	l2s=l2.toShape();
	l3s=l3.toShape();
	l4s=l4.toShape();


	W1 = Part.Wire([l1s,l2s,l3s,l4s ])
	return ( W1 )


def hole_rect( centerx,centery,width,height ,radius ):
	halfheight= height /2;
	halfwidth=width/2;


#      v1   v2
#
#      v4   v3

	v1=Base.Vector(centerx- halfwidth,centery+halfheight )
	v2=Base.Vector(centerx+ halfwidth,centery+halfheight )

    
	v3=Base.Vector(centerx+ halfwidth,centery-halfheight )
	v4=Base.Vector(centerx- halfwidth,centery-halfheight )
	
	h1 = Part.Circle(v1,Base.Vector(0,0,1),radius)
	Part.show( h1.toShape() )
	
	h2 = Part.Circle(v2,Base.Vector(0,0,1),radius)
	Part.show( h2.toShape() )
	
	h3 = Part.Circle(v3,Base.Vector(0,0,1),radius)
	Part.show( h3.toShape() )
	
	h4 = Part.Circle(v4,Base.Vector(0,0,1),radius)
	Part.show( h4.toShape() )
	



def speaker_plate(centerx, centery, width,height):

	centerx =0
	centery =0
	speaker_diameter = 51.
	distance_holes = 42

	W =rect( 0. ,0., width , height )	
	Part.show(W)
		
	hole = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),speaker_diameter/2.)
		
	Part.show(hole.toShape())
	
	hole_rect( 0. ,0., distance_holes , distance_holes,2. )

	fix1 = Part.Circle(Base.Vector(centerx+15,centery,0),Base.Vector(0,0,1),2.)
	fix2 = Part.Circle(Base.Vector(centerx-15,centery,0),Base.Vector(0,0,1),2.)
	Part.show(fix1.toShape())
	Part.show(fix2.toShape())




def sidespeaker_disk():
	global centerx
	global centery
	global inner_radius   #95
	global outer_radius     #110
	global middle_radius  
	global hole_radius 
	

	outer_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),outer_radius)
	Part.show( outer_circle.toShape() )
		
	speaker_diameter = 51.
	distance_holes = 42

	#W =rect( 0. ,0., width , height )	
	#Part.show(W)
		
	hole = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),speaker_diameter/2.)
		
	Part.show(hole.toShape())
	
	hole_rect( 0. ,0., distance_holes , distance_holes,2. )

	hole = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	pocket= Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),pocket_radius)
	
	
	
	hole_wire1 = Part.Wire([ hole.toShape() ] )
	hole_wire1.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 20. )
	hole_wire2 = Part.Wire([ hole.toShape() ] )
	hole_wire2.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 160. )
	hole_wire3 = Part.Wire([ hole.toShape() ] )
	hole_wire3.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), -90. )
		
	#Part.show( inner_circle.toShape() )
	#Part.show( outer_circle.toShape() )
		

	Part.show( hole_wire1)
	Part.show( hole_wire2)
	Part.show( hole_wire3)
	
	fix1 = Part.Circle(Base.Vector(centerx+15,centery,0),Base.Vector(0,0,1),2.)
	fix2 = Part.Circle(Base.Vector(centerx-15,centery,0),Base.Vector(0,0,1),2.)
	Part.show(fix1.toShape())
	Part.show(fix2.toShape())







def hollow_disk():
	
	
	global centerx
	global centery
	global inner_radius   #95
	global outer_radius     #110
	global middle_radius  
	global hole_radius 
	global pocket_radius



	outer_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),outer_radius)
	inner_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),inner_radius)
	
	
	
	hole = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	pocket= Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),pocket_radius)
	
	
	
	hole_wire1 = Part.Wire([ hole.toShape() ] )
	hole_wire1.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 20. )
	
	pocket_wire1 = Part.Wire([ pocket.toShape() ] )
	pocket_wire1.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 20. )
	
	
	
	hole_wire2 = Part.Wire([ hole.toShape() ] )
	hole_wire2.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 160. )
	
	pocket_wire2 = Part.Wire([ pocket.toShape() ] )
	pocket_wire2.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 160 )
	
	
	
	hole_wire3 = Part.Wire([ hole.toShape() ] )
	hole_wire3.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), -90. )
	
	pocket_wire3 = Part.Wire([ pocket.toShape() ] )
	pocket_wire3.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), -90 )
	
	
	Part.show( inner_circle.toShape() )
	Part.show( outer_circle.toShape() )
	
	Part.show( hole_wire1)
	Part.show( hole_wire2)
	Part.show( hole_wire3)
	
	#Part.show( pocket_wire1)
	#Part.show( pocket_wire2)
	#Part.show( pocket_wire3)


def battery_disk(version):
	global centerx
	global centery
	global inner_radius   
	global outer_radius     
	global middle_radius  
	global hole_radius 
	
	

	outer_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),outer_radius)
	inner_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),inner_radius)
	

	link1_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1), 31)
	link2_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1), 34)

	if version == 1:
		Part.show(link1_circle.toShape() )
		Part.show(link2_circle.toShape() )


	#outer circle comprises one arc interleaved with one line
	
	D= 18.
	R = 55.
	w= 180. /pi *2. * math.asin( D/(2*R))
	print( "winkel", w )


	#arc1 = Part.Arc(outer_circle, (265. -( 0) )/180. *pi  ,(235 -0. ) /180*pi   )
	arc1 = Part.Arc(outer_circle, (265. +( 0.) )/180. *pi  ,(265 - w ) /180*pi   )
	


	arc1s=arc1.toShape()

	Part.show( arc1s)

	# v1 to v4 is for the power supply
	v1=arc1.StartPoint
	v4 = arc1.EndPoint

	# v4 liegt oberhalb von v1

	dir = v1 - v4

	dirnorm= dir.normalize() # points downwards

	ortho_dir = Base.Vector(-dir.y,dir.x,0).normalize() # points to the right up
	thick =ortho_dir.normalize().multiply(3.) 	

	v2 = v1.add(thick) # thickness power plate 

	offset_down = dirnorm.multiply(4.).negative()
	
	v2a = v2.add(offset_down  ) # where do the the inlay start 
	
	depth = ortho_dir.normalize().multiply(28.)

	v2b = v2a.add( depth  )

	width = dirnorm.normalize().multiply(10.).negative()

	v2c = v2b.add( width )
	
	v2d = v2a.add( width )
	
	thick =ortho_dir.normalize().multiply(3.)

	v3 = v4.add(thick) # thickness power plate

	
	l1=Part.LineSegment(v1,v2 )
	l1s=l1.toShape();

	l1a=Part.LineSegment(v2,v2a )
	l1as=l1a.toShape();
	l1b=Part.LineSegment(v2a,v2b )
	l1bs=l1b.toShape();

	l1c=Part.LineSegment(v2b,v2c )
	l1cs=l1c.toShape();

	l1d=Part.LineSegment(v2c,v2d )
	l1ds=l1d.toShape();

	l1e=Part.LineSegment(v2d,v2a )
	l1es=l1e.toShape();



	l2=Part.LineSegment(v2d,v3 )
	l2s=l2.toShape();


	l3=Part.LineSegment(v3,v4 )
	l3s=l3.toShape();


	#Part.show(l1s )
	#Part.show(l1as )
	#Part.show(l1bs )
	#Part.show(l1cs )
	#Part.show(l1ds )
	#Part.show(l1es )
	#Part.show(l2s )
	#Part.show(l3s )

	if version == 2:
		Wx = Part.Wire([l1bs,l1cs,l1ds, l1es ])
		Wm = Wx.mirror(Base.Vector(0,0,0), Base.Vector(1,0. ,0))
		Part.show( Wx)
		Part.show( Wm)
	
		outer_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),outer_radius)
		Part.show( outer_circle.toShape() )
		

	#to do mirror the box


	if version == 1:
		Wu = Part.Wire([l1s,l1as,l1bs,l1cs,l1ds, l2s,l3s,arc1s ])
		Part.show( Wu)
	
	
	hole = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	
	
	
	hole_wire1 = Part.Wire([ hole.toShape() ] )
	hole_wire1.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 20. )
	
	
	
	hole_wire2 = Part.Wire([ hole.toShape() ] )
	hole_wire2.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 160. )
	
	
	
	
	hole_wire3 = Part.Wire([ hole.toShape() ] )
	hole_wire3.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), -90. )
	
	
	
	#Part.show( inner_circle.toShape() )
	#Part.show( outer_circle.toShape() )
	
	Part.show( hole_wire1)
	Part.show( hole_wire2)
	Part.show( hole_wire3)
	
	#W1 = arcrect( 0.,0. ,78. ,44. +3. ,2. ) #original
	W1 = arcrect( 0.,0.+ 3 +2 ,78. ,44. +3. ,2. ) #original

	Part.show( W1)
	

	#PCB with big converter
	#height 14 width 44
	W2 = arcrect( 0.,44.0 /2. + 14./2 +3 +3+3 +1.  ,44. + 3.  ,14.  ,2. )
	Part.show( W2)
	
	
	if version == 1:
	
		#little converter 
		#	
		#W3 = arcrect( +20.,-44.0 /2. - 12./2 -3. ,22. + 3.  ,12.  ,2. )
		W3 = arcrect( +20.,-44.0 /2. - 12./2 -3. ,22+3.  ,4  ,1.5 )
	
		Part.show( W3)
		
		fix1 = Part.Circle(Base.Vector(centerx+15,centery+ 3 +2,0),Base.Vector(0,0,1),2.)
		fix2 = Part.Circle(Base.Vector(centerx-15,centery+ 3 +2,0),Base.Vector(0,0,1),2.)
		Part.show(fix1.toShape())
		Part.show(fix2.toShape())
	
		fix3 = Part.Circle(Base.Vector(centerx+15,centery+ 44.0 /2. + 14./2 +3 +3+3. ,0),Base.Vector(0,0,1),2.)
		fix4 = Part.Circle(Base.Vector(centerx-15,centery+ 44.0 /2. + 14./2 +3 +3+3. ,0),Base.Vector(0,0,1),2.)
		Part.show(fix3.toShape())
		Part.show(fix4.toShape())
	





def power_plate():
		
	global centerx
	global centery

	# outer rectangular 28 x 12
	#Part.show(rect(0 , 0 ,12.,14. ))
	# outer rectangular 28 x 12
	Part.show(rect(0 , 0 ,12.5,33. ))



	# USB connector 
	usbheight= 3.2
	usbwidth = 9.5

	Part.show( arcrect( 0, -33. /2. +8.5 , usbwidth , usbheight,  1. ))
	
	
	#light indicator	
	Part.show( arcrect( 0, -33. /2. +12.5 , 5.5 , 2.1 , 1.))

	# switch
	Part.show( rect( 0, -33. /2. +22.5 , 5. ,5.  ))

	fix1 = Part.Circle(Base.Vector(centerx,centery- (33. /2.  -2 ),0 ),Base.Vector(0,0,1),1.1)
	fix2 = Part.Circle(Base.Vector(centerx,centery+ (33. /2.  -2) ,0),Base.Vector(0,0,1),1.1)
	Part.show(fix1.toShape())
	Part.show(fix2.toShape())


def amp_disk():
	global centerx
	global centery
	global inner_radius   
	global outer_radius     
	global middle_radius  
	global hole_radius 
	
	

	outer_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),outer_radius)
	inner_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),inner_radius)
	

	link1_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1), 31)
	link2_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1), 34)

	Part.show(link1_circle.toShape() )
	Part.show(link2_circle.toShape() )
	
	D= 18.
	R = 55.
	w= 180. /pi *2. * math.asin( D/(2*R))
	print( "winkel", w )


	#arc1 = Part.Arc(outer_circle, (265. -( 0) )/180. *pi  ,(235 -0. ) /180*pi   )
	arc1 = Part.Arc(outer_circle, (120. +( 0.) )/180. *pi  ,(120. - w ) /180*pi   )
	


	arc1s=arc1.toShape()

	Part.show( arc1s)

	# v1 to v4 is for the power supply
	v1=arc1.StartPoint
	v4 = arc1.EndPoint

	# v4 liegt oberhalb von v1

	dir = v1 - v4

	dirnorm= dir.normalize() # points downwards

	ortho_dir = Base.Vector(-dir.y,dir.x,0).normalize() # points to the right up
	thick =ortho_dir.normalize().multiply(3.) 	

	v2 = v1.add(thick) # thickness power plate 

	offset_down = dirnorm.multiply(4.).negative()
	
	v2a = v2.add(offset_down  ) # where do the the inlay start 
	
	depth = ortho_dir.normalize().multiply(10)

	v2b = v2a.add( depth  )

	width = dirnorm.normalize().multiply(10.).negative()

	v2c = v2b.add( width )
	
	v2d = v2a.add( width )
	
	thick =ortho_dir.normalize().multiply(3.)

	v3 = v4.add(thick) # thickness power plate

	
	l1=Part.LineSegment(v1,v2 )
	l1s=l1.toShape();

	l1a=Part.LineSegment(v2,v2a )
	l1as=l1a.toShape();
	l1b=Part.LineSegment(v2a,v2b )
	l1bs=l1b.toShape();

	l1c=Part.LineSegment(v2b,v2c )
	l1cs=l1c.toShape();

	l1d=Part.LineSegment(v2c,v2d )
	l1ds=l1d.toShape();

	l1e=Part.LineSegment(v2d,v2a )
	l1es=l1e.toShape();



	l2=Part.LineSegment(v2d,v3 )
	l2s=l2.toShape();


	l3=Part.LineSegment(v3,v4 )
	l3s=l3.toShape();


	#Part.show(l1s )
	#Part.show(l1as )
	#Part.show(l1bs )
	#Part.show(l1cs )
	#Part.show(l1ds )
	#Part.show(l1es )
	#Part.show(l2s )
	#Part.show(l3s )

	#Wx = Part.Wire([l1bs,l1cs,l1ds, l1es ])
	#Wm = Wx.mirror(Base.Vector(0,0,0), Base.Vector(1,0. ,0))
	#Part.show( Wx)
	#Part.show( Wm)
	
	#outer_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),outer_radius)
	#Part.show( outer_circle.toShape() )

	Wu = Part.Wire([l1s,l1as,l1bs,l1cs,l1ds, l2s,l3s,arc1s ])
	Part.show( Wu)

	
	hole = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	
	hole_wire1 = Part.Wire([ hole.toShape() ] )
	hole_wire1.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 20. )
	
	
	
	hole_wire2 = Part.Wire([ hole.toShape() ] )
	hole_wire2.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 160. )
	
	
	
	
	hole_wire3 = Part.Wire([ hole.toShape() ] )
	hole_wire3.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), -90. )
	
	
	Part.show( hole_wire1)
	Part.show( hole_wire2)
	Part.show( hole_wire3)
	
	# bluetooth PCB 
	center_angle = 120.-w/2
	distance = 35.
	
	# change the sizes of the board

	R2= rect(0,0 ,20,30  ) 
	R2.rotate(Base.Vector(0.,0,0.),Base.Vector(0.,0.,1. ), center_angle )
	R2.translate(Base.Vector(distance*cos(center_angle / 180*pi ) ,distance * sin(center_angle / 180*pi  ) , 0))	

	Part.show( R2 )
	
	# amplifier PCB
	R3= rect(20,0 ,30,20  ) 
	Part.show( R3 )
	


def amp_plate():

	global centerx
	global centery

	# outer rectangular 28 x 12
	#Part.show(rect(0 , 0 ,12.,14. ))
	# outer rectangular 28 x 12
	Part.show(rect(0 , 0 ,12.5,33 ))

	
	# for switches
	sw1 = Part.Circle(Base.Vector(centerx-3,centery- 7.5 ,0),Base.Vector(0,0,1),1.6)
	sw2 = Part.Circle(Base.Vector(centerx-3,centery+ 7.5 ,0),Base.Vector(0,0,1),1.6)

	Part.show(sw1.toShape())
	Part.show(sw2.toShape())


	
	#led 
	Part.show( arcrect( 12.5/ 2.- 3 , 0, 2.2 , 5,  1.05))


	# holes 
	
	fix1 = Part.Circle(Base.Vector(centerx,centery- (33. /2.  -2 ),0 ),Base.Vector(0,0,1),1.1)
	fix2 = Part.Circle(Base.Vector(centerx,centery+ (33. /2.  -2) ,0),Base.Vector(0,0,1),1.1)
	Part.show(fix1.toShape())
	Part.show(fix2.toShape())





a = 10


if a ==1 :

	end_disk()


	
if a ==2 :
	calcalpha()
	print( width_plate)	
	speaker_disk(1)



if a == 3:
	calcalpha()
	
	speaker_disk(0)


	speaker_disk_protect()


if a == 4:
	calcalpha()
	print( width_plate)	

	speaker_plate(0.,0. ,width_plate, 60. )


if a == 5: # 1 for main disk, 2 for both side disks
	battery_disk(2)	


if a == 6:
	sidespeaker_disk()	


if a == 7:
	hollow_disk()	


if a == 8: 
	power_plate()

if a == 9: 
	amp_disk()


if a == 10: 
	amp_plate()



