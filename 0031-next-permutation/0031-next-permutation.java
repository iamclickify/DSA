class Solution {
    public void nextPermutation(int[] nums) {

        int n = nums.length;
        int pivot = -1;

        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                pivot = i;
                break;
            }
        }

        if (pivot != -1) {
            for (int j = n - 1; j > pivot; j--) {
                if (nums[j] > nums[pivot]) {

                    int temp = nums[pivot];
                    nums[pivot] = nums[j];
                    nums[j] = temp;

                    break;
                }
            }
        }

        int l = pivot + 1;
        int r = n - 1;

        while (l < r) {
            int temp = nums[l];
            nums[l] = nums[r];
            nums[r] = temp;

            l++;
            r--;
        }
    }
}