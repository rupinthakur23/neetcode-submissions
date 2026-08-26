class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        left, right = 0, len(people) - 1
        people.sort()

        while left < right:
            if (people[left] + people[right]) > limit:
                right -=1
            else:
                right -=1
                left +=1
            result +=1

        return result + 1 if left == right else result
        