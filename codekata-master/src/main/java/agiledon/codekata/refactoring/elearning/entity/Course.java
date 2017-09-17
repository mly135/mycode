package agiledon.codekata.refactoring.elearning.entity;

public class Course {
    public static final int ENTERPRISE = 0;
    public static final int COMMUNITY = 1;
    public static final int COMMONWEAL = 2;

    private String title;


    public Course(String title, int priceCode) {
        this.title = title;

    }

    public String getTitle() {
        return title;
    }

    public double getAmount(int count) {

        Price price = null;
        return price.getPrice(count);
    }

}
