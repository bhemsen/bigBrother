<?php require 'header.php';?>
<p>
    Zum Überschreiben einer Karte den Button drücken und die Karte an den Sensor halten
</p>
<small  class="form-text text-muted">
    Beachte: Das Programm das die Chips ausließt muss vorher beendet werden.
</small>

<form action="http://localhost/writeRFID/openWrite.py">
    <button type="submit">Schreiben</button>
</form>

<?php require 'footer.php';?>
