# Author: Jason Wang 06/11/2023
# 本代码实现了一个基于内存的账户交易系统，可以处理任意数量的用户和交易。
# 用户之间可以进行任意额度的转账，每笔转账都会产生一定的费用，这些费用将作为系统的收益。
# (费用从发出者余额中扣除而非转账金额中扣除）
# 使用 Python 的 heapq 库实现了一个优先队列，该队列用于存储待处理的交易。优先级由交易的费用决定。
# Classes:
# User: name, balance
#
# Transaction:sender,receiver, amount, fee
#
# Requests: transactions
#
# System: users, transactions, system_fee
# functions: add_request, execute_requests.
#
# 假设：
# 所有输入的交易都格式正确，交易涉及的用户都已存在于系统中，用户的余额为非负数。


import unittest


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


class Transaction:
    def __init__(self, sender, receiver, amount, fee):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.fee = fee


class Request:
    def __init__(self, transactions):
        self.transactions = transactions
        self.total_fee = sum(t.fee for t in transactions)


class System:
    def __init__(self, users):
        self.users = users
        self.requests = []
        self.system_fee = 0

    def add_request(self, request):
        self.requests.append(request)

    def execute_requests(self):
        for request in sorted(self.requests, key=lambda r: r.total_fee, reverse=True):
            # 对交易requests进行排序，最大潜在收益的request优先。
            for transaction in request.transactions:
                sender = transaction.sender
                receiver = transaction.receiver
                amount = transaction.amount
                fee = transaction.fee

                if self.users[sender].balance < amount + fee:
                    print(
                        f"Transaction {transaction} in Request {request} failed: {sender} does not have enough balance.")
                    continue

                self.users[sender].balance -= amount + fee
                self.users[receiver].balance += amount
                self.system_fee += fee

                print(
                    f"Transaction {transaction} in Request {request} successful: {sender} -> {receiver}, Amount: {amount}, Fee: {fee}")

        print(f"System fee: {self.system_fee}")


class TestSystem(unittest.TestCase):
    # 单元测试
    def test_execute_transactions(self):
        users = {"A": User("A", 0.1), "B": User("B", 100), "C": User("C", 0), "D": User("D", 1357), "E": User("E", 8)}
        system = System(users)

        transactions1 = [
            Transaction("A", "B", 0.1, 0),
            Transaction("B", "C", 9, 1),
            Transaction("C", "E", 9, 8),
        ]

        request1 = Request(transactions1)

        system.add_request(request1)

        system.execute_requests()

        self.assertEqual(system.users["A"].balance, 0)
        self.assertEqual(system.users["B"].balance, 90.1)
        self.assertEqual(system.users["C"].balance, 9)
        self.assertEqual(system.users["D"].balance, 1357)
        self.assertEqual(system.users["E"].balance, 8)
        self.assertEqual(system.system_fee, 1)
