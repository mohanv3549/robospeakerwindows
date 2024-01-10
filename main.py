import os
if __name__ == '__main__':
    print("WELCOME TO ROBO SPEAKER.............")
    print("VER 1.2v")
    while True:
        s=input("what do you want me to speak")
        if(s=='0'):
            break
        else:
            command=f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{s}\')"'
            os.system(command)

