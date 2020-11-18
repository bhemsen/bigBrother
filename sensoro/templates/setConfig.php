<?php require 'header.php';?>

<section>
<form action="http://localhost/sensoro/functions/writeCritTemp.php" method="POST">
        <div class="form-group">
            <label for="inputMaxTemp">Kritische Temperatur: </label>
            <input id="inputMaxTemp" class="form-control" type="number" name="inputMaxTemp">
            <small  class="form-text text-muted">
                Wenn die Raumtemperatur diese Grenze erreicht, werden sie per Mail benachrichtigt (Default = 70)
            </small>
            <button class="btn btn-primary" type="submit">Bestätigen</button>
        </div>
    </form>

    <form action="http://localhost/sensoro/functions/writeDaysToDel.php" method="POST">
        <div class="form-group">
            <label for="daysToDelete">Speicher Grenze: </label>
            <input id="daysToDelete" class="form-control" type="text" name="daysToDelete">
            <small id="" class="form-text text-muted">Hier legen sie fest, nach wie vielen Tage die einträge der Datenbank gelöscht werden (Defaut = 7).</small>
            <button class="btn btn-primary" type="submit">Bestätigen</button>
        </div>
    </form>

</section>

<?php require 'footer.php';?>
