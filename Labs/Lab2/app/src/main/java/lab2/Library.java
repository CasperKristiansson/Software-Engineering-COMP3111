package lab2;

public class Library {
	public static void main (String arg[]) {
			final String array[] = {"Basic Java", "Advanced Java", "Guru Java"};
			Book b = new Book(array);
			int k = 2;
			System.out.println("The title of the Chapter " + k + " is " + b.getChapters(k - 1));
			String anotherArray[] = b.getChapters();
			
			System.out.println("There are " + anotherArray.length + " chapters.");
			System.out.println(java.util.Arrays.toString(anotherArray));
		
			// Computer a = new MobileComputer();
			// for (int i = 0; i < 10; i++) {
			// 	a.work();
			// }
			
			// Charger c = new Charger();
			// Phone p = new Phone();
			// MobileComputer m = new MobileComputer();
			
			// c.charge(p);
			// c.charge(m);
	
	
	}
	
    public boolean someLibraryMethod() {
        return true;
    }
}
