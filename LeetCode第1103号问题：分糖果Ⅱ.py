class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        give_candy = 1
        queue = [0 for _ in range(num_people)]
        if candies == 0:
            return queue

        while candies:
            for i in range(num_people):
                if candies > give_candy:
                    queue[i] += give_candy
                    candies = candies - give_candy
                    give_candy += 1
                else:
                    queue[i - 1] += candies
                    candies = 0
                    break
        return queue


if __name__ == "__main__":
    s = Solution()
    candies = 7
    num_people = 4
    print s.distributeCandies(candies, num_people)