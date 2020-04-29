#This is a simplified version of the abstract math task
#Participants watch instructional videos (only the shortest videos are included; GitHub does not allow me to upload the other videos)
#After watching the videos, subjects solve practice problems,instructional problems, and a post test
#This task does not have multiple conditions
#Every participant solves all problems

from psychopy import gui, visual, sound, event, core, misc
from psychopy.hardware import keyboard

window = None
task_start_time = None
kb = None
log_file = None
procs = []
rules = []
pracs = []
rulenames = []
pracnames = []
instnames = []
insts = []
postnames = []
posts = []


def Initialize():
    #declare global variables
    global task_start_time
    global window
    global kb
    global log_file
    global procs
    global rules
    global pracs
    global rulenames
    global pracnames
    global instnames
    global insts
    global postnames
    global posts
    global gui
    
    #Calculate start time of the task. 
    task_start_time = core.getTime()
    
    #define window for experiment
    window = visual.Window([1200, 750], monitor = "testMonitor", units = "deg", screen = 0, color = 'white')
    
    #initialize keyboard
    kb = keyboard.Keyboard()
    
    #log data and append new data to existing file
    log_file = open('abstractmathdatafile.csv', 'a')
    
    #path for where my files are located on my personal computer
    path = '/Users/MaryAldugom/Desktop/ProgrammingMathTask'
    
    #images for all of the instructions along the way
    procs = ['Proc01.jpeg','Proc03.jpeg','Proc04.jpeg','Proc05.jpeg']
        
    #names for each rule video
    rulenames = ['Rule03', 'Rule04', 'Rule05']
    
    #video files for each rule (only included the ones that would upload to GitHub due to size issues)
    rules = ['Rule_3_GE.mp4','Rule_4_GE.mp4','Rule_5_GE.mp4']
    
    #names for each practice problem
    pracnames = ['Prac01', 'Prac02', 'Prac03', 'Prac04', 'Prac05', 'Prac06']
    
    #practice problems image files
    pracs = ['Prac01.jpeg', 'Prac02.jpeg', 'Prac03.jpeg', 'Prac04.jpeg', 'Prac05.jpeg', 'Prac06.jpeg']
    
    #names for each instructional problem
    instnames = ['Inst01', 'Inst02', 'Inst03', 'Inst04', 'Inst05', 'Inst06', 'Inst07', 'Inst08']
    
    #instructional problem image files
    insts = ['Inst01.jpeg', 'Inst02.jpeg', 'Inst03.jpeg', 'Inst04.jpeg', 'Inst05.jpeg', 'Inst06.jpeg', 'Inst07.jpeg', 'Inst08.jpeg']
    
    #names for each post test problem
    postnames = ['Post01', 'Post02', 'Post03', 'Post04', 'Post05', 'Post06', 'Post07', 'Post08',
        'Post09', 'Post10', 'Post11', 'Post12', 'Post13', 'Post14', 'Post15', 'Post16',
        'Post17', 'Post18', 'Post19', 'Post20', 'Post21', 'Post22', 'Post23', 'Post24',
        'Post25', 'Post26', 'Post27', 'Post28', 'Post29', 'Post30', 'Post31', 'Post32',
        'Post33', 'Post34', 'Post35']
    
    #posttest that consists of 35 questions ranging in complexity
    posts = ['Post01.jpeg', 'Post02.jpeg', 'Post03.jpeg', 'Post04.jpeg', 'Post05.jpeg', 'Post06.jpeg', 'Post07.jpeg', 'Post08.jpeg',
        'Post09.jpeg', 'Post10.jpeg', 'Post11.jpeg', 'Post12.jpeg', 'Post13.jpeg', 'Post14.jpeg', 'Post15.jpeg', 'Post16.jpeg',
        'Post17.jpeg', 'Post18.jpeg', 'Post19.jpeg', 'Post20.jpeg', 'Post21.jpeg', 'Post22.jpeg', 'Post23.jpeg', 'Post24.jpeg',
        'Post25.jpeg', 'Post26.jpeg', 'Post27.jpeg', 'Post28.jpeg', 'Post29.jpeg', 'Post30.jpeg', 'Post31.jpeg', 'Post32.jpeg',
        'Post33.jpeg', 'Post34.jpeg', 'Post35.jpeg']
    
    
    
