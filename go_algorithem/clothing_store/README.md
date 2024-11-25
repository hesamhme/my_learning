
# Clothing Store

**Time Limit:** 1 second  
**Memory Limit:** 256 MB  

Jole, Jack's sister, owns a clothing store and has decided to encourage customers to buy multiple types of clothing by offering special discounts on bulk purchases. Since Jack has recently joined the GoLang course at Quera, Jole asks him to write a program that calculates the final price of a customer's shopping cart with the maximum possible discount.

Jole's store has 5 different types of clothing:

- Shirt  
- Pants  
- Jacket  
- Shoes  
- Hoody  

The price of each item is 800,000 Rials under normal circumstances, but if customers buy multiple types of clothing together, the following discounts apply:

- If you buy 2 different types, you get a 5% discount.  
- If you buy 3 different types, you get a 10% discount.  
- If you buy 4 different types, you get a 20% discount.  
- If you buy all 5 types, you get a 25% discount.  

**Note:** Discounts are applied only to distinct clothing types. For example, if you buy 4 items with only 3 distinct types, the discount applies to those 3 types, and the fourth item is priced at the full amount.

**Constraints:**  
It is guaranteed that there will be at most 15 items in the shopping cart.

## Input  
The input is an array of items purchased. For example:  
`shirt,shirt,pants,pants,jacket,jacket,shoes,hoody`

This indicates the purchase of:
- 2 shirts  
- 2 pants  
- 2 jackets  
- 1 pair of shoes  
- 1 hoody  

## Output  
Print a single integer representing the total cost of the shopping cart in Rials after applying the maximum possible discount.

### Example

#### Sample Input 1:
```plaintext
shirt,shirt,pants,pants,jacket,jacket,shoes,hoody
```

#### Sample Output 1:
```plaintext
51200000
```

**Explanation:**  
There are two ways to group these 8 items:

1. Form one group of 5 items and another group of 3 items:
   - Group 1 contains 5 distinct types (shirt, pants, jacket, shoes, hoody), costing 3,000,000 Rials after a 25% discount.
   - Group 2 contains 3 remaining items (shirt, pants, jacket), costing 2,160,000 Rials after a 10% discount.
   - Total: 5,160,000 Rials (51,600,000 Rials).

2. Form two groups of 4 items:
   - Group 1 contains 4 distinct types (shirt, pants, jacket, shoes), costing 2,560,000 Rials after a 20% discount.
   - Group 2 contains another 4 distinct types (shirt, pants, jacket, hoody), costing 2,560,000 Rials after a 20% discount.
   - Total: 5,120,000 Rials (51,200,000 Rials).

The correct answer is **51,200,000 Rials**, as it gives the maximum discount.

---

#### Sample Input 2:
```plaintext
shirt,pants,shoes,pants,shirt,shirt,jacket,jacket,hoody
```

#### Sample Output 2:
```plaintext
59200000
```

**Explanation:**  
This input can be grouped in multiple ways (details omitted due to complexity).  
The best grouping results in a total cost of **59,200,000 Rials**.
