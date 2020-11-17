<?php

require '../includes.php';

$sql = SELECT AVG(a.temperature) AS avg 
FROM ( SELECT temperature as temperature, HOUR(time) as hour
       FROM temperature
       GROUP BY hour) AS a;

function getTemperature(){
    $sql = "SELECT temperature,time 
        FROM temperature WHERE ID % 240 = 0";

    $con = getDB();

    $result = $con->query($sql);

    if(false === $result){
        return json_encode([]);
    }
    $json_array = [];

    while ($row = $result->fetch()){
        $json_array[]= $row;
    }

    $json_response = json_encode($json_array);


    return $json_response;

}

echo getTemperature();
