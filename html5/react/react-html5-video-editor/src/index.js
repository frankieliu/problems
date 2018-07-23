import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import {RdxVideo, Overlay, Controls} from 'react-html5-video-editor';

// ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();

ReactDOM.render(
    <RdxVideo autoPlay loop muted poster="src/img/poster.png">
      <Overlay />
      <Controls />
      <source src="src/video/small.mp4" type="video/mp4" />
    </RdxVideo>,
    document.getElementById('root')
);

RdxVideo.Props = {
    autoPlay: false,
    loop: false,
    controls: true,
    volume:	1.0,
    preload: "auto",
    cropEnabled: true
};

