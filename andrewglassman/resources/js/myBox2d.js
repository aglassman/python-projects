function createWorld()
{
	var worldAABB = new b2AABB();
	worldAABB.minVertex.Set(-1000, -1000);
	worldAABB.maxVertex.Set(1000, 1000);
	var gravity = new b2Vec2(0, 300);
	var doSleep = true;
	return new b2World(worldAABB, gravity, doSleep); 
}

function createGround(world,x,y,w,h) {
	var groundSd = new b2BoxDef();
	groundSd.extents.Set(w, h);
	groundSd.restitution = 0.8;
	var groundBd = new b2BodyDef();
	groundBd.AddShape(groundSd);
	groundBd.position.Set(x, y);
	return world.CreateBody(groundBd)
}

function createCircleBody(x,y,r,world)
{
	var circleSd = new b2CircleDef();
	circleSd.density = 6;
	circleSd.radius = r;
	circleSd.restitution = .2;
	circleSd.friction = 1.0;
	var circleBd = new b2BodyDef();
	circleBd.AddShape(circleSd);
	circleBd.position.Set(x,y);
	var circleBody = world.CreateBody(circleBd);
	return circleBody;
}

function createBox(world, x, y, width, height, fixed) {
	if (typeof(fixed) == 'undefined') fixed = true;
	var boxSd = new b2BoxDef();
	if (!fixed) boxSd.density = 1.0;
	boxSd.extents.Set(width, height);
	var boxBd = new b2BodyDef();
	boxBd.AddShape(boxSd);
	boxBd.position.Set(x,y);
	return world.CreateBody(boxBd)
}