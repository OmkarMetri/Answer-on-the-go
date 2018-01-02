# /usr/bin/python3

from tkinter import *
import tkinter.ttk
import os

global search_list
global name
global number
global query_answer

ques="Question.txt"

name=[]
number=[]
search_list=[]                #List which will have all the user history it is a stack  
query_answer=[]
no_answer=["You havent written any answer for the question asked"]
question=[]                   #Question list which is queue here 


def create_widgets_in_user_frame():

    def Signup():
        call_zero_frame_on_top()

    def Login():
        call_first_frame_on_top()

    label=Label(user_frame,text="\n        Answer on the go      \n",bg="#333")
    label.config(font=("Ariel",22),fg="white")
    label.grid(row=0)

    new_user= Button(user_frame, text='New user',bg='#D1DDDB', command=Signup) 
    new_user.config(font=("Ariel", 15))
    new_user.grid(row=3,column=0,pady=10)

    Login= Button(user_frame, text='Login',bg='#D1DDDB', command=Login) 
    Login.config(font=("Ariel", 15))
    Login.grid(row=5,column=0,pady=10)
    
def create_widgets_in_AQ_frame():

    def get_ques():

            ques_list=question[int(number[0])-1]
            CategoryA.insert(END,str(number[0])+'.'+ques_list.rstrip())
            query_answer.append(str(number[0])+'.'+ques_list.rstrip())


    def back():

        call_second_frame_on_top()

    def Homepage():

        call_third_frame_on_top()

    def Save():


        
        text = tex.get("1.0",'end-1c')
        if(len(text)>0 and text.rstrip().lower()!=no_answer[0].rstrip().lower()):
            c=int(query_answer[0][0])
            with open("Data.txt","a") as f:
                f.write('\n'+query_answer[0][2:]+','+text)
            with open("Question.txt","r") as f:
                data=f.readlines()
            with open("Question.txt","w") as f:
                for i in range(len(data)):
                    if(i!=c-1):
                        f.write(data[i])
            tex.delete('0.0',END)
            CategoryA.delete(0,END)
            tex.insert('0.0',"Your answer has been saved \n Thanks for answering")
        else:
            text = tex.get("1.0",'end-1c')
            tex.insert(END,"You havent written any answer for the question asked")
            tex.see(END)

    label=Label(AQ_frame,text="Answer on the go",bg="#333")
    label.config(font=("Ariel",22),fg="white")
    label.pack()

    Category=Label(AQ_frame,text="Enter the Question with its number:",bg="#333")
    Category.config(font=("Ariel",15),fg="white")
    Category.pack()

    CategoryA = Entry(AQ_frame)
    CategoryA.config(font=("Ariel", 15))
    CategoryA.pack(pady=10)

    answer=Label(AQ_frame,text="Your answer:",bg="#333")
    answer.config(font=("Ariel",15),fg="white")
    answer.pack(pady=10)


    tex =Text(master=AQ_frame)   
    tex.pack(side=LEFT,fill='both',expand=True,pady=10)

    get= Button(AQ_frame, text='Get question',bg='#D1DDDB', command=get_ques) 
    get.config(font=("Ariel", 15))
    get.pack(pady=10)

    save= Button(AQ_frame, text='Save',bg='#D1DDDB', command=Save) 
    save.config(font=("Ariel", 15))
    save.pack(pady=10)

    Go= Button(AQ_frame, text='HomePage',bg='#D1DDDB', command=Homepage) 
    Go.config(font=("Ariel", 15))
    Go.pack(pady=10)

    back= Button(AQ_frame, text='Back',bg='#D1DDDB', command=back) 
    back.config(font=("Ariel", 15))
    back.pack(pady=10)

