from tkinter import *
from tkinter import messagebox, ttk
from random import *
import tkinter as tk


def District(HOSPL_ID):

    def show_Cases():
        top4 = tk.Toplevel(top)
        top4.geometry('1290x500')
        Label(top4, text="", font=('bold', 30)).grid(row=1, column=1)
        Label(top4, text="Cases Bulletine", font=('bold', 30)).grid(row=1, column=2)
        fm = Frame(top4)
        fm.grid(row=2, column=1, padx=30, pady=20)

        disp = ttk.Treeview(fm, columns=(1, 2, 3, 4, 5, 6, 7),show="headings", height="10")
        disp.grid(row=3, column=2)

        disp.heading(1, text="HOSPITAL_ID", anchor=CENTER)
        disp.heading(2, text="Case_numbers", anchor=CENTER)
        disp.heading(3, text="Age", anchor=CENTER)
        disp.heading(4, text="Sex", anchor=CENTER)
        disp.heading(5, text="District", anchor=CENTER)
        disp.heading(6, text="History", anchor=CENTER)
        disp.heading(7, text="Isolated_at", anchor=CENTER)

        def delete_case():
            del_case = list()
            del_case_1 = list()
            for i in disp.selection():
                deleting = disp.set(i, '#7')
                disp.delete(i)

                with open('Cases.txt', 'r') as file:
                    for line in file:
                        line = line.split('/')
                        del_case.append(line)

                    for i in del_case:
                        if deleting in i:
                            del_case.remove(i)
                        else:
                            continue
                    print(del_case)

                    for j in del_case:
                        j = '/'.join(j)
                        del_case_1.append(j)

                    with open('Cases.txt', 'w') as file:
                        file.writelines(del_case_1)

        delete = Button(top4, text='Delete Selected', font=(
            'bold', 15), command=delete_case)
        delete.grid(row=7, column=1)

        with open('Cases.txt', 'r') as file:
            case_list = list()
            for line in file:
                line = line.split('/')
                case_list.append(line)

            for i in case_list:
                if HOSPL_ID in i:
                    disp.insert('', 'end', values=i)
                else:
                    continue

    def Case_entry():
        Cases = Caseno.get()
        Ageyear = Age.get()
        SexMFO = MFO.get()
        District_w = District.get()
        Histo = History.get()
        Isolated_at=Isolated.get()

        with open('Cases.txt', 'a') as file:
            file.write(HOSPL_ID+'/')
            file.write(Cases+'/')
            file.write(Ageyear+'/')
            file.write(SexMFO+'/')
            file.write(District_w+'/')
            file.write(Histo+'/')
            file.write(Isolated_at+'/'+'\n')
            messagebox.showinfo('Success!', 'Case Saved')



    top3 = tk.Toplevel(top)
    top3['background']='#000033'
    top3.geometry('1200x900')

    Label(top3, text="                  ",bg='#000033', font=('bold', 28)).grid(row=0, column=1)
    Label(top3, text="      ADD COVID CASE      ",fg='white',bg='red', font=('bold', 28)).grid(row=0, column=2)
    Label(top3, text='Hospital-ID:'+HOSPL_ID,bg='red',font=('bold', 15),fg='white', pady=20, padx=20).grid(row=1, column=2)
    Label(top3, text='Enter Case NO',font=('bold', 15),bg='#000033',fg='white', pady=40, padx=40).grid(row=2, column=0)
    Label(top3, text='Age(Years):',font=('bold', 15),bg='#000033',fg='white', pady=40, padx=40).grid(row=3, column=0)
    Label(top3, text='Sex:',font=('bold', 15),bg='#000033',fg='white', pady=40, padx=40).grid(row=4, column=0)
    Label(top3, text='District:',bg='#000033',font=('bold', 15),fg='white', pady=40, padx=40).grid(row=2, column=2)
    Label(top3, text='History:',bg='#000033',font=('bold', 15),fg='white', pady=40, padx=40).grid(row=3, column=2)
    Label(top3, text='Isolated at:',bg='#000033',font=('bold', 15),fg='white', pady=40, padx=40).grid(row=4, column=2)
    Caseno = StringVar()
    Entry(top3, textvariable=Caseno,font=('bold', 15)).grid(row=2, column=1)
    Age = StringVar()
    Entry(top3, textvariable=Age, font=('bold', 15)).grid(row=3, column=1)
    MFO = StringVar()
    Entry(top3, textvariable=MFO, font=('bold', 15)).grid(row=4, column=1)
    District = StringVar()
    Entry(top3, textvariable=District, font=('bold', 15)).grid(row=2, column=3)
    History = StringVar()
    Entry(top3, textvariable=History, font=('bold', 15)).grid(row=3, column=3)
    Isolated = StringVar()
    Entry(top3, textvariable=Isolated, font=('bold', 15)).grid(row=4, column=3)
    submit = Button(top3, text='Submit', font=('bold', 15), command=Case_entry).grid(row=8, column=1)
    Label(top3, text="").grid(row=7, column=1)
    Button(top3, text='Log-Out', font=('bold', 15), command=top.quit).grid(row=8, column=3)
    Button(top3, text="Show the Cases", font=('bold', 15), command=show_Cases).grid(row=8, column=2)


def login():
    with open('file.txt', 'r') as f:
        # print(f.readlines())
        HOSPL_ID= hospid.get()
        print(HOSPL_ID)
        passcode = pswd.get()
        print(passcode)
        for line in f:
            line = line.rstrip()
            if re.search(HOSPL_ID,line) and re.search(passcode,line):
                District(HOSPL_ID)
                break
            else:
                continue
        else:
            messagebox.showerror('Oops!', 'Invalid Credentials')


