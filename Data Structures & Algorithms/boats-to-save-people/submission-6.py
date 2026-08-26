class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left, right, result = 0, len(people) - 1, 0

        while(left < right):
            total = people[left] + people[right]

            if total > limit:
                right -=1
            else:
                left +=1
                right -=1
            result +=1
        return result + 1 if left == right else result
            