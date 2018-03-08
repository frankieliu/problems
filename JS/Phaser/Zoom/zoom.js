/// TODO: When mouse is going out of canvas, you need to click into canvas to get game react again

var game = new Phaser.Game(800, 600, Phaser.CANVAS, 'phaser-example', {
    preload: preload,
    create: create,
    update: update,
    render: render
});

var enemies, buildings, environment, worldStage, ui;
var enemyBullets, towerBullets;
var gameBounds = {
    x1: 0,
    y1: 0,
    x2: 2560,
    y2: 1280
}

    function preload() {
        game.load.image('backdrop', 'http://wakeskaterstudio.com/images/bkg_Space.png');
        game.load.image('test', 'http://png-3.findicons.com/files/icons/1588/farm_fresh_web/32/box.png');
    }

    function create() {
        game.world.setBounds(gameBounds.x1, gameBounds.y1, gameBounds.x2, gameBounds.y2);

        setupGroups();
        setupGUI();

        if (CAMERA) {
            game.input.mouse.mouseWheelCallback = function (event) {
                CAMERA.zoom_mousewheel.call(CAMERA, game.input.mouse);
            };
        }


        environment.add(game.add.sprite(0, 0, 'backdrop'));
        enemies.add(game.add.sprite(300, 300, 'test'));
        enemies.add(game.add.sprite(1000, 900, 'test'));
    }

    function update() {
        //Check for our Camera Functions
        if (CAMERA) {
            CAMERA.drag_camera(game.input.mousePointer);
            CAMERA.drag_camera(game.input.pointer1);
            CAMERA.update_camera();
        }
    }

    function render() {
        game.debug.text('Camera Velocity X: ' + CAMERA.velX, 32, 24 * 1, '#FFF');
        game.debug.text('Camera Velocity Y: ' + CAMERA.velY, 32, 24 * 2, '#FFF');
        game.debug.text('Camera Left X: ' + game.camera.x, 256, 24 * 1, '#FFF');
        game.debug.text('Camera Top  Y: ' + game.camera.y, 256, 24 * 2, '#FFF');
        game.debug.text('Camera Width:  ' + game.camera.screenView.width, 480, 24 * 1, '#FFF');
        game.debug.text('Camera Height: ' + game.camera.screenView.height, 480, 24 * 2, '#FFF');
        game.debug.text('Camera Focus X: ' + (game.camera.position.x), 700, 24 * 1, '#FFF');
        game.debug.text('Camera Focus Y: ' + (game.camera.position.y), 700, 24 * 2, '#FFF');
        game.debug.text('World State Scale: ' + worldState.scale, 32, 24 * 3, '#FFF');
        game.debug.text('Mouse X: ' + game.input.mousePointer.worldX, 32, 24 * 4, '#FFF');
        game.debug.text('Mouse Y: ' + game.input.mousePointer.worldY, 32, 24 * 5, '#FFF');
        game.debug.text('Mouse Position Vector from Center: {X: ' + (game.input.mousePointer.worldX - game.camera.position.x) + ',Y: ' + (game.input.mousePointer.worldY - game.camera.position.y) + '}', 32, 24 * 6, '#FFF');
    }

    function setupGroups() {
        worldState = game.add.group();
        enemies = game.add.group();
        buildings = game.add.group();
        environment = game.add.group();
        enemyBullets = game.add.group();
        towerBullets = game.add.group();
        ui = game.add.group();

        //Add all our groups to the world group
        worldState.add(environment);
        worldState.add(enemies);
        worldState.add(buildings);

        //Add our weaponry to the appropriate groups
        enemies.add(enemyBullets);
        buildings.add(towerBullets);

        //Set our UI so that it stays fixed ot the camera
        ui.fixedToCamera = true;
    }

    function setupGUI() {}



    //CAMERA.JS

var CAMERA = CAMERA || {};
var o_camera = o_camera || null;

CAMERA.settings = {
    drag: 6,
    accel: 3,
    maxSpeed: 80,
    zoomMax: 1,
    zoomMin: .5,
    zoomStep: .1
};

//Drag Variables
CAMERA.velX = 0;
CAMERA.velY = 0;

