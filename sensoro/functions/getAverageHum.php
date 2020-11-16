<?php

require '../includes.php';

function getHumidity(){
    $sql = "SELECT humidity,time 
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

echo getHumidity();