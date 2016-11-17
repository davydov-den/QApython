__author__ = 'Давыдов'

# coding: utf-8

class Lion():

    def __init__ (self,status_list,argument_list,action_list,current_stat,current_act,table_act,table_stat,last_arg):
        self.status = status_list
        self.arguments = argument_list
        self.action = action_list
        self.current_action = current_act
        self.current_status = current_stat
        self.table_of_action = table_act
        self.table_of_status = table_stat
        self.last_argument =  last_arg

    def getStatus(self):
        return self.current_status

    def getAction(self):
        return self.current_action

    def sendData(self, arg):
        i = -1
        if arg in self.arguments:
            i = self.arguments.index(arg)
        j = 1
        if self.current_status == "сытый":
            j = 0
        self.current_status = self.table_of_status[j][i]
        self.current_action = self.table_of_action[j][i]
        if i > -1:
            self.last_argument = arg
        else:
            self.last_argument = None






if __name__  == '__main__':

    status = ["сытый","голодный"]
    argument = ["антилопа", "охотник", "дерево"]
    action = ["спать","убежать","смотреть","съесть","ничего не делать"]
    current_status = status[0]
    current_action = action[4]
    table_of_action = [
        [action[0],action[1],action[2]],
        [action[3],action[4],action[4]]
    ]
    table_of_status = [
        [status[1],status[1],status[1]],
        [status[0],status[1],status[1]]
    ]

    lion = Lion(status,argument,action,current_status,current_action,table_of_action,table_of_status,None)


    print ("Выберите слово: антилопа, охотник, дерево")
    print("Для выхода введите слово выход")

    while True:
        result = input()
        if result in argument:
            lion.sendData(result)
            print ("Лев должен ",lion.getAction()," и теперь он ",lion.getStatus(),)

        else:
            if result == "выход":
                break;
            else:
                print("Некорретный ввод")



