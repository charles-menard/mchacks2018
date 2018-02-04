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
$model_dir = "model/";
$model = htmlspecialchars($_GET["model"]);
$result = "";
if (file_exists($model_dir . $model))
{
	if ($_SERVER["REQUEST_METHOD"] == "POST")
	{
		if (empty($model))
			$file_errors[] = "Select a model first";
		else
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
}
else if (!empty($model))
	$model = "Not found. <a href='index.php'>You have to go back</a>";
else
	$model = "";
?>
<!DOCTYPE html>
<html lang="en">
<head>

	<link rel="shortcut icon" type="image/gif" href="favicon.gif"/>
	<title>This is not NOT the model page</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	<style>
	.navbar {
	  margin-bottom: 0;
	  border-radius: 0;
	}
	.row.content {height: 450px}
	.sidenav {
	  padding-top: 20px;
	  background-color: #f1f1f1;
	  height: 100%;
	}
	footer {
	  background-color: #555;
	  color: white;
	  padding: 15px;
	}
	@media screen and (max-width: 767px) {
	  .sidenav {
		height: auto;
		padding: 15px;
	  }
	  .row.content {height:auto;} 
	}
.success {
	color: green;
}
.error {
	color: red;
}
  </style>
</head>
<body>

<nav class="navbar navbar-inverse">
  <div class="container-fluid">
	<div class="navbar-header">
	  <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
		<span class="icon-bar"></span>
		<span class="icon-bar"></span>
		<span class="icon-bar"></span>                        
	  </button>
	  <a class="navbar-brand" href="#">Es tu, AI?</a>
	</div>
	<div class="collapse navbar-collapse" id="myNavbar">
	  <ul class="nav navbar-nav">
		<li class="active"><a href="index.php">Home</a></li>
		<li><a href="model.php">Models</a></li>
		<li><a href="create.php">Create New Model</a></li>
	  </ul>
	</div>
  </div>
</nav>

<div class="container-fluid text-center">    
  <div class="row content">
	<div class="col-sm-2 sidenav">
	  <p><a href="#">Dude</a></p>
	  <p><a href="#">Weed</a></p>
	  <p><a href="#">Lamo</a></p>
	</div>
	<div class="col-sm-8 text-left"> 
		<h1>Model <?php echo $model; ?></h1>
		<p>
			<div class="error"><?php foreach ($file_errors as $d) echo $d . "<br>"; ?></div>
			<div class="success"><?php echo $success; ?></div>
			<form action="model.php" method="GET" class="form-group">
				<label for="modelinput">Select a model</label>
				<input id="modelinput" class="form-control" type="text" name="model" list="model_list">
				<datalist id="model_list">
					<?php echo_models(); ?>
				</datalist>
				<br>
				<input type="submit" class="form-control" value="Go">
			</form>
			<form method="POST" action="model.php" enctype="multipart/form-data" class="form-group">
				<label for="inputfile">Image to predict:</label><input class="form-control" id="inputfile" type="file" name="image"><br>
				<input type="submit" class="form-control">
			</form>
			<div id="result">
				<?php echo $result; ?>
			</div>
		</p>
	</div>
	<div class="col-sm-2 sidenav">
	  <div class="well">
		<p><i><u>AIDS</u></i></p>
	  </div>
	  <div class="well">
		<p>Crypto Miner, <strong>please ignore</strong></p>
	  </div>
	</div>
  </div>
</div>

<footer class="container-fluid text-center">
  <p>Copyright [Current year], no right reserved.</p>
</footer>

</body>
</html>
