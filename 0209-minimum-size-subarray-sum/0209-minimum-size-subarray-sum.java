class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int low = 0;
        int n = nums.length;
        int result = Integer.MAX_VALUE;
        int sum = 0;
        for(int high = 0; high < n; high++){
            sum = sum + nums[high];

            while(sum >= target){
                result = Math.min(result, high-low + 1);
                sum = sum - nums[low];
                low++;
            }
        }

        if(result == Integer.MAX_VALUE){
            return 0;
        }
        else{
            return result;
        }
    }
}