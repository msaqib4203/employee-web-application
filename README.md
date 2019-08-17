# employee-web-application
A demonstrable web application using Vue.js, Bootstrap, Flask and pymysql.
<br>

**Requirement:**

  

Develop a user friendly web application with the following features using Python/Flask/Vue.js/MySQL

  

● List Employees from the Database

● Add Employee

● Delete employee

● Search Employee ○ Name ○ Designation ○ phone

  

**Design & Implementation:**

  

Client side implemented using **Vue.js** and **Bootstrap-vue** for user friendly and adaptive interface, triggers asynchronous API calls using **axios** (an HTTP client) to server side.

Server side is implemented using **Flask** and **pymysql** (a Python module) is used to manage interaction with a **MySQL** database.

The database consists of a table ‘employees’ with attributes as id, name, designation and phone.

  

Listing Employees:

As the application is loaded with URL [http://localhost:8080/employee](http://localhost:8080/employee),

a GET API call is triggered which fetches and list all employees.

  

**Adding Employee:**

On clicking the ‘Add Employee’ button a modal appears, which on submitting with all the required information sends a POST API call with payload as employee info which adds the employee to database.

  

**Deleting Employee:**

On clicking a respective ‘Delete’ button present with each row,a GET API call is triggered which deletes the corresponding employee from the database.

  
  
  

**Searching Employee:**

Employee can be search by using any or combining the search input fields available just below the table headers. As the user types in the search input fields, table content is filtered automatically as per the search query.
