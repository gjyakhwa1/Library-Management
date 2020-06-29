# Library Management System

Web Programming with Python and JavaScript

### accounts app
It handles all the account related activities like new account, login, logout

#### templates folder in accounts app
1. confirmationpage.html--->Page from which we can confirm to delete any student accounts
2. loginpage.html--->Student or Librarian can login from this page
3. registerpage.html---->Page from which new student can be registered
4. updatepage.html------>Page from which librarian can update data of existing students

##### forms.py
It is created to handle the register forms and update forms

#### Other python files are as per the Django documentation

### books app
It is created so as to control all the book related pages like issuing books, adding books and many more

##### templates folder in books app

1. addbooks.html--->page from which new books can be added
2. issuebooks.html--->page from which student can issue books (controlled by librarian)
3. searchbook.html--->page from which books can be searched from which we can know about the availability of books
4. searchresults.html--->result of searching book is displayed in this page
5. studentsview.html--->This page displays all the books issued by the student (view for student account),access for only one particular student
6. viewissuebooks.html--->This page displays all the books issued by students and is viewed by librarian, view all the books issued till now

##### filters.py
Python file to filter as per user description

##### forms.py
forms for adding and issuing books

###library app
app that contains pages and views inherited by other app pages

##### templates folder in library app
1. error.html---->page to display error messages
2. index.html---->homepage for website that contains short information about Library
3. layout.html-->provides the base layout for our website, created with help of bootstrap and custom CSS
4. studentlist.html--->page to display the list of students

### static folder
It handles all the CSS as well as images of website

### Javascript is used in the html files where JS is needed

### inventory app is main app
