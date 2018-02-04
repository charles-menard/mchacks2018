<?php
$model_dir = "model/";
$model = htmlspecialchars($_GET["model"]);
$result = "";
if (file_exists($model_dir . $model))
{
	if ($_SERVER["REQUEST_METHOD"] == "POST")
	{
		$tmp_name = $_FILES["image"]["tmp_name"];
		$name = $_FILES["image"]["name"];
		$upload_dir = "./uploads/";
		$upload_name = $upload_dir . hash("sha1", $tmp_name) . "." . pathinfo($name, PATHINFO_EXTENSION);
		$file_errors = [];
		$success = "";
		$size = $_FILES["image"]["size"];

		if (empty($name))
			$file_errors[] = "No image";
		else if (pathinfo($name, PATHINFO_EXTENSION) != "jpg")
			$file_errors[] = "File must be jpg only.";
		else if ($size > 1048576)
			$file_errors[] = "File is to large. Limit is 1MiB";
		else
		{
			if (move_uploaded_file($tmp_name, $upload_name))
			{
				$success = "Image UPLOADED.";
				$result = "Doing stuff inside some python script.";
			}
			else
				$file_errors[] = "IMAGE <u>NOT</u> UPLOADED";
		}
	}
}
else
	$model = "Not found. <a href='index.php'>You have to go back</a>";
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css.css">
	<link rel="shortcut icon" type="image/gif" href="favicon.gif"/>
	<title>Model</title>
</head>
<body>
	<h1>Model: <?php echo $model; ?></h1>
	<div class="error"><?php foreach ($file_errors as $d) echo $d . "<br>"; ?></div>
	<div class="success"><?php echo $success; ?></div>
	<form method="POST" action="model.php" enctype="multipart/form-data">
		Image to predict: <input type="file" name="image"><br>
		<input type="submit">
	</form>
	<div id="result">
		<?php echo $result; ?>
	</div>
</body>
</html>
