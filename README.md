
Brett Hirsch 		ET 574 Programming Applications with Python	3/11/2024

Honors Project: Mortgage Calculation
First, I defined a function called calculate_mortgage and set it to the argument purchase_price. Next, I set three variables which are as follows: down_payment_percentage is 0.10, annual _interest _rate is 0.12, and monthly _payment _percentage is 0.05. After that, I created a variable called down_payment, which is the purchase price multiplied by the down payment percentage. Then, I created a variable called balance which is the purchase price minus the down payment. This was all done to make sure that the 10 percent down payment is not considered when calculating the balance payments. 
After that, I set two more variables: monthly_payment which is equal to the balance multiplied by the monthly payment percentage, and the monthly_interest_payment which is equal to the annual interest rate divided by 12. Overall, this meant that the monthly payment is 5 percent of the balance, and the interest rate is 1 percent per month. 
Next, I used a format string to create the table headers. The table headers are as follows: "Month", "Balance", "Interest Owed", "Principal Paid", "Payment", "Remaining Balance". I made sure to use “{:<n}” to left align the headers. n has a value of 10 for “Month” and a value of 20 for the rest.
	After that, I created a variable called month and set it equal to 1. 
 Then, I created a while statement that would be the way I loop the program until it is finished. 
 The condition was that while the balance is greater than zero the following would occur. 
 A variable called interest_payment is created that is equal to the balance times monthly interest rate of 1 percent. 
 Another variable called principal_payment is created which is equal to the monthly payment minus the interest payment. 
 Inside this while statement I nested an if statement which contained the following: If the value of the principal payment is greater than the balance, then set the principal payment equal to the balance. 
 This is to make sure that in the final month, the principal payment is not higher than the balance that’s left to pay off. Next, I created a variable called payment and set it equal to the interest payment plus the principal payment. 
 After that, I used an f string to print out the values for each section of the table in the following order: month, balance, interest_payment, principal_payment, payment, balance - principal_payment.
 The last value is the remaining balance which is equal to the balance minus the principal payment. Then I used the subtraction assignment operator (-=) to have the principal payment subtract from the previous balance left remaining. After that I used the addition assignment operator to have the month go up by one after each time. Then, I set the purchase_price variable equal to an input statement typecasted as a float, which asks the user to input a purchase price. 
 Finally, I used the calculate_mortgage function on the purchase_price variable and ran the program. The program worked as inteneded
