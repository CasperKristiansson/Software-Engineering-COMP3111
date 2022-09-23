package lab2;

public class Book {
	private String chapters[];
	private static final int DEFAULT_CHAPTERS = 10;
	
	public Book() {
		chapters = new String[DEFAULT_CHAPTERS];
		for (int i = 0; i < chapters.length; i++) {
			chapters[i] = "n/a";
		}
	}
	
	public Book(String argument[]) {
		/* construct the object with an array of chapter names */
        chapters = new String[argument.length];
        for (int i = 0; i < argument.length; i++) {
        	chapters[i] = argument[i];
        }
	}
	
	public String getChapters(int i) {
		/* return the chapter by the given index */
        return chapters[i];
	}
	
	public String[] getChapters() {
		return chapters;
	}
}
