/// <autosync enabled="true" />
/// <reference path="../p5.global-mode.d.ts" />

var myCanvas;
var myimg;

function drawCat(img0) {
    image(img0, 0, 0);
}

function setup() { 
  myCanvas = createCanvas(640, 480);
  myCanvas.parent('container');
  drawingContext.shadowOffsetX = 5;
  drawingContext.shadowOffsetY = -5;
  drawingContext.shadowBlur = 10;
  drawingContext.shadowColor = "black";
  background(200);
  ellipse(width/2, height/2, 50, 50);
  myimg = loadImage('cat.jpg', drawCat);
} 

var x = 0;
function draw() { 
  // background(220);
  console.log(typeof myimg);
  drawCat(myimg);
  if (mouseIsPressed) {
    fill(0);
  } else {
    fill(255);
  }
  ellipse(mouseX, mouseY, 80, 80);
  line(x, 0, width/2, height/2);
  x = x + 1
  if (x > width) x = 0;
}