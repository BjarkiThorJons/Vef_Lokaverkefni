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
	<form action="/">
		<input type="submit" name="submit" value="borga">
	</form>
</body>
</html>