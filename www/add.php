<?php
if ($_SERVER["REQUEST_METHOD"] == "POST")
{
	$host = "http://127.0.0.1:5000/upload/";
	$category = $_POST["category"];
	$sub_category = $_POST["sub_category"];
	$urls = explode(",", $_POST["urls"]);

	foreach ($urls as $url)
		file_get_contents($host . $category . "/" . $sub_category . "/" . $url);
}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css.css">
	<link rel="shortcut icon" type="image/gif" href="favicon.gif"/>
	<title>Add</title>
</head>
<body>
	<form method="POST" action="add.php">
		Model: <input type="text" name="category"><br>
		Class: <input type="text" name="sub_category"><br>
		<textarea placeholder="URL1, URL2, URL3..." name="urls" cols="80" rows="20"></textarea><br>
		<input type="submit">
	</form>
</body>
</html>
