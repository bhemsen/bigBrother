<h1>sensoro</h1>

<div class="container d-flex justify-content-center">
    <section>
        <div class="d-flex justify-content-around">
            <iframe id="iframe" src="" data-src="http://localhost:8081" frameborder="0"></iframe>
            <div class="table-wrapper">
                <table class="table">
                    <thead>
                        <tr>
                            <th scope="col">Zeit</th>
                            <th scope="col">Name</th>
                            <th scope="col">RFID</th>
                            <th scope="col">Zutritt</th>
                        </tr>
                    </thead>
                    <tbody id="tbody"></tbody>
                </table>
            </div>
            <button id="refresh" class="btn btn-primary">Aktualisieren</button>
        </div>
    </section>

    <section>
        <ul>
            <li>aktuelle Temperatur: <span id="temp"></span></li>
            <li>aktuelle Luftfeutchtigkeit: <span id="humidity"></span></li>
        </ul>

    </section> 


    <section>
            <canvas id="chart"></canvas>
            <canvas id="avarage-chart"></canvas>
    </section>
  
</div>