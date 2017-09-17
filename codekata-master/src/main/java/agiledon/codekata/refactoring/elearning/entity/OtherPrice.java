package agiledon.codekata.refactoring.elearning.entity;

public class OtherPrice extends Price {
    @Override
    public double getPrices(int count) {
        double thisAmount = 0;
        thisAmount += 100 * count;
        return thisAmount;
    }

}
