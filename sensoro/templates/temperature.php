<?php require 'header.php';?>


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
  



<script type="application/javascript" src="temperature.js"></script>
<?php require 'footer.php';?>
