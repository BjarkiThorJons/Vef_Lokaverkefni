<!DOCTYPE html>
<html>
<head>
	<title>{{posts["nafn"]}}</title>
</head>
<body>
	<img src="myndir/{{posts['myndir']}}">
	<h2>{{posts["nafn"]}}</h2>
	<h2>{{posts["verð"]}}</h2>
	<h2>{{posts["lysing"]}}</h2>
	<form action="/rsadea" method="post">
		<input type="hidden" name="vara" value="{{posts['nafn']}}">
		<input type="number" name="fjoldi" value="1"><input type="submit" name="submit" value="bæta í körfu"><br>
	</form>
	<form action="/karfa" method="post">
		<input type="submit" name="submit" value="fara í körfu">
	</form>
</body>
</html>