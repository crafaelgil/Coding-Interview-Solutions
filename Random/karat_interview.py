"""
We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

Sample input:

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

Sample output:

findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
findContiguousHistory(user0, user2) => [] (empty)
findContiguousHistory(user0, user0) => ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
findContiguousHistory(user2, user1) => ["a"]
findContiguousHistory(user5, user2) => ["a"]
findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]

n: length of the first user's browsing history
m: length of the second user's browsing history
"""
import collections

def findContiguousHistory(user0, user1):
    if not user0 or not user1:
        return []

    ans = []
    start = 0

    for i in range(len(user0)):
        for j in range(len(user1)):
            if user0[i] == user1[j]:
                start = i
                while i + 1 < len(user0) and j + 1 < len(user1) and user0[i+1] == user1[j+1]:
                    i+=1
                    j+=1
                ans.append(user0[start:i+1])

    max_len = 0
    result = []

    for i in range(len(ans)):
        if max_len < len(ans[i]):
            max_len = len(ans[i])
            result = ans[i]

    return result

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]


# #Time Complexity: O(n*len(subdomains))
# #Space Complexity : O(n*len(subdomains))
# def calculateClicksByDomain(counts):
#     if not counts:
#         return []

#     ans = collections.defaultdict(int)

#     for count in counts: #O(n)
#         num_visits, domain = count.split(",") #O(len(count))
#         num = int(num_visits) #O(1)
#         subdomains = domain.split(".") #O(len(subdomain))
#         #O(n + len(subdo) + len(count)) = O(max(n, ))
#         for i in range(len(subdomains)):
#             ans['.'.join(subdomains[i:])] += num

#     return ans

# counts = [
#     "900,google.com",
#     "60,mail.yahoo.com",
#     "10,mobile.sports.yahoo.com",
#     "40,sports.yahoo.com",
#     "300,yahoo.com",
#     "10,stackoverflow.com",
#     "20,overflow.com",
#     "5,com.com",
#     "2,en.wikipedia.org",
#     "1,m.wikipedia.org",
#     "1,mobile.sports",
#     "1,google.co.uk"
# ]

# print(calculateClicksByDomain(counts))

