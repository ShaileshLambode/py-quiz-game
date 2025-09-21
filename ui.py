from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self,quiz_brain : QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler !")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text="Score : 00",fg="white",bg=THEME_COLOR,font=("Ariel",20,"bold"))
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(height=250,width=300,bg="white")
        self.que_text = self.canvas.create_text(150,125,width=280,text="Some Question is here !!",fill=THEME_COLOR,font=("Ariel",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.get_next_que()

        green_img = PhotoImage(file="./images/true.png")
        self.green_btn = Button(image=green_img,command=self.true_pressed)
        self.green_btn.grid(row=2, column=0)

        red_img = PhotoImage(file="./images/false.png")
        self.red_btn = Button(image=red_img,command=self.false_pressed)
        self.red_btn.grid(row=2 ,column=1)

        self.window.mainloop()

    def get_next_que(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score:{self.quiz.score}")
            que_text = self.quiz.next_question()
            self.canvas.itemconfig(self.que_text,text=que_text)
        else:
            self.canvas.itemconfig(self.que_text,text=f"You have reached at end \nYour score is {self.quiz.score}/10")
            self.green_btn.config(state="disabled")
            self.red_btn.config(state="disabled")
            self.canvas.config(bg="white")


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else :
            self.canvas.config(bg="red")
        self.window.after(1000,func=self.get_next_que)
        # self.canvas.config(bg="white")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)