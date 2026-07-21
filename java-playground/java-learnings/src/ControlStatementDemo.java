public class ControlStatementDemo {

    public static void main(String[] args) {


        double[] claimAmounts={45.50D,120.00D,18.75D,320.00D,60.00D};
        char[] categoryCodes={'T','H','F','T','O'};
        boolean hasReciepts=true;
        double approvalThreshold=100.00D;

        System.out.println("------------------------- if/else ----------------------");
//        single Yes/No decision

        double firstClaim=claimAmounts[0];

        if(firstClaim>approvalThreshold){
            System.out.println("Claim of GBP "+firstClaim+" needs manager approval");
        }else {
            System.out.println("Claim of GBP "+firstClaim+" is auto-approved");
        }

        System.out.println("------------------------- else if ladder ----------------------");

//        for(initialization;condition;increment/decrement){
//
//        }

        for(int index=0;index< claimAmounts.length;index++){
            double amount=claimAmounts[index];
            String tier;

            if(amount<50){
                tier="Small";
            }else if(amount<150){
                tier="Medium";
            } else if (amount<300) {
                tier="Large";
            }else{
                tier="Critical - needs Director sign off";
            }
            System.out.println("Claim "+(index+1)+" : GBP:"+amount+" --> "+tier);
        }


        System.out.println("------------------------- switch case ----------------------");



        for(int index=0;index< categoryCodes.length;index++){
            char code=categoryCodes[index];
            String categoryName;

            switch (code){
                case 'T':
                    categoryName="Travel";
                    break;
                case 'H':
                    categoryName="Hotel";
                    break;
                case 'F':
                    categoryName="Food";
                    break;
                case 'O':
                    categoryName="Other";
                    break;
                default:
                    categoryName="Unknown";
                    break;
            }

            System.out.println("Category "+(index+1)+" : category:"+categoryName);
        }

        System.out.println("------------- for loop -----------------------");

        double total=0;

        for(int index=0;index<claimAmounts.length;index++){
            total=total+claimAmounts[index];
        }
        System.out.println("Total of all claims is GBP:"+total);

        System.out.println("------------- while loop -----------------------");

//        we stop as soon as montly budget cap is hit
//        however many claim it takes

        double monthlyBudgetCap=200.00;
        double runningTotal=0;
        int claimsWithinBudget=0;

        while(claimsWithinBudget <claimAmounts.length && runningTotal< monthlyBudgetCap){
            runningTotal+=claimAmounts[claimsWithinBudget];
            claimsWithinBudget++;
        }

        System.out.println("Stopped after "+claimsWithinBudget+ "claim(s) - cap GBP "+monthlyBudgetCap+" was breached, running total GBP:"+runningTotal);

        System.out.println("------------------------- Ternary Operator----------------------");

        for(int index=0;index< claimAmounts.length;index++) {

//            variable= condition ? value-if-condition-is-true : value-if-condition-is-false

            String status = (claimAmounts[index] > approvalThreshold || !hasReciepts) ? "Needs Approval" : "Auto Approved";

            System.out.println("Claim " + (index + 1) + " :GBP:" + claimAmounts[index] + " Status -->" + status);
        }

    }


}
