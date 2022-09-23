## Identify the error in the initial version of MobileComputer.java
The problem with the initial version of MobileComputer.java is that it is not implementing the chargeable interface. This means that the MobileComputer.java can’t use the interface methods which in this case is charge. It is also not of the type “Chargeable”. This means when you try to just pass the MobileComputer object to the Charger.charge method it will not work due to MobileComputer being the wrong type.

## Describe how you have fixed the problem and explain why your solution works
The solution to the problem is to add so that MobileComputer class implements the interface Chargeable.

```java
public class MobileComputer extends Computer implements Chargeable
```

The reason why this work is because the interface Chargeable will be implemented by the MobileComputer class. This means that the class will now have access to the charge method. This means that when running the command from Library:

```java
c.charge(m);
```

The method will not complain because MobileComputer is of the correct type (Chargeable).
