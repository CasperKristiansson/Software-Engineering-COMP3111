public class main {
	public static void main(String[] args) {
		Animal animals[] = new Animal[10];

        // BUG: This code gives a NullPointerException. This is because
        // the for loop doesn't update the array with the new Animal
        // objects. This means that the array is full of null values.
        // When the for loop then tries to access a the method isAlive()
        // on the null values, it throws a NullPointerException.
		// for (Animal a : animals)
        //     a = new Animal();
        
        // This can simply be fixed by updating the array with the new
        // Animal objects by using a normal for loop.
        for (int i = 0; i < animals.length; i++)
            animals[i] = new Animal();

		for (int iii = 0; iii < 10; iii++) {
			int ii = 0;
			for (; ii < 100 && animals[iii].isAlive() ; ii++) {
				System.out.print(animals[iii].getWeight() + " ");
				animals[iii].eat();
				if (ii % 3 == 0)
				animals[iii].poo();
			}
		}	
	}
}
