def main():
    import time
    import playsound
    start = time.time()
    playsound.playsound('first_love.mp3')
    time.sleep(2)
    print('playing sound using  playsound')
    end = time.time()
    cg=end - start 
    print(cg)
    from pydub import AudioSegment
#loading audio file form our system
    sound = AudioSegment.from_file("first_love.mp3")
#duration calculation function
    sound.duration_seconds == (len(sound) / 1000.0)
    h=sound.duration_seconds
    while True:
        if cg==h:
            sys.exit()
time.sleep(1)
print('The sound is stopped playing now')
main()