//Zoom Variables
CAMERA.zoomed = false;
CAMERA.cameraPosition = new Phaser.Point(0, 0);
CAMERA.zoompoint = new Phaser.Point(0, 0);

CAMERA.pinchCenterX;
CAMERA.pinchCenterY;

CAMERA.update_camera = function () {
    this.velX = Phaser.Math.clamp(this.velX, -this.settings.maxSpeed, this.settings.maxSpeed);
    this.velY = Phaser.Math.clamp(this.velY, -this.settings.maxSpeed, this.settings.maxSpeed);

    game.camera.x += this.velX;
    game.camera.y += this.velY;

    //Set Camera Velocity X Drag
    if (this.velX > this.settings.drag) {
        this.velX -= this.settings.drag;
    } else if (this.velX < -this.settings.drag) {
        this.velX += this.settings.drag;
    } else {
        this.velX = 0;
    }

    //Set Camera Velocity Y Drag
    if (this.velY > this.settings.drag) {
        this.velY -= this.settings.drag;
    } else if (this.velY < -this.settings.drag) {
        this.velY += this.settings.drag;
    } else {
        this.velY = 0;
    }
};

CAMERA.drag_camera = function (o_pointer) {
    if (!o_pointer.timeDown) {
        return;
    }
    if (o_pointer.isDown && !o_pointer.targetObject) {
        if (o_camera) {
            this.velX = (o_camera.x - o_pointer.position.x) * this.settings.accel;
            this.velY = (o_camera.y - o_pointer.position.y) * this.settings.accel;
        }
        o_camera = o_pointer.position.clone();
    }

    if (o_pointer.isUp) {
        o_camera = null;
    }
};

CAMERA.zoom_pinch = function (event) {
    var scale = event.gesture.scale;

    worldState.scale.set(scale);
    game.camera.focusOnXY(event.center.x, event.center.y);

    worldState.scale.x = Phaser.Math.clamp(worldState.scale.x, this.settings.zoomMin, this.settings.zoomMax);
    worldState.scale.y = Phaser.Math.clamp(worldState.scale.y, this.settings.zoomMin, this.settings.zoomMax);

    game.world.setBounds(gameBounds.x1 * worldState.scale.x, gameBounds.y1 * worldState.scale.y, gameBounds.x2 * worldState.scale.x, gameBounds.y2 * worldState.scale.y);
};

CAMERA.zoom_mousewheel = function (o_pointer) {

    var prevScale = {};
    var nextScale = {};
    prevScale.x = worldState.scale.x;
    prevScale.y = worldState.scale.y;

    console.log('PrevScale: ' + prevScale.x + ',' + prevScale.y);

    var wheelDelt = o_pointer.wheelDelta;
    var delt = Math.max(-1, Math.min(1, (wheelDelt)));

    worldState.scale.x += delt * this.settings.zoomStep;
    worldState.scale.y += delt * this.settings.zoomStep;

    worldState.scale.x = Phaser.Math.clamp(worldState.scale.x, this.settings.zoomMin, this.settings.zoomMax);
    worldState.scale.y = Phaser.Math.clamp(worldState.scale.y, this.settings.zoomMin, this.settings.zoomMax);

    nextScale.x = worldState.scale.x;
    nextScale.y = worldState.scale.y;
    
    var xAdjust = (game.input.mousePointer.worldX - game.camera.position.x) * (nextScale.x - prevScale.x);
    var yAdjust = (game.input.mousePointer.worldY - game.camera.position.y) * (nextScale.y - prevScale.y);

    //Only move screen if we're not the same scale
    if (prevScale.x != nextScale.x || prevScale.y != nextScale.y) {
        var scaleAdjustX = nextScale.x / prevScale.x;
        var scaleAdjustY = nextScale.y / prevScale.y;
        var focusX = (game.camera.position.x * scaleAdjustX) + xAdjust;
        var focusY = (game.camera.position.y * scaleAdjustY) + yAdjust;
        game.camera.focusOnXY(focusX, focusY);
    }

    game.world.setBounds(gameBounds.x1 * worldState.scale.x, gameBounds.y1 * worldState.scale.y, gameBounds.x2 * worldState.scale.x, gameBounds.y2 * worldState.scale.y);
};
