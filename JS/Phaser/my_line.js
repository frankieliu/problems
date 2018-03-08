var config = {
    width: 800,
    height: 600,
    type: Phaser.AUTO,
    parent: 'phaser-example',
    scene: {
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);
var graphics;
var line;
var text;

function create ()
{
    graphics = this.add.graphics({ lineStyle: { width: 4, color: 0xaa00aa } });

    line = new Phaser.Geom.Line(300, 300, 400, 300);

    text = this.add.text(100, 50, '');

    this.input.on('pointermove', function(pointer) {

        Phaser.Geom.Line.CenterOn(line, pointer.x, pointer.y);

    });

    var headings = ['1','2','3','4'];
    var headings_style = { font: "16x Courier", fill:"#fff", tabs: [20,20,20] };
    text_headings = this.add.text(32, 64, '', headings_style);
    text_headings.parseList(headings);

}

function update ()
{
    Phaser.Geom.Line.Rotate(line, 0.02);

    graphics.clear();

    graphics.strokeLineShape(line);

    var angle = Phaser.Geom.Line.Angle(line);

    text.setText('Line Angle: ' + Phaser.Math.RadToDeg(angle));
}
