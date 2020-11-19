<?php require 'header.php';?>
<p>
    Zum Überschreiben einer Karte den Button drücken und die Karte an den Sensor halten
</p>
<br>
<small  class="form-text text-muted">
    Beachte: Das Programm das die Chips ausließt muss vorher beendet werden.
</small>

<form action="http://localhost/writeRFID/openWrite.py" method="POST">
    <div class="form-group">
        <label for="name">Name: </label>
        <input name="name" class="form-control" id="name" type="text">
    </div>
    <div class="form-group">
        <label for="securityLevel">Sicherheitsstufe: </label>
        <input name="securityLevel" class="form-control" id="securityLevel" type="number">
        <small  class="form-text text-muted">
    1 für Angestellte, 2 Für Leitende Angestellte
</small>
    </div>
    <button class="btn btn-primary" type="submit">Schreiben</button>
</form>

<?php require 'footer.php';?>
