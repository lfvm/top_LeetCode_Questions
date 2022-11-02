"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
"""



def maxProfit( prices ) -> int:
        
    maximumProfit = 0     
    #Two pointers 
    i = 0 
    j = 1 
        
    while j < len(prices):
        
        currentProfit = prices[j] - prices[i]
        maximumProfit = max(currentProfit, maximumProfit)
        
        if prices[j] < prices[i]:
            i = j 
            j += 1 
        else:
            j += 1
        
    return maximumProfit     

"""
Explicación:
Para solucionar este problema se utilizan dos pointers (i,j) 
se inicializa i en el primer dia y j en el segundo.


De ahi en adelante se debe revizar la diferencia de precios entre ambos dias y actualizar maximumProfit en caso de que la diferencia sea mayor
por ultimo solo moveremos i cuando prices[j] sea menor que i. y en este caso lo moveremos hasta j 


"""