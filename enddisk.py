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

def calc_ts_beta(alpha, d_half):
	
	#d_half = (outer_radius-inner_radius)/ 2.
	
	plate_angle = alpha #  22.5 # degree, alpha
	
	#plate_angle = 45. # degree, alpha
	
	
	
	
	a= math.tan(plate_angle*math.pi / 180. )
	b = inner_radius + d_half
	
	print("a",a )
	print("b",b )
	
	
	
	p = -2. * b/(a*( 1.+ 1./(a**2 )))
	q = (b**2 -inner_radius**2) /( 1.+ 1. /(a**2) ) 
	
	#p = -5
	#q = 6
	
	z1 = -0.5 *p  + math.sqrt(p**2 / 4.0 - q) 
	z2 = -0.5 *p  - math.sqrt(p**2 / 4.0 - q ) 
	
	
	print("z1",z1 )
	
	print("z2",z2)
	
	z = z2
	print("z",z)
	
	
	beta = math.asin(z/inner_radius) 
	print("beta", beta* 180 / math.pi )
	x = z/ math.tan(plate_angle*math.pi / 180. )
	y = inner_radius* math.cos(beta)
	
	print("d_half", d_half )
	print("x", x)
	print("y", y)
	print("Ri + d/2", inner_radius+d_half, x+y )
	
	return beta* 180 / math.pi




# This file calculates an angle at the thales circle
# Th circle has a radius ra in the IV and III quadrant 
# and midpoint M. At a distance of x from M to the left a 
# line under an angle of alpha is drawn to the III quadrant
# the line crosses the thales circle at a point. This file calculates 
# the angle from the midpoint M to this new point 


def calc_ts_beta_outer(alpha,x):
	a= math.tan(alpha*math.pi / 180. )
	r= outer_radius
	p =  2.*x/( (1/a**2 +1.) * a )
	q = (x**2 -r**2 ) /(1/(a**2) +1 ) 

	h1 = -0.5 *p  + math.sqrt(p**2 / 4.0 - q) 
	h2 = -0.5 *p  - math.sqrt(p**2 / 4.0 - q ) 

	h = h1
	valid = (h**2 ) *( (1/a**2) +1) + h*2*x/a -r**2+ x**2
	print("valid h1 ",valid )
	h= h1 

	print("h1", h1 )

	y= h/a

	print("y",y )
	z = h **2 /(x + y + r ) 
	print("x,y,z",x+y +z,"r", outer_radius )
	beta1 =180/math.pi * math.atan( h/( x+y ) )
	print( "beta in grad", beta1)

	return( beta1)



# inner arc v0 is   
#
#


def two_speakers_disk():
	global thick_plate
	global deltax		

	#ts = two speakers

	d_half = (outer_radius-inner_radius)/ 2.
	anchor_x = d_half + inner_radius



	ts_alpha = 40  # change this 
	ts_beta = calc_ts_beta(ts_alpha, d_half)
	#ts_beta = 30.
	
	#thickness is  4
	
	plate_off = 4./ math.sin( ts_alpha/180*math.pi)
	print("plate_off", plate_off) 
	print("my x", inner_radius+ d_half+ plate_off)

	ts_beta_outer = calc_ts_beta_outer(ts_alpha, inner_radius+ d_half+ plate_off )
	#ts_beta = 10.0
	
	
	
	inner_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),inner_radius)
	arc2 = Part.Arc(inner_circle, ( -ts_beta ) /180. *pi,(ts_beta+180. )/180. *pi  )
	
	arc2s=arc2.toShape()

	outer_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),outer_radius)
