$("#topContainer").css("min-height",$(window).height());
$("#newsContainer").css("min-height",$(window).height());
$("#bottomContainer").css("min-height",$(window).height());

function message(msg, tag) {
  		document.getElementById(tag).innerHTML = msg;
    }

function initDateFields() {
      $('input.dateinput').datetimepicker({
        'format': 'YYYY-MM-DD'
      }).on('dp.hide', function(event){
        $(this).blur();
      });
    }

$(document).ready(function(){
      initDateFields();
});

var movementStrength = 5;

var height = movementStrength / $(window).height();
var width = movementStrength / $(window).width();

$("html").mousemove(function(e){

		  var pageX = e.pageX - ($(window).width() / 2);
		  var pageY = e.pageY - ($(window).height() / 2);

		  var newvalueX = width * pageX * -1;
		  var newvalueY = height * pageY * -1;

		  $('body').css("background-position", (50+newvalueX)+"% "+(50+newvalueY)+"%");
});
