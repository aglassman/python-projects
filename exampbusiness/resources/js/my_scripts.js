function ajaxFadeInOut(onhover,selector,url)
{
	loaded = 0;
	$(onhover).hover(
		function(){
			
			if(loaded == 0)
			{
				loaded = -1;
				$(selector).load(url,function(){$(selector).fadeIn(1000);loaded = 1;});
			}
			if(loaded == 1)
			{
				$(selector).stop(true,true);
				$(selector).fadeIn(1000);
			}
		}
		,function(){
			if(loaded == 1)
			{
				$(selector).stop(true,true);
				$(selector).fadeOut(1000);
			}
	});
}