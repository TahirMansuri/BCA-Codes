<?php
/**
 * ===================================================================
 * Program Name : 01_hello_world.php
 * Subject      : Web Development with PHP (TYBCA - Sem 5)
 * Institution  : IMRD, Shahada
 * Description  : Basic PHP syntax, embedding in HTML, echo vs print.
 * ===================================================================
 */
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TYBCA - PHP Lecture 01</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; background-color: #f4f6f9; }
        .card { background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        h2 { color: #2c3e50; }
    </style>
</head>
<body>

<div class="card">
    <h2>IMRD, Shahada - TYBCA Semester 5</h2>
    <p>
        <?php
            // Outputting text using PHP
            echo "Hello, Welcome to PHP Programming!<br>";
            
            $batchYear = "2026-2027";
            $subject = "PHP & MySQL Web Development";
            
            echo "Academic Batch: <strong>" . $batchYear . "</strong><br>";
            echo "Subject: <strong>" . $subject . "</strong>";
        ?>
    </p>
</div>

</body>
</html>
