<?php

require '../includes.php';

function getTemperature(){
    $sql = "SELECT temperature,time 
        FROM temperature WHERE day = CURRENT_DATE()";

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
