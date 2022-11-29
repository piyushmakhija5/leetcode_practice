## https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        
        tasks_count = list(collections.Counter(tasks).values()) ## Counts for each unique tasks
        max_count = max(tasks_count) ## maximum count value
        max_count_tasks = tasks_count.count(max_count) ## how many tasks have max task count
        
        return max(len(tasks), (max_count-1)*(n+1)+max_count_tasks)
