<!DOCTYPE html>
<html>
<head>
	<title>FIlter</title>
</head>
<body>
% for x in posts:

%	if x["hopur"] == "skjakort":
		<p>{{ x["nafn"] }}</p>
	<img src='myndir/{{ x["myndir"] }}'>
%end
<p>end</p>
</body>
</html>