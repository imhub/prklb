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
