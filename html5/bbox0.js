function bbox(canvasId) {

    this.canvas = document.getElementById(canvasId),
    this.ctx = this.canvas.getContext('2d'),
    this.rect = {
        x: 150,
        y: 100,
        w: 123,
        h: 58
    },
    this.handlesSize = 8,
    this.currentHandle = false,
    this.drag = false;
    
    this.init = function() {
        this.canvas.addEventListener('mousedown', this, false);
        this.canvas.addEventListener('mouseup', this, false);
        this.canvas.addEventListener('mousemove', this, false);
    };

    this.handleEvent = function(e) {
        switch(e.type) {
        case 'mousedown':
            this.mouseDown(e);
            break;
        case 'mouseup':
            this.mouseUp();
            break;
        case 'mousemove':
            this.mouseMove(e);
            break;
        }
    };
    
    this.point = function(x, y) {
        return {
            x: x,
            y: y
        };
    };

    this.dist = function (p1, p2) {
        return Math.sqrt((p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y));
    };

    this.getHandle = function (mouse) {
        let m = mouse,
            x0 = this.rect.x,
            y0 = this.rect.y,
            x1 = this.rect.w + this.rect.x,
            y1 = this.rect.h + this.rect.y,
            x2 = this.rect.w / 2 + this.rect.x,
            y2 = this.rect.h / 2 + this.rect.y,
            tl = this.point(x0, y0),
            tr = this.point(x1, y0),
            bl = this.point(x0, y1),
            br = this.point(x1, y1),
            t = this.point(x2, y0),
            l = this.point(x0, y2),
            b = this.point(x2, y1),
            r = this.point(x1, y2),
            mid = this.point(x2, y2),
            d = this.dist,
            hs = this.handlesSize;
        if (d(m, tl) <= hs) return 'topleft';
        if (d(m, tr) <= hs) return 'topright';
        if (d(m, bl) <= hs) return 'bottomleft';
        if (d(m, br) <= hs) return 'bottomright';
        if (d(m, t) <= hs) return 'top';
        if (d(m, l) <= hs) return 'left';
        if (d(m, b) <= hs) return 'bottom';
        if (d(m, r) <= hs) return 'right';
        if (d(m, mid) <= hs) return 'middle';
        return false;
    };

    this.mouseDown = function (e) {
        if (!this.drag) {
            var mousePos = this.point(
                e.pageX - this.canvas.offsetLeft,
                e.pageY - this.canvas.offsetTop);
            console.log(e.clientX, e.pageX, this.canvas.offsetLeft);
            this.currentHandle = this.getHandle(mousePos);
        }
        if (this.currentHandle) {
            this.drag = true;
            this.draw();
        }
    };

    this.mouseUp = function () {
        this.drag = false;
        this.currentHandle = false;
        this.draw();
    };
    
    this.mouseMove = function (e) {
        var previousHandle = this.currentHandle;
        if (this.currentHandle && this.drag) {
            var mousePos = this.point(
                e.pageX - this.canvas.offsetLeft,
                e.pageY - this.canvas.offsetTop);
            switch (this.currentHandle) {
            case 'topleft':
                this.rect.w += this.rect.x - mousePos.x;
                this.rect.h += this.rect.y - mousePos.y;
                this.rect.x = mousePos.x;
                this.rect.y = mousePos.y;
                break;
            case 'topright':
                this.rect.w = mousePos.x - this.rect.x;
                this.rect.h += this.rect.y - mousePos.y;
                this.rect.y = mousePos.y;
                break;
            case 'bottomleft':
                this.rect.w += this.rect.x - mousePos.x;
                this.rect.x = mousePos.x;
                this.rect.h = mousePos.y - this.rect.y;
                break;
            case 'bottomright':
                this.rect.w = mousePos.x - this.rect.x;
                this.rect.h = mousePos.y - this.rect.y;
                break;
                
            case 'top':
                this.rect.h += this.rect.y - mousePos.y;
                this.rect.y = mousePos.y;
                break;
                
            case 'left':
                this.rect.w += this.rect.x - mousePos.x;
                this.rect.x = mousePos.x;
                break;

            case 'bottom':
                this.rect.h = mousePos.y - this.rect.y;
                break;

            case 'right':
                this.rect.w = mousePos.x - this.rect.x;
                break;

            case 'middle':
                this.rect.x = mousePos.x - this.rect.w / 2;
                this.rect.y = mousePos.y - this.rect.h / 2;
                break;
            }


            
        }
        
        if (this.drag || this.currentHandle != previousHandle)
            this.draw();
        
    };

    this.draw = function() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        // ctx.fillStyle = 'black';
        // ctx.fillRect(rect.x, rect.y, rect.w, rect.h);
        this.ctx.setLineDash([6,6]);
        this.ctx.strokeStyle = "rgba(255,255,255,0.7)";
        this.ctx.lineWidth = 3;
        this.ctx.strokeRect(this.rect.x, this.rect.y, this.rect.w, this.rect.h);

        if (this.currentHandle) {
            var posHandle = this.point(0, 0);
            switch (this.currentHandle) {
            case 'topleft':
                posHandle.x = this.rect.x;
                posHandle.y = this.rect.y;
                break;
            case 'topright':
                posHandle.x = this.rect.x + this.rect.w;
                posHandle.y = this.rect.y;
                break;
            case 'bottomleft':
                posHandle.x = this.rect.x;
                posHandle.y = this.rect.y + this.rect.h;
                break;
            case 'bottomright':
                posHandle.x = this.rect.x + this.rect.w;
                posHandle.y = this.rect.y + this.rect.h;
                break;
            case 'top':
                posHandle.x = this.rect.x + this.rect.w / 2;
                posHandle.y = this.rect.y;
                break;
            case 'left':
                posHandle.x = this.rect.x;
                posHandle.y = this.rect.y + this.rect.h / 2;
                break;
            case 'bottom':
                posHandle.x = this.rect.x + this.rect.w / 2;
                posHandle.y = this.rect.y + this.rect.h;
                break;
            case 'right':
                posHandle.x = this.rect.x + this.rect.w;
                posHandle.y = this.rect.y + this.rect.h / 2;
                break;
            case 'middle':
                posHandle.x = this.rect.x + this.rect.w / 2;
                posHandle.y = this.rect.y + this.rect.h / 2;
                break;
            }
            this.ctx.globalCompositeOperation = 'xor';
            this.ctx.beginPath();
            this.ctx.arc(posHandle.x, posHandle.y, this.handlesSize, 0, 2 * Math.PI);
            this.ctx.fill();
            this.ctx.globalCompositeOperation = 'source-over';
        }
    };

    // init();
    // draw();
}
