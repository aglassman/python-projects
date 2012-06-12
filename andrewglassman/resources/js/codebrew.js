function BoxWidget (topOffset,leftOffset,headerSize,menuParams){
	var boxColors = ["blue","yellow","orange","green","red","pink"];

	for (menuParameterMap in menuParams.menu)
	{
		$("#boxWidget").append("<div></div>");
	}
	var boxindex = 0;
	var leftPos = leftOffset+headerSize;

	var topPos=topOffset;
	$("#boxWidget div").addClass("box");
	$("#boxWidget div").each(function(index,element) {
		$(element).addClass(boxColors[index%boxColors.length]);
		$(element).attr("style","top: "+topPos+"px; left:"+leftPos+"px;");
		new Box(element,leftPos,topPos,menuParams.menu[index]);
		topPos+=20;
	});

	$("#boxWidget").prepend("<div id=\"header\"><h1 class=\"top\">ANDREW--</h1><h1 class=\"bottom\">GLASSMAN</h1></div>");
	$("#header").attr("style","width:"+headerSize+"px;left:"+leftOffset+"px ; top:"+topOffset+"px ;");

	function Box (boxObj,leftPos,topPos,menuParams){
				this.boxObj = boxObj;
				this.boxObj._index = 0;
				this.boxObj._leftPos = leftPos;
				this.boxObj._topPos = topPos;
				this.boxObj._state = 0;
				this.boxObj._url = menuParams.url;
				this.boxObj._shortName = menuParams.shortName;
				this.boxObj._longName = menuParams.longName;
				this.boxObj._directLink = menuParams.directLink;
				this.boxObj._animation = menuParams.animation;

				$(this.boxObj).html("<p>"+this.boxObj._shortName+"</p>");

				$(this.boxObj).hover(
				  function () {
				  	if (this._state == 0)
				  	{
				  		this._index = boxindex++;
				  		$(this).css('z-index',this._index);
				  		
				  		$(this).stop();
				  		$(this).animate({ 
						           width:"100px"
						    }, 200,"easeOutSine",function(){
						    	if(this._directLink == true)
						    	{	
						    		$(this).html("<p><a href=\""+this._url+"\">"+this._longName+"</a></p>");
						    	}
						    	else
						    	{	
						    		$(this).html("<p>"+this._longName+"</p>");
						    	}
						    });
					}
				  }, 
				  function () {
				  	if (this._state == 0)
				  	{
				  		$(this).stop();
				  		$(this).animate({ 
						           width:"20px"
						    }, 200,"easeInSine",function(){
						    	$(this).html("<p>"+this._shortName+"</p>");
						    });
					}
				  }
				);

				if(this.boxObj._directLink == false)
				{
					$(this.boxObj).click(GetAnimation(this.boxObj));
				} 		
			}

		function GetAnimation(currentBox)
		{
			//move box, then expand.
			if(currentBox._animation == 1)
			{
				return function(){
					var currentBox = this
					if(currentBox._state == 0)
					{
						currentBox._state = 1;
						currentBox._index = boxindex++;
						$(currentBox).css('z-index',currentBox._index);
					    $(this).animate({ 
					           left: (currentBox._leftPos + 100) + "px",
					           top: "160px"
					    }, 500,"easeOutSine").animate({
					    	opacity:0.25,
					    },100).animate({
					    	opacity:1.0,
					    },100).animate({
					    	opacity:0.25,
					    },100).animate({
					    	opacity:1.0,
					    },100).animate({ 
					           width: "400px",
					           height: "250px"
					    }, 500,"easeOutSine",function(){
						    	$.get(currentBox._url, function(data) {
							 	$(currentBox).html("<p>"+data+"</p>");
							});
						});
					}
					else if (currentBox._state == 1)
					{
						$(currentBox).html("<p>"+currentBox._shortName+"</p>");
					    $(this).animate({ 
					           width: "20px",
					           height: "20px"
					    }, 500,"easeOutSine").animate({ 
					           top: currentBox._topPos + "px",
					           left: currentBox._leftPos + "px"
					    }, 500,"easeOutSine",function(){currentBox._state = 0;});
					    
					}

				}
			}
			//Lengthen box, then increase width.
			else if(currentBox._animation == 2)
			{
				return function(){
					var currentBox = this
					if(currentBox._state == 0)
					{
						currentBox._state = 1;
						currentBox._index = boxindex++;
						$(currentBox).css('z-index',currentBox._index);
					    $(this).animate({
					    	   left: currentBox._leftPos + 20 + "px", 
					           width: 400 + "px",
					    }, 400,"easeOutSine").animate({ 
					           height: "250px"
					    }, 500,"easeOutSine",function(){
						    	$.get(currentBox._url, function(data) {
							 	$(currentBox).html("<p>"+data+"</p>");
							});
						});
					}
					else if (currentBox._state == 1)
					{
						$(currentBox).html("<p>"+currentBox._shortName+"</p>");
					    $(this).animate({ 
					           width: "20px",
					           height: "20px"
					    }, 500,"easeOutSine").animate({
					    	   left: currentBox._leftPos + "px",
					    	},200,"easeOutSine",function(){currentBox._state = 0;
					    });
					    
					}

				}
			}
		}
}