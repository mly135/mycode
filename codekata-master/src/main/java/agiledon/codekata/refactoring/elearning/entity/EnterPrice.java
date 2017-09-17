package agiledon.codekata.refactoring.elearning.entity;

public class EnterPrice extends Price {

    public double getPrices(int count) {
        double thisAmount = 0;
        if (count > 15)
            thisAmount += 1000 * count * 0.8;
        else thisAmount += 1000 * count;
        return thisAmount;
    }

}
