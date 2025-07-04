package view;

import controller.Controller;
import exceptions.MyException;

public class RunExample extends Command{
    private Controller controller;

    public RunExample(String key, String desc, Controller controller){
        super(key, desc);
        this.controller = controller;
    }

    @Override
    public void execute() {
        try{
            controller.typeCheck();
            controller.allSteps();
        } catch (MyException exception) {
            System.out.println(exception.getMessage());
        }
    }
}
