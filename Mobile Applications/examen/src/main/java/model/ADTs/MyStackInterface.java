package model.ADTs;

import exceptions.MyException;

import java.util.List;

public interface MyStackInterface<T> {
    T pop() throws MyException;
    void push(T val);
    boolean isEmpty();
    int size();
    T top() throws MyException;

    List<T> getAllList();
}
