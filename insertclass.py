class RandomizedSet:
    def __init__(self):
       self.set = set()

    def insert(self, val:int) -> bool:
        if val not in self.set:
            self.set.add(val)
            return True

        return False
    
    def remove(self, val:int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True

        return False

    def getRandom(self) -> int:
        pass


def solve(func):
    from solve import cin, parr
    ans = []
    t = cin('int')
    for i in range(t):
        nums = cin('arr')
        ans.append(func(nums))
    parr(ans)

if __name__ == "__main__":
    rset = RandomizedSet()

