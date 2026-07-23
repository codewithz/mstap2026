package exceptions;

public class ExpenseRunner {

    public static void main(String[] args) {
        ExpenseClaim validClaim=new ExpenseClaim(45.00,false);
        ExpenseClaim invalidClaim=new ExpenseClaim(250.00,false);

        try{
            validClaim.submit();
            invalidClaim.submit();
        }catch (Exception e){
            System.out.println(e);
        }

    }
}
