
  $("#topContainer").css("min-height",$(window).height());
  $("#newsContainer").css("min-height",$(window).height());
  $("#bottomContainer").css("min-height",$(window).height());

  function message(msg, tag)
  	{
    		document.getElementById(tag).innerHTML = msg;
	}
