<!DOCTYPE html>
<html>
<head>
	<title>Leita</title>
</head>
<body>
	% for x in posts:

		<img src='myndir/{{ x["myndir"] }}'>
		<p>{{ x["nafn"] }}</p>
		<p>Verð: {{ x["verð"] }}</p>
	%end

</body>
</html>