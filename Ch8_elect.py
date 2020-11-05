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

        if youVotes > bidenVotes and trumpVotes:
            self.winner.setText("You")
        elif bidenVotes > youVotes and trumpVotes:
            self.winner.setText("Biden")
        else:
            self.winner.setText("Trump")
        
        
        
        

        
        







def main():
    election().mainloop()

if __name__ == "__main__":
    main()
