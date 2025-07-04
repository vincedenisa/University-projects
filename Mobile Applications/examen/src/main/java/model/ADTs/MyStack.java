package model.ADTs;

import exceptions.MyException;

import java.util.List;
import java.util.Stack;

public class MyStack<T> implements MyStackInterface<T>{
    private Stack<T> stack;

    public MyStack() {
        this.stack = new Stack<>();
    }

    @Override
    public T pop() throws MyException {
        try{
            return this.stack.pop();
        }
        catch (Exception e) {
            throw new MyException("Stack is empty");
        }
    }

    @Override
    public void push(T val) {
        this.stack.push(val);
    }

    @Override
    public boolean isEmpty() {
        return this.stack.isEmpty();
    }

    @Override
    public int size() {
        return this.stack.size();
    }

    @Override
    public T top() throws MyException {
        try {
            return this.stack.peek();
        } catch (Exception e) {
            throw new MyException("Can't extract the top from an empty stack");
        }
    }

    @Override
    public String toString() {
        return this.stack.toString();
    }

    @Override
    public List<T> getAllList() {
        return this.stack;
    }
}
