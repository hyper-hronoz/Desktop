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
#     return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

# @lru_cache(None)
# def f(h):
#     if (sum(h) >= 144):
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
#     h = 3, i
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
        node.children.append(Node((node.value[0] + 1, node.value[1])))
        node.children.append(Node((node.value[0], node.value[1] + 1)))
        node.children.append(Node((node.value[0] * 2, node.value[1])))
        node.children.append(Node((node.value[0], node.value[1] * 2)))
        return node



class Game:
    def __init__(self, first_heep, condition) -> None:
        self.condition = condition
        self.first_heep = first_heep
        self.first_task_answer = []
        self.second_task_answer = []
        self.third_task_answer = []

    def first_task(self, counter, break_point=0):
        if (counter >= break_point):
            return self.first_task_answer
        tree: Node = Tree().create_tree(Node((self.first_heep, counter))) 

        p1_nodes = [p1 for p1 in tree.children]
        if not any([self.condition(i.value) for i in p1_nodes]):
            for p1 in p1_nodes:
                w1_nodes = [w1 for w1 in p1.children]
                if any([self.condition(i.value) for i in w1_nodes]):
                    self.first_task_answer.append(counter)

        return self.first_task(counter + 1, break_point)

    def second_task(self, counter, break_point=0):
        if (counter >= break_point):
            return sorted(list(set(self.second_task_answer)))
        tree: Node = Tree().create_tree(Node((self.first_heep, counter))) 

        pretendent = ""

        p1_nodes = [p1 for p1 in tree.children]
        if not any([self.condition(i.value) for i in p1_nodes]):
            # print("p1", [i.value for i in p1_nodes])
            for p1 in p1_nodes:
                w1_nodes = [w1 for w1 in p1.children]
                if not any([self.condition(i.value) for i in w1_nodes]):
                    c = 0
                    for w1 in w1_nodes:
                        p2_nodes = [p2 for p2 in w1.children]
                        if any([self.condition(i.value) for i in p2_nodes]):
                            c += 1
                            pretendent = counter
                    if (c == 4):
                        self.second_task_answer.append(pretendent)

        return self.second_task(counter + 1, break_point)

def condition(value: tuple):
    if (value[1] * value[0] >= 144):
        return True
    return False

game = Game(3, condition)
print(min(game.first_task(1, 100)))
print(game.second_task(1, 100)) # range

# def second_task_first_part(self, counter, break_point=0):
#     tree: Node = Tree().create_tree(Node((self.first_heep, counter))) 
#     if (counter >= break_point):
#         return sorted(list(set(self.second_task_first_answer)))[:-1]
#     p1_nodes = [p1 for p1 in tree.children]
#     if not any([self.condition(i.value) for i in p1_nodes]):
#         w1_all_nodes = []
#         p2_all_nodes = []
#         for p1 in p1_nodes:
#             w1_all_nodes += [w1 for w1 in p1.children]
#         if not any([self.condition(i.value) for i in w1_all_nodes]):
#             for w1 in w1_all_nodes:
#                 p2_all_nodes += [p2 for p2 in w1.children]
#         if any([self.condition(p2.value) for p2 in p2_all_nodes]):
#             self.second_task_first_answer.append(counter)

#     return self.second_task_first_part(counter + 1, break_point)
