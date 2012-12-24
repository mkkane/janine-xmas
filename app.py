import os
from functools import wraps
from flask import *
import settings
import logging

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY
app.config.from_object('settings')


########################
#        VIEWS         #
########################


###### Basic Setup ######

@app.after_request
def add_header(response):
    """Add header to force latest IE rendering engine and Chrome Frame."""
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    return response

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_error(error):
    """Custom 500 page."""
    return render_template('500.html'), 500

@app.context_processor
def override_url_for():
    return dict(url_for=cache_buster_url_for)

def cache_buster_url_for(endpoint, **values):
    if endpoint == 'static':
        values['v'] = settings.STATIC_RESOURCE_VERSION
    return url_for(endpoint, **values)

@app.route('/robots.txt')
def robots():
    return '''
User-agent: *
Disallow: /
'''

###### Helpers ######

def redirect_back_internal_url():
    """
    Get a url to send the user back to previous page

    If they would be sent to an off-site page, return the url for the
    homepage
    """
    from urlparse import urlparse
    if request.referrer:
        referrer_netloc = urlparse(request.referrer).netloc
        app_netloc = urlparse(request.url_root).netloc
        if referrer_netloc == app_netloc:
            return request.referrer
    return url_for('home')


###### Pages ######

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/find-janine')
def find_janine():
    return render_template('find-janine.html')

@app.route('/santa')
def santa():
    return render_template('santa.html')

@app.route('/come-to-matilda')
def come_to_matilda():
    return render_template('come-to-matilda.html')

@app.route('/come-to-matilda/will-come', methods=['GET', 'POST'])
def will_come():
    subject = 'Janine will come!'
    default_message = '''Dear Michael,

I will come to Matilda with you!

Janine'''

    if request.method == 'POST':
        email()
        return render_template('thanks.html')
    
    return render_template('will-come.html', subject=subject, default_message=default_message)

@app.route('/come-to-matilda/wont-come', methods=['GET', 'POST'])
def wont_come():
    subject = 'Janine won\'t come...'
    default_message = '''Michael,

Regarding your recent request that I accompany you to Matilda The Musical.  No.  I'm afraid that won't work for me.

Janine'''

    if request.method == 'POST':
        email()
        return render_template('thanks.html')

    return render_template('wont-come.html', subject=subject, default_message=default_message)


@app.route('/email', methods=['POST'])
def email():
    mail("m.k.kane@gmail.com",
         request.form['subject'],
         request.form['body'])

    return jsonify(result='ok')


def mail(to, subject, text):
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEBase import MIMEBase
    from email.MIMEText import MIMEText
    import os

    gmail_user = os.environ['GMAIL_USER']
    gmail_pwd = os.environ['GMAIL_PASSWORD']

    msg = MIMEMultipart()
    
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    
    msg.attach(MIMEText(text))

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    host = str(os.environ.get('HOST', '0.0.0.0'))
    app.run(host=host, port=port, debug=True)
