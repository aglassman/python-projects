function FunNav(navItems)
{
	this.navItemArr = [];
	var spacing = 800/(navItems.items.length+1);
	var ref = this;
	for(var index = 0; index < navItems.items.length; index++)
	{
		this.navItemArr.push(
			new NavItem( 
				((index+1)*spacing)-50 ,
		 		20 ,
		 		100,
		 		25,
		 		navItems.items[index].name)
				);
	}

	this.draw = function(ctx)
	{
		for(var index = 0; index < ref.navItemArr.length; index++)
		{
			ref.navItemArr[index].draw(ctx);
		}
	};
}

function NavItem(x,y,w,h,text)
{
	this.x = x;
	this.y = y;
	this.w = w;
	this.h = h;
	this.rotation = .8;
	this.text=text;
	console.debug(x,y,w,h);
	var ref = this;

	this.draw = function(ctx)
	{
		console.debug(ref.x,ref.y,ref.w,ref.h);
		
		ctx.save();
				
		ctx.beginPath();
		
		ctx.translate(ref.x,ref.y);
		ctx.rotate(ref.rotation);
		ctx.rect(-ref.w/2,-ref.h/2,ref.w,ref.h);
		ctx.fill();
		//ctx.rect(ref.x-1+(ref.w/2),ref.y-2,2,ref.h+4);
		//ctx.fill();
		ctx.strokeStyle = "green";
		ctx.lineWidth = 2;
		ctx.stroke();
		ctx.fillStyle = "white";
		ctx.textBaseline = "top";
		ctx.fillText(ref.text,ref.x,ref.y);

		ctx.restore();
	};
}