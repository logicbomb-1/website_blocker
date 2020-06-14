from flask import Flask, request, render_template
from datetime import datetime, time
import time
import os

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/block')
def block():
    return render_template("block.html")

def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

@app.route('/wblock', methods = ['GET','POST'])
def website_block():
    host = "/etc/hosts"
    redirect = "127.0.0.1"
    website = "facebook.com"
    web1 = "google.com"
    web2 = "site.com"
    with open(host, "a") as myfile:
        myfile.write(redirect + " " + web1 + "\n")

    if (request.method == 'POST' or request.method == 'GET'):
        site = request.form['block']
        print request.form['totime']
        print request.form['fromtime']
        now = datetime.now()
        fromdate = datetime.strptime(request.form['fromtime'],'%Y-%m-%dT%H:%M')
        todate = datetime.strptime(request.form['totime'],'%Y-%m-%dT%H:%M')
        print fromdate - now
        pause =  todate - fromdate
        wait = fromdate - now
        waittime = wait.days * 24 * 3600 + pause.seconds
        print waittime
        notify(title = 'Warning',
                subtitle = "Your site is getting  blocked",
                message = web1)
        print "Your sites will be blocked in ", waittime, " seconds..."
        time.sleep(waittime)
        blocktime =  pause.days * 24 * 3600 + pause.seconds
        print "Your site is blocked. Wait for ", blocktime, "seconds.."
        notify(title = 'Warning',
                subtitle = "Your site is blocked",
                message = web1)
        time.sleep(blocktime)
        with open(host) as f1:
            lines = f1.readlines()

        with open(host, 'w') as f2:
            f2.writelines(lines[:-2])

        #each_site = site.split("\n")
        #print each_site[2]
        #es = str(each_site[2])
        #print len(each_site)
        #with open(host, "a") as mfile:
        #    print "inside"
        #    mfile.write("sdfsds")
        #    mfile.write(web1)
        #    mfile.write(es)
    #return each_site[1]

if __name__ == '__main__':
    app.run(debug=True)
