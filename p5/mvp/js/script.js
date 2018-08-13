import {popCode} from 'popCode';

var script = {

    popcorn: null,

    init: function() {

        var pop = Popcorn.smart("#videoClip", ["assets/video.webm","assets/video.mp4"]);
        pop.video.setAttribute("controls","controls");

        /*
          $("#welcome").fadeOut();
          $("#videoCanvas").fadeIn(); 
          $("#p5").fadeIn(); 
          $("#pause").fadeIn();
          pop.play(0);
        */
        
        pop.autoplay(false);      

        if (true) {

            pop.on( "canplayall", function(e) {
                // This is necessary to create the clipping effect
                main.prepareVideo();
                // $("#begin").button('reset');
            });  

            pop.on( "play", function(e) {
                $("#pauseButton").addClass("fa-pause");
                $("#pauseButton").removeClass("fa-play"); 
            });

            pop.on( "pause", function(e) {
                $("#pauseButton").removeClass("fa-pause");
                $("#pauseButton").addClass("fa-play"); 
            });   

            pop.on("timeupdate", function(e) {
                var position = pop.currentTime() / pop.duration();
                var width = position * $("#main").width();
                $("#progress").css('width', width);
            });

            // Set external

            script.popcorn = pop;

        } // true
        
        let lpopCode = popCode();

    } // init

}
