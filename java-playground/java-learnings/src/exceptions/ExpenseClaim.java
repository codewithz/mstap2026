package exceptions;

public class ExpenseClaim {
    double amount;
    boolean hasReceipt;

    public ExpenseClaim(double amount, boolean hasReceipt) {
        this.amount = amount;
        this.hasReceipt = hasReceipt;
    }

    public void submit() throws MissingReceiptException{
        if(amount >100 && !hasReceipt){
            throw
                    new MissingReceiptException(
                            "Claim over 100 GBP need a receipt: Your amount:"+amount);
        }

            System.out.println("Claim of GBP "+amount+" ahs been submitted.");

    }
}
