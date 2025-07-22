/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {

     int* result = (int*)malloc(2 * sizeof(int));
    int i;
    int second_number,j;
    for(i=0;i<numsSize;i++){
        second_number=target-nums[i];
        for(j=i+1;j<numsSize;j++){
            if(second_number==nums[j]){
                result[0]=i;
                result[1]=j;
                *returnSize=2;
                return result;
            }
        }
    }
    *returnSize=0;
    return NULL;
    
}