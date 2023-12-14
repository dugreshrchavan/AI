<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }

        form {
            max-width: 400px;
            margin: 20px auto;
            padding: 20px;
            background-color: yellow;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        select {
            box-sizing: border-box;
            width: 80%;
            margin: 8px 0;+
            padding: 10px 5px;
            border-radius: 5px;
        }

        header {
            font-size: 55px;
            padding: 5px;
            border-radius: 5px;
            text-decoration: underline;
            text-align: center;
            font-family: Arial;
            color: black;
        
 }

        label {
            display: block;
            margin: 10px 0 5px;
        }

        input[type="text"],
        input[type="date"],
        textarea {
            width: 100%;
            padding: 8px;
            margin: 5px 0 15px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
         }

        input[type="submit"],
        input[type="reset"] {
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
        }

        input[type="submit"] {
            background-color: #4caf50; /* Green color for Submit button */
            color: #fff;
        }

        input[type="submit"]:hover {
            background-color: #45a049;
        }

        input[type="reset"] {
            background-color: #3498db; /* Blue color for Clear button */
            color: #fff;
        }

        input[type="reset"]:hover {
            background-color: #2980b9;
        }

    </style>
    <title>Project Form</title>
</head>
<body>
    <header>Project Management</header>

    <form>
        <label for="projectName">Project Name:</label>
        <input type="text" id="projectName" name="projectName" placeholder="Project name" required>

        <label for="ASSIGNED">ASSIGNED</label>
           <select>
           <option value="option">tushar rajaram</option>
           <option value="option">aniket</option>
           <option value="option">joshi</option>
           <option value="option">durgesh</option>
           </select>

        <label for="startDate">Start Date:</label>
        <input type="date" id="startDate" name="startDate" required>

        <label for="endDate">End Date:</label>
        <input type="date" id="endDate" name="endDate" required>

        <th class="row1">Priority: </th>
        <tr><td>
        <input type="radio" name="priority" id="high" value="High"> High
       <input type="radio" name="priority" id="average" value="Average"> Average
       <input type="radio" name="priority" id="low" value="Low"> Low
         </td>
        </tr>


        <label for="description">Description:</label>
        <textarea id="description" name="description" rows="4" required></textarea>

        

        <input type="submit" value="Submit">
        <input type="reset" value="Clear">
    </form>

</body>
</html>
