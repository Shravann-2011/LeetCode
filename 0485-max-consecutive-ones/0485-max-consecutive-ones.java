class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int current_count = 0;
        int max_ans = 0;
        int j = 0;
        int n = nums.length;
        while(j < n)
        {
            if(nums[j] == 1)
            {
                j++;
                current_count+=1;
                max_ans = Math.max(max_ans,current_count);
            }
            else
            {
                j++;
                current_count = 0;
            }
        }
        return max_ans;
    }
}