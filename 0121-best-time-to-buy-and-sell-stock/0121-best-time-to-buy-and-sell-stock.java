class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit = 0;
        int buy=prices[0];
        for(int i=0;i<prices.length;i++){
            int currentprofit = prices[i] - buy;

            if(currentprofit>maxprofit){
                maxprofit=currentprofit;
            }
            if(prices[i]<buy){
                buy=prices[i];
            }
        }
        return maxprofit;
    }
}