#	arc1 = Part.Arc(outer_circle, 150/180. *pi,30/180. *pi  )
	arc1 = Part.Arc(outer_circle, (ts_beta_outer) /180. *pi, (-ts_beta_outer +180. )/180. *pi  )
	#arc1 = Part.Arc(outer_circle, (-ts_beta_outer) /180. *pi, (ts_beta_outer +180. )/180. *pi  )
	
	
	
	Part.show(arc1.toShape())
	Part.show(arc2.toShape())
	
	#right half
	v0=arc2.StartPoint
	v1 = Base.Vector(anchor_x,0.,0)		
	l1=Part.LineSegment(v0,v1 )
	l1s=l1.toShape();
	Part.show(l1s)
	
	dir = v0 - v1
	dirnorm= dir.normalize() # points downwards

	ortho_dir = Base.Vector(-dir.y,dir.x,0).normalize() # points to the right up
	thick =ortho_dir.normalize().multiply(4.) 	
	v2 = v1.add(thick) # thickness power plate 
	l2=Part.LineSegment(v1,v2 )
	l2s=l2.toShape();
	Part.show(l2s)
	
	v3=arc1.StartPoint
	
	l3=Part.LineSegment(v2,v3 )
	l3s=l3.toShape();
	Part.show(l3s)
	
	# left half
	v10=arc2.EndPoint
	v11 = Base.Vector(-anchor_x,0.,0)		
	l10=Part.LineSegment(v10,v11 )
	l10s=l10.toShape();
	Part.show(l10s)
	
	dir = v10 - v11
	dirnorm= dir.normalize() # points downwards

	ortho_dir = Base.Vector(-dir.y,dir.x,0).normalize() # points to the right up
	thick =ortho_dir.normalize().multiply(-4.) 	
	v12 = v11.add(thick) # thickness power plate 	
	l12=Part.LineSegment(v11,v12 )
	l12s=l12.toShape();
	Part.show(l12s)
	
	v13=arc1.EndPoint
	
	l13=Part.LineSegment(v12,v13 )
	l13s=l13.toShape();
	Part.show(l13s)
	
	
	
	hole = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	#pocket= Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),pocket_radius)
		
		
		
	hole_wire1 = Part.Wire([ hole.toShape() ] )
	hole_wire1.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 20. )
	hole_wire2 = Part.Wire([ hole.toShape() ] )
	hole_wire2.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 160. )
	hole_wire3 = Part.Wire([ hole.toShape() ] )
	hole_wire3.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), -90. )

			
	Part.show( hole_wire1)
	Part.show( hole_wire2)
	Part.show( hole_wire3)
	
	

def two_speakers_disk_protect(protect):
	global thick_plate
	global deltax		

	#ts = two speakers
################################
#circles arcs and calculations

	d_half = (outer_radius-inner_radius)/ 2.
	anchor_x = d_half + inner_radius

	#the flange is the length of the plate starting from the inner circle to the end of the plate 
	flange = 5.

	# length of plate without offsets
	length = sqrt( (inner_radius+ d_half )**2 + (inner_radius)**2  )

	ts_alpha = 180 / math.pi * math.atan( inner_radius / (inner_radius+ d_half ) )


	ts_alpha = ts_alpha +2  # change this 
	ts_beta = calc_ts_beta(ts_alpha, d_half)
	#ts_beta = 30.
	
	h = inner_radius * math.sin( ts_beta /180. *math.pi )
	print("h in twosp_prot", h ) 
	x = inner_radius * math.cos( ts_beta /180. *math.pi )
	y = inner_radius +d_half -x
	
	e = sqrt ( y **2 + h**2 )
	print("e in twosp_prot", e ) 
	
	
	#thickness is  4
	
	plate_off = 4./ math.sin( ts_alpha/180*math.pi)
	print("plate_off", plate_off) 
	print("my x", inner_radius+ d_half+ plate_off)

	ts_beta_outer = calc_ts_beta_outer(ts_alpha, inner_radius+ d_half+ plate_off )
	#ts_beta = 10.0
	
	
	
	inner_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),inner_radius)
	arc2 = Part.Arc(inner_circle, ( -ts_beta ) /180. *pi,(ts_beta+180. )/180. *pi  )
	
	
	arc2s=arc2.toShape()
	#if protect == 1:                #or protect == 0:
	#	Part.show(arc2.toShape())
	
	

	outer_circle = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),outer_radius)
	
	#if protect == 1 :
	# insert this for a protecting disk 
	#	Part.show(outer_circle.toShape())
	

	#arc1 = Part.Arc(outer_circle, 150/180. *pi,30/180. *pi  )
	#arc1 = Part.Arc(outer_circle, (ts_beta_outer) /180. *pi, (-ts_beta_outer +180. )/180. *pi  )
	arc1 = Part.Arc(outer_circle, (-ts_beta) /180. *pi, (ts_beta  +180. )/180. *pi  )
	
	
	
	#if protect == 0: 
	#	Part.show(arc1.toShape())
	
	
	if protect == 2: 
		arc_out_join = Part.Arc(outer_circle, (-ts_beta-90) /180. *pi, (ts_beta  -90. )/180. *pi  )
		#Part.show(arc_out_join.toShape())
	
	
	
	epsilon = 90 -(ts_alpha +ts_beta ) 
	# thickness = 4
	
