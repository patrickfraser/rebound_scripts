#include "colors.inc"
#include "stdcam.inc"             

background { color Black }  
       
//Coordinate system is such that when loaded:
//X is positive to the left (West)
//Z is positive pointing down (South)
//Y is positive when pointing out of the screen           
                      
                    
                      
#fopen position "vector_38.txt" read 
#fopen rrradius "radius_38.txt" read          
union{
#while (defined(position))
    #while (defined(rrradius)) 
        #read (position, Vector)
        #read (rrradius, Float)   
        sphere { Vector, Float     
        texture { 
        pigment { colour White
            }}}
#end   
#end
rotate <90, 90, 0>   
translate <0, 20, -3000>
}          

global_settings { ambient_light rgb<0,0,0> }
                                                 
              
//Sun                                                 
light_source{ <0,0,0> color rgb <1,1,1>
              parallel             
              rotate <0, 0 ,0>
              point_at<0, 0, -1> 
            }                                              
              
//Ambience Light
//light_source{ <0,0,1000> color rgb <0.1,0.1,0.1>
//              parallel             
//              rotate <0, 0 ,0>
//              point_at<0, 0, 1001> 
//           } 
                          
//Background plane on or off
              
plane { <0, 1, 0>, 1
    pigment { color Black
    }
  }
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
// origin axis display   this file is  axis.inc as of 07Feb2009
                     
#ifndef( ORIGIN_Inc_Temp)  
#declare ORIGIN_Inc_Temp = version;
                                 
#include "colors.inc"

#declare DisplayFont = "arial.ttf"

// let's label the origin of the scene with a black sphere
#declare MyOrigin = object {
     sphere {
         <0, 0, 0> // center of sphere <X Y Z>
         1.0       // radius of sphere
        texture{
           pigment{Black}
        }
     }  
}   
//---------------------------------------------                                
// X-axis pointer:
#declare MyXPointer = union {
cylinder {
    0*x,  10*x,  1
    open
    texture{
       pigment{ Red }
    }
}
cone {
  10*x,  1.0,
  11*x, 0.0
   texture{pigment{ Red}}
}

text {
  ttf             // font type (only TrueType format for now)
  DisplayFont,
  "X",      // the string to create
  1,              // the extrusion depth
  0               // inter-character spacing
  //rotate 90*y
  scale <5,5,1>
  translate <11,2,0>
  texture{pigment{Red}}
}
}
//------------------------------------------------
// y-axis pointer:
#declare MyYPointer = 
union {
cylinder {
    0*y,  10*y,  1
    open
    texture{
       pigment{ White }
    }
}
cone {
  10*y,  1.0,
  11*y, 0.0
   texture{pigment{ White}}
}

text {
  ttf             // font type (only TrueType format for now)
  DisplayFont,
  "Y",      // the string to create
  1,              // the extrusion depth
  0               // inter-character spacing
  //rotate 90*y
  scale <5,5,1>
  translate <5,9,5>
  texture{pigment{White}}
  
}      
}

//------------------------------------------------
// z-axis pointer:
#declare MyZPointer = 
union {
cylinder {
    0*z,  10*z,  1
    open
    texture{
       pigment{ Blue }
    }
}
cone {
  10*z,  1.0,
  11*z, 0.0
   texture{pigment{ Blue}}
}

text {
  ttf             // font type (only TrueType format for now)
  DisplayFont,
  "Z",      // the string to create
  1,              // the extrusion depth
  0               // inter-character spacing
  //rotate 90*y
  scale <5,5,1>
  translate <2,5,11>
  texture{pigment{Blue}}
  
}
}
#declare MyAxisDisplay = 
union {          
	object {MyOrigin }
	object {MyXPointer}
	object {MyYPointer}
	object {MyZPointer}
}

#end

object { MyAxisDisplay}

camera {
    location <0, 3200, -3400>
    look_at  <0, 0, -3401>
    rotate <0, 0 ,0>
}                                    