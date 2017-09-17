package agiledon.codekata.refactoring.elearning.entity;

public abstract class Price {

    protected abstract double getPrices(int count);

    private int priceCode;
    public int getPriceCode() {
        return priceCode;
    }
    public void setPriceCode(int arg) {
        priceCode = arg;
    }

    public double getPrice(int count) {
        Price price;
        int priceCode = getPriceCode();
        if (priceCode == Course.ENTERPRISE) {
            price = new EnterPrice();
            return price.getPrices(count);
        }
        if (priceCode == Course.COMMUNITY) {
            price = new CommunityPrice();
            return price.getPrices(count);
        }
        if (priceCode == Course.COMMONWEAL) {
            price = new OtherPrice();
            return price.getPrices(count);

        }
        return 0;
    }
}
