package ex2;

public class MobileComputer extends Computer implements Chargeable {
	private int battery;
	
	public MobileComputer() {
		this.secret = "MobileComputer secret";
		this.battery = 5;
	}
	
	@Override
	public void work() {
		if (this.battery > 0) {
			System.out.println("It is working on my lap.");
			this.battery--;
		}
		else {
			System.out.println("Running out of battery.");
		}
	}
	
	public void charge() {
		if (this.battery < 10)
			this.battery++;
	}
}
