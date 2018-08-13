var main = {};

$(function () {
    main.sketch = new p5(divTest, "main");
});

var canv1, input, abutton, greeting, div0, div1, div2, div3;

function divTest(sketch) {

    sketch.setup = function() {
        console.log("Entering setup");

        // create canvas
        canv1 = sketch.createCanvas(710, 400);

        div0 = sketch.createDiv(
            "<i class='mymove fas fa-arrows-alt fa-fw'></i>" +
                "<i class='mydelete far fa-trash-alt fa-fw'></i>");

        div1 = sketch.createDiv("Div1");
        div2 = sketch.createDiv("Div2");
        div3 = sketch.createDiv("");
        div0.parent(div3);
        div1.parent(div3);
        div2.parent(div3);
        div3.position(20,200);
        div1.elt.setAttribute("contenteditable",true);
        div2.elt.setAttribute("contenteditable",true);
        div0.elt.style.display = "none";
        div2.elt.style.display = "none";
        div3.elt.id = 'div3';

        var $div3 = $('#div3');
        $div3.draggable({handle:".mymove"});

        $(".mydelete")[0].addEventListener("click", function(e){
            console.log("Clicked on delete");
            console.log(this.parentElement.parentElement.remove());
        });
        
        //div2.elt.setAttribute("hidden",true);

        div3.elt.addEventListener("mouseenter", function(e) {
            console.log("mouseover div1");
            div2.elt.style.display = "block";
            div0.elt.style.display = "block";
            //  div2.elt.setAttribute("hidden",false);
        });

        div3.elt.addEventListener("mouseleave", function(e) {
            console.log("mouseover div1");
            div2.elt.style.display = "none";
            div0.elt.style.display = "none";
            //  div2.elt.setAttribute("hidden",false);
        });

        input = sketch.createInput();
        input.position(20, 65);

        abutton = sketch.createButton('submit');
        abutton.position(input.x + input.width, 65);
        abutton.mousePressed(sketch.greet);
        
        greeting = sketch.createElement('h2', 'what is your name?');
        greeting.position(20, 5);

        sketch.textAlign(sketch.CENTER);
        sketch.textSize(50);
    };

    sketch.greet = function() {
        var name = input.value();
        greeting.html('hello '+name+'!');
        input.value('');

        for (var i=0; i<200; i++) {
            push();
            fill(random(255), 255, 255);
            translate(random(width), random(height));
            rotate(random(2*PI));
            text(name, 0, 0);
            pop();
        }
    };

    return sketch;
}