#####################
	#right half
#####################
	
	v0=arc2.StartPoint
	v1 = Base.Vector(anchor_x,0.,0)	
	
			
				
	#l1=Part.LineSegment(v0,v1 )
	#l1s=l1.toShape();
	#Part.show(l1s)
	
	dir = v0 - v1
	dirnorm= dir.normalize() # points downwards
	inwards = dirnorm.normalize().multiply(flange) 
	v1 = v0.add( -inwards ) 
	l1=Part.LineSegment(v0,v1 )
	l1s=l1.toShape();
	
	#if protect == 1: # or protect == 0:
	#	Part.show(l1s)
	
	dir = v0 - v1
	dirnorm= dir.normalize() 
	ortho_dir = Base.Vector(-dir.y,dir.x,0).normalize() # points to the right up
	thick =ortho_dir.normalize().multiply(4.) 	
	v2 = v1.add(thick) # thickness power plate 
	l2=Part.LineSegment(v1,v2 )
	l2s=l2.toShape();
	#if protect == 1: # or protect == 0:
	#	Part.show(l2s)
	
	
	dirnorm= dir.normalize()
	
	if protect == 1:
		offset= 2.*(e -flange )
		
		front =  dirnorm.multiply(length-offset ) 
		v3 = v2.add ( front )
		
		l3=Part.LineSegment(v2,v3 )
		l3s=l3.toShape();
		#Part.show(l3s)
		
		v4 = v3.add( - thick )
		
		l4=Part.LineSegment(v3,v4 )
		l4s=l4.toShape();
		#Part.show(l4s)
		
		dirnorm= dir.normalize()
		back = dirnorm.multiply(- flange)
		
		v5 = v4.add(back )  
		
		l5=Part.LineSegment(v4,v5 )
		l5s=l5.toShape();
		#Part.show(l5s)
		
		
		
		
	if protect == 2:
		offset= 2.*(e -flange )
		
		front =  dirnorm.multiply(length-offset ) 
		
		v3 = v2.add ( front )
		
		l3=Part.LineSegment(v2,v3 )
		l3s=l3.toShape();
		#Part.show(l3s)
		
		## the short segment is added to v3 
		f1 = 4. * tan( epsilon /180 * math.pi )
		offset= (flange-f1  )
		
		dirnorm= dir.normalize()
		v7_f1 =  dirnorm.multiply( -offset ) 
		v7 = v3.add ( v7_f1 )

		l7=Part.LineSegment(v3,v7 )
		l7s=l7.toShape();
		#Part.show(l7s)			
		
		
		
		v4 = v3.add( - thick )
		
		l4=Part.LineSegment(v3,v4 )
		l4s=l4.toShape();
		#Part.show(l4s)
		
		dirnorm= dir.normalize()
		back = dirnorm.multiply( flange)
		
		v5 = v4.add(back )  
		
		l5=Part.LineSegment(v4,v5 )
		l5s=l5.toShape();
		#Part.show(l5s)
			
		
	if protect == 0:
		f1 = 4. * tan( epsilon /180 * math.pi )
		offset= (flange-f1  )
		
		v7_f1 =  dirnorm.multiply( offset ) 
		v7 = v2.add ( v7_f1 )
		l7=Part.LineSegment(v2,v7 )
		l7s=l7.toShape();
		#Part.show(l7s)	
		v8 = arc1.StartPoint	
		l8=Part.LineSegment(v7,v8 )
		l8s=l8.toShape();
		#Part.show(l8s)	
		
		
	
	#v3=arc1.StartPoint
	
	#l3=Part.LineSegment(v2,v3 )
	#l3s=l3.toShape();
	#Part.show(l3s)
	############################
	# left half
	############################
	
	v10=arc2.EndPoint
	v11 = Base.Vector(-anchor_x,0.,0)		
	#l10=Part.LineSegment(v10,v11 )
	#l10s=l10.toShape();
	#Part.show(l10s)
	
	dir = v10 - v11
	dirnorm= dir.normalize() # points downwards
	inwards = dirnorm.normalize().multiply(flange) 
	v11 = v10.add( -inwards ) 
	l11=Part.LineSegment(v10,v11 )
	l11s=l11.toShape();
	#if protect == 1: # or protect == 0:
	#	Part.show(l11s)
	
	
	
	dir = v10 - v11
	dirnorm= dir.normalize() # points downwards

	ortho_dir = Base.Vector(-dir.y,dir.x,0).normalize() # points to the right up
	thick =ortho_dir.normalize().multiply(-4.) 	
	v12 = v11.add(thick) # thickness power plate 	
	l12=Part.LineSegment(v11,v12 )
	l12s=l12.toShape();
	#if protect == 1: # or protect == 0:
	#	Part.show(l12s)
		
		
	front =  dirnorm.multiply(length-offset ) 
	
	if protect == 1:
		
		v13 = v12.add ( front )
		
		l13=Part.LineSegment(v12,v13 )
		l13s=l13.toShape();
		#Part.show(l13s)
		v14 = v13.add( - thick )
		
		l14=Part.LineSegment(v13,v14 )
		l14s=l14.toShape();
		#Part.show(l14s)
		
		dirnorm= dir.normalize()
		back = dirnorm.multiply(-flange)
		
		v15 = v14.add(back )  
		
		l15=Part.LineSegment(v14,v15 )
		l15s=l15.toShape();
		#Part.show(l15s)
		
	if protect == 2:
		dir = v10 - v11
		dirnorm= dir.normalize()
		
		
		#print("in protect")
		offset= 2.*(e -flange )
		
		front =  dirnorm.multiply(length-offset ) 
		
		v13 = v12.add ( front )
		
		l13=Part.LineSegment(v12,v13 )
		l13s=l13.toShape();
		#Part.show(l13s)
		
		## the short segment is added to v3 
		f1 = 4. * tan( epsilon /180 * math.pi )
		offset= (flange-f1  )
		
		dirnorm= dir.normalize()
		v7_f1 =  dirnorm.multiply( -offset ) 
		v17 = v13.add ( v7_f1 )

		l17=Part.LineSegment(v13,v17 )
		l17s=l17.toShape();
		#Part.show(l17s)			
		
		
		
		v14 = v13.add( - thick )
		
		l14=Part.LineSegment(v13,v14 )
		l14s=l14.toShape();
		#Part.show(l14s)
		
		dirnorm= dir.normalize()
		back = dirnorm.multiply( flange)
		
		v15 = v14.add(back )  
		
		l15=Part.LineSegment(v14,v15 )
		l15s=l15.toShape();
		#Part.show(l15s)
				
		
		
	if protect == 0:
		f1 = 4. * tan( epsilon /180 * math.pi )
		offset= (flange-f1  )
		
		dirnorm= dir.normalize()
	
		v17_f1 =  dirnorm.multiply( offset ) 
		v17 = v12.add ( v17_f1 )
		l17=Part.LineSegment(v12,v17 )
		l17s=l17.toShape();
		#Part.show(l17s)	
		v18 = arc1.EndPoint	
		l18=Part.LineSegment(v17,v18 )
		l18s=l18.toShape();
		#Part.show(l18s)	
		
		
	
	
	
	if protect == 1 or protect == 2 :
		#e = (length -2.*flange) /2.
		v = inner_radius - ( e  )
		
		vArc = Base.Vector(0.,-v ,0)	
		
		arc = Part.Arc(v5,  vArc,v15,)
		#if protect == 2:
		#	Part.show(arc.toShape())	
		
		#v13=arc1.EndPoint
		
		#l13=Part.LineSegment(v12,v13 )
		#l13s=l13.toShape();
		#Part.show(l13s)
	
	if protect == 2:
		#connect the lines from the outer circle to the innerarc 
		v18 = arc_out_join.StartPoint
		l18=Part.LineSegment(v17,v18 )
		l18s=l18.toShape();
		#Part.show(l18s)
				
		v8 = arc_out_join.EndPoint
		l8=Part.LineSegment(v7,v8 )
		l8s=l8.toShape();
		#Part.show(l8s)
			
		
	if protect == 0:	
		outer_arcs =arc1.toShape()
		Wu = Part.Wire([l11s,l12s,l17s,l18s,outer_arcs,l8s,l7s,l2s,l1s, arc2s ])
		Part.show( Wu)
		
	if protect == 1:	
		outer_arcs =arc1.toShape()
		Wu = Part.Wire([l11s,l12s,l13s,l14s,l15s,arc.toShape(),l5s,l4s,l3s,l2s,l1s,arc2s ])
		#l17s,l18s,outer_arcs,l8s,l7s,l2s,l1s, arc2s ])
		Part.show( Wu)
		Part.show(outer_circle.toShape())
			
	if protect == 2:	
		#Wu = Part.Wire([l14s,l15s, l17s ])
		#Part.show( Wu)
		Wu = Part.Wire([l18s,l17s,l14s,l15s,arc.toShape(),l5s,l4s,l7s,l8s,arc_out_join.toShape() ])
		Part.show( Wu)
		#  l8s,,l18s,,arc_out_join.toShape() 
						
	################			
	#holes
	################
	hole = Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),hole_radius)
	#pocket= Part.Circle(Base.Vector(centerx+ middle_radius,centery,0),Base.Vector(0,0,1),pocket_radius)
		
	hole_aux1= Part.Circle(Base.Vector(centerx+ 25,centery,0),Base.Vector(0,0,1),hole_radius)
	hole_aux2= Part.Circle(Base.Vector(centerx- 25,centery,0),Base.Vector(0,0,1),hole_radius)
	
	
	
	#pocket 	
		
	hole_wire1 = Part.Wire([ hole.toShape() ] )
	hole_wire1.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 20. )
	hole_wire2 = Part.Wire([ hole.toShape() ] )
	hole_wire2.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), 160. )
	hole_wire3 = Part.Wire([ hole.toShape() ] )
	hole_wire3.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), -90. )

	hole_wire4 = Part.Wire([ hole.toShape() ] )
	hole_wire4.rotate(Base.Vector(0.,0.,0.),Base.Vector(0.,0.,1. ), -90. )
	hole_wire4.translate(Base.Vector(0.,12. ,0.))
	
	if protect == 1 :				
		Part.show( hole_aux1.toShape())		
		Part.show( hole_aux2.toShape())			
									
	if protect != 2 :				
		Part.show( hole_wire1)
		Part.show( hole_wire2)
	if protect != 0 :				
		Part.show( hole_wire3)	
		Part.show( hole_wire4)	
		