def create_widgets_in_zero_frame():
    
     def Back():

        call_user_frame_on_top()

     def Signup():
      
      with open("Signup.txt", 'a+') as f: 
        f.write(nameE.get()+','+pwordE.get()+'\n')
        f.close()
        name.append(nameE.get())
      call_first_frame_on_top()

     global pwordE 
     global nameE
     global roots

     label = Label(zero_frame, text='Enter new Credidentials\n',bg='#333')
     label.config(font=("Ariel", 22),fg="white") 
     label.grid(row=0, column=0, sticky=E) 
 
     nameL = Label(zero_frame, text='New Username: ',bg='#333')
     nameL.config(font=("Ariel", 15),fg="white")
     nameL.grid(row=1, column=0, sticky=W)  
     
     pwordL = Label(zero_frame, text='New Password: ',bg='#333')
     pwordL.config(font=("Ariel", 15),fg="white") 
     pwordL.grid(row=3, column=0, sticky=W) 
 
     nameE = Entry(zero_frame)
     nameE.config(font=("Ariel", 15))
     nameE.grid(row=2, column=0,sticky=W)

     pwordE = Entry(zero_frame, show='*') 
     pwordE.config(font=("Ariel", 15))     
     pwordE.grid(row=4, column=0,sticky=W) 
 
     signupButton = Button(zero_frame, text='Signup',bg='#D1DDDB', command=Signup) 
     signupButton.config(font=("Ariel", 15))
     signupButton.grid(columnspan=2, sticky=W,pady=10)

     back = Button(zero_frame, text='Back',bg='#D1DDDB', command=Back) 
     back.config(font=("Ariel", 15))
     back.grid(columnspan=2, sticky=W,pady=10)
    
     

def create_widgets_in_first_frame():
    
    def CheckLogin():
     
     c=0
     with open("Signup.txt","r") as f:
        data = f.readlines()
     for i in data:
        if(i!='\n'):
            i=i.split(',')
            uname=i[0].rstrip()
            pword=i[1].rstrip()
            if(uname==nameEL.get() and pword==pwordEL.get()):
          
             if(os.path.isfile(ques)):
                name.append(nameEL.get())
                with open(ques) as f:
                    data=f.readlines()

                    if(len(data)>0):
                      call_second_frame_on_top()
                    else:
                        call_third_frame_on_top()
       
     else:
        
          a=Label(first_frame,text="Either your password or your id \n is wrong",fg='#F70909',bg='#333')
          a.config(font=("Ariel", 15),fg="white")
          a.grid(row=1)
        
    def Back():

        call_user_frame_on_top()
    

    label = Label(first_frame, text='Login\n',bg='#333',width=20)
    label.config(font=("Ariel", 22),fg="white")
    label.grid(sticky=E) 
 
    nameL = Label(first_frame, text='Username: ',bg='#333') 
    nameL.config(font=("Ariel", 15),fg="white")
    nameL.grid(row=2, sticky=W)

    pwordL = Label(first_frame, text='Password: ',bg='#333') 
    pwordL.config(font=("Ariel", 15),fg="white")
    pwordL	.grid(row=4, sticky=W)
 
    nameEL = Entry(first_frame,width=25) 
    nameEL.config(font=("Ariel", 15))
    nameEL.grid(row=3, sticky=W)
    
    pwordEL = Entry(first_frame, show='*',width=25)
    pwordEL.config(font=("Ariel", 15))
    pwordEL.grid(row=5,sticky=W)
 
    loginB = Button(first_frame, text='Login',bg='#D1DDDB',command=CheckLogin,width=8,height=1) 
    loginB.config(font=("Ariel",15))
    loginB.grid(columnspan=2, sticky=W,pady=10)

    Back_Button = Button(first_frame, text='Back',bg='#D1DDDB',width=8,height=1,command=Back) 
    Back_Button.config(font=("Ariel",15))
    Back_Button.grid(columnspan=2, sticky=W,pady=10)
    
    
