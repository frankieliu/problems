// http://ronallo.com/demos/webvtt-cue-settings/
// From ronallo.com/demons/webvtt-cue-settings/webbtt-cue-settings.js
var video = document.querySelector('video');
var track_elem = document.querySelector('track');

track_elem.addEventListener('loaded',initialize_test,false); // Bug in FF31 MAC: wrong event name
track_elem.addEventListener('load',initialize_test,false);

function create_sample_cue(cue){
    var vtt_cue;
    var timestamps = "00:00.000 --> 00:33.000";
    var settings = " line:" + cue.line;
    settings += " position:" + cue.position + "%";
    settings += " align:" + cue.align;
    settings += " size:" + cue.size + "%";
    if (cue.vertical != "") {
      settings += " vertical:" + cue.vertical;
    }
    var timing = timestamps + settings;
    vtt_cue = timing + "\n" + cue.text;
    $('#sample_cue').html(vtt_cue);
  }

function initialize_test(){
  var track = video.textTracks[0];
  var cue = track.cues[0];

  // Set some of these values initially
  cue.line = 13;
  cue.position = 50;
  cue.align = 'middle';
  cue.size = 100;
  cue.vertical = '';

  $('form#caption-change-form textarea#input-change-caption').on('keyup', function(e){
    cue.text = $(this).val();
    create_sample_cue(cue);
  });
  $('form#caption-change-form input#input-change-line').on('change input', function(e){
    var line = $(this).val();
    cue.line = parseInt(line);
    $('#line-setting')[0].value = line;
    create_sample_cue(cue);
  });
  $('form#caption-change-form input#input-change-position').on('change input', function(e){
    var position = $(this).val();
    cue.position = parseInt(position);
    $('#position-setting')[0].value = position;
    create_sample_cue(cue);
  });
  $('form#caption-change-form .align-radio input').on('change input', function(e){
    cue.align = $(this).val();
    create_sample_cue(cue);
  });
  $('form#caption-change-form input#input-change-size').on('change input', function(e){
    var size = $(this).val();
    cue.size = parseInt(size);
    $('#size-setting')[0].value = size;
    create_sample_cue(cue);
  });
  $('form#caption-change-form .vertical-radio input').on('change input', function(e){
    cue.vertical = $(this).val();
    create_sample_cue(cue);
  });
  $('form#style-change-form textarea').on('keyup', function(){
    $('#extra-textarea-styles').html('::cue{' + $(this).val() + '}');
    create_sample_cue(cue);
  });

  create_sample_cue(cue);

}

video.pause();
setTimeout(function(){
  video.play();
  // initialize_test();
}, 2000);