def SIGNUPINT():
    def signin():
        with open('text.txt', 'r') as f:
            # print(f.readlines())
            HOSPL_ID = HOSPITAL_ID
            print(HOSPL_ID)
            hospital_name = Hname.get()
            print(hospital_name)
            passcode = pwd.get()
            print(passcode)
            for line in f:
                line = line.rstrip()
                if re.search(HOSPL_id, line):
                    messagebox.showinfo('Error!', 'Hospital already exists')
                    break
                else:
                    continue
            else:
                with open('file.txt', 'a') as file:
                    file.write(str(HOSPL_ID)+' /')
                    file.write(passcode+' /'+'/')
                    file.write(hospital_name + ' \n')

                # with open('wallet.txt', 'a') as file:
                #     file.write(name+'/')
                #     file.write(str(walletID)+'/')
                #     file.write(balance_amt+'/'+'\n')

                messagebox.showinfo('Success!', 'Signin Successful')
                # ********SIGNUP INTERFACE******
    top2 = tk.Toplevel(top)
    top2.title('COVID-19INDIA')
    Label(top2, text="",bg='#170632').grid(row=0, column=1)
    Label(top2, text="",bg='#170632').grid(row=0, column=2)
    Label(top2, text="",bg='#170632').grid(row=0, column=3)
    Label(top2, text="",bg='#170632').grid(row=0, column=4)
    Label(top2,text="             COVID-19INDIA",font=('bold',30),bg='red',fg='white',cursor='dot').grid()
    Label(top2,text="               SIGNIN",font=('bold',30),bg='red',fg='white',cursor='dot').grid(column=0)
    Label(top2,text='',fg='white',font=('bold',15),pady=40,padx=40,bg='#000033').grid(row=2,column=1)
    Label(top2,text='',fg='white',font=('bold',15),pady=40,padx=40,bg='#000033').grid(row=3,column=1)
    Label(top2,text='Hospital Name:        ',fg='white',font=('bold',15),pady=60,padx=40,bg='#000033').grid(row=4,column=1)
    Label(top2,text='Hospital id:          ',fg='white',font=('bold',15),pady=60,padx=40,bg='#000033').grid(row=5,column=1)
    Label(top2,text='passcode:          ',fg='white',font=('bold',15),pady=60,padx=40,bg='#000033').grid(row=6,column=1)
    Hname=StringVar()
    pwd=StringVar()

    Hname_Entry=Entry(top2,bd=1,textvariable=Hname).grid(row=4,column=2)
    HOSPITAL_ID=randint(1,1000)
    Label(top2,text=HOSPITAL_ID,fg='white',font=('bold',15),pady=60,padx=40,bg='#000033').grid(row=5,column=2)
    pwd1=Entry(top2,bd=1,textvariable=pwd).grid(row=6,column=2)
    proceed=Button(top2,text='Proceed',padx=30,bg='#170632',fg='white',activebackground='#170632',activeforeground='cyan',command=signin).grid(row=7,column=2)
    # Label(top, text='Existing Center ?',font=('bold',14),pady=60,padx=40,bg='#000033',fg='white').grid(row=7,column=1)
    # Signup=Button(top, text='Login',padx=30,bg='#170632',fg='white',activebackground='#170632',activeforeground='cyan',command=createNewWindow).grid(row=7,column=2)
    # top.geometry("400x200")
    top2['background']='#000033'


# creating a window

# **************LOGIN INTERFACE*************
top = Tk()
top.title('COVID-19INDIA')
Label(top, text="",bg='#170632').grid(row=0, column=1)
Label(top, text="",bg='#170632').grid(row=0, column=2)
Label(top, text="",bg='#170632').grid(row=0, column=3)
Label(top, text="",bg='#170632').grid(row=0, column=4)
Label(top,text="             COVID-19INDIA",font=('bold',30),bg='red',fg='white',cursor='dot').grid()
Label(top,text="               LOG-IN",font=('bold',30),bg='red',fg='white',cursor='dot').grid(column=0)
Label(top,text='',fg='white',font=('bold',15),pady=40,padx=40,bg='#000033').grid(row=2,column=1)
Label(top,text='',fg='white',font=('bold',15),pady=40,padx=40,bg='#000033').grid(row=3,column=1)
Label(top,text='HOSPITAL_ID :',fg='white',font=('bold',15),pady=60,padx=40,bg='#000033').grid(row=4,column=1)
Label(top,text='Password :',fg='white',font=('bold',15),pady=60,padx=40,bg='#000033').grid(row=5,column=1)
hospid=StringVar()
H_ID=Entry(top,bd=1,textvariable=hospid).grid(row=4,column=2)
pswd=StringVar()
PASSCODE=Entry(top,bd=1,textvariable=pswd).grid(row=5,column=2)
Button(top,text='Login',padx=30,bg='#170632',fg='white',activebackground='#170632',activeforeground='cyan',command=login).grid(row=6,column=2)
Label(top, text='New User ?',font=('bold',14),pady=60,padx=40,bg='#000033',fg='white').grid(row=7,column=1)
Button(top, text='Signin',padx=30,bg='#170632',fg='white',activebackground='#170632',activeforeground='cyan',command=SIGNUPINT).grid(row=7,column=2)
top.geometry("400x200")
top['background']='#000033'
top.mainloop()



top.title('Login')
top.geometry('1000x900')
top.mainloop()