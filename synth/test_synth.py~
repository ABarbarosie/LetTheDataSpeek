import time
import fluidsynth

fs = fluidsynth.Synth()
fs.start()

sfid = fs.sfload("JR_String2.sf2")
fs.program_select(0, sfid, 0, 0)

print "note on"

fs.noteon(0, 60, 30)
fs.noteon(0, 67, 30)
fs.noteon(0, 76, 30)

time.sleep(5.0)

fs.noteoff(0, 60)
fs.noteoff(0, 67)
fs.noteoff(0, 76)

print "note off"

time.sleep(1.0)

fs.delete()