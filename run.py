# -*- coding: utf-8 -*-
import os
import flask
import random
from flask import Flask, request, jsonify,render_template
from flask_table import Table, Col
from werkzeug.utils import secure_filename
import vlc
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

UPLOAD_FOLDER = 'C:/Users/shrey/Desktop/kannada_tts/env/uploads'
ALLOWED_EXTENSIONS = {'txt', 'docx'}

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["DEBUG"] = True

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def home():
	return render_template("frontend.html")


@app.route('/play', methods=['GET'])
def play():
	return render_template("play.html")

'''@app.route('/form')
def form():
    return render_template('frontend.html')'''


@app.route('/submit',methods = ['POST'])
def submit():

    inp=request.form.get('testinput')
    print(inp)
    inp=(transliterate(inp, sanscript.ITRANS, sanscript.KANNADA))
    print(inp)

    from gtts import gTTS
    myobj = gTTS(text=inp, lang="kn", slow=False)


    def save_file():

        audio_file = ("output.mp3")
        os.chdir('C:/Users/shrey/Desktop/kannada_tts/env/static/audio')

        myobj.save(audio_file)

        #os.system(audio_file)
        print("Done")

        #os.remove("C:/Users/shrey/Desktop/kannada_tts/env/static/audio/output.mp3")
        """#opening,writing and closing the text file '<file_input>.txt'
        txt_file = open(file_input+".txt","w")
        txt_file.write(mytext)
        txt_file.close()"""

    save_file()
    '''def main(inp):
	audio = np.zeros((0,2),dtype=np.int16)
	#t=input("input in kannada")
	t = inp
	c=0
	for i in t:
	    if(c==(len(t)-1)):
	        break
	    c+=1
	    k=i+'.wav'
	    fs,data=wavfile.read(k)

	    print(audio.shape, data.shape,fs)
	    audio = np.concatenate((audio,data), axis=0)
	    print(i)

	fs1,data1=wavfile.read(t[len(t)-1]+'.wav')
	sh = data1.shape[0]
	print(sh)
	audio = np.concatenate((audio,data1[:int(sh*0.75),:]), axis=0)


	wavfile.write("out.wav",fs,audio)
    """
    #pygame.mixer.pre_init(44100, 16, 2, 4096)
    #pygame.mixer.init(22000)
    pygame.init()

    pygame.display.set_mode()
    pygame.display.set_mode()
    mixer.init
    mixer.music.load("C:/Users/shrey/Desktop/kannada_tts/env/static/audio/output.mp3")
    mixer.music.play()
    time.sleep(5)"""
    '''
    p = vlc.MediaPlayer("C:/Users/shrey/Desktop/kannada_tts/env/static/audio/output.mp3")
    p.play()
    return inp

if __name__ == '__main__':
    app.run(debug=True)
