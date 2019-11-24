from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button


class Board(GridLayout):
    def __init__(self, queens=[-1]*8):
        GridLayout.__init__(self)
        self.cols = len(queens)
        self.solution = 1
        self.originalQueens = queens
        self.queens = list(queens)
        self.solutions = list()
        self.images = list()
        for i in range(len(queens)):
            self.images.append(list())
            for j in range(len(queens)):
                self.images[i].append(Image())
                self.add_widget(self.images[i][j])
        self.newSolution = Button(text="Generate new solution")
        self.newSolution.bind(on_press=self.generate_solution)
        self.brute_force()
        self.solutionLabel = Label(text="Solution number " + str(self.solution))
        self.print_queens()
        self.add_widget(self.newSolution)
        self.add_widget(self.solutionLabel)

    def generate_solution(self, touch):
        self.solution += 1
        self.queens = list(self.originalQueens)
        self.brute_force()
        self.print_queens()

    def brute_force(self, index=0):
        if index == len(self.queens):
            if self.queens not in self.solutions:
                self.solutions.append(self.queens)
                return True
            return False
        for x in range(len(self.queens)):
            predetermined = True
            if self.queens[index] == -1:
                self.queens[index] = x
                predetermined = False
            if self.check_placement(index) and self.brute_force(index + 1):
                return True
            if predetermined:
                break
            self.queens[index] = -1
        return False

    def check_placement(self, index):
        for i, q in enumerate(self.queens):
            if i != index and (self.queens[index] == q or self.queens[index] - index == q - i or self.queens[index] + index == q + i) and q != -1:
                return False
        return True

    def print_queens(self):
        self.solutionLabel.text = "Solution number " + str(self.solution)
        for i in range(len(self.queens)):
            for j in range(len(self.queens)):
                if self.queens[i] == j:
                    print(1, end=" ")
                    self.images[i][j].source = "queen.jpg"
                else:
                    print(0, end=" ")
                    self.images[i][j].source = "white.jpg"
            print()
        print()


class TestApp(App):
    def build(self):
        self.title = 'Eight Queens Brute Force'
        return Board()


TestApp().run()
