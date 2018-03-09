export default class Game {
    create() {
	this.add.sprite(0,0,"game_bg");
	this.clouds = this.add.group();
	this.score = 0;
	var style = { font: "24px Arial", fill: "#FFFFFF" };
	this.txtScore = this.add.text(10,10,this.score.toString(), style);
    }
    update() {
	if(Math.random() < 0.01) {
	    var cloud = this.clouds.getFirstDead();
	    if(cloud) {
		cloud.x = Math.random() * this.game.width;
		cloud.y = Math.random() * this.game.height;
		cloud.revive();
	    } else {
		var cloud = this.clouds.create(
		    Math.random() * this.game.width,
		    Math.random() * this.game.height,
		    "cloud");
		cloud.inputEnabled = true;
		cloud.events.onInputDown.add(this.onCloudClick, this);
	    }
	    cloud.alpha = 0;
	    this.add.tween(cloud).to({ y: "-50", alpha: 1 },
				     800,
				     Phaser.Eating.Cubic.Out, true);
	}
    }
    onCloudClick(cloud) {
	cloud.kill();
	this.score++;
	this.textScore.setText(this.score.toString());
    }
}
