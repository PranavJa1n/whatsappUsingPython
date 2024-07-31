from flask import Flask
app = Flask(__name__)

@app.route("/wmsg/<personno>/<msg>")
def wspmsg(personno, msg):
	import pywhatkit
	pywhatkit.sendwhatmsg_instantly(personno, msg,wait_time = 20)
	return "Whatsapp message sent."

@app.route("/wmsgshedule/<personno>/<msg>/<hour>/<min>")
def wspmsgs(personno, msg, hr, mn):
	import pywhatkit
	pywhatkit.sendwhatmsg(personno, msg, int(hr), int(mn))	
	return "Whatsapp message sent."

app.run(host = "0.0.0.0", port = 80)
