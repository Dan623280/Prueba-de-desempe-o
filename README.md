#🧾 Performance test

## Description

This project allows you to manage the basic information of the students. The system
allows register, Consult, update and Delete students, as well as storing the
information in a structured way for later use.


------------------------------------------------------------------------

## How to access the project?

To do the project from your computer, follow these steps:

### 1. Clone the repository

``` bash

git clone https://github.com/Dan623280/Prueba-de-desempe-o.git

```

### 2. open file

Open the main.py file

------------------------------------------------------------------------


## Usage example

When the application starts, it loads the data from the json file.

``` bash
data.json

```

The application displays a menu with the following options:

1. Register new students
2. Consult student list
3. Look for students
4. update a student's information.
5. Delete students
6. go_out

## register

if the user selects option 1:

The program will ask you:

- Name
- age
- Course (referring to the training program)
- Status (active/inactive)

and these are registered in the list "list_students" found in the file list_students

## Consult

if the user selects option 2:

The program will show the data per student:


- go
- Name
- age
- Course
- Status


example

``` bash

"Index = 2, Name = Juan, Age = 23, Course = English, Status = active"

```

## Look for

if the user selects option 3:

The program will allow you to search by:


- go
- Name
- age
- Course
- Status

and the program will filter depending on the option chosen

## Update

The program filter by student id

The program will ask you:

- Name
- age
- Course (referring to the training program)
- Status (active/inactive)

and this updates the list record of the selected student with the id

## Update

The program filter by student id

The program will ask you:

- Name
- age
- Course (referring to the training program)
- Status (active/inactive)

and this updates the list record of the selected student with the id


## Delete

Selecting the id shows and removes the student from the record

## go out

Save the json file

and exit the program

------------------------------------------------------------------------


## 👤 Autor

Daniel Alvarez

------------------------------------------------------------------------