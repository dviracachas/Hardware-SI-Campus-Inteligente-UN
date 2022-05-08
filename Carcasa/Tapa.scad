difference(){
minkowski(){
cube([153,173,5], center=true);
//sphere(105, $fn=100);
sphere(2);
}

translate([0,0,-3])
minkowski(){
cube([150,170,3], center=true);
//sphere(105, $fn=100);
sphere(2);
}

translate([67,78,0])
cylinder(h=20, r=6);

minkowski(){
translate([-67,-78,0])
cube([33.5,34,50]);
sphere(0.5);
}


translate([15,-78,0])
cube([3,1.4,50]);

translate([20,-78,0])
cube([3,1.4,50]);

translate([25,-78,0])
cube([3,1.4,50]);
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

translate([16.5,-80,3.5])
color("black")
letter("Bic");

translate([21.5,-80,3.5])
color("black")
letter("Com");

translate([26.5,-80,3.5])
color("black")
letter("Bib");

letter_size_1 = 7;
letter_height_1 = 1;

module letter_1(l) {
  // Use linear_extrude() to make the letters 3D objects as they
  // are only 2D shapes when only using text()
  linear_extrude(height = letter_height_1) {
    text(l, size = letter_size_1, font = font, halign = "center", valign = "center", $fn = 16);
  }
}

translate([-50,78,3.5])
color("black")
letter_1("Sistema de");

translate([-50,70,3.5])
color("black")
letter_1("información");

translate([-50,62,3.5])
color("black")
letter_1("un");