import numpy as np
import pandas as pd
from tkinter import *
from tkinter import filedialog

matrix = pd.read_csv('dane.csv')
textMessage = []
textPlayer = ''


def add_file():
    matrix = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    print(matrix)


#matrix = np.loadtxt('dane.txt', usecols=range(3), dtype=int)
print(matrix, end='\n')
print('\n')
df = pd.DataFrame(matrix)
print(df)
iteration_number = 3
strategy_A = []
strategy_A_value = []
strategy_B = []
strategy_B_value = []


class AlgorithmBrowna:

    def iteration_of_strategy(player, strategy_index):
        if player == 'A':
            if strategy_index in strategy_A:
                array = np.array(strategy_A_value)
                strategy_A_value[strategy_A.index(strategy_index)] = array[strategy_A.index(strategy_index)] + 1
            else:
                strategy_A.append([strategy_index])
                strategy_A_value.append([1])
        else:
            if strategy_index in strategy_B:
                array = np.array(strategy_B_value)
                strategy_B_value[strategy_B.index(strategy_index)] = array[strategy_B.index(strategy_index)] + 1
            else:
                strategy_B.append([strategy_index])
                strategy_B_value.append([1])

    def show_frequency_of_use_strategy(array, strategy_label, player):
        length = len(array)
        print(player)
        if player == "A":
            for i in range(0, length):
                frequency = array[i]
                print('Strategia: ')
                print(strategy_label[i])
                print((frequency[0] / (iteration_number + 1)))
                textMessage.append((frequency[0] / (iteration_number + 1)))
        else:
            for i in range(0, length):
                frequency = array[i]
                print('Strategia: ')
                print(strategy_label[i])
                print((frequency[0] / (iteration_number + 1)))
                textMessage.append((frequency[0] / (iteration_number + 1)))

    def lower_value_of_the_game(array):
        print(np.argmax(player_B_score))
        print(np.argmin(array) / (iteration_number + 1))

    def top_value_of_the_game(array):
        print(np.argmax(array) / (iteration_number + 1))

    def get_frequency_A(self):
        return AlgorithmBrowna.show_frequency_of_use_strategy(strategy_A_value)

    def get_frequency_B(self):
        return AlgorithmBrowna.show_frequency_of_use_strategy(strategy_B_value)

    def brown_algorithm(self):
        player_A_strategy = df.values
        player_B_strategy = df.transpose().values
        player_A_score = player_A_strategy[1]
        AlgorithmBrowna.iteration_of_strategy('A', 1)
        best_strategy_for_B = np.argmin(player_A_score)
        AlgorithmBrowna.iteration_of_strategy('B', best_strategy_for_B)
        player_B_score = player_B_strategy[best_strategy_for_B]
        for i in range(0, iteration_number):
            best_strategy_for_A = np.argmax(player_B_score)
            AlgorithmBrowna.iteration_of_strategy('A', best_strategy_for_A)
            player_A_score = player_A_score + player_A_strategy[best_strategy_for_A]
            best_strategy_for_B = np.argmin(player_A_score)
            AlgorithmBrowna.iteration_of_strategy('B', best_strategy_for_B)
            player_B_score = player_B_score + player_B_strategy[best_strategy_for_B]

        print(player_A_score)
        print(player_B_score)
        print(strategy_A)
        print(strategy_A_value)
        print(strategy_B)
        print(strategy_B_value)
        print(strategy_A_value)
        print('Czestotliwosc A')
        AlgorithmBrowna.show_frequency_of_use_strategy(strategy_A_value, strategy_A, "A")
        print('Czestotliwosc B')
        AlgorithmBrowna.show_frequency_of_use_strategy(strategy_B_value, strategy_B, "B")

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Brown")
        self.pack(fill=BOTH, expand=1)
        addFileButton = Button(self, text="Add file...", command=add_file)
        addFileButton.place(x=50, y=50)
        runButton = Button(self, text="Run", command=self.run())
        runButton.place(x=50, y=100)

    def run(self):
        AlgorithmBrowna.brown_algorithm(self)
        Window.print(self)
        #text = Label(self, text=textMessage)
        #text.pack()

    def print(self):
        for i in range(0, len(textMessage)):
            text = Label(self, text=textMessage[i])
            text.pack()

root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()
