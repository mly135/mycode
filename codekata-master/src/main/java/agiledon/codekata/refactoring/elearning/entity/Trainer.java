package agiledon.codekata.refactoring.elearning.entity;

import java.util.ArrayList;
import java.util.List;

public class Trainer {
    private String name;
    private List<Training> trainings = new ArrayList<Training>();

    public Trainer(String name) {
        this.name = name;
    }

    public void addTraining(Training training) {
        trainings.add(training);
    }

    public String getName() {
        return name;
    }

    public String statement() {
        double totalAmount = 0;
        int points = 0;
        String result = "Subscription Record for " + getName() + "\n";

        for (Training each : trainings) {

            //determine amounts for each line
            double thisAmount = each.getThisAmount();
            // add frequent renter points
            points++;
            // add points for enterprise course
            points = Training.getPoints(points, each);
            //show figures
            result += "\t" + each.getCourse().getTitle() + "\t" + String.valueOf(thisAmount) + "\n";
            totalAmount += thisAmount;
        }

        //add footer lines
        result += "Amount owed is " + String.valueOf(totalAmount) + "\n";
        result += "You earned " + String.valueOf(points) +
                " points";
        return result;
    }


}
