"""

"""

import random

from breezypythongui import EasyFrame



class election(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self)
        self.setBackground("black")
        self.addLabel(text = "2020 Election Simulation", row = 0,\
                      column = 0)
        self.addButton(text = "Simulate",  row = 1, column = 0,\
                       command = self.votes)
        self.addLabel(text = "Biden votes", row = 2, column = 0)
        self.biden = self.addTextField(text = "", row = 2, column = 1,\
                                       state = "readonly", width = 5)
        self.addLabel(text = "Your votes", row = 4, column = 0)
        self.you = self.addTextField(text = "", row = 4, column = 1,\
                                     state = "readonly", width = 5)
        self.addLabel(text = "Trump votes", row = 5, column = 0)
        self.trump = self.addTextField(text = "", row = 5, column = 1,\
                                                state = "readonly", width = 5)
        self.addLabel(text = "The winner is", row = 6, column = 0)
        self.winner = self.addTextField(text = "", row = 6, column = 1)
        




    def votes(self):
        f = open("votes.txt", "w+")
        candidates = ["Biden ", "You ", "Trump "]
        votes = []
        for vote in range(1000):
            f.write(random.choice(candidates))
            
        f.close()
        file = open("votes.txt","r")
        names = file.read()
        votes = names.split()
        
        bidenVotes = votes.count("Biden")
        youVotes = votes.count("You")
        trumpVotes = votes.count("Trump")
        self.biden.setText(bidenVotes)
        self.you.setText(youVotes)
        self.trump.setText(trumpVotes)

        if youVotes > trumpVotes:
            if youVotes > bidenVotes:
                self.winner.setText("You")
            elif youVotes == bidenVotes:
                self.winner.setText("Tied")
            else:
                self.winner.setText("Biden")
        elif youVotes > bidenVotes:
            if youVotes > trumpVotes:
                self.winner.setText("You")
            elif youVotes == trumpVotes:
                self.winner.setText("Tied")
            else:
                self.winner.setText("Trump")
        elif bidenVotes > youVotes:
            if bidenVotes > trumpVotes:
                self.winner.setText("Biden")
            elif bidenVotes == trumpVotes:
                self.winner.setText("Tied")
            else:
                self.winner.setText("Trump")
        elif bidenVotes > trumpVotes:
            if bidenVotes > youVotes:
                self.winner.setText("Biden")
            elif bidenVotes == youVotes:
                self.winner.setText("Tied")
            else:
                self.winner.setText("You")
        elif trumpVotes > bidenVotes:
            if trumpVotes > youVotes:
                self.winner.setText("Trump")
            elif trumpVotes == youVotes:
                self.winner.setText("Tied")
            else:
                self.winner.setText("You")
        else:
            self.winner.setText("broken")
        
        
        
        

        
        







def main():
    election().mainloop()

if __name__ == "__main__":
    main()
