<?php

echo floatval($_POST);
$file = 'temp.py';
$temp = floatval($_POST['inputMaxTemp']);
$insert = "maxTemperature = $temp";

file_put_contents($file, $insert);


header("Location: http://localhost/index.php");
exit();
