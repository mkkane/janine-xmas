$(function(){
  if ($('body.home').length > 0) {
    
  }

  // Make sure the canvas always takes up the whole window And the
  // body has the right padding to push lower than the (absolutely
  // positioned) navbar
  $(window).resize(function() { 
    set_body_padding();
    set_canvas_dimensions();
  });
  set_body_padding();
  set_canvas_dimensions();

});

var set_canvas_dimensions = function() {
  $('.canvas').css({
    'width': $(window).width(),
    'height': $(window).height()
  });
}

var $body = $('body');
var $navbar = $('.navbar-fixed-top');
var set_body_padding = function() {
  $body.css({
    'padding-top': $navbar.height(),
  });
}