<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="css/styles.css">
	<title></title>
</head>
<body>
	% include('template/header.tpl')
	%verd=0
	%for x in posts:
		%for y in x:
			<h2>{{y}}</h2>
			<h2>fjöldi: {{x[y]["fjoldi"]}} verð: {{x[y]["verd"]}}</h2>
			%verd=verd+x[y]["verd"]
		
	%end
	%end
	<p>Samtals: {{verd}}</p>
	<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
	<form action="/">
		<input type="submit" name="submit" value="borga">
	</form>
	</a>
</body>
</html>