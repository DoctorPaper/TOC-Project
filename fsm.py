from transitions.extensions import GraphMachine

from utils import send_text_message, get_menu, get_random_recommend



class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        self.machine.get_graph().draw("FSM.png", prog= 'dot')

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "找好茶"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "找新鮮"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "找奶茶"

    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "找拿鐵"

    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "本日推薦"

    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "使用教學"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        menu =  get_menu(1)
        send_text_message(reply_token, menu)
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        menu =  get_menu(2)
        send_text_message(reply_token, menu)
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        menu =  get_menu(3)
        send_text_message(reply_token, menu)
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")

    def on_enter_state4(self, event):
        print("I'm entering state4")

        reply_token = event.reply_token
        menu =  get_menu(4)
        send_text_message(reply_token, menu)
        self.go_back()

    def on_exit_state4(self):
        print("Leaving state4")

    def on_enter_state5(self, event):
        print("I'm entering state5")

        reply_token = event.reply_token
        recommend = get_random_recommend()
        send_text_message(reply_token, recommend)
        self.go_back()

    def on_exit_state5(self):
        print("Leaving state5")

    def on_enter_state6(self, event):
        print("I'm entering state6")

        #reply_token = event.reply_token
        #send_text_message(reply_token, "")
        self.go_back()

    def on_exit_state5(self):
        print("Leaving state5")