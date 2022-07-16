from tkinter import *
import tkinter as tk
import pygame
import os
from PIL import Image, ImageTk
from winsound import *
from tkinter.ttk import Button, Scrollbar, Radiobutton, Style
import pandas as pd
import requests
from io import BytesIO
####################the main window specifications:
window=Tk()
window.title('project CSCI102')
window.resizable(False, False)

# #the window size + to keep it in center:   
# window_width = 500
# window_height = 500
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight() 
# center_x = int(screen_width/2 - window_width / 2)
# center_y = int(screen_height/2 - window_height / 2)
# window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.geometry("500x500+420+100") 
## 500x500= dimensions of the window (first 500= width, second 500 = height)
### 420+100 = position (420=width, 100=height)

# ##===============================================================================
# #sound automatically
pygame.init()
mypath=os.path.dirname(os.path.realpath(__file__))
start_sound= pygame.mixer.Sound(mypath+'\\Soundtracks\\hello.wav').play()
# ##===============================================================================
# ###the favicon code:
p1 = PhotoImage(file = mypath+ '\\Images\\favicon.png')
window.iconphoto(True, p1)

# ##===============================================================================
# ##the background code:
bg = PhotoImage(file=mypath+'\\Images\\Films.png')

#create a canvas,  The Canvas is a rectangular area intended for drawing pictures or other complex layouts. You can place graphics, text, widgets or frames on a Canvas.
start_canvas = Canvas(window, width=700, height=500)
start_canvas.pack(fill="both", expand=True)
start_canvas.create_image(0,0, image=bg, anchor="nw")

#create text
start_canvas.create_text(258,230, text="Welcome!", font=("Cabin Sketch",70), fill="white")
### 263= width (x axis)
### 250= height (y axis)
# ######################################################################################################################################

# sound of the button:
play = lambda: PlaySound(mypath+'\\Soundtracks\\click.wav', SND_FILENAME)


questions = [
    {"question": "How are you feeling today?",
     "answers": ("Happy", "Neutral",
                 "Sad")},
    {"question": "What's the occasion?",
    "answers": ("Date" ,"Alone","with Family", "with Friends")},
    {"question": "Genre of the film?",
    "answers": ("Romance","Action" ,"Comedy", "Horror")},
    {"question":    "Year published in it the film?",
    "answers": ("Doesn't matter","2020-2021" ,"Last 5 years", "Last 15 years")}
    ]

##

