import Part, FreeCAD, math
from FreeCAD import Base
from math import *




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
	

a = 0


h1 = Part.Circle(Base.Vector(14.-12,0,0),Base.Vector(0,0,1),1.1)
Part.show( h1.toShape() )
		
	
h2 = Part.Circle(Base.Vector(14.-20,0,0),Base.Vector(0,0,1),1.1)
Part.show( h2.toShape() )
	




Part.show( rect( 0,0 , 50,50 ))
hole_rect( 0,0 ,40 ,40  ,1.5 )
		
Part.show( rect( 0,0 , 28,18 ))



if a == 0:
	

	
	
	v1 = Base.Vector( 14-7,-9  )
	v2 = v1 + Base.Vector(0, 4 )
	v3 = v2 + Base.Vector(7, 0 )
	v4 = v3 + Base.Vector(0, 10 )
	v5 = v4 + Base.Vector(-4, 0.)
	v6 = v5 + Base.Vector(0. , 4. )
	v7 = v6 + Base.Vector(-(28-4) , 0. )
	v8 = v7 + Base.Vector(0,  -7.5 )
	v9 = v8 + Base.Vector(4.5 , 0 )
	v10 = v9 + Base.Vector(0. ,-3. )
	v11 = v10 + Base.Vector(-4.5, -0. )
	v12 = v11 + Base.Vector(0,  -7.5 )
	
	
	
	l1=Part.LineSegment(v1,v2 )
	l2=Part.LineSegment(v2,v3 )
	l3=Part.LineSegment(v3,v4 )
	l4=Part.LineSegment(v4,v5 )
	l5=Part.LineSegment(v5,v6 )
	l6=Part.LineSegment(v6,v7 )
	l7=Part.LineSegment(v7,v8 )
	l8=Part.LineSegment(v8,v9 )	
	l9=Part.LineSegment(v9,v10 )	
	l10=Part.LineSegment(v10,v11 )	
	l11=Part.LineSegment(v11,v12 )	
	l12=Part.LineSegment(v12,v1 )	
	
	
	
	
	
	l1s=l1.toShape();
	l2s=l2.toShape();
	l3s=l3.toShape();
	l4s=l4.toShape();
	l5s=l5.toShape();
	l6s=l6.toShape();
	l7s=l7.toShape();
	l8s=l8.toShape();
	l9s=l9.toShape();
	l10s=l10.toShape();
	l11s=l11.toShape();
	l12s=l12.toShape();

	
	W1 = Part.Wire([l1s,l2s,l3s,l4s,l5s,l6s,l7s,l8s,l9s,l10s,l11s,l12s ])
	
	
	Part.show( W1 )
	
if a == 1:	


	h3 = Part.Circle(Base.Vector(14.-12,0,0),Base.Vector(0,0,1),2.)
	Part.show( h3.toShape() )
		
	
	h4 = Part.Circle(Base.Vector(14.-20,0,0),Base.Vector(0,0,1),2.)
	Part.show( h4.toShape() )





	v1 = Base.Vector( 14,-3.5  )
	v2 = v1 + Base.Vector(-7, 0 )
	v3 = v2 + Base.Vector(0, -(12-7)/2 )
	v4 = v3 + Base.Vector(-2.1, 0 )
	v5 = v4 + Base.Vector(0, 12)
	v6 = v5 + Base.Vector(2.1 , 0 )
	v7 = v6 + Base.Vector(0, -(12-7)/2 )
	v8 = v7 + Base.Vector(7,  0 )





	l1=Part.LineSegment(v1,v2 )
	l2=Part.LineSegment(v2,v3 )
	l3=Part.LineSegment(v3,v4 )
	l4=Part.LineSegment(v4,v5 )
	l5=Part.LineSegment(v5,v6 )
	l6=Part.LineSegment(v6,v7 )
	l7=Part.LineSegment(v7,v8 )
	l8=Part.LineSegment(v8,v1 )	
	
	
	
	
	l1s=l1.toShape();
	l2s=l2.toShape();
	l3s=l3.toShape();
	l4s=l4.toShape();
	l5s=l5.toShape();
	l6s=l6.toShape();
	l7s=l7.toShape();
	l8s=l8.toShape();

	
	W1 = Part.Wire([l1s,l2s,l3s,l4s,l5s,l6s,l7s,l8s ])
	
	
	Part.show( W1 )
	