<?php
$csv = file_get_contents('http://www.google.com/trends/viz?q=london,+paris&date=all&geo=all&graph=all_csv&sort=0&sa=N');    
echo $csv;
?>