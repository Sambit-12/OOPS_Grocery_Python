# The Grocery Raja store

## Requirements 📝

### Introduction
A grocery store is present in this project, and we will use the concepts of inheritance, classes, exception handling, and regular expressions to determine the price of an item and its expiration date.
### Research
*	In this Store we are having different products like Staple food Beverages and Snack Items.
*	This Store helps to find Expiry date of the food in Year Month Day format.
*	This store helps to check the price of the all the food items of the list.

### Inheritence
*	Usage of Multilevel Inheritence concept.
*	There is a Parent class which has all the attributes and methods which is to be used in the code.
*	There are other Derived Classes which Inherits the attributes of the parent class and some other function so that you dont need to write the Parent class all the time again.
* Usage of Constructor to call the methods of the class.

### Regular expression
*	Usage of import re package for implementation of regular expression commands. 
*	using regular expression for converting Paragraph into sentence only alphabetical parameters.
*	using regular expression for checking the pattern that only email Id of the user should be shown nothing else even if User Input is something else than email id.

### Data Encapsulation
*	Usage ._ while declaring a variable so that the object is protected. 
*	Data Encapsulation is used because the barcode detail shouldn't shared with customer thatswhy user cant see that only programmer can see.
*	Even if u try create object and call the object then it will throw an not attribute found in the class Error.

### Polymorphism
*	In polymorphism the function defination's name  of base and Derived have same.
*	Even after same name of the defination of function we can give different parameters thorugh.
*	Used Polymorphism technique for advertisement of sale of different 
*	used Polymorphism technique for implementing customer 
*	It makes the program more dynamic


### Exception Handling
*	Usage of Excpetion class and making an object with super keyword to raise the issue
*	By using this concept we ensured that no item in the store will cost 0 ruppes as it isnt possible.
*	If price is given as 0 then it will throw an exception error and wont be able to see the items other details too.

## Cost and Features
*	This system saves a lot of time for the user and results in quick and accurate manner.
* More option too choose without even going away from your home computer does the job for you.

## Defining our system
*	In this system, the essential parameters are obtained from the user as input and this system will check the cost expiry date of the item  depending on the choice you place in the store.


## SWOT ANALYSIS🔍
![Screenshot (1)]


# 4W&#39;s and 1&#39;H ❓

## 1️⃣Who?
- Any person who wants to buy grocery Products while sitting at home in single go.
- It can be used by anyone at any place.
- Can by used All age group people above an age of 12+.

## 2️⃣Why?
- To reduce the complexity faced by the shopkeeper to fulfill customer demands
- To make the process of buying grocery enjoyable with many options and different suggestion based on your watch history.
- To make a Time effecient, reliable .

## 3️⃣When?
- A virtual and command line interface based project which makes the shopping more user friendly and easily accessible from anywhere which is developed as a part of           "Object  oriented Programming  using Python" of Genesis internship program.
- The project can be employed when there is need in calculation of basic Electrical concepts either in day-to-day aplplication or for labrotary procedures. 

## 4️⃣Where?
- The program is developed in Pycharm IDE.
- Users can use this application on their desktop or laptop terminal
- Can be used in small shops at your locality and even it is useful if u want to buy anything from sitting at home
 
## 1️⃣How?
- The module was build solely by using Python and by using some key concepts like  Inheritence Polymorphism Data Encapsulation ".
- Testing has been carried out by "Pytest"
- And the code quality is ensured by screening the code in various code reviewing entities such as "Codacy", "Git Inspector", etc.


# Detail requirements 📋

## High Level Requirements
| ID | Description | Status (Implemented) |
| ---- | ----------- | --------------------------- |
| HA01 | Calculation for the Price of Snacks| Implemented|
| HA02 | Display for expiry date of the Snacks and its best before period in months of  |  Implemented |
| HA03 | Calculation for the Price of Beverages| Implemented |
| HA04 | Display for expiry date of the Beverages and its best before period in months of| Implemented |
| HA05 | Calculation for the Price of Staples| Implemented |
| HA06 | Display for expiry date of the staples and its best before period in months of |  Implemented|
| HA07 | Usage of Polymorphism| Implemented|
| HA08 | Usage of Data Encapsulation| Implemented |
| HA09 | Usage of Regular Expression| Implemented |



## Low level Requirements
| ID | Description |HLR|Status (Implemented)| 
| ---- | ----------- | --------------------------- |-----------|
| LA01 | Calculation of Price of Snacks by inherting attributes from Parent class| HA01 | Implemented|
| LA02 | Throwing an Error in Price of if user give the input as 0 via using concept of Exception Handling| HA01 | Implemented|
| LA03 | Declaring variables and string input for YYY-MM-DD format of manufacturing date using dateutil.relativedelta package and datetime for expiry date format|HA02|Implemented|
| LA04 | Calculation of Price of Snacks by inherting attributes from Parent class| HA03 |Implemented|
| LA05 | Throwing an Error in Price of if user give the input as 0 via using concept of Exception Handling| HA03 |Implemented|
| LA06 | Declaring variables and string input for YYY-MM-DD format of manufacturing date using dateutil.relativedelta package and datetime for expiry date forma|HA04|Implemented|
| LA07 | Calculation of Price of Beverages by inherting attributes from Parent class| HA05 |Implemented|
| LA08 | Throwing an Error in Price of if user give the input as 0 via using concept of Exception Handling | HA05 |Implemented|
| LA09 | Declaring variables and string input for YYY-MM-DD format of manufacturing date using dateutil.relativedelta package and datetime for expiry date format|HA06|Implemented|
| LA10 | Polymorphism for Advertisement of the shop |HA07 |Implemented|
| LA11 | Polymorphism for Features of Store of the shop |HA07|Implemented|
| LA12 | Data Encapsulation being used to hide the Product Id of the Product in barcode form| by using._ form  to  protect attribute object of Product Id class |HA08| Implemented|
| LA13 | Usage of Regular expression to get only the Email Id of the user nothing else should be displayed if written by mistake using pattern format| HA09| Implemented|
| LA14 | Usage of Regular expression to get the Customer review from Paragraph to sentence format| HA09| Implemented|
