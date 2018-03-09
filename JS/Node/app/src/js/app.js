// import SecondScript from "./Second.js";
// this is a test hope this works  asdf

// var game;

// import Boot from "./states/Boot.js";
// import p from "./states/test.js";
// import Game from "./states/Game.js";

// window.onload = function() {
    // game = new Phaser.Game(800, 600, Phaser.AUTO, 'game');
    // game.state.add('boot', Boot);
    // game.state.add('preload', p);
    // game.state.add('game', Game);
    // game.state.start('boot');
// };

// import Ellipse from "./states/ellipse.js";

var config = {
    width: 800,
    height: 600,
    type: Phaser.AUTO,
    parent: 'phaser-example'
    /*
    ,
    scene: {
        create: create
    }
*/
};

console.log('hello');

import Ellipse from './states/Ellipse.js';

var game = new Phaser.Game(config);
game.scene.add('boot', Ellipse);
game.scene.start('boot');
/*
export default function create ()
{
    //  Our ellipse is centered at 400x300 and is 600px wide by 300px tall
    var ellipse = new Phaser.Geom.Ellipse(400, 300, 600, 300);

    var graphics = this.add.graphics({ lineStyle: { width: 2, color: 0x00ff00 } });

    graphics.strokeEllipseShape(ellipse, 64);

    this.input.on('pointermove', function (pointer) {
    
        ellipse.width = Math.abs(pointer.x - ellipse.x) * 2;
        ellipse.height = Math.abs(pointer.y - ellipse.y) * 2;

        graphics.clear();
        graphics.strokeEllipseShape(ellipse, 64);
    
    });
}

*/
