public class FizzBuzz {

    private int firstDivider;
    private int secondDivider;
    private int count;

    public FizzBuzz(int firstDivider, int secondDivider, int count) {
        this.firstDivider = firstDivider;
        this.secondDivider = secondDivider;
        this.count = count;
    }

    public int getFirstDivider() {
        return this.firstDivider;
    }

    public int getSecondDivider() {
        return this.secondDivider;
    }

    public int getCount() {
        return this.count;
    }

    public void setFirstDivider(int firstDivider) {
        this.firstDivider = firstDivider;
    }

    public void setSecondDivider(int secondDivider) {
        this.secondDivider = secondDivider;
    }

    public void setCount(int count) {
	this.count = count;
    }
}
