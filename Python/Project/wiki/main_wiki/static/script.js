$(window).scroll(function() {
	var element = $('.onLook');
	var elementTop = element.offset().top;
	var elementBottom = element.offset().top + element.height();
	var w_height = $(window).height();
	if (($(window).scrollTop() < elementTop - w_height) || ($(window).scrollTop() > elementBottom))
	{

	}
	else
	{
		$('.onLook').attr()
	}
})