<!DOCTYPE html>
<html>
<head>
	<title>{{posts[0]["hopur"]}}</title>
</head>
<body>
	<form action = "/check", method="post">
		<h2>Leita með skráningarnúmeri</h2>
		<input type="text" name="search">
		<input type="submit" name="check" value="Leita">
	</form>
	% for x in posts:

		<a href="/{{ x['link'] }}"><img src='myndir/{{ x["myndir"] }}'></a>
		<p>{{ x["nafn"] }}</p>
		<p>Verð: {{ x["verð"] }}</p>
	%end

<p>end</p>
</body>
</html>