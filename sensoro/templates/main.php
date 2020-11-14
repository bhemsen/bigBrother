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
        <iframe src="http://localhost:8081" frameborder="0"></iframe>
    </section>

</div>