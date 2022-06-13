# def convert_base(number, to_base=10, from_base=10):
#     if isinstance(number, str):
#         number = int(number)
#     alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     if number < to_base:
#         return alphabet[number]
#     else:
#         return convert_base(number // to_base) + alphabet[number % to_base]

# counter = 0
# for i in convert_base(4**700 + 4**100 - 16**100 - 64, to_base=4):
#     if i == "3":
#         counter += 1

# print(counter)

# string = "1" * 91

# while "2222" in string or "1111" in string:
#     if "2222" in string:
#         string = string.replace("2222", "11")
#     else:
#         string = string.replace("1111", "22")

# print(string)

# def implication(x, y):
#     if (x == 1 and y == 0):
#         return False
#     return True

# def main(a, x):
#     return implication(not(x % a == 0), implication((x % 24 == 0), not(96 % x == 0)))

# for a in range(1, 100):
#     array = []
#     for x in range(1, 10000):
#         array.append(main(a,x))
#     if all(array):
#         print(a)

# def main(n):
#     if n == 1:
#         return 1
#     elif n % 2 == 0:
#         return n + main(n - 1)
#     elif n > 1 and n % 2 == 1:
#         return 2 * main(n - 1) + main(n - 2)

# print(main(20))


# from math import inf


# with open("var5.txt", "r") as file:
#     counter = 0
#     text = [i.replace("\n", "") for i in file.readlines()]
#     maximal = -inf
#     for i in range(1, len(text)):
#         first_number = text[i - 1]
#         second_number = text[i]
#         if (int(first_number[-1]) % 2 == 1 and int(second_number[-1]) % 2 == 1 and second_number[-1] == first_number[-1]):
#             counter += 1
#             if (new_max := abs(int(first_number) * int(second_number))) > maximal:
#                 maximal = new_max
#                 print(first_number, second_number)
#     print(counter, maximal)

# from functools import lru_cache


# def moves(h):
#     a, b = h
#     return (a + 2, b), (a, b + 2), (a * 2, b), (a, b * 2)

# @lru_cache(None)
# def f(h):
#     if (sum(h) >= 122):
#         return "END"
#     elif (any(f(x) == "END" for x in moves(h))):
#         return "П1"
#     elif (all(f(x) == "П1" for x in moves(h))):
#         return "В1"
#     elif (any(f(x) == "В1" for x in moves(h))):
#         return "П2"
#     elif (all(f(x) == "П2" or f(x) == "П1" for x in moves(h))):
#         return "В2"

# for i in range(1, 100):
#     h = 2, i
#     print(i, f(h))


# class Node:
#     def __init__(self, value) -> None:
#         self.value: tuple = value

#         self.first_value: Node = None
#         self.second_value: Node = None
#         self.third_value: Node = None
#         self.fourth_value: Node = None


# class Tree:
#     def __init__(self, initional_node: Node) -> None:
#         self.initional_node = initional_node

#     def create_tree(self):
#         self.initional_node = self.append_to_one_node(self.initional_node)

#         self.initional_node.first_value = self.append_to_one_node(self.initional_node.first_value)
#         self.initional_node.second_value = self.append_to_one_node(self.initional_node.second_value)
#         self.initional_node.third_value = self.append_to_one_node(self.initional_node.third_value)
#         self.initional_node.fourth_value = self.append_to_one_node(self.initional_node.fourth_value)

#     def append_to_one_node(self, node: Node):
#         node.first_value = Node((node.value[0] + 2, node.value[1]))
#         node.second_value = Node((node.value[0], node.value[1] + 2))
#         node.third_value = Node((node.value[0] * 2, node.value[1]))
#         node.fourth_value = Node((node.value[0], node.value[1] * 2))

#         return node


# node = Node((3, 30))

# tree = Tree(node)

# tree.create_tree()

# tree.initional_node.__dict__
import sys
sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, value: tuple) -> None:
        self.value: tuple = value
        self.children: list = []


class Tree:

    def create_tree(self, node: Node):
        node = self.fill_node(node)

        for i in range(0, 4):
            node.children[i] = self.fill_node(node.children[i])

        for i in range(0, 4):
            for j in range(0, 4):
                node.children[i].children[j] = self.fill_node(
                    node.children[i].children[j])

        return node

    def fill_node(self, node: Node):
        node.children.append(Node((node.value[0] + 2, node.value[1])))
        node.children.append(Node((node.value[0] * 2, node.value[1])))
        node.children.append(Node((node.value[0], node.value[1] + 2)))
        node.children.append(Node((node.value[0], node.value[1] * 2)))
        return node



class Game:
    def __init__(self, condition) -> None:
        self.condition = condition
        self.first_task_answer = []
        self.second_task_answer = []
        self.third_task_answer = []

    def second_task(self, counter, break_point=0):
        if (counter <= break_point):
            return self.second_task_answer[-2:]

        tree: Node = Tree().create_tree(Node((3, counter))) 
        
        if any([self.condition(i.value) for i in tree.children]):
            return self.second_task(counter - 1, break_point)

        w1_lose_nodes = []
        for p1_node in tree.children:
            w1_nodes = [w1_node for w1_node in p1_node.children]
            if not any([self.condition(i.value) for i in w1_nodes]):
                w1_lose_nodes.append(w1_nodes) # двумерная матрица нод, которые ведут к проигрышу Вани

        if not len(w1_lose_nodes):
            return self.second_task(counter - 1, break_point)

        for p1 in w1_lose_nodes:
            for w1 in p1:
                p2_win_variants = [p2 for p2 in w1.children]
                if any( [self.condition(x.value) for x in p2_win_variants] ) == True:
                    self.second_task_answer.append(counter)
                    self.second_task_answer = sorted(list(set(self.second_task_answer)))

        return self.second_task(counter - 1, break_point)

def condition(value: tuple):
    if (sum(value) >= 122):
        return True
    return False

game = Game(condition)
print(game.second_task(100))

