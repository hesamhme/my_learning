# Finding Delayed Restaurants and Active Orders

## Problem Description

Given a list of restaurants with their average preparation times and a list of orders for a day, you are required to:

1. **Identify delayed orders for a specific restaurant.**
   - An order is considered delayed if its actual preparation time exceeds the restaurant's average preparation time.

2. **Determine the maximum number of active orders at any time during the day.**
   - Active orders are those that are being prepared or delivered at a given moment.

## Input Format

- **First Line:** An integer `n` (1 ≤ n ≤ 100), the number of restaurants.
- **Next `n` Lines:** Each line contains a restaurant name (which may include spaces) and its average preparation time in minutes.

```
kababi haj ali 30 sushi express 45
```
- **Next Line:** An integer `m` (100 ≤ m ≤ 1000), the number of orders for that day.
- **Next `m` Lines:** Each line contains order information in one of the following formats:

**Format A (starts with restaurant name):** RestaurantName OrderTime DeliveryTime CustomerName

- `DeliveryTime`: Time when the customer received the order (HH:MM).
- `ConfirmationTime`: Time when the restaurant confirmed the order (HH:MM).

- **Last Line:** A single word, either a restaurant name or the word `overlap`.
- If a restaurant name is given, output the number of delayed orders for that restaurant.
- If `overlap` is given, output the maximum number of active orders at any time during the day.

## Additional Information

- **Order Confirmation:**
- When an order is placed, it takes **5 minutes** on average for the restaurant to confirm it.
- **Delivery Time:**
- After the food is prepared, it takes **10 minutes** on average for delivery to the customer.
- **Food Preparation Start Time:**
- Begins immediately after the order is confirmed.
- **Delivery Start Time:**
- Starts **10 minutes** before the `DeliveryTime`.

## Output Format

- **If a restaurant name is provided:**
- Output a single integer indicating the number of delayed orders for that restaurant.
- **If `overlap` is provided:**
- Output a single integer indicating the maximum number of active orders at any time during the day.

## Sample Input 1
```
2 kababi haj ali 30 sushi express 45 2 kababi haj ali 10:25 11:15 Gholi Zahra 14:17 14:50 sushi express kababi haj ali
```
## Sample output 1

```
1
```

## Explanation

- **Order from Gholi:**
  - **OrderTime:** 10:25
  - **ConfirmationTime:** 10:30 (OrderTime + 5 minutes)
  - **DeliveryTime:** 11:15
  - **DeliveryStartTime:** 11:05 (DeliveryTime - 10 minutes)
  - **PreparationTime:** 35 minutes (DeliveryStartTime - ConfirmationTime)
  - **AveragePrepTime:** 30 minutes
  - Since 35 > 30, this order was **delayed**.

## Sample Input 2
```
3 burger king 25 pizza hut 30 taco bell 20 4 burger king 12:00 12:45 Alice Bob 13:40 13:10 pizza hut taco bell 11:50 12:30 Charlie Diana 14:35 14:00 burger king overlap
```
## Sample output 2
```
2
```

## Notes

- **Calculating Active Orders:**
  - An order is active from its **ConfirmationTime** until its **DeliveryTime**.
  - To find the maximum number of active orders, track overlapping time intervals.
- **Time Calculations:**
  - Be cautious with orders crossing midnight (e.g., 23:55 to 00:25).
  - Convert all times to a consistent unit (e.g., minutes since midnight) for accurate calculations.
- **Parsing Input:**
  - Carefully parse each line to determine whether it starts with a restaurant name or a customer name.
  - Use appropriate data structures to store and manipulate time intervals.

## Implementation Guidelines

- **Data Structures:**
  - Use lists or arrays to store orders and their time intervals.
  - Consider using priority queues or interval trees for efficient overlap calculations.
- **Libraries and Functions:**
  - Utilize time parsing and manipulation libraries available in your programming language.
  - Regular expressions may help in parsing complex input lines.
- **Edge Cases:**
  - Ensure your program handles edge cases like overlapping midnight times and inconsistent input formats.

---
