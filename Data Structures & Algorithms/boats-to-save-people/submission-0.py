class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right = 0, len(people) - 1
        people.sort()
        result = 0

        while(left < right):
            if(people[left] + people[right] <= limit):
                result +=1
                left +=1
                right -=1
            else:
                 result +=1
                 right -=1
        
        return result + 1 if (left == right) else result