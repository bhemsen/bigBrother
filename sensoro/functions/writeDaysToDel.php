<?php

$file = 'days.py';
$days = strval($_POST['daysToDelete']);
$insert = "days = $days";

file_put_contents($file, $insert);

header("Location: http://localhost/sensoro/index.php");
exit();
