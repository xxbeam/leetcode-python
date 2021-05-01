# 690. 员工的重要性

class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: list[Employee], id: int) -> int:
        queue = []
        map = {}
        count = 0
        for i in employees:
            map[i.id] = i

        queue.append(id)

        while queue:
            next_id = queue.pop()
            employer = map.get(next_id)
            count += employer.importance
            queue += employer.subordinates
        return count
