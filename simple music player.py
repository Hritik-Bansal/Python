def resumemusic():
    root.ResumeButton.grid_remove()
    root.pauseButton.grid()
    mixer.music.unpause()
    AudiostatusLabel.configure(text='playing....')
def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.02)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    ProgressbarVolume['value'] = mixer.music.get_volume() * 100

def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol + 0.02)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100
def stopmusic():
    mixer.music.stop()
    AudiostatusLabel.configure(text='stopped....')
def pausemusic():
    mixer.music.pause()
    root.pauseButton.grid_remove()
    root.ResumeButton.grid()
    AudiostatusLabel.configure(text='paused....')
def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    ProgressbarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    ProgressbarVolume['value']=40
    ProgressbarVolumeLabel['text'] = '40%'
    mixer.music.play()
    AudiostatusLabel.configure(text='playing....')
     
def musicurl():
    dd = filedialog.askopenfilename()
    audiotrack.set(dd)
def createwidthes():
    global implay,impause,imstop,immusic,imvolumeup,imvolumedown,imresume,AudiostatusLabel
    global ProgressbarVolumeLabel,ProgressbarVolume,ProgressbarLabel,ProgressbarMusicLabel
    ###############################################################################  images register
    implay = PhotoImage(file='play.png')
    impause = PhotoImage(file='pause.png')
    imstop = PhotoImage(file='stop.png')
    immusic = PhotoImage(file='music.png')
    imresume = PhotoImage(file='resume.png')
    imvolumeup = PhotoImage(file='volume-up.png')
    imvolumedown = PhotoImage(file='volume-down.png')
    ################## change size of image
    implay = implay.subsample(2,2)
    impause = impause.subsample(2,2)
    imstop = imstop.subsample(2,2)
    immusic = immusic.subsample(2,2)
    imvolumeup = imvolumeup.subsample(2,2)
    imvolumedown = imvolumedown.subsample(2,2)
    imresume = imresume.subsample(2, 2)


    ####################################################################### labels
    TrackLabel = Label(root,text='select audio track:',bg='lightskyblue',font=('aerial','15','italic bold'),)
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)
    AudiostatusLabel = Label(root,text='',bg='lightskyblue',font=('aerial','15','italic bold'),width=20)
    AudiostatusLabel.grid(row=2,column=1)
    ######################################################################### Entry box
    TrackLabelEntry = Entry(root,font=('aerial','16','italic bold'),width=35,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)
    ###############################################################################  buttons
    BrowseButton = Button(root,text='search',bg='red',font=('aerial','13','italic bold'),width=200,bd=5,activebackground='purple',image=immusic,compound=RIGHT,command=musicurl)
    BrowseButton.grid(row=0,column=3,padx=20,pady=20)
    ################################################################################    play button
    playButton = Button(root, text='play', bg='green2', font=('aerial', '13', 'italic bold'), width=200, bd=5, activebackground='purple',image= implay,compound=RIGHT,command=playmusic)
    playButton.grid(row=1, column=0, padx=20, pady=20)
    ################################################################################   pause button
    root.pauseButton = Button(root, text='pause', bg='blue', font=('aerial', '13', 'italic bold'), width=200, bd=5,
                        activebackground='purple',image=impause,compound=RIGHT,command=pausemusic)
    root.pauseButton.grid(row=1, column=1, padx=20, pady=20)
    #################################################################################  Resume button
    root.ResumeButton = Button(root, text='Resume', bg='blue', font=('aerial', '13', 'italic bold'), width=200, bd=5,
                         activebackground='purple', image=imresume, compound=RIGHT,command=resumemusic)
    root.ResumeButton.grid(row=1, column=1, padx=20, pady=20)
    root.ResumeButton.grid_remove()
    ################################################################################## stop button
    stopButton = Button(root, text='stop', bg='green2', font=('aerial', '13', 'italic bold'), width=200, bd=5,
                        activebackground='purple',image=imstop,compound=RIGHT,command=stopmusic)
    stopButton.grid(row=2, column=0, padx=20, pady=20)
    volumeupButton = Button(root, text='volumeup', bg='yellow', font=('aerial', '13', 'italic bold'), width=200, bd=5,
                        activebackground='purple',image=imvolumeup,compound=RIGHT,command=volumeup)
    volumeupButton.grid(row=1, column=3, padx=20, pady=20)
    volumedownButton = Button(root, text='volumedown', bg='yellow', font=('aerial', '13', 'italic bold'), width=200, bd=5,
                        activebackground='purple',image=imvolumedown,compound=RIGHT,command=volumedown)
    volumedownButton.grid(row=2, column=3, padx=20, pady=20)

##################################################################################  progressbar volume
    ProgressbarLabel = Label(root,text='',bg='red')
    ProgressbarLabel.grid(row=0,column=4,rowspan=3,padx=40,pady=20)
    ProgressbarLabel.grid_remove()

    ProgressbarVolume = Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',value=0,length=250)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)

    ProgressbarVolumeLabel = Label(ProgressbarLabel,text='0%',bg='lightgray', width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)
###################################################################################  Progressbar music
    ProgressbarMusicLabel = Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=4,padx=40,pady=20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel, text='0:00:0', bg='red')
    ProgressbarMusicStartTimeLabel.grid(row=0, column=0 )

    ProgressbarMusic = Progressbar(ProgressbarMusicLabel ,orient=HORIZONTAL,mode='determinate',value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=390,ipady=3)

    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel, text='0:00:0', bg='red')
    ProgressbarMusicEndTimeLabel.grid(row=0, column=2)

###########################################################################################
from  tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
root = Tk()
root.geometry('1200x600+200+100')
root.title('simple music player..')
root.resizable(False,False)
root.configure(bg='lightskyblue')
####################################################################################   global variables
audiotrack = StringVar()
##################################################  create slider
ss = 'Developed by hritik bansal'
count = 0
text = ''
SliderLabel = Label(root,text=ss,bg='lightskyblue',font=('aerial', '40', 'italic bold'))
SliderLabel.grid(row=4,column=0,padx=20,pady=20,columnspan=4)
def IntroLabelTrick():
     global count,text
     if(count>=len(ss)):
         count = -1
         text = ''
         SliderLabel.configure(text=text)
     else:
         text = text+ss[count]
         SliderLabel.configure(text=text)
         count += 1
         SliderLabel.after(200,IntroLabelTrick)
IntroLabelTrick()
mixer.init()
createwidthes()
root.mainloop()