def create_widgets_in_second_frame():
    
    def No():

        call_third_frame_on_top()
        

    def save():
                                              # Saves all the data entered to a file
        call_third_frame_on_top()

    def yes():

        def back_window():
            number.append(num.get())
            call_AQ_frame_on_top()
            r.destroy()

        r = Tk()

        r.title('Answer On the go')
        r.config(bg="#333")

        rlbl = Label(r, text='Enter the question number \n you would like to answer')
        rlbl.config(font=("Ariel",15),fg="white",bg="#333")
        rlbl.pack()

        num=Entry(r);
        num.config(font=("Ariel",12))
        num.pack(pady=10)

        back=Button(r,text="Back",command=back_window)
        back.config(font=("Ariel",15))
        back.pack(pady=10)

        r.mainloop()


    def Note():
        
        c=0
        j=0
        count=0

        with open(ques) as f:
            data=f.readlines()
        for i in range(len(data)):

            que=data[i].split(",")
            if(que[0].rstrip()!=name[0]):
                question.append(que[1])
                j=j+1
                tex.insert(END,str(j)+'.'+que[1])
                tex.see(END)

                if(c==0):

                    first_window_label = Label(second_frame, text='\n\n Somebody has asked these question \n Would you like to answer these question \n\n',bg='#333',width=45)
                    first_window_label.config(font=('Ariel',12),fg="white")
                    first_window_label.pack(padx=10)

                    yes_button = tkinter.Button(second_frame, text = "Yes",command=yes)
                    yes_button.config(font=('Ariel',12))
                    yes_button.pack(pady=10)

                    no_button = tkinter.Button(second_frame, text = "No",command=No)
                    no_button.config(font=('Ariel',12))
                    no_button.pack(pady=10)
                    
                    c=c+1;
                    count=1

        if(count==0):

            first_window_label = Label(second_frame, text='\n\n No New Notification \n\n',bg='#333',width=45)
            first_window_label.config(font=('Ariel',12),fg="white")
            first_window_label.pack(padx=10)  

            tex.insert(END,"No new Notification")
            tex.see(END)       

            home_button=Button(second_frame,text="HomePage",command=No)
            home_button.config(font=('Ariel',12))
            home_button.pack(pady=10,padx=10)
   

    request_button = tkinter.Button(second_frame, text = "Notification",command=Note)
    request_button.config(font=('Ariel',12))
    request_button.pack(pady=10)

    


    tex =Text(master=second_frame)   
    tex.pack(fill='both',expand=True)

    

def create_widgets_in_third_frame():
         
        def back():
            call_second_frame_on_top()

        def exit():
            root_window.destroy()

        def search():
           call_search_frame_on_top()

        def history():
           call_history_frame_on_top()

        def bookmark():
            call_bookmark_frame_on_top()

        def add():
            call_add_frame_on_top()

        
        label=Label(third_frame,text="\n      Answer on the go      \n",bg="#333")
        label.config(font=('Ariel',22),fg="white")
        label.pack(pady=10)

        search_button = Button(third_frame, text='Search'    ,bg='#D1DDDB',fg='black',command=search)
        search_button.config(font=('Ariel',12))
        search_button.pack(pady=10)
        
        History_button = Button(third_frame, text="History",bg='#D1DDDB',fg='black', command=history)
        History_button.config(font=('Ariel',12)) 
        History_button.pack(pady=10)           
        
        Bookmark_button = Button(third_frame, text="Bookmark",bg='#D1DDDB',fg='black', command=bookmark)
        Bookmark_button.config(font=('Ariel',12))
        Bookmark_button.pack(pady=10)
      
        Add_button = Button(third_frame, text="Add data",bg='#D1DDDB',fg='black', command=add)
        Add_button.config(font=('Ariel',12))
        Add_button.pack(pady=10)

        back_button = Button(third_frame, text="Back",bg='#D1DDDB',fg='black', command=back)
        back_button.config(font=('Ariel',12))
        back_button.pack(pady=10)

        exit_button = Button(third_frame, text="Exit",bg='#D1DDDB',fg='black', command=exit)
        exit_button.config(font=('Ariel',12))
        exit_button.pack(pady=10)

