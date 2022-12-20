## https://leetcode.com/problems/k-closest-points-to-origin/description/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Heap: sort by the distance to origin, in ascending order
        k_closet = heapq.nsmallest( k, points, key = lambda point: point[0]**2 + point[1]**2  )
        
        return k_closet
       
        # ## Using heap
        # A = [] 
        # for point in points: 
        #     heapq.heappush(A, ((point[0])**2 + (point[1])**2, point))

        # B = [] 
        # for i in range(k):
        #     B.append(heapq.heappop(A))
        # return [x[1] for x in B] 
        
        ## Custom sorting function using distance -> Fastest among these 3 solutions !!
        # points.sort(key=lambda point: (point[0]**2 + point[1]**2))
        # return points[:k]
