let labels = [];
let temperatures = [];
let humidity = [];
let labelsAverage = [];
let temperaturesAverage = [];
let humidityAverage = [];
let currTemp = document.getElementById('temp');
let currHumidity = document.getElementById('humidity');

let canvas = document.getElementById('chart');
let ctx = canvas.getContext('2d');

let canvasAverage = document.getElementById('avarage-chart');
let ctxAverage = canvasAverage.getContext('2d');



// ______________________________________________________________--Drawing Charts
let chart = new Chart(canvas, {
    type:'line',
    data:{
        labels:[],
       
        datasets: [{
            label:'Temperature',
            data: [],
            borderColor: '#ff6666',
            backgroundColor: 'transparent',
            borderWidth: 2,
            yAxisID: 'A',
            data: []
          }, {
            label:'humidity',
            yAxisID: 'B',
            data: [],
            borderColor: '#6666ff',
            backgroundColor: 'transparent',
            borderWidth: 2
          }]
    },
    options: {
        scales: {
            yAxes: [{
                id: 'A',
                type: 'linear',
                position: 'left',
            }, {
                id: 'B',
                type: 'linear',
                position: 'right',
                ticks: {
                    max: 100,
                    min: 0
                }
            }]
        },
        title:{
            display:true,
            text:'Heute'
        }
    }
})


let chartAverage = new Chart(canvasAverage, {
    type:'line',
    data:{
        labels:[],
        datasets: [{
            label:'Temperature',
            data: [],
            borderColor: '#ff6666',
            backgroundColor: 'transparent',
            borderWidth: 2,
            yAxisID: 'A',
            data: []
          }, {
            label:'humidity',
            yAxisID: 'B',
            data: [],
            borderColor: '#6666ff',
            backgroundColor: 'transparent',
            borderWidth: 2
          }]
    },
    options: {
        scales: {
            yAxes: [{
                id: 'A',
                type: 'linear',
                position: 'left',
            }, {
                id: 'B',
                type: 'linear',
                position: 'right',
                ticks: {
                    max: 100,
                    min: 0
                }
            }]
        },
        title:{
            display:true,
            text:'Durchschnitt 7 Tage'
        }
    }
})

// ______________________________________________________________--Create Update-Functions

function addDataTemp(chart, label, data) {
    chart.data.labels.push(label);
    chart.data.datasets[0].data.push(data);
    chart.update();
}


function addDataHum(chart, data) {
    chart.data.datasets[1].data.push(data);
    chart.update();
}

// ______________________________________________________________--Create Temperature-Functions

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


function getTemperatureAverage() {

    let xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://localhost/functions/getAverageTemp.php', true)
    xhr.onload = function () {
        if(xhr.status === 200){
            let result = JSON.parse(this.response);
            
                
        for (let tupel in result) {
            labelsAverage.push(result[tupel].HOUR);
            temperaturesAverage.push(parseFloat(result[tupel].temperature));
            addDataTemp(chartAverage, labelsAverage[tupel], temperaturesAverage[tupel]); 
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

// ______________________________________________________________--Create Humidity-Functions

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

function getHumidityAverage() {

    let xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://localhost/functions/getAverageHum.php', true)
    xhr.onload = function () {
        if(xhr.status === 200){
            let result = JSON.parse(this.response);
            
            for (let tupel in result) {
                humidityAverage.push(parseFloat(result[tupel].humidity));
                console.log(humidityAverage);
                addDataHum(chartAverage, humidityAverage[tupel]); 
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


function updateArrays(){
    
    setInterval(function(){ 
        getTemperatureUpdate();
        getHumidityUpdate();
    }, 15000);

}


function main(){
    
    getTemperatureInitial();
    getHumidityInitial();
    getHumidityAverage();
    getTemperatureAverage();
    updateArrays();
}

window.onload = function(){
    main();
}