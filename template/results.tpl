<!DOCTYPE html>
<html>
<head>
	<title>Leita</title>
</head>
<body>
	<form action="/karfa" method="post">
		<input type="submit" name="submit" value="fara í körfu">
	</form>
	% for x in posts:

		<a href="/{{ x['link'] }}"><img src='myndir/{{ x["myndir"] }}'></a>
		<p>{{ x["nafn"] }}</p>
		<p>Verð: {{ x["verð"] }}</p>
	%end

</body>
</html>