def create_widgets_in_add_frame():

    def Homepage():
        call_third_frame_on_top()
        tex.delete('0.0',END)

    def Save():
        answer=CategoryA.get()
        text1 = tex.get("1.0",'end-1c')
        if(len(text1)>0 and len(answer)>0):
            
            with open("Data.txt","a") as f:
                f.write('\n'+answer+','+text1)
            tex.delete('0.0',END)
            CategoryA.delete(0,END)
            tex.insert('0.0',"Your answer has been saved \n Thanks for answering")
        else:
            tex.insert('0.0',"Trying to save an empty answer")
        

    label=Label(add_frame,text="Answer on the go",bg="#333")
    label.config(font=("Ariel",22),fg="white")
    label.pack()

    Category=Label(add_frame,text="Enter the Category",bg="#333")
    Category.config(font=("Ariel",15),fg="white")
    Category.pack()

    CategoryA = Entry(add_frame)
    CategoryA.config(font=("Ariel", 15))
    CategoryA.pack(pady=10)

    answer=Label(add_frame,text="Your answer:",bg="#333")
    answer.config(font=("Ariel",15),fg="white")
    answer.pack(pady=10)


    tex =Text(master=add_frame)   
    tex.pack(side=LEFT,fill='both',expand=True,pady=10)

    save= Button(add_frame, text='Save',bg='#D1DDDB', command=Save) 
    save.config(font=("Ariel", 15))
    save.pack(pady=10)

    Go= Button(add_frame, text='Back',bg='#D1DDDB', command=Homepage) 
    Go.config(font=("Ariel", 15))
    Go.pack(pady=10)

def create_widgets_in_search_frame():
     
     def Back():
        call_third_frame_on_top()
        tex.delete('0.0',END)
        temp.delete(0,END)

     def search():

        tex.delete('0.0',END)
        search_query=temp.get()
        search_query=search_query.lower()
        search_list.append(search_query)

        with open("Data.txt") as f:
            c=0
            i=0
            lc=0
            data=f.readlines()
            for i in range(len(data)):
                l=data[i].split(",")
                if(len(search_query)!=len(l[0])):
                            lc=1
                if(len(l[0])!=0):
                    if(l[0].rstrip("?").rstrip().lower()==search_query.rstrip()):

                        lc=0
                        c=1
                        tex.insert(END,l[0]+'\n')
                        tex.see(END)
                        tex.insert(END,l[1])
                        tex.see(END)
                        for j in range(i+1,len(data)):
                            l=data[j].split(",")
                            if(len(l)==1):
                                tex.insert(END,l[0]+'\n')
                                tex.see(END)
                            if(len(l)!=1):
                                    break
    


                #if(c==0 or c==1):
                if(lc==1):
                    s=l[0]
                    s=l[0].split(" ")
                    for m in range(len(s)):
                        if(s[m].rstrip("?").rstrip().lower()==search_query.rstrip()):
                            c=1
                            tex.insert(END,l[0]+'\n')
                            tex.see(END)
                            tex.insert(END,l[1])
                            tex.see(END)
                            for j in range(i+1,len(data)):
                                l=data[j].split(",")
                                if(len(l)==1):
                                    tex.insert(END,l[0])
                                    tex.see(END)
                                if(len(l)!=1):
                                    break
                    
            if(c==0):
                call_QA_frame_on_top()

     temp = Entry(search_frame)  
     temp.config(font=("Ariel", 15)) 
     temp.pack() 
 
     searchButton = Button(search_frame, text='Search',bg='#D1DDDB', command=search) 
     searchButton.config(font=("Ariel", 15))
     searchButton.pack(pady=10)

     back = Button(search_frame, text='Back',bg='#D1DDDB', command=Back) 
     back.config(font=("Ariel", 15))
     back.pack()
     
     tex =Text(master=search_frame)   
     tex.pack(fill='both',expand=True)
     

     

