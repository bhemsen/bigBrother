<?php

require '../includes.php';

function getAverageTemperature(){
    $sql = "SELECT day,HOUR(time) as HOUR, avg(temperature) as temperature FROM `temperature` GROUP by day , HOUR(time)";

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

echo getAverageTemperature();
