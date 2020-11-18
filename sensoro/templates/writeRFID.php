<?php require 'header.php';?>
<p>
    Zum Überschreiben einer Karte den Button drücken und die Karte an den Sensor halten
</p>
<br>
<small  class="form-text text-muted">
    Beachte: Das Programm das die Chips ausließt muss vorher beendet werden.
</small>

<form action="http://localhost/writeRFID/openWrite.py">
    <div class="form-group">
        <label for="name">Name: </label>
        <input name="name" id="name" type="text">
    </div>
    <div class="form-group">
        <label for="securityLevel">Sicherheitsstufe: </label>
        <input name="securityLevel" id="securityLevel" type="number">
    </div>
    <button class="btn btn-primary" type="submit">Schreiben</button>
</form>

<?php require 'footer.php';?>