def create_widgets_in_history_frame():

    def Back():

        call_third_frame_on_top()
        tex.delete('0.0',END)

    def View():

            j=len(search_list)-1
            if(len(search_list)>0):
                for i in range(len(search_list)):
                    tex.insert(END,search_list[j]+'\n')
                    tex.see(END)
                    j=j-1
            else:
                tex.delete('0.0',END)
                tex.insert(END,"No Search History")
                tex.see(END)


    def clear():

        tex.delete('0.0',END)
        while(len(search_list)!=0):
            search_list.remove(search_list[0])
        tex.insert(END,"History Cleared")
        tex.see(END)


    tex =Text(master=history_frame)   
    tex.pack(side=RIGHT,fill='both',expand=True)

    View_Button = Button(history_frame, text='View History',bg='#D1DDDB', command=View) 
    View_Button.config(font=("Ariel", 15))
    View_Button.pack(pady=10)

    Clear_Button = Button(history_frame, text='Clear History',bg='#D1DDDB', command=clear) 
    Clear_Button.config(font=("Ariel", 15))
    Clear_Button.pack(pady=10)
    
    Back_Button = Button(history_frame, text='Back',bg='#D1DDDB', command=Back) 
    Back_Button.config(font=("Ariel", 15))
    Back_Button.pack(pady=10)
    

def create_widgets_in_bookmark_frame():

    def Back():
        call_third_frame_on_top()
        add.delete(0,END)
        tex.delete('0.0',END)

    def Add():
        tex.delete('0.0',END)
        if(len(add.get())!=0):
            with open("Bookmark.txt","a") as f:
                f.write(name[0]+','+add.get()+'\n')
            add.delete(0,END)
        else:
            tex.insert(END,"Trying to save a empty Category")
            tex.see(END)

    def View():
        tex.delete('0.0',END)
        c=0
        with open("Bookmark.txt","r") as f:
            data=f.readlines()
            for i in range(len(data)):
                j=data[i].split(',')
                if(name[0]==j[0].rstrip()):
                    with open("Data.txt","r") as file:
                        file_data=file.readlines()
                        for m in range(len(file_data)):
                                List=file_data[m].split(',')
                                for n in range(1,len(j)):
                                        if(j[n].rstrip().lower()==List[0].rstrip().lower()):

                                            c=1
                                            
                                            tex.insert(END,List[0].rstrip()+'\n')
                                            tex.see(END)
                                            tex.insert(END,List[1].rstrip()+'\n')
                                            tex.see(END)
                                            for x in range(m+1,len(file_data)):
                                                        data1=file_data[x].split(",")
                                                        
                                                        if(data1[0]!='\n'):
                                                            if(len(data1)==1):
                                                                tex.insert(END,data1[0]+'\n')
                                                                tex.see(END)
                                                        if(len(data)!=1):
                                                            break;
                                        if(len(List[0].split(" "))>1):
                                            s=List[0].split(" ")
                                            for k in range(len(s)):
                                                if(s[k].rstrip().lower()==j[n].rstrip().lower()):
                                                    c=1
                                                    tex.insert(END,List[0].rstrip()+'\n')
                                                    tex.see(END)
                                                    tex.insert(END,List[1].rstrip()+'\n')
                                                    tex.see(END)
                                                    for x in range(m+1,len(file_data)):
                                                        data1=file_data[x].split(",")
                                                        if(data1[0]!='\n'):
                                                            if(len(data1)==1):
                                                                tex.insert(END,data1[0]+'\n')
                                                                tex.see(END)
                                                        if(len(data1)!=1):
                                                            break;

        if(c==0):
            tex.insert(END,"No bookmarked topic \n")
            tex.see(END)

    add = Entry(bookmark_frame)  
    add.config(font=("Ariel", 15)) 
    add.pack()

    add_button=Button(bookmark_frame,text="Add",bg='#D1DDDB',command=Add)
    add_button.config(font=("Ariel", 15))
    add_button.pack(pady=10)

    view_button=Button(bookmark_frame,text="View",bg='#D1DDDB',command=View)
    view_button.config(font=("Ariel", 15))
    view_button.pack(pady=10)
 
    Back_Button = Button(bookmark_frame, text='Back',bg='#D1DDDB', command=Back) 
    Back_Button.config(font=("Ariel", 15))
    Back_Button.pack(pady=10)

    tex =Text(master=bookmark_frame)   
    tex.pack(side=RIGHT,fill='both',expand=True)

