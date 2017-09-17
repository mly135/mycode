package agiledon.codekata.refactoring.elearning.entity;

public class Training {
    private Course course;
    private int traineeCount;

    public Training(Course course, int traineeCount) {
        this.course = course;
        this.traineeCount = traineeCount;
    }

    public Course getCourse() {
        return course;
    }

    public int getTraineeCount() {
        return traineeCount;
    }


    public double getThisAmount() {
        return getCourse().getAmount(getTraineeCount());
    }

    public static int getPoints(int points, Training each) {
        if (each.getCourse().getPriceCode() == Course.ENTERPRISE) {
            points = points + 2;
        } else {
            points++;
        }
        return points;
    }
}