def open(e):
    window.destroy()
    class App(Tk): ### we used a class because we will open several windows next
        def __init__(survey): ### window's name = survey
            super().__init__() ### The super() function in Python makes class inheritance more manageable and extensible. 
            #The function returns a temporary object that allows reference to a parent class by the keyword super.

            # # root_width = 500
            # root_height = 500
            # screen_width = survey.winfo_screenwidth()
            # screen_height = survey.winfo_screenheight() 
            # center_x = int(screen_width/2 - root_width / 2)
            # center_y = int(screen_height/2 - root_height / 2)
            # survey.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')

            survey.geometry("500x500+420+100") 
            ## 500x500= dimensions of the window (first 500= width, second 500 = height)
            ### 420+100 = position (420=width, 100=height)

            survey.title("Survey Window")  # set the window title
            survey.resizable(False, False)  # make window unresizable by width
            mypath= os.path.dirname(os.path.realpath(__file__))

            p1 = PhotoImage(file = mypath+ '\\Images\\favicon.png')
            survey.iconphoto(True, p1)

            bg = PhotoImage(file=mypath+'\\Images\\Films.png')

            canv_frame = Frame(survey) 
            survey_canv = Canvas(canv_frame, bg='#1F1F1F', width=420)  
            survey_canv.pack()

            # add scrolling when mouse wheel is rotated
            survey_canv.bind_all("<MouseWheel>", lambda event: survey_canv.yview_scroll(-1 * (event.delta // 120), "units"))
            #####  you need to divide event.delta by 120 (or some other factor depending on how fast you want the scroll)
            ##### -1 = you want to scroll 1 question per scroll
            
            survey_canv.pack(fill='both', expand=True, side=LEFT) 
            scrollbar = Scrollbar(canv_frame, command=survey_canv.yview) 
            ###command= survey_canv.yview to connect the scrollbar with the mousewheel
            survey_canv["yscrollcommand"] = scrollbar.set
            ##### set is used to connect the scrollbar with canvas of the survey 
            #### y scrollbar to make the scrollbar appear on the y axis
            
            scrollbar.pack(fill=Y, side=LEFT)  # pack the Scrollbar
            #### fill=Y (to fill along the y axis)


            for question_id, counter in enumerate(questions, 1):
                ###The enumerate () function allows you to loop over an iterable object and keep track of how many iterations have occurred.
                qaframe = Frame(survey_canv, bg="#1F1F1F")  # create the question-answers (QA) frame
                l= tk.Label(qaframe,text=counter['question'], font=("Cabin Sketch",20), fg='white', bg="#1F1F1F").pack()
                aframe = Frame(qaframe,  bg="#1F1F1F")  # create the answers frame
                # Create the question variable and add it to the variables list
                question_var = IntVar(survey)
                counter["variable"] = question_var
                # we used Style to change the background of the radiobuttons
                style1 = Style(aframe)
                ### we used configure to edit the color and font size and font family of the radiobuttons
                style1.configure("TRadiobutton", background="#1F1F1F",foreground = "white", font = ("Cabin Sketch", 14)) ### foreground for the color of the text itself (answers)
                for answer_id, answer in enumerate(counter["answers"]):
                    radiobutton=Radiobutton(aframe, variable=question_var, text=answer,  value=answer_id).pack()
                    #The Radio Button's variable will be: A numeric value matching the choice the learner made.
                    #### variable of the radiobutton = question_var to print value of the selected choices
                    ### value = answer_id which is the index of the answer (0,1,2..etc)
                aframe.pack(fill=Y)  # pack the answers frame
                survey_canv.create_window(210, question_id * 175, window=qaframe)  # insert the QA frame into the Canvas
            
        
            canv_frame.pack(fill=BOTH, expand=YES)  # pack the canvas frame
            submit_button= tk.Button(survey, text="Submit", command=survey.submit, bg='gray', font=("Calibri 12 bold"))
            submit_button.pack(fill=X)  # create the "Submit" button
            survey.update()  # update everything to get the right scrollregion.
            survey_canv.configure(scrollregion=survey_canv.bbox("all"))  # set the canvas scrollregion
            #returns the minimum and maximum x and y coordinates of all items on canvas.
        
        def submit(survey):
            mypath=os.path.dirname(os.path.realpath(__file__))
            database=pd.read_excel(mypath+'\\DataBase\\RecommendationsUpdated.xlsx')
            counter=0
            for question in questions:
                if counter==0:
                   mood=question["variable"].get()
                elif counter==1:
                    situation=question["variable"].get()
                elif counter==2:
                    category=question["variable"].get()
                elif counter==3:
                    date_of_publication=question["variable"].get() 
                counter+=1
            choice=database.loc[(database['Mood']==mood) & (database['Situation']==situation) 
            & (database['Category']==category) & (database['Date of Publication']==date_of_publication)]
            print(choice)
            final=choice['MOVIE NAME']
            final=list(final) ###to remove name and dtype of the cell
            print(final)
            
            survey.destroy()
            
            root = Tk()
            root.title('Final Result')
            root.resizable(False, False)
            # root_width = 500
            # root_height = 500
            # screen_width = survey.winfo_screenwidth()
            # screen_height = survey.winfo_screenheight() 
            # center_x = int(screen_width/2 - root_width / 2)
            # center_y = int(screen_height/2 - root_height / 2)
            # survey.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')

            root.geometry("500x500+420+100") 
            ## 500x500= dimensions of the window (first 500= width, second 500 = height)
            ### 420+100 = position (420=width, 100=height)

            pygame.init()
            mypath=os.path.dirname(os.path.realpath(__file__))
            start_sound= pygame.mixer.Sound(mypath+'\\Soundtracks\\win.wav').play()            
            # ##===============================================================================
            # ###the favicon code:
            p1 = PhotoImage(file = mypath+ '\\Images\\favicon.png')
            root.iconphoto(False, p1)
            # ##===============================================================================
            # ###the background code:

            bg = PhotoImage(file=mypath+'\\Images\\Films.png')
            #create a canvas,  The Canvas is a rectangular area intended for drawing pictures or other complex layouts. You can place graphics, text, widgets or frames on a Canvas.
            root_canvas = Canvas(root, width=700, height=500)
            root_canvas.pack(fill="both", expand=True)
            #Set image in Canvas
            root_canvas.create_image(0,0, image=bg, anchor="nw")
            #create a label:
            for item in final:
                str(item) ##### to remove the square brackets and the quotations, to print the movie name only

            for url in list(choice['Poster']):
                r = requests.get(url)
                print(url)
            poster = Image.open(BytesIO(r.content))
            resized_poster = poster.resize((180, 250))
            
            resizedimg = ImageTk.PhotoImage(resized_poster)
            label_poster = Label(root_canvas,image=resizedimg)
            
            label_poster.pack(anchor='s', side=LEFT, padx=160, pady=90)

            #####TRANSPARENT CODE!!!!
            # images=[]
            # def create_rectangle(x,y,a,b,**options):
            #     if 'alpha' in options:
            #             # Calculate the alpha transparency for every color(RGB)
            #             alpha = int(options.pop('alpha') * 255)
            #             # Use the fill variable to fill the shape with transparent color
            #             fill = options.pop('fill')
            #             fill = root.winfo_rgb(fill) + (alpha,)
            #             image = Image.new('RGBA', (a-x, b-y), fill)
            #             images.append(ImageTk.PhotoImage(image))
            #             root_canvas.create_image(x, y, image=images[-1], anchor='nw')
            #             root_canvas.create_rectangle(x, y,a,b, **options)
            
            def change_tryagain(e):
                mypath=os.path.dirname(os.path.realpath(__file__))
                button_after= PhotoImage(file=mypath+'\\Images\\light.png')
                tryagain.config(image=button_after, bg="black", border=0)
                tryagain.image = button_after
                pygame.init()
                start_button_sound= pygame.mixer.Sound(mypath+"\\Soundtracks\\click.wav").play()
            
            def open(e):
                root.destroy()
                survey.__init__()

            def change_back_tryagain(e):
                button_before = PhotoImage(file= mypath+"\\Images\\darker.png")
                tryagain.config(image=button_before, bg="black", border=0)
                tryagain.image = button_before
           
            tryagain_img = PhotoImage(file= mypath+"\\Images\\darker.png")
            tryagain = tk.Button(root, image=tryagain_img, bg='black', fg='black')
            tryagain.config(bg="black", border=0)
            tryagain.image = tryagain_img
            tryagain.pack()

            # A window is a rectangular area that can hold one Tkinter widget 
            # C.create_window(x, y, option, ...)
            my_button_window = root_canvas.create_window(250,485,anchor="s", window=tryagain)
            tryagain.bind("<Enter>", change_tryagain) ###when you hover over the button
            tryagain.bind("<Button-1>", open) ###when you click on the button
            tryagain.bind("<Leave>", change_back_tryagain)	###when you hover out from the button

           
           
            
            # create_rectangle(30, 30,470,470, fill= "white", alpha=.5)
            root_canvas.create_text(195,50,text="Your movie suggestion is:" , font=("Times new Roman",20, "bold"), fill="red")
            root_canvas.create_text(250,100,text="\n %s " %item, font=("Times new Roman",30, "bold"), fill="red")
            
           
            #button exit:
            def exit_hover(e):
                exit["bg"] = "red"
            def exit_hover_leave(e):
                exit["bg"] = "orange"

            exit = tk.Button(root, text="Exit", font=("Calibri 14 bold"), command=lambda:[play(), root.destroy() ], bg="orange")
            exit.pack()
            exit_window = root_canvas.create_window(447,10, anchor="nw", window=exit)
            exit.bind("<Enter>", exit_hover)
            exit.bind("<Leave>", exit_hover_leave)
            
            root.mainloop()
                
    if __name__ == "__main__":  # if the App is not imported from another module,
        App().mainloop()  # create it and start the mainloop

def change(e):
    mypath=os.path.dirname(os.path.realpath(__file__))
    button_after= PhotoImage(file=mypath+'\\Images\\after.png')
    start_button.config(image=button_after, bg="black", border=0)
    start_button.image = button_after
    pygame.init()
    start_button_sound= pygame.mixer.Sound(mypath+'\\Soundtracks\\click.wav').play()

def change_back(e):
	button_before = PhotoImage(file= mypath+"\\Images\\before.png")
	start_button.config(image=button_before, bg="black", border=0)
	start_button.image = button_before


startpic = PhotoImage(file= mypath+"\\Images\\before.png")
start_button = tk.Button(window, image=startpic, bg='black', fg='black')
start_button.config(bg="black", border=0)
start_button.image = startpic
start_button.pack()

# A window is a rectangular area that can hold one Tkinter widget 
# C.create_window(x, y, option, ...)
my_button_window = start_canvas.create_window(250,485,anchor="s", window=start_button)

### Binding mouse movement with tkinter Frame. 
start_button.bind("<Enter>", change) ####'<Enter>'= when you hover over the button
start_button.bind("<Button-1>", open)  ####'<Button-1>'= when you click on the button
start_button.bind("<Leave>", change_back)  ####'<Leave>'= when you hover out from the button

###############################
#button exit:
def exit_hover(e):
 	exit["bg"] = "red"
def exit_hover_leave(e):
	exit["bg"] = "orange"

exit = tk.Button(window, text="Exit", font=("Calibri 14 bold"), command=lambda:[play(), window.destroy() ], bg="orange")
exit.pack()

# A window is a rectangular area that can hold one Tkinter widget 
# C.create_window(x, y, option, ...)
exit_window = start_canvas.create_window(447,10, anchor="nw", window=exit)
exit.bind("<Enter>", exit_hover) ####'<Enter>'= when you hover over the button
exit.bind("<Leave>", exit_hover_leave) ####'<Leave>'= when you hover out from the button
# ##=====================================================================================================================
# ##=====================================================================================================================
# ##=====================================================================================================================
# ##=====================================================================================================================
# ##=====================================================================================================================

window.mainloop()
