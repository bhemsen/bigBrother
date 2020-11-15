<?php

require '../includes.php';

function getEntrylog(){
    $sql = "SELECT time, name, rfid, access 
        FROM entrylog ORDER BY ID DESC";

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

echo getEntrylog();