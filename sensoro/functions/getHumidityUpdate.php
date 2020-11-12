<?php

require '../includes.php';

function getTemperature(){
    $sql = "SELECT humidity,time 
    FROM temperature
    ORDER BY ID DESC LIMIT 1";

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