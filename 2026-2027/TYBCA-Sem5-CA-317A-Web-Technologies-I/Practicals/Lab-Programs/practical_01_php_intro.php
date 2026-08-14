<?php
/**
 * ===================================================================
 * Practical No : Practical 01
 * Course Code  : CA - 317(A) Practical based on Web Technologies-I
 * Class        : TYBCA (Semester-V) | Academic Year: 2026-2027
 * Institution  : S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada
 * Faculty      : Mr. Tahir Mansuri (HOD & Asst. Prof.)
 * Aim          : Embedding PHP in HTML, variable declarations, 
 *                string concatenation, and server date display.
 * ===================================================================
 */

$college_name = "S.T.E.S. & Co-Op. Ed. Soc. Ltd. IMRD, Shahada";
$department   = "Department of Computer Applications";
$course_code  = "CA - 317(A)";
$subject      = "Practical based on Web Technologies-I";
$student_name = "BCA Student";
$academic_yr  = "2026 - 2027";
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TYBCA - Practical 01 Output</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #eef2f7; margin: 40px; }
        .container { max-width: 600px; margin: 0 auto; background: #ffffff; padding: 25px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 5px solid #007bff; }
        h2 { color: #1a365d; margin-bottom: 5px; font-size: 20px; }
        h3 { color: #4a5568; margin-top: 0; font-size: 16px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { text-align: left; padding: 10px; border-bottom: 1px solid #e2e8f0; font-size: 14px; }
        th { background: #f8fafc; color: #475569; width: 35%; }
        .footer { margin-top: 20px; font-size: 12px; color: #64748b; text-align: center; }
    </style>
</head>
<body>

<div class="container">
    <h2><?php echo $college_name; ?></h2>
    <h3><?php echo $department; ?></h3>
    <hr>
    
    <table>
        <tr>
            <th>Course Code</th>
            <td><strong><?php echo $course_code; ?></strong></td>
        </tr>
        <tr>
            <th>Subject Title</th>
            <td><?php echo $subject; ?></td>
        </tr>
        <tr>
            <th>Student Name</th>
            <td><?php echo $student_name; ?></td>
        </tr>
        <tr>
            <th>Academic Year</th>
            <td><?php echo $academic_yr; ?></td>
        </tr>
        <tr>
            <th>Server Timestamp</th>
            <td><?php echo date("l, d-F-Y h:i:s A"); ?></td>
        </tr>
    </table>

    <div class="footer">
        Generated dynamically by PHP Engine (XAMPP Server)
    </div>
</div>

</body>
</html>