def create_widgets_in_QA_frame():

    def Back():

        call_third_frame_on_top()

    def Post():

        with open("Question.txt","a") as f:
            f.write(name[0]+','+temp1.get()+'\n')
        call_third_frame_on_top()

    temp=Label(QA_frame,text="Sorry we couldnt find any post related to your search \n \n Post this question on the Engine \n for other user to answer",bg="#333")
    temp.config(font=("Ariel",15),fg="white")
    temp.pack(pady=10)

    temp1 = Entry(QA_frame)  
    temp1.config(font=("Ariel", 15)) 
    temp1.pack()

    PostButton = Button(QA_frame, text='Post',bg='#D1DDDB', command=Post) 
    PostButton.config(font=("Ariel", 15))
    PostButton.pack(pady=10)
 
    Back_Button = Button(QA_frame, text='Back',bg='#D1DDDB', command=Back) 
    Back_Button.config(font=("Ariel", 15))
    Back_Button.pack(pady=10)
     
def call_user_frame_on_top():
    
     zero_frame.grid_forget()
     first_frame.grid_forget()
     second_frame.grid_forget()
     third_frame.grid_forget()
     search_frame.grid_forget()
     history_frame.grid_forget()
     bookmark_frame.grid_forget()
     AQ_frame.grid_forget()
     QA_frame.grid_forget()
     add_frame.grid_forget()
     user_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))
        

def call_AQ_frame_on_top():
    
     user_frame.grid_forget()
     zero_frame.grid_forget()
     first_frame.grid_forget()
     second_frame.grid_forget()
     third_frame.grid_forget()
     search_frame.grid_forget()
     history_frame.grid_forget()
     bookmark_frame.grid_forget()
     QA_frame.grid_forget()
     add_frame.grid_forget()
     AQ_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))
        

def call_zero_frame_on_top():
    
     user_frame.grid_forget()
     first_frame.grid_forget()
     second_frame.grid_forget()
     third_frame.grid_forget()
     AQ_frame.grid_forget()
     QA_frame.grid_forget()
     second_frame.grid_forget()
     history_frame.grid_forget()
     bookmark_frame.grid_forget()
     add_frame.grid_forget()
     zero_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


def call_first_frame_on_top():

    user_frame.grid_forget()
    zero_frame.grid_forget()
    second_frame.grid_forget()
    third_frame.grid_forget()
    AQ_frame.grid_forget()
    QA_frame.grid_forget()
    second_frame.grid_forget()
    history_frame.grid_forget()
    bookmark_frame.grid_forget()
    add_frame.grid_forget()
    first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


def call_second_frame_on_top():
    
    user_frame.grid_forget()
    zero_frame.grid_forget()
    first_frame.grid_forget()
    third_frame.grid_forget()
    AQ_frame.grid_forget()
    QA_frame.grid_forget()
    second_frame.grid_forget()
    history_frame.grid_forget()
    bookmark_frame.grid_forget()
    add_frame.grid_forget()
    second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


def call_search_frame_on_top():
    
    user_frame.grid_forget()
    zero_frame.grid_forget()
    first_frame.grid_forget()
    second_frame.grid_forget()
    third_frame.grid_forget()
    AQ_frame.grid_forget()
    QA_frame.grid_forget()
    history_frame.grid_forget()
    bookmark_frame.grid_forget()
    add_frame.grid_forget()
    search_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


def call_add_frame_on_top():
    
    user_frame.grid_forget()
    zero_frame.grid_forget()
    first_frame.grid_forget()
    second_frame.grid_forget()
    third_frame.grid_forget()
    AQ_frame.grid_forget()
    QA_frame.grid_forget()
    history_frame.grid_forget()
    bookmark_frame.grid_forget()
    second_frame.grid_forget()
    add_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


def call_history_frame_on_top():
    
    user_frame.grid_forget()
    zero_frame.grid_forget()
    first_frame.grid_forget()
    second_frame.grid_forget()
    third_frame.grid_forget()
    search_frame.grid_forget()
    AQ_frame.grid_forget()
    QA_frame.grid_forget()
    search_frame.grid_forget()
    bookmark_frame.grid_forget()
    add_frame.grid_forget()
    history_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


