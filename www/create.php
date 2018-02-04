<?php
include 'functions.php';

$debug_mode = true;
$model_dir = "./model/";

function check_files()
{
	return (true);
}

if ($_SERVER["REQUEST_METHOD"] == "POST")
{
	$files = reArrayFiles($_FILES['images']);
	$error = "";
	$success = "";
	$category = htmlspecialchars($_POST["category"]);
	$sub_category = $_POST["sub_category"];
	$imgnbr = $_POST["imgnbr"];

	//echo "Category: " . $category . "<br>";
	//echo "sub_category: " . $sub_category[0] . "<br>";
	//echo "imgnbr: " . $imgnbr[0] . "<br>";
	//
	if (file_exists('model/' . $category))
		$error = "Category already exist, silly.";
	else if (check_files())
	{
		mkdir($model_dir . $category, 0777, true);
		$nf = 0;
		foreach ($sub_category as $i => $sub)
		{
			//echo $imgnbr[$i] . "<br>";
			mkdir($model_dir . $category . "/" . $sub, 0777, true);
			$cur_dir = $model_dir . $category . "/" . $sub . "/";
			for ($j = 0; $j < $imgnbr[$i]; $j++)
			{
				if (true || in_array(pathinfo($files[$nf]["name"], PATHINFO_EXTENSION), ["jpg"]))
				{
					$newfile = $cur_dir . hash("sha1", $files[$nf]["tmp_name"]) . "." . pathinfo($files[$nf]["name"], PATHINFO_EXTENSION);
					echo $newfile . "<br>";
					if (move_uploaded_file($files[$nf]["tmp_name"], $newfile))
						$success = "Model added";
				}
				//echo $category . "/" . $sub . "/" .  $files[$nf]["name"] . "<br>";
				$nf++;
			}
		}
		//foreach ($files as $i => $file)
		//{
		//	echo $file["name"] . "<br>";
		//}
	}
}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css.css">
	<link rel="shortcut icon" type="image/gif" href="favicon.gif"/>
	<title>Create a model</title>
<script>
		function set_imgnbr() {
			var img = document.querySelectorAll('input[type="file"]');
			var nbr = document.querySelectorAll('input[type="hidden"]');

			for (var i = 0; i < img.length; i++) {
				nbr[i].value = img[i].files.length;
			}
		}
		function add_subcat() {
			var subcat = '<div class="subcat">Sub-category: <input type="text" name="sub_category[]"><br>Files...: <input type="file" name="images[]" multiple onchange="set_imgnbr() accept=".jpg"><br><input type="hidden" name="imgnbr[]" value=""></div><hr>';
			var submit = document.getElementById('addsubcat');
			var dummy = document.createElement('div');
			
			dummy.innerHTML = subcat;
			submit.parentNode.insertBefore(dummy, submit);
		}
	</script>
</head>
<body>
	<h1>Create new model</h1>
	<p>
		<a href="add.php">Broken, plz use this</a>
		<form action="create.php" method="POST" enctype="multipart/form-data">
			<h2>Category: <input type="text" name="category"></h2>
			Add sub-category: <button id="addsubcat" type="button" onclick="add_subcat()">+</button><br>
			<input type="submit" value="Submit">
		</form>
	</p>
</body>
</html>
