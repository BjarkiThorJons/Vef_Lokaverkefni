<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	%for x in posts:
		%for y in x:
			<h2>{{y}} fjöldi: {{x[y]}}</h2>
		
	%end
</body>
</html>