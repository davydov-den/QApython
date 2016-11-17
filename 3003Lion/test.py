__author__ = 'Давыдов'

# coding: utf-8
import unittest
import main

class Test_Leon(unittest.TestCase):
    status = None
    argument = None
    action = None
    current_status = None
    current_action = None
    table_of_action = None
    table_of_status = None
    current_agr = None

    def setUp(self):
        self.status = ["status","status2"]
        self.argument = ["argument","argument2"]
        self.action = ["action","action2"]
        self.current_action = self.action[0]
        self.current_status =self.status[0]
        self.current_agr = self.argument[0]
        self.table_of_action = [
            [self.action[0],self.action[1]],
            [self.action[0],self.action[1]]
        ]
        self.table_of_status = [
            [self.status[0]],
            [self.status[0]]
        ]
        self.l= main.Lion(self.status,self.argument,self.action,self.current_status,self.current_action,self.table_of_action,self.table_of_status,self.current_agr)

    def test_correctData(self):
        self.l.sendData(self.current_agr)
        self.assertEqual(self.l.last_argument,self.current_agr,"некорретная передача")
        self.assertEqual(self.l.current_status,self.status[0],"не правильный статус!")
        
    def test_uncorrectData(self):
        self.l.sendData("funny child")
        self.assertEqual(self.l.last_argument,None,"некорректная обработка")

    def test_getAction(self):
        self.assertEqual(self.action[0],self.l.getAction(),"не правильное действие")

    def test_getStatus(self):
        self.assertEqual(self.status[0],self.l.getStatus(),"не правильный статус")

    def test_init(self):
        self.assertEqual(self.status,self.l.status,"не правильный список состояний")
        self.assertEqual(self.action,self.l.action,"не правильный список действий")
        self.assertEqual(self.argument,self.l.arguments,"не правильный список входный слов")
        self.assertEqual(self.current_action,self.l.current_action,"не правильно инициализировано текущее действие")
        self.assertEqual(self.current_status,self.l.current_status,"не правильно инициализировано текущее состояние")
        self.assertEqual(self.current_agr,self.l.last_argument,"не правильно передано текущее входное слово")
        self.assertEqual(self.table_of_action,self.l.table_of_action,"не правильно передана таблица соответствий для действий")
        self.assertEqual(self.table_of_status,self.l.table_of_status,"не правильно передана таблица соответствий для состояний")


if __name__ == "__main__":
    unittest.main()
