difference(){

minkowski(){
cube([150,170,20], center=true);
//sphere(105, $fn=100);
sphere(2);
}

translate([0,0,3])
minkowski(){
cube([147,167,17], center=true);
//sphere(105, $fn=100);
sphere(2);
}

translate([57,-8,0])
rotate([90,0,90])
cylinder(h=20, r=6);

translate([57,8,-1])
rotate([90,0,90])
cube([8,2,80]);

}

difference(){
    
    translate([73, 83,-8]) 
cylinder(h=7, r=2);
    
    translate([73, 83,-8]) 
cylinder(h=7, r=1.5);
}

difference(){
    
    translate([73, -83,-8]) 
cylinder(h=7, r=2);
    
    translate([73, -83,-8]) 
cylinder(h=7, r=1.5);
}

difference(){
    
    translate([-73, -83,-8]) 
cylinder(h=7, r=2);
    
    translate([-73, -83,-8]) 
cylinder(h=7, r=1.5);
}

difference(){
    
    translate([-73, 83,-8]) 
cylinder(h=7, r=2);
    
    translate([-73, 83,-8]) 
cylinder(h=7, r=1.5);
}


letter_size = 1.5;
letter_height = 1;

module letter(l) {
  // Use linear_extrude() to make the letters 3D objects as they
  // are only 2D shapes when only using text()
  linear_extrude(height = letter_height) {
    text(l, size = letter_size, font = font, halign = "center", valign = "center", $fn = 16);
  }
}

translate([76,12,-3])
rotate([90,0,90])
color("black")
letter("Micro USB-B");

translate([76,-7.5,-7.5])
rotate([90,0,90])
color("black")
letter("BNC macho");

translate([76,-7.5,7.5])
rotate([90,0,90])
color("black")
letter("Panel Solar");