def RunMathTask(): 
    #declare global variables
    global task_start_time
    global window
    global kb
    global log_file
    global procs
    global rules
    global pracs
    global rulenames
    global pracnames
    global instnames
    global insts
    global postnames
    global posts
    global gui
    
    #Get Subject ID using gui
    
    gui = gui.Dlg()
    gui.addField("Subject ID:")
    gui.show()
    SubjectID = gui.data[0]
    print(SubjectID)
    
    
    #onset of first instruction via image
    
    proc1 = visual.ImageStim(window, image = 'Proc01.jpeg')
    
    proc1.draw()
    window.flip()
    
    proc1response = event.waitKeys(keyList = ['space',], timeStamped = True)
    
    
    #Rule videos and practice problem sequence
    
    #play each of the 6 rule videos
    for i in range(3):
        rulemov = visual.MovieStim3(window, name=rulenames[i], noAudio=False, filename=rules[i])
        
        rulemov.play()

    #play full video for each
        for j in range(int(rulemov.duration*60)):
            rulemov.draw()
            window.flip()
            
            
    
    #show each of the 6 practice problems, participants have to answer each one using '1', '2', or '3'
    responserec = ""
    
    for i in range(6):
        ruleprac = visual.ImageStim(window, name=pracnames[i], image=pracs[i])
        
        ruleprac.draw()
        window.flip()
        
        pracresponse = event.waitKeys(keyList = ['1', '2', '3',], timeStamped = True)
        
        #log Subject ID, name of the problem, and response to each problem
        log_file.write(SubjectID + "," + pracnames[i] + "," + pracresponse[0][0] + "\n")
    
    
    #onset of second instruction via image (we skip Proc02 in the lab and go right to Proc03)
    proc3 = visual.ImageStim(window, image = 'Proc03.jpeg')
    
    proc3.draw()
    window.flip()
    
    proc3response = event.waitKeys(keyList = ['space',], timeStamped = True)
    
    #instructional problem sequence
    
    #show each of the 8 instructional problems, participants have to answer each one using '1', '2', or '3'
    responserec = ""
    
    for i in range(8):
        instprobs = visual.ImageStim(window, name=instnames[i], image=insts[i])
        
        instprobs.draw()
        window.flip()
        
        instresponse = event.waitKeys(keyList = ['1', '2', '3',], timeStamped = True)
        
        #log Subject ID, name of the problem, and response to each problem
        log_file.write(SubjectID + "," + instnames[i] + "," + instresponse[0][0] + "\n")
        
        
    #onset of next instruction screen via image (this image prompts the post test)
    proc4 = visual.ImageStim(window, image = 'Proc04.jpeg')
    
    proc4.draw()
    window.flip()
    
    proc4response = event.waitKeys(keyList = ['space',], timeStamped = True)
    
    
    
    
    #beginning of post test
    
    #show each of the 8 instructional problems, participants have to answer each one using '1', '2', or '3'
    responserec = ""
    
    for i in range(35):
        postprobs = visual.ImageStim(window, name= postnames[i], image=posts[i])
        
        postprobs.draw()
        window.flip()
        
        postresponse = event.waitKeys(keyList = ['1', '2', '3',], timeStamped = True)
        
        #log Subject ID, name of the problem, and response to each problem
        log_file.write(SubjectID + "," + postnames[i] + "," + postresponse[0][0] + "\n")
    
    
    #onset of final instruction  screen thanking participant for participation
    proc5 = visual.ImageStim(window, image = 'Proc05.jpeg')
    
    proc5.draw()
    window.flip()
    
    proc5response = event.waitKeys(keyList = ['space',], timeStamped = True)
    


def TerminateTask():
    global window
    global log_file
    
    log_file.close()
    window.close()
    core.quit()


Initialize()
RunMathTask()
TerminateTask()
