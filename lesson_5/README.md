# Python Basics
## Working with files in Python
<div style="text-align: right; text-decoration: underline"> Practice, practice, more practice!</div>

```
My goal in completing these tasks was not to demonstrate my knowledge of the basics of Python, but to use tasks to improve the practice of writing structured applications that satisfy some minimum requirements for code readability and lack of redundancy relative to the source task.
```

1. Create a program file in text format and write in it line by line the data entered by the User. An empty line will indicate the end of data entry.

2. Create a text file _(not programmatically)_ and save several lines in it. Count the lines and words in each line.

3. Create a text file _(not programmatically)_. Write down line by line the names of employees and the amount of their salaries (at least 10 lines). Determine which of the employees has a salary of less than 20 thousand and output their names. Calculate the average amount of employee income.
</br>_Sample file:_
```
Ivanov 23543.12
Petrov 13749.32
```

4. Create _(not programmatically)_ a text file with the following contents:
```
One — 1
Two — 2
Three — 3
Four — 4
```
Write a program that opens the file for reading and reads the data line by line. At the same time English numerals should be replaced with Russian ones. A new block of lines should be written to a new text file.

5. Create _(programmatically)_ a text file, write to it programmatically a set of numbers separated by spaces. The program should calculate the sum of the numbers in the file and display it on the screen.

6. Generate _(not programmatically)_ a text file, where each line should describe the ```academic subject``` and the ```availability of lectures```, ```practical``` and ```laboratory``` classes on the subject. This should include the number of classes. It is not necessary that there are all types of classes for each subject.
Create a dictionary containing the name of the subject and the total number of classes on it. Bring it to the screen.
</br></br>_Examples of file lines:_
```
Computer Science: 100(l) 50(pr) 20(lab).
Physics: 30(L) — 10(lab)
Physical education: — 30(pr) —
```
_Dictionary example:_
```
{“Computer Science": 170, “Physics": 40, “Physical Education": 30}
```

7. Create _manually_ text file with several lines which will contain data about the company: ```name```, ```form of ownership```, ```revenue```, ```costs```.
</br>_Example of a file line:_ ```firm_1 OOO 10000 5000```
</br>
Need to read the file line by line and calculate the profit of each company and the average profit for all companies. If the company has received losses, it should not be included in the calculation of the average profit.
Next, implement the list. It should contain a dictionary with firms and their profits, and a dictionary with average profits. If the company has received losses, also add it to the dictionary (with the value of losses).
</br>_Example list:_
```
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit": 2000}].
```
</br>Save the final list as a ```json``` object to the corresponding file.
_Example of a ```json``` object:_
``` json
[
    {
        "firm_1": 5000,
        "firm_2": 3000,
        "firm_3": 1000
    },
    {
        "average_profit": 2000
    }
]
```
_Hint:_ use the ```context manager```.
</br></br>
#### **Completed by**
Evgeny Nemykin | nonwander@gmail.com | _@nonwander_