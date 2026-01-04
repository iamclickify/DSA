class Solution {
    public int missingNumber(int[] nums) {
        int n= nums.length; // n is no of elements in an array
        int sum = n*(n+1)/2;
        int arraysum = 0;

        for(int i = 0;i<nums.length;i++){
            arraysum = arraysum + nums[i];
        }
        return sum - arraysum;
    }
}