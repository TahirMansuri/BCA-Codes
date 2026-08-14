<?php
/**
 * ===================================================================
 * Assignment   : Assignment 01 - PHP Basics (TYBCA Sem-V)
 * Question 01  : Electricity Bill Calculator (Slab-based calculation)
 * Institution  : IMRD, Shahada
 * ===================================================================
 */

function calculate_bill($units) {
    $bill = 0;
    if ($units <= 50) {
        $bill = $units * 3.50;
    } elseif ($units <= 150) {
        $bill = (50 * 3.50) + (($units - 50) * 4.00);
    } elseif ($units <= 250) {
        $bill = (50 * 3.50) + (100 * 4.00) + (($units - 150) * 5.20);
    } else {
        $bill = (50 * 3.50) + (100 * 4.00) + (100 * 5.20) + (($units - 250) * 6.50);
    }
    return $bill;
}

$consumed_units = 180;
$total_amount = calculate_bill($consumed_units);
?>
<!DOCTYPE html>
<html>
<head>
    <title>Electricity Bill Solution - Assignment 01</title>
</head>
<body style="font-family: Arial; padding: 20px;">
    <h2>Electricity Bill Receipt</h2>
    <p>Units Consumed: <strong><?php echo $consumed_units; ?> kWh</strong></p>
    <p>Total Payable Amount: <strong>₹<?php echo number_format($total_amount, 2); ?></strong></p>
</body>
</html>
