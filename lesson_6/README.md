# Python Basics
## Object-oriented programming
<div style="text-align: right; text-decoration: underline"> Practice, practice, more practice!</div>

```
My goal in completing these tasks was not to demonstrate my knowledge of the basics of Python, but to use tasks to improve the practice of writing structured applications that satisfy some minimum requirements for code readability and lack of redundancy relative to the source task.
```

1. Create a ```TrafficLight``` class:
1) define ```color``` attribute as *private* and ```running``` method for it;
2) implement in the method switching the traffic light to the modes: ```red```, ```yellow```, ```green```;
3) the duration of the _red_ state is ```7 seconds```, the _yellow_ state is ```2 seconds```, the _green_ state is any at your discretion;
4) switching between modes should be carried out only in the specified order (red, yellow, green);
5) check the operation of the example by creating an instance and calling the described method.
The task can be complicated by implementing a check of the order of modes. If it is violated, output the appropriate message and terminate the script.

2. Implement the ```Road``` class.
1) define attributes: ```length```, ```width```;
2) attribute values must be passed when creating an instance of the class;
make attributes *protected*;
3) determine the method of calculating the _mass of asphalt_ required to cover the entire road;
4) use the formula: ```length * width * mass``` of asphalt to cover 1 sq.m. of asphalt road and 1 cm thick multiplied by the value in cm of the road thickness;
5) check the operation of the method.
_Example:_ ```20m * 5000m * 25kg * 5cm = 12500t```

3. Implement the ```Worker``` base class.
1) define attributes: ```name```, ```surname```, ```position```, ```income```;
2) ```income``` attribute must be *protected* and refer to a dictionary containing elements: ```wage``` and ```bonus``` 
_Example:_ ```{"wage": wage, "bonus": bonus}```
3) create a ```Position``` class based on the ```Worker``` class;
4) in the ```Position``` class implement methods for obtaining the ```full name``` of the employee (*get_full_name*) and ```income```, taking into account the bonus (get_total_income);
5) test the execution of the example on real data:
- create instances of the _Position_ class
- pass data
- check attribute values
- call instance methods.

4. Implement the ```Car``` base class.
1) the class must have the following *attributes*: ```speed```, ```color```, ```name```, ```is_police``` _(boolean)_.
2) and the *methods*: ```go```, ```stop```, ```turn (direction)```, which should report that the car has _gone_, _stopped_, _turned (direction)_;
3) describe several child classes: ```TownCar```, ```SportCar```, ```WorkCar```, ```PoliceCar```;
4) the ```show_speed``` method in the base class, which should show the current speed of the car;
5) for the ```TownCar``` and ```WorkCar``` classes override the ```show_speed``` method: if the speed value *exceeds 60* _(TownCar)_ and *exceeds 40* _(WorkCar)_, a message of speed excess should be displayed.
- create instances of classes
- pass attribute values
- access the attributes
- output the result.
- call the methods and show the result.

5. Implement the ```Stationery``` class.
1) define the ```title``` attribute and the ```draw``` method in it. The method outputs the message _"Starting rendering"_;
2) create three child classes ```Pen```, ```Pencil```, ``Handle``;
3) implement redefinition of the ```draw``` method in each class. For each class the method must output a unique message;
4) create instances of classes and check what the described method outputs for each instance.
</br></br>
#### **Completed by**
Evgeny Nemykin | nonwander@gmail.com | _@nonwander_