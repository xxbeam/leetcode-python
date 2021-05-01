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
            if i.id == id:
                queue.append(map.get(id))

        while queue:
            employees = queue.pop()
            count += employees.importance
            for i in employees.subordinates:
                queue.append(map.get(i))
        return count
