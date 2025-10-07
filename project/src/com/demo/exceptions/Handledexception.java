package com.demo.exceptions;

public class Handledexception {
    public Handledexception() {
        result = 0;
    }
    int result;
    private void test() {
        try { //block scope
            int i = 100;
            System.out.println("divide be zero");
            result = i / 0;
        } catch (Exception exception)
        {
            System.out.println("Exception occurs : " +  exception);
        }
        System.out.println("abruptly terminate, so this does not execute");
        System.out.println(result);
    }
    public static void main(String[] args) {
        Handledexception handledexception =  new Handledexception();
        handledexception.test();
    }
}
