# 1418. 点菜展示表

class Solution:
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
        dishes = set()
        table_menu = {}
        for order in orders:
            dishes.add(order[2])
            table = int(order[1])
            if table not in table_menu:
                table_menu[table] = {}
            if order[2] not in table_menu[table]:
                table_menu[table][order[2]] = 0
            table_menu[table][order[2]] += 1
        head = list(dishes)
        head.sort()
        head.insert(0, "Table")
        tables = list(table_menu.keys())
        tables.sort()
        res = [head]
        for table in tables:
            menu = [str(table)]
            for dish in head[1:]:
                if dish in table_menu[table]:
                    menu.append(str(table_menu[table][dish]))
                else:
                    menu.append('0')
            res.append(menu)
        return res


if __name__ == '__main__':
    print(Solution().displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))
    print(Solution().displayTable([["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]))
    print(Solution().displayTable([["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]))