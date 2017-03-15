from tkinter import *

def previewPressed():
        preview.config(state=DISABLED)
        stop.config(state="normal")

def stopPressed():
        preview.config(state="normal")
        stop.config(state=DISABLED)

def makeWindow():
        global preview
        global stop
        
        win = Tk()
        win.wm_title("Remind Me")

        header = LabelFrame(win)
        header.pack(fill='both', expand='yes')

        headertext = Label(header, text='Remind Me')
        headertext.pack()

        main = Frame(win)
        main.pack(expand='yes')
        maintext = Label(main, text='Remind me to: ')
        maintext.pack(side=LEFT, padx=10)
        textarea = Text(main, height=1, width=30)
        textarea.pack(side=LEFT, padx=10)
        textarea.insert(END, "Do Something")

        options = Frame(win)
        options.pack(fill='both', expand='yes')

        times = [
                "5 minutes",
                "10 minutes",
                "15 minutes",
                "30 minutes",
                "45 minutes",
                "60 minutes",
                "90 minutes",
                "2 hours",
                "3 hours",
                "4 hours",
                "5 hours",
                "6 hours",
                "7 hours",
                "8 hours",
                "9 hours",
                "10 hours",
                "11 hours",
                "12 hours"
                ]
        
        firstvar = StringVar(options)
        firstvar.set("every")
        firstdrop = OptionMenu(options, firstvar, "every", "in")
        firstdrop.config(width=20)
        firstdrop.pack(side=LEFT, padx=10)

        secondvar = StringVar(options)
        secondvar.set(times[0])
        seconddrop = OptionMenu(options, secondvar, *times)
        seconddrop.config(width=20)
        seconddrop.pack(side=LEFT, padx=10)

        sounds = Frame(win)
        sounds.pack(fill='both', expand='yes')
        soundtext = Label(sounds, text='Select an alarm sound: ')
        soundtext.pack()

        soundlist = [
                "Alarm Clock",
                "Sunday Church",
                "Rooster",
                "Fog Horn",
                "Cheer",
                "Music Box"
                ]
        soundvar = StringVar(sounds)
        soundvar.set(soundlist[0])
        sounddrop = OptionMenu(sounds, soundvar, *soundlist)
        sounddrop.config(width=15)
        sounddrop.pack(side=LEFT, padx=10)

        preview = Button(sounds, text="Preview", command=previewPressed)
        preview.config(width=10)
        preview.pack(side=LEFT, padx=10)
        8
        stop = Button(sounds, text="Stop", state=DISABLED, command=stopPressed)
        stop.config(width=10)
        stop.pack(side=LEFT, padx=10)

        return win


win = makeWindow()
win.mainloop()
