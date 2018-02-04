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
<html lang="en">
<head>

	<link rel="shortcut icon" type="image/gif" href="favicon.gif"/>
	<title>Add + plus</title>
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
		<h1>Add stuff</h1>
		<div class="form-group"><form method="POST" action="add.php">
			<label for="category">Model:</label><input class="form-control" id="category" type="text" name="category"><br>
			<label for="sub_category">Class:</label><input class="form-control" id="sub_category" type="text" name="sub_category"><br>
			<label for="urls">Urls:</label>
			<textarea id="urls" class="form-control" placeholder="URL1, URL2, URL3..." name="urls" cols="80" rows="20"></textarea><br>
			<input class="form-control" type="submit">
		</form></div>
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
