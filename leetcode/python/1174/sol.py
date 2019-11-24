In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1174.immediate-food-delivery-ii.database.json

I am a little bit confused by the solution

https://leetcode.com/problems/immediate-food-delivery-ii/discuss/370681

* Lang:    python
* Author:  serpol
* Votes:   2

I tried the solution like:
```
WITH R AS (
SELECT customer_id, MIN(order_date) order_date
FROM Delivery
GROUP BY customer_id),
F AS (
SELECT D.order_date, customer_pref_delivery_date
FROM Delivery D INNER JOIN R ON D.customer_id = R.customer_id AND D.order_date = R.order_date),
I AS (
SELECT CAST(COUNT(*) AS FLOAT) num
FROM F
WHERE order_date = customer_pref_delivery_date),
A AS (
SELECT CAST(COUNT(*) AS FLOAT) num
FROM F)
SELECT ROUND((I.num * 100) / A.num, 2) immediate_percentage 
FROM I CROSS JOIN A
```
It looks as correct solution as I take all first orders, calculate number of immediate ones and divide by total amount.
But the solution fails for some tests.
Output:
{"headers":["immediate_percentage"],"values":[[9.82]]}
Expected:
{"headers":["immediate_percentage"],"values":[[11.11]]}
We have for the case 99 customers, 112 first orders for them as a customer can make multiple orders for the first day and 11 first orders which are immediate.
From the task description:
Write an SQL query to find the percentage of immediate orders in the first orders of all customers.

Should it be 11 form 112 (9.82%) or 11 from 99 (11.11%)?
The next solution works:
```
WITH R AS (
SELECT customer_id, MIN(order_date) order_date
FROM Delivery
GROUP BY customer_id),
F AS (
SELECT D.order_date, customer_pref_delivery_date, D.customer_id
FROM Delivery D INNER JOIN R ON D.customer_id = R.customer_id AND D.order_date = R.order_date),
I AS (
SELECT CAST(COUNT(DISTINCT customer_id) AS FLOAT) num
FROM F
WHERE order_date = customer_pref_delivery_date),
A AS (
SELECT COUNT(DISTINCT customer_id)  num
FROM R)
SELECT ROUND((I.num * 100) / A.num, 2) immediate_percentage 
FROM I CROSS JOIN A
```
Which looks for me as a percentage of customers which have at least one first order as immediate.

Am I wrong?
