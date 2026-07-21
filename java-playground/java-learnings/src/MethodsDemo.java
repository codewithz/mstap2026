public class MethodsDemo {

//    Syntax of a method
  /*
    access-specifier access-modifier[optional] return-type nameOfTheMethod(parameters[optional]){
        statements;
        statements;
        statement;  --> if return-type is not void , last statment of the method has to be a retun statment  --> return something;
    }
   */
//   No Parameter No Return
   public void sayHello(){
       System.out.println("Hello There!!");
   }
//   With Parameter No Return
   public void add(int one,int two){
       int addition=one+two;
       System.out.println("Addition is:"+addition);
   }

//   No Parameter With Return

    public int getTaxRate(){
       int taxRate=10;
       return taxRate;
    }

//    With PArameter With Return

    public int getSqaureValue(int number){
       int square=number*number;
       return square;

    }


}
