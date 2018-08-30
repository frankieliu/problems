var formsSketch = function( sketch ) {

    sketch.scaleFactor = 1.0;

    sketch.forms = [];
    sketch.formHover = false;

    sketch.paths = [];
    sketch.buffer = null;
    sketch.alphaBuffer = null;

    sketch.osc = null;
    sketch.lfo = null;

    sketch.painting = false;
    sketch.mouseEnabled = true;
    sketch.next = 0;
    sketch.lastPosition = null;

    // Range of midi notes to select on path creation.

    sketch.notes = [60,62,64,65,67,69,71,72,74,76];

    //sketch.notes = [60,64,67,71,72,76,79,83];

    sketch.hoverKeypress = function(e) {
    };

    sketch.normalPauseKeypress = function(e) {
        if (e.which == 32) {
            e.preventDefault();
            if ($video.paused == true) {
                if (main.sketch) {
                    main.sketch.remove();
                }
                $video.play();
                bodyBindKeypress(normalPlayKeypress);
            } else {
                $video.pause();
            }
        } else if (e.which == 105) {
            e.preventDefault();
            console.log("Pause insert");
        }
    };

    sketch.setup = function() {

        // Full-window canvas
        sketch._pixelDensity = 1;
        sketch.masterVolume(.5);
        sketch.createCanvas(1280, 800);
        sketch.container = sketch.canvas.parentElement;

        /*
        sketch.canvas.onkeydown(function(e) {
          console.log(e.code);
        });
        */
        $video.removeAttribute('controls');
        
        sketch.keymap = {};
        sketch.container.addEventListener("keypress", function(e) {
            console.log(e.code);
            if (e.code == "KeyC" && e.ctrlKey) {
                console.log("C-c");
            } else {
                console.log(e.code);
                switch(e.code) {
                case "KeyI":
                    sketch.insertMode = true;
                    console.log("Insert mode");
                    break;
                default:
                    break;
                }
            }
            //            map[e.code] = true;
            //            if (map["Control"]) {
            //                console.log("Control");
            //            }
        });

        sketch.container.addEventListener("keyup", function(e) {
            sketch.keymap = {};
        });


        //sketch.strokeWeight(2);
        sketch.colorMode(sketch.HSB, 100);

        // Off-screen buffer for fading old elements
        //
        sketch.buffer = sketch.createGraphics(sketch.width, sketch.height);
        sketch.buffer.colorMode(sketch.HSB, 100);
        //sketch.buffer.strokeWeight(2);

        sketch.alphaBuffer = sketch.createGraphics(sketch.width, sketch.height);
        sketch.alphaBuffer.noStroke();


        // Current and previous mouse position for force calculations
        //
        sketch.mousePosition = new p5.Vector(0,0);
        sketch.lastPosition = new p5.Vector(0,0);

        // Main oscillator
        //
        sketch.osc = new p5.SinOsc(440);
        sketch.osc.amp(0);

        // LFO to modify main oscillator
        //
        sketch.lfo = new p5.SinOsc(2);
        sketch.lfo.disconnect();
        sketch.lfo.amp(0);
        sketch.osc.amp(sketch.lfo);

        sketch.osc.start();
        sketch.lfo.start();

	if (false) {
	    // Add play button
	    var br = sketch.canvas;
	    console.log(br);
            sketch.playButton = sketch.createDiv("<i class='fas fa-play'></i>");
	    sketch.playButton.addClass("playButton");
	    sketch.playButton.parent(sketch.canvas);
	    sketch.playButton.position(100, 100);
	    sketch.playButton.show();
	}

    };

    sketch.draw = function() {
        sketch.clear();
        // Draw image buffer
        //
        sketch.alphaBuffer.clear();
        sketch.alphaBuffer.elt.getContext('2d').globalAlpha =.95;
        sketch.alphaBuffer.image(sketch.buffer,0,0);
        sketch.image(sketch.alphaBuffer, 0, 0);

        sketch.buffer.clear();
        sketch.buffer.image(sketch.alphaBuffer, 0, 0);

        // sketch.buffer.colorMode(sketch.RGB,100);
        // sketch.buffer.fill(95,95,95,10);
        // sketch.buffer.noStroke();
        // sketch.buffer.rect(0,0,sketch.width,sketch.height);
        // sketch.buffer.colorMode(sketch.HSB,100);
        // sketch.image(sketch.buffer, 0, 0);

        // Add a circle to the current path
        if (sketch.millis() > sketch.next && sketch.painting && sketch.mouseEnabled) {

            // Grab mouse position

            sketch.mousePosition.x = (sketch.mouseX > sketch.touchX) ? sketch.mouseX : sketch.touchX;
            sketch.mousePosition.y = (sketch.mouseY > sketch.touchY) ? sketch.mouseY : sketch.touchY;

            sketch.mousePosition.x /= sketch.scaleFactor;
            sketch.mousePosition.y /= sketch.scaleFactor;

            // New particle's force is based on mouse movement
            var force = p5.Vector.sub(sketch.mousePosition, sketch.lastPosition);
            force.mult(.05);

            // Add new particle
            sketch.paths[sketch.paths.length - 1].add(sketch.mousePosition, force);

            // Schedule next circle
            sketch.next = sketch.millis() + sketch.random(100);

            // Store mouse values
            sketch.lastPosition.x = sketch.mousePosition.x;
            sketch.lastPosition.y = sketch.mousePosition.y;
        }

        // Modify the oscillators while painting
        if (sketch.painting) {

            // Tone frequency is based on mouseX
            // LFO frequency is based on mouseY
            var note = sketch.midiToFreq(sketch.notes[sketch.floor(sketch.map(sketch.mousePosition.x, 0, sketch.width, 0, sketch.notes.length ))]);;
            var mod = sketch.map(sketch.mousePosition.y, 0, sketch.height, 4, 16);

            sketch.osc.freq(note);
            sketch.lfo.freq(mod);
        }

        // Draw all paths
        for( var i = 0; i < sketch.paths.length; i++) sketch.paths[i].display();
    };

    // Mouse/Touch events
    sketch.mousePressed = function() {
        if ((sketch.mouseEnabled) && (!(sketch.formHover))) {
            console.log("touch");
            sketch.startForms_1();
        }
    };

    sketch.mouseReleased = function() {
        if (sketch.mouseEnabled) sketch.stopDrawing();
    };
    
    sketch.touchStartd = function() {
        if (sketch.mouseEnabled) sketch.startDrawing();
    };
    sketch.touchEnded = function() {
        if (sketch.mouseEnabled) sketch.stopDrawing();
    };

    sketch.disableMouse = function() {
        sketch.mouseEnabled = false;
    };

    sketch.enableMouse = function() {
        sketch.mouseEnabled = true;
    };

    sketch.addPoint = function(position, force) {

        sketch.paths[sketch.paths.length - 1].add(position, force);

        sketch.mousePosition.x = position.x;
        sketch.mousePosition.y = position.y;

    };

    // Create a new path and ramp up oscillators

    sketch.startDrawing = function() {
        sketch.next = 0;
        sketch.painting = true;


        sketch.osc.fade(.5,.2);
        sketch.lfo.fade(.5,.2);

        sketch.lastPosition.x = ((sketch.mouseX > sketch.touchX) ? sketch.mouseX : sketch.touchX) - 10;
        sketch.lastPosition.y = ((sketch.mouseY > sketch.touchY) ? sketch.mouseY : sketch.touchY) - 10;

        sketch.lastPosition.x /= sketch.scaleFactor;
        sketch.lastPosition.y /= sketch.scaleFactor;

        sketch.paths.push(new sketch.Paths());
    };

    sketch.showCode = function (text,x,y) {
        sketch.codePanel.html(text);
        sketch.codePanel.position(x,y);
        sketch.codePanel.show();
        return sketch.codePanel;
    };

    sketch.startForms = function() {

        sketch.lastPosition.x = ((sketch.mouseX > sketch.touchX) ? sketch.mouseX : sketch.touchX);
        sketch.lastPosition.y = ((sketch.mouseY > sketch.touchY) ? sketch.mouseY : sketch.touchY);

        sketch.lastPosition.x /= sketch.scaleFactor;
        sketch.lastPosition.y /= sketch.scaleFactor;

        console.log(sketch.lastPosition.x, sketch.lastPosition.y);

        sketch.codePanel = sketch.createDiv("");
        sketch.codePanel.addClass("codePanel");
        sketch.codePanel.elt.setAttribute("contenteditable","true");

        var curidx = sketch.forms.length;
        sketch.codePanel.elt.setAttribute("tabindex", curidx+1);
        sketch.codePanel.elt.id = "codePanel" + curidx;
        sketch.forms.push(sketch.codePanel);
        console.log(sketch.forms.length);

        // Current code panel $cp
        var $cp = $("#codePanel" + curidx);
        // var cp = $cp[0];

        $cp.draggable();

        $cp.focusin(
            function() {
                sketch.inFormFocus = true;
                console.log("+ focus: " + document.activeElement.id);
            });

        $cp.focusout(
            function() {
                sketch.inFormFocus = false;
                console.log("- focus: " + this[0].id);
            });
        $cp[0].addEventListener("keydown", function(e) {
            if (e.ctrlKey) {
                switch (e.code) {
                case "Delete":
                    console.log("C-Delete");
                    break;
                case "Enter":
                    console.log("C-Enter");
                    break;
                case "Insert":
                    console.log("C-Insert");
                    break;
                case "End":
                    console.log("C-End");
                    break;
                case "Home":
                    console.log("C-Home");
                    break;
                case "Esc":
                    console.log("C-Esc");
                    break;
                }
                e.preventDefault();
            }
        });

        $cp.hover(
            function() {
                if ($cp.is(":focus")) {
                    $.noop();
                } else {
                    $cp.focus();
                    document.execCommand('selectAll', false, null);
                }
                console.log("hover:" + this.id);
                sketch.formHover = true;
                sketch.bodyBindKeypress(sketch.hoverKeypress);
            },
            function() {
                console.log("-hover:" + this.id);
                sketch.formHover = false;
                /*
                if ($("#codePanel" + curidx).is(":focus")) {
                    $("#codePanel" + curidx).focus(
                        function() {
                            console.log($(this).id + " is focused.");
                        },
                        function() {

                            console.log(document.activeElement.id + " has focus now.");
                            if (document.activeElement.id.indexOf("codePanel") != -1) {
                                // still in codePanel focus
                                sketch.bodyBindKeypress(sketch.hoverKeypress);
                            } else {
                                sketch.bodyBindKeypress(sketch.normalPauseKeypress);
                            }

                            $(":focus").each(function() {
                                alert(this.id + " has focus!");
                            });
                        });
                } else {
                    sketch.bodyBindKeypress(sketch.normalPauseKeypress);
                }
                */
            });

        /*
        sketch.codePanel.elt.hover(function() {
            console.log("hover");
        });
        */
        /*
        sketch.codePanel.elt.setAttribute("id","true");
        if ($('#element:hover').length != 0) {
            // do something ;)
        }
        */
        // sketch.codePanel.hide();
        sketch.showCode("if (mousePressed()) {<br/>  &emsp;fill(r,g,b); <br/> }",
                        sketch.lastPosition.x,sketch.lastPosition.y);
    };

    sketch.startForms_1 = function() {

        sketch.lastPosition = sketch.getMousePosition();
        console.log(sketch.lastPosition.x, sketch.lastPosition.y);

        // Creating four div's:
        // Container one, icon one, title one, subject one
        sketch.codePanel = {
            icons: sketch.createDiv(""),
            container: sketch.createDiv(""),
            title: sketch.createDiv(""),
            subject: sketch.createDiv("")};

        // Position the container and show it
        sketch.codePanel.container.position(sketch.lastPosition.x, sketch.lastPosition.y);

        // set the group
        var group = sketch.codePanel;
        
        // set the html
        group.icons.html(
            "<i class='mymove fas fa-arrows-alt fa-fw'></i>" +
                "<i class='mydelete far fa-trash-alt fa-fw'></i>" +
                "<i class='myclock far fa-clock'></i>");
        group.title.html("title");
        group.subject.html("subject");
        
        // set the parents
        group.icons.parent(group.container);
        group.title.parent(group.container);
        group.subject.parent(group.container);

        // set the class
        group.container.addClass("codePanel_container");
        group.icons.addClass("codePanel_icons");
        group.title.addClass("codePanel_title");
        group.subject.addClass("codePanel_subject");

        // set contenteditable
        group.title.elt.setAttribute("contenteditable","true");
        group.subject.elt.setAttribute("contenteditable","true");

        // set the index of the element
        var curidx = sketch.forms.length;

        // set the ids
        group.container.elt.id = "codePanel" + curidx;
        group.title.elt.setAttribute("tabindex", curidx + 1);
        group.title.elt.id = "codePanelt" + curidx;

        // add to forms
        sketch.forms.push(sketch.codePanel);
        console.log(sketch.forms.length);

        // Current code panel $cp
        // Alternatively
        // var $cp = $("#codePanel" + curidx);
        var $cp = $(group.container.elt);
        $cp.draggable({handle:".mymove"});
        $cp.hover(function() {
            console.log("hover:" + this.id);
            sketch.bodyBindKeypress(sketch.hoverKeypress);
            sketch.formHover = true;
            var c = $cp.children();                
            console.log(c.length);
            for (var i = 0; i < c.length; i++) {
                console.log(i + " " + c[i]);
                if($(c[i]).is(".codePanel_icons") || $(c[i]).is(".codePanel_subject")) {
                    c[i].style.display = "block";
                }
            }
        }, function() {
            console.log("-hover:" + this.id);
            sketch.formHover = false;
            var c = $cp.children();
            console.log(c.length);
            for (var i = 0; i < c.length; i++) {
                console.log(i + " " + c[i]);
                if($(c[i]).is(".codePanel_icons") || $(c[i]).is(".codePanel_subject")) {
                    c[i].style.display = "none";
                }
            }
        });

        $cp.focusin(
            function() {
                sketch.inFormFocus = true;
                console.log("+focus: " + document.activeElement.id);
            });

        $cp.focusout(
            function() {
                sketch.inFormFocus = false;
                console.log("-focus: " + this.id + "->" + document.activeElement);
            });

        // On title
        var $cpt = $("#codePanelt" + curidx);
        $cpt.hover(
            function() {
                if ($cpt.is(":focus")) {
                    $.noop();
                } else {
                    $cpt.focus();
                    document.execCommand('selectAll', false, null);
                }

            }, function() {
            });
        $cpt[0].addEventListener("keydown", function(e) {
            if (e.ctrlKey) {
                switch (e.code) {
                case "Delete":
                    console.log("C-Delete");
                    e.preventDefault();
                    break;
                case "Enter":
                    console.log("C-Enter");
                    e.preventDefault();
                    break;
                case "Insert":
                    console.log("C-Insert");
                    e.preventDefault();
                    break;
                case "End":
                    console.log("C-End");
                    e.preventDefault();
                    break;
                case "Home":
                    console.log("C-Home");
                    e.preventDefault();
                    break;
                case "Esc":
                    console.log("C-Esc");
                    e.preventDefault();
                    break;
                default:
                    break;
                }
            }
        });

        // Show the codePanel
        sketch.codePanel.container.show();
        sketch.codePanel.icons.show();
        sketch.codePanel.title.show();
        sketch.codePanel.subject.show();
   };

    // Ramp down oscillators
    sketch.stopDrawing = function() {
        sketch.painting = false;
        sketch.osc.fade(0,.4);
        sketch.lfo.fade(0,.4);
    };

    // Class to handle paths of circles
    sketch.Paths = function () {
        this.path = [];
        this.hue = sketch.random() * 100;
    };

    // Make the position a little fuzzy and add a circle
    sketch.Paths.prototype.add = function(position, force) {
        position.x += sketch.random(-5,5);
        position.y += sketch.random(-5,5);
        this.path.push(new sketch.Circle(position, force, this.hue));
    };

    // Draw circles or stamp them to the buffer based on age
    sketch.Paths.prototype.display = function() {

        sketch.stroke( this.hue, 100, 100, 100);
        sketch.fill( this.hue, 100, 100, 50);

        sketch.buffer.stroke( this.hue, 100, 100, 100);
        sketch.buffer.fill( this.hue, 100, 100, 50);

        var i = this.path.length;

        while (i--) {

            var lastCircle = null;
            if (i < this.path.length) lastCircle = this.path[i+1];

            this.path[i].display(lastCircle);

            if (this.path[i].age > 100) {
                this.path[i].stamp(lastCircle);
                this.path.splice(i, 1);
            }
        }

    };

    // Class for individual circles on a path
    sketch.Circle = function (position, force, hue) {
        this.position = new p5.Vector(position.x,position.y);
        this.velocity = new p5.Vector(force.x,force.y);
        this.startMagnitude = this.velocity.mag();
        this.currentMagnitude = this.velocity.mag();
        this.drag = .95;
        this.hue = hue;
        this.age = 0;
    };

    // Draw a circle with size based on current magnitude
    // Draw a line to the previous circle
    sketch.Circle.prototype.display = function(lastCircle) {
        this.position.add(this.velocity);
        this.currentMagnitude = this.velocity.mag();

        var size = sketch.map( this.currentMagnitude, 0, this.startMagnitude, 12, 4);

        //sketch.stroke( this.hue, 100, 100, 100);
        //sketch.fill( this.hue, 100, 100, 50);
        sketch.ellipse(this.position.x,this.position.y, size, size);

        if (lastCircle)
            sketch.line(this.position.x, this.position.y,
                        lastCircle.position.x, lastCircle.position.y);

        this.velocity.mult(this.drag);

        this.age++;
    };

    // Stamp a circle to the buffer so we don't have to track them forever
    sketch.Circle.prototype.stamp = function(lastCircle) {

        //sketch.buffer.stroke( this.hue, 100, 100, 100);
        //sketch.buffer.fill( this.hue, 100, 100, 50);
        sketch.buffer.ellipse(this.position.x,this.position.y, 12, 12);

        if (lastCircle) {
            sketch.buffer.line(this.position.x, this.position.y,
                               lastCircle.position.x, lastCircle.position.y);
        }
    };

    sketch.bodyBindKeypress = function (f) {
        $('body').unbind('clear keypress').bind('click keypress', f);
    };

    /*
    sketch.keyPressed = function() {
        switch(sketch.keyCode) {
        case sketch.CONTROL:
            console.log("Control");
            console.log(sketch.key);
            break;
        };
    };
    */

    sketch.getMousePosition = function() {
        var canvas = sketch.canvas;
        var rect = canvas.getBoundingClientRect();
        var scaleX = canvas.width / rect.width;   // rel bitmap vs. element for X
        var scaleY = canvas.height / rect.height; // rel bitmap vs. element for Y

        sketch.boundingRect = rect;
        sketch.scaleX = scaleX;
        sketch.scaleY = scaleY;
        var mouseX = ((sketch.mouseX > sketch.touchX) ? sketch.mouseX : sketch.touchX);
        var mouseY = ((sketch.mouseY > sketch.touchY) ? sketch.mouseY : sketch.touchY);
        return {
            x: (mouseX - rect.left) * scaleX,    // scale mouse coordinates after they have
            y: (mouseY - rect.top) * scaleY      // been adjusted to be relative to element
        };
    };

    return sketch;
};
