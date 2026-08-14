# 📄 Practical Sheet 01: Embedding PHP in HTML & Formatted Output
**Course Code**: CA - 317(A) Practical based on Web Technologies-I | **Class**: TYBCA (Sem-V)  
**Academic Year**: 2026–2027 | **Institution**: IMRD, Shahada  

---

### 1. Aim:
Write a PHP script to demonstrate embedding PHP code within HTML5 structure, declaring variables, string concatenation, and displaying dynamic web content.

### 2. Objectives:
- To understand server-side vs client-side script execution.
- To use `echo` and `print` statements for HTML output.
- To practice string interpolation and concatenation operators (`.`).

### 3. Algorithm:
- **Step 1**: Start the Apache server in XAMPP.
- **Step 2**: Create standard HTML5 document structure with CSS styling.
- **Step 3**: Open PHP tag `<?php ... ?>`.
- **Step 4**: Declare student variables: `$student_name`, `$roll_no`, `$class`, `$college`, `$subject`.
- **Step 5**: Render formatted HTML card dynamically using PHP `echo`.
- **Step 6**: Display current server date and time using `date()` function.
- **Step 7**: Stop.

---

### 4. Source Code:
*(Refer to executable file: [`../Lab-Programs/practical_01_php_intro.php`](../Lab-Programs/practical_01_php_intro.php))*

---

### 5. Viva Questions:
1. **Q**: What is the difference between `echo` and `print` in PHP?  
   **A**: `echo` can take multiple parameters and has no return value, making it slightly faster; `print` takes only one argument and always returns `1`.
2. **Q**: Why do PHP scripts need a web server (like Apache) to execute?  
   **A**: PHP is a server-side scripting language; the web server interprets the PHP code and sends plain HTML/CSS back to the client browser.
3. **Q**: What is the string concatenation operator in PHP?  
   **A**: The dot operator (`.`).
