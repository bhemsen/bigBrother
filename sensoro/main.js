

// ______________________________________________________________--Display Entrylogging

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
    xhr.open("POST", 'http://localhost/functions/getEntryLogging.php', true)
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


// ______________________________________________________________-- Call functions in main()




window.onload = function(){
    getEntrylog();
    let refreshTableBtn = document.getElementById('refresh');
    refreshTableBtn.addEventListener('click', ()=>{
        refreshTable();
        getEntrylog();
    });

    let iFrame = document.getElementById('iframe');
    iFrame.setAttribute("src", iFrame.dataset.src) 

}


