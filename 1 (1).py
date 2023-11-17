from tkinter import *
import imdb
from tkinter import messagebox


##############Functionality Part

def search_movie():
    if movieEntry.get() == '':
        messagebox.showerror('Error', 'Please Enter A Movie Name')

    else:

        try:


            root1=Toplevel()
            root1.resizable(False, False)

            root1.geometry('890x600+200+50')
            root1.config(bg='orange')
            root1.grab_set()


            titleLabel=Label(root1,text='Title',font=('cooper black',30,'bold'),fg='white',bg='orange')
            titleLabel.place(x=60,y=30)

            titlenameLabel=Label(root1,font=('algerian',20,'bold'),fg='white',bg='orange')
            titlenameLabel.place(x=300,y=30)

            directorLabel = Label(root1, text='Director', font=('cooper black', 30, 'bold'), fg='white', bg='orange')
            directorLabel.place(x=60, y=100)

            directornameLabel=Label(root1,font=('algerian',20,'bold'),fg='white',bg='orange')
            directornameLabel.place(x=300,y=100)

            yearLabel = Label(root1, text='Year', font=('cooper black', 30, 'bold'), fg='white', bg='orange')
            yearLabel.place(x=60, y=170)

            yearnameLabel = Label(root1, font=('algerian', 20, 'bold'), fg='white', bg='orange')
            yearnameLabel.place(x=300, y=170)

            runtimeLabel = Label(root1, text='Runtime', font=('cooper black', 30, 'bold'), fg='white', bg='orange')
            runtimeLabel.place(x=60, y=240)

            runtimenameLabel = Label(root1, font=('algerian', 20, 'bold'), fg='white', bg='orange')
            runtimenameLabel.place(x=300, y=240)

            genreLabel = Label(root1, text='Genres', font=('cooper black', 30, 'bold'), fg='white', bg='orange')
            genreLabel.place(x=60, y=310)

            genrenameLabel = Label(root1, font=('algerian', 20, 'bold'), fg='white', bg='orange')
            genrenameLabel.place(x=300, y=310)

            ratingLabel = Label(root1, text='Rating', font=('cooper black', 30, 'bold'), fg='white', bg='orange')
            ratingLabel.place(x=60, y=380)

            ratingnameLabel = Label(root1, font=('algerian', 20, 'bold'), fg='white', bg='orange')
            ratingnameLabel.place(x=300, y=380)

            castLabel = Label(root1, text='Cast', font=('cooper black', 30, 'bold'), fg='white', bg='orange')
            castLabel.place(x=60, y=450)

            castnameLabel = Label(root1, font=('algerian', 20, 'bold'), fg='white', bg='orange',
                                  wraplength=600,justify=LEFT)
            castnameLabel.place(x=300, y=450)

            hr=imdb.IMDb()

            movie_name=movieEntry.get()
            movies=hr.search_movie(movie_name)

            index=movies[0].getID()
            movie=hr.get_movie(index)
            title=movie['title']
            titlenameLabel.config(text=title)

            year=movie['year']
            yearnameLabel.config(text=year)

            rating=movie['rating']
            ratingnameLabel.config(text=rating)

            genre=movie['genres']
            genrenameLabel.config(text=genre)

            director=movie['directors'][0]
            directornameLabel.config(text=director)

            runtime=movie['runtime'][0]
            hours=int(runtime)//60
            rem=int(runtime)%60
            runtimenameLabel.config(text=f'{hours} hours {rem} minutes')

            cast=movie['cast']
            list_of_cast=list(map(str,cast))

            castlist=list_of_cast[:6]
            strr=''
            for item in castlist:
                if item==castlist[-1]:
                    strr=strr+item+'.'
                else:
                    strr=strr+item+','

            castnameLabel.config(text=strr)


            root1.mainloop()

        except:
            messagebox.showerror('message','Data doesnt exist!')



    







#################GUIII
root=Tk()
root.title('Movie Description')
root.geometry('1057x650+100+50')
root.resizable(False,False)

bgpic=PhotoImage(file='pic.png')

bgLabel=Label(root,image=bgpic)
bgLabel.place(x=0,y=0)

movieLabel=Label(root,text='Movie Name:',font=('algerian',30,'bold'),bg='#DEDCDD')
movieLabel.place(x=200,y=570)

movieEntry=Entry(root,font=('FELIX TITLING',20,'bold'),bd=5,relief=GROOVE,justify=CENTER)
movieEntry.place(x=490,y=575)
movieEntry.focus_set()

moviesearchButton=Button(root,text='SEARCH',font=('FELIX TITLING',20,'bold'),cursor='hand2',bd=5,
                         relief=GROOVE,command=search_movie)
moviesearchButton.place(x=880,y=565)



root.mainloop()

