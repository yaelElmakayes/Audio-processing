import vlc
import time
sound = vlc.MediaPlayer(r"C:\Users\יעל אלמקייס\Downloads\creativeminds.mp3")
sound.play()
for i in range(60):
   time.sleep(1)
