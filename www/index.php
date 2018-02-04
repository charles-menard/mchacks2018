<?php
function echo_models()
{
	$model_dir = "model/";
	$list = scandir($model_dir);
	$list = array_diff($list, array('..', '.'));
	foreach ($list as $model)
	{
		echo "<option value='".$model."'>";
	}
}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css.css">
	<link rel="shortcut icon" type="image/gif" href="favicon.gif"/>
	<title>Dude Weed Lmao</title>
</head>
<body>
	<h1>Walcame to ur wabsoite mate</h1>
	<p>
		<a href="predict.php">Prediction</a> | <a href="create.php">Create new model</a>
	</p>
	<p>
		<form action="model.php" method="GET">
			Select a model 
			<input type="text" name="model" list="model_list">
			<datalist id="model_list">
				<?php echo_models() ?>
			</datalist>
			<input type="submit" value="Go">
		</form>
	</p>
</body>
</html>