def call_bookmark_frame_on_top():
    
    user_frame.grid_forget()
    zero_frame.grid_forget()
    first_frame.grid_forget()
    second_frame.grid_forget()
    third_frame.grid_forget()
    search_frame.grid_forget()
    history_frame.grid_forget()
    AQ_frame.grid_forget()
    QA_frame.grid_forget()
    add_frame.grid_forget()
    bookmark_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


def call_QA_frame_on_top():
    
    user_frame.grid_forget()
    zero_frame.grid_forget()
    first_frame.grid_forget()
    second_frame.grid_forget()
    third_frame.grid_forget()
    search_frame.grid_forget()
    history_frame.grid_forget()
    bookmark_frame.grid_forget()
    AQ_frame.grid_forget()
    add_frame.grid_forget()
    QA_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


def call_third_frame_on_top():
    
    user_frame.grid_forget()
    zero_frame.grid_forget()
    first_frame.grid_forget()
    second_frame.grid_forget()
    search_frame.grid_forget()
    history_frame.grid_forget()
    bookmark_frame.grid_forget()
    QA_frame.grid_forget()
    AQ_frame.grid_forget()
    add_frame.grid_forget()
    third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))



# Main program starts here  #


# Create the root GUI window.
root_window =Tk()

# Define window size
window_width = 800
window_heigth = 500


# Create frames inside the root window to hold other GUI elements. All frames must be created in the main program, otherwise they are not accessible in functions.

user_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#333')
user_frame['borderwidth'] = 2
user_frame['relief'] = 'sunken'
user_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

zero_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#333')
zero_frame['borderwidth'] = 2
zero_frame['relief'] = 'sunken'
zero_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E)) 


first_frame=Frame(root_window, width=300, height=200,bg='#333')
first_frame['borderwidth'] = 2
first_frame['relief'] = 'sunken'
first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

second_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#333')
second_frame['borderwidth'] = 2
second_frame['relief'] = 'sunken'
second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

search_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#333')
search_frame['borderwidth'] = 2
search_frame['relief'] = 'sunken'
search_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

history_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#333')
history_frame['borderwidth'] = 2
history_frame['relief'] = 'sunken'
history_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

bookmark_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#333')
bookmark_frame['borderwidth'] = 2
bookmark_frame['relief'] = 'sunken'
bookmark_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E)) 

QA_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#333')
QA_frame['borderwidth'] = 2
QA_frame['relief'] = 'sunken'
QA_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

AQ_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#333')
AQ_frame['borderwidth'] = 2
AQ_frame['relief'] = 'sunken'
AQ_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


third_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#333')
third_frame['borderwidth'] = 2
third_frame['relief'] = 'sunken'
third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

add_frame=Frame(root_window, width=window_width, height=window_heigth,bg='#333')
add_frame['borderwidth'] = 2
add_frame['relief'] = 'sunken'
add_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


# Create all widgets to all frames

create_widgets_in_history_frame()
create_widgets_in_AQ_frame()
create_widgets_in_search_frame()
create_widgets_in_bookmark_frame()
create_widgets_in_add_frame()
create_widgets_in_QA_frame()
create_widgets_in_third_frame()
create_widgets_in_second_frame()
create_widgets_in_first_frame()
create_widgets_in_zero_frame()
create_widgets_in_user_frame()

# Hide all frames in reverse order, but leave first frame visible (unhidden).


third_frame.grid_forget()
search_frame.grid_forget()
history_frame.grid_forget()
bookmark_frame.grid_forget()
add_frame.grid_forget()
QA_frame.grid_forget()
AQ_frame.grid_forget()
second_frame.grid_forget()
first_frame.grid_forget()
zero_frame.grid_forget()

# Start tkinter event - loop
root_window.title('Answer On The Go')
root_window.configure(background='#333')


root_window.mainloop()  
