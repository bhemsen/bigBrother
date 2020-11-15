<h1>sensoro</h1>

<div class="container d-flex justify-content-center">

    <section>
        <div class="d-flex justify-content-around">
            <canvas id="temperature-chart"></canvas>
            <ul>
                <li>
                    aktuelle Temperatur: <span id="temp"></span>
                </li>
                <li>
                    aktuelle Luftfeutchtigkeit: <span id="humidity"></span>
                </li>
            </ul>
        </div>
    </section>

    <section>
        <div class="d-flex justify-content-around">
            <iframe src="http://localhost:8081" frameborder="0"></iframe>
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
                <button id="refresh" class="btn btn-primary">Aktualisieren</button>
            </div>
        </div>
    </section>

</div>