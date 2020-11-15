let labels = [];
let temperatures = [];
let humidity = [];
let currTemp = document.getElementById('temp');
let currHumidity = document.getElementById('humidity');

let canvas = document.querySelector('canvas');
let ctx = canvas.getContext('2d');

let chart = new Chart(canvas, {
    type:'line',
    data:{
        labels:[],
       
        datasets:[{
            label:'Temperature',
            data: [],
            borderColor: '#ff6666',
            backgroundColor: 'transparent',
            borderWidth: 2
        },
        {
            label:'humidity',
            data: [],
            borderColor: '#6666ff',
            backgroundColor: 'transparent',
            borderWidth: 2

        }]
    },
    options:{
        title:{
            display:true,
            text:'Seit Aufzeichnung'
        }
    }
})


function addDataTemp(chart, label, data) {
    chart.data.labels.push(label);
    chart.data.datasets[0].data.push(data);
    chart.update();
}


function addDataHum(chart, data) {
    chart.data.datasets[1].data.push(data);
    chart.update();
}


function getTemperatureInitial() {

    let xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://localhost/functions/getTemperature.php', true)
    xhr.onload = function () {
        if(xhr.status === 200){
            let result = JSON.parse(this.response);
            
                
        for (let tupel in result) {
            labels.push(result[tupel].time);
            temperatures.push(parseFloat(result[tupel].temperature));
            addDataTemp(chart, labels[tupel], temperatures[tupel]); 
        }
        
        } else {
            console.log(xhr.status);
            return;
        }
    };
    xhr.send();
}


function getTemperatureUpdate(){
    labels = [];
    temperatures = [];
    let xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://localhost/functions/getTemperatureUpdate.php', true)
    xhr.onload = function () {
        if(xhr.status === 200){
            let result = JSON.parse(this.response);
            
                
        for (let tupel in result) {
            labels.push(result[tupel].time);
            temperatures.push(parseFloat(result[tupel].temperature));
            addDataTemp(chart, labels[tupel], temperatures[tupel]); 
            currTemp.innerText = temperatures[tupel];
        }
        
        } else {
            console.log(xhr.status);
            return;
        }
    };
    xhr.send();

}

function getHumidityInitial() {

    let xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://localhost/functions/getHumidity.php', true)
    xhr.onload = function () {
        if(xhr.status === 200){
            let result = JSON.parse(this.response);
            
                
        for (let tupel in result) {
            humidity.push(parseFloat(result[tupel].humidity));
            addDataHum(chart, humidity[tupel]); 
        }
        
        } else {
            console.log(xhr.status);
            return;
        }
    };
    xhr.send();
}


function getHumidityUpdate(){
    labels = [];
    temperatures = [];
    let xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://localhost/functions/getHumidityUpdate.php', true)
    xhr.onload = function () {
        if(xhr.status === 200){
            let result = JSON.parse(this.response);
            
        for (let tupel in result) {
            humidity.push(parseFloat(result[tupel].humidity));
            addDataHum(chart, humidity[tupel]); 
            currHumidity.innerText = humidity[tupel];
        }
        
        } else {
            console.log(xhr.status);
            return;
        }
    };
    xhr.send();

}


function createTableEntry(result) {

    for (let tupel in result) {
        let tbodyRef = document.getElementById('tbody')
        let array = [];
        array.push(result[tupel].time, result[tupel].name,result[tupel].rfid, result[tupel].access);
        // Insert a row at the end of table
        let newRow = tbodyRef.insertRow();

        for (let i = 0; i < array.length; i++){
             // Insert a cell at the end of the row
            let newCell = newRow.insertCell();
            newCell.innerText = array[i];
            
        }   
    }

}

function refreshTable(){
    let tbody = document.getElementById('tbody');
    tbody.innerHTML = "";
}

function getEntrylog() {

    let xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://localhost/functions/getEntrylogging.php', true)
    xhr.onload = function () {
        if(xhr.status === 200){
            let result = JSON.parse(this.response);
            
            createTableEntry(result);
        
        } else {
            console.log(xhr.status);
            return;
        }
    };
    xhr.send();
}


function updateArrays(){
    
    setInterval(function(){ 
        getTemperatureUpdate();
        getHumidityUpdate();
        getEntrylog()
        
    }, 15000);

}

getTemperatureInitial();
getHumidityInitial();
getEntrylog()
updateArrays();

window.onload = function(){
    let refreshTableBtn = document.getElementById('refresh');
    console.log(refreshTableBtn);
    refreshTableBtn.addEventListener('click', ()=>{
        refreshTable();
        getEntrylog();
    });
}





