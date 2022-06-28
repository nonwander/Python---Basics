# Python Basics
## Object-oriented programming - Useful additions
<div style="text-align: right; text-decoration: underline"> Practice, practice, more practice!</div>

```
My goal in completing these tasks was not to demonstrate my knowledge of the basics of Python, but to use tasks to improve the practice of writing structured applications that satisfy some minimum requirements for code readability and lack of redundancy relative to the source task.
```

1. Implement the ```Date``` class. Constructor function should accept the ```date``` as a _string_ of the *"day-month-year"* format. Implement two methods within the class. The first one with the decorator _@classmethod_. It should extract the ```number```, ``month``, ``year`` and convert their type to the ```Number``` type. The second one with the decorator ```@staticmethod```. It should *validate* the day, month and year _(example: the month is from 1 to 12)_.
</br>Check the operation of the resulting structure with real data.

2. Create your own exception class that handles the situation of division by zero. Check its operation on the data entered by the User. When entering zero as a divisor the program must correctly handle this situation and not fail with an error.

3. Create your own exception class that should check the contents of the list for the presence of only numbers. Check the operation of the exception on a real example. Request data from the User and add to the list only numbers. The exception class must control the data types of the list items.
</br>_Note:_ the length of the list is not fixed.
</br>The elements are requested endlessly until the user stops the script by entering cpecial command _(example: the command "stop")_. After the script ends the generated list with displayed on the screen.
</br>_Hint:_ For this task assume that the User can only enter numbers and strings. When the User enters the next element, it is necessary to implement an element type check. Add it to the list only if a number is entered. The exception class should prevent the User from entering text (not a number) and displaying the corresponding message and should not be terminated.

4. Start the project _"Office equipment Warehouse"_. Create a class describing the warehouse. Also ```OfficeEquipment``` class, which will be the base for the child classes. These classes are specific types of office equipment (```printer```, ```scanner```, ```copier```). In the base class define the common parameters to the types listed. In the child classes implement parameters that are unique for each type of office equipment.

5. Continue the first part of the project _"Office equipment Warehouse"_.
Develop methods that are responsible for receiving office equipment to the warehouse and transferring it to a specific division of the company. To store data on the name and number of office equipment units you can use any suitable structure (for example, a dictionary).

6. Continue the second part of the project _"Office equipment Warehouse"_.
Implement a mechanism for validating user input data.
</br>_Example:_ you cannot use a string data type to specify the number of printers sent to the warehouse.
</br>_Hint:_ try to implement in the project "Office equipment Warehouse" the maximum of the possibilities studied in the lessons on OOP.

7. Implement the project _"Operations with complex numbers"_. Create a ```ComplexNumber``` class. Implement overloading of the methods of addition (```__add__```) and multiplication (```__mul__```) of complex numbers.
- check the work of the project;
- create instances of the class (complex numbers);
- perform addition and multiplication of the created instances;
- check the correctness of the received result.
</br></br>
#### **Completed by**
Evgeny Nemykin | nonwander@gmail.com | _@nonwander_