def two_speakers_plate(centerx, centery, width,height):

	centerx =0
	centery =0
	speaker_diameter = 36.2
	distance_holes = 41. /(sqrt(2)) 

	W =rect( 0. ,0., 48.8 , 48.8 )	
	Part.show(W)
		
	hole = Part.Circle(Base.Vector(centerx,centery,0),Base.Vector(0,0,1),speaker_diameter/2.)
		
	Part.show(hole.toShape())
	
	hole_rect( 0. ,0., distance_holes , distance_holes,1.6 )

	fix1 = Part.Circle(Base.Vector(centerx+8,centery,0),Base.Vector(0,0,1),1.6)
	fix2 = Part.Circle(Base.Vector(centerx-8,centery,0),Base.Vector(0,0,1),1.6)
	fix3 = Part.Circle(Base.Vector(centerx-0,centery,0),Base.Vector(0,0,1),1.6)
	
	Part.show(fix1.toShape())
	Part.show(fix2.toShape())
	#Part.show(fix3.toShape())





a = 15


if a ==1 :

	end_disk()


	
if a ==2 :
	calcalpha()
	print( width_plate)	
	speaker_disk(1)

	Part.show( rect( 0,0,120,120 ) )

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


if a == 11: #not in use
	two_speakers_disk()


if a == 12: # the part joining the loadspeaker plates together 
	two_speakers_disk_protect(2)

if a == 13: 
	two_speakers_disk_protect(1)
	
if a == 14: 
	two_speakers_disk_protect(0)


if a == 15:
	two_speakers_plate(0, 0, 0,0)

