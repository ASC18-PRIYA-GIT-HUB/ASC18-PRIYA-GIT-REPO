package com.demo.Inheritance;

interface DebitCard {
}

interface NetBanking {
}

interface SavingsAccount extends DebitCard, NetBanking {
}
