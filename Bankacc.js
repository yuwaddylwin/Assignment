let balance = 5000;
const transactionHistory = ['Deposited 10000 into Savings Account', 'Withdrawn 5000 form Savings Account'];

function getBalance(){
    return balance;
}


function deposit(amount) {
    balance = balance +  amount;
    transactionHistory.push("Deposit Amount:{amount}")

}

function withdraw(amount) {
    if (amount <= balance) {
        balance -= amount;
        transactionHistory.push(`Withdrawn Amount:{amount}`);
    } 
    else {
        console.log('Insufficient Amount!')
    }
}


function getTransactionHistory() {
    return transactionHistory;
}



console.log(getBalance());
// Expected Output: 5000

deposit(4000);
console.log(getBalance());
// Expected Output: 9000

withdraw(3000);
console.log(getBalance());
// Expected Output: 6000

console.log(getTransactionHistory());

