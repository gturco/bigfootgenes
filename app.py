"""
bigfootgenes

"""

import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename

app = Flask(__name__, static_folder='public', static_url_path='')

app.debug = True
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = "/tmp/uploads"
app.config['SNP_REPORT_OUTPUT_FOLDER'] = "/tmp/snp-reports"
ALLOWED_EXTENSIONS = set(['txt', 'tsv'])

# production
app_env = 'development'
if 'APP_ENV' in os.environ:
   app_env = os.environ['APP_ENV']

if app_env == 'production':
    pass
else:
    pass

###
# Routing for your application.
###
@app.route('/')
def index():
    """Render website's home page."""
    return app.send_static_file(os.path.join('index.html'))

@app.route('/23andme/report', methods=['POST'])
def create():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)

        # TODO queue up task or run in thread?
        output = os.path.join(app.config['SNP_REPORT_OUTPUT_FOLDER'], filename)

        # import subprocess
        # cmd = "python write_twenty_three_and_me_report.py -i {0} -o {1}".format(path, output)
        # output = subprocess.check_output(cmd, shell=True)

    return render_template('queued.html')

@app.route('/snps/report')
def get():
    snps = {count: 0, records: [{'rsid': '23423', 'summary': 'This is a test'}]}
    return render_template('snps/report.html', snps=snps)

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return app.send_static_file(os.path.join('404.html'))

if __name__ == '__main__':
    app.run(debug=True)

