1a. Duck typing is a way to get polymorphism without inheritance. Python does not check an object’s class. It only checks that the object has the methods and attributes the code needs. If it walks like a duck and quacks like a duck, it is treated as a duck.

1b. The Car class needed a speak() method and an alive attribute, the same ones that Dog and Cat have. With these, it worked in the same loop even though it does not inherit from Animal.

3. The code shows polymorphism because start_trip(vehicle) calls vehicle.move() on every object, and each object responds in its own way. The car drives, the boat sails, and the drone flies. The three classes are not related by inheritance. They only share the method name move(), which is duck typing.