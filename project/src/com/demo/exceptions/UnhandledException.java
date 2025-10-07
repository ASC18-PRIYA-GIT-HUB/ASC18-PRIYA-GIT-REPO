package com.demo.exceptions;
public class UnhandledException {
    public static void main(String[] args) {
        int i = 100;
        System.out.println("divide be zero");
        int result = i / 0;
        System.out.println("abruptly terminate, so this does not execute");
        System.out.println(result);
    }
}
