"""
bigfootgenes

"""

import logging
import uuid
import os
import subprocess
import json
import mysql.connector
from contextlib import closing
from multiprocessing import Process

from flask import Flask, render_template, request, redirect, url_for, g, json
from werkzeug import secure_filename

logger = logging.getLogger(__name__)
app = Flask(__name__, static_folder='public', static_url_path='')

app.debug = True
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = "./uploads"
ALLOWED_EXTENSIONS = set(['txt', 'tsv'])

app_env = 'development'
if 'APP_ENV' in os.environ:
   app_env = os.environ['APP_ENV']

db_user = "bigfootgenes"
db_pass = "dk34DFko99FDOQ"
db_name = "bigfootgenes_development"
db_url = "127.0.0.1"

# overwrite any default settings for production
if app_env == 'production':
    pass

@app.before_request
def before_request():
    if 'cnx_pool' in g:
        g.conn = g.cnx_pool.get_connection()
    else:
        mysql_config = {'pool_name': "bigfootgenes_pool",
                        'pool_size': 10,
                        'autocommit': True,
                        'user': db_user,
                        'password': db_pass,
                        'host': db_url,
                        'database': db_name}

        g.cnx_pool = mysql.connector.pooling.MySQLConnectionPool(**mysql_config)
        g.conn = g.cnx_pool.get_connection()
###
# Routing for your application.
###
@app.route('/')
def index():
    """Render website's home page."""
    return render_template('index.html')

@app.route('/help')
def help():
    """Render help page."""
    return render_template('help.html')

@app.route('/snps/reports', methods=['POST'])
def create_report():
    report_id = str(uuid.uuid4())
    file = request.files['file']

    if file:
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
    else:
        return render_template('error.html')

    # start in separate process to avoid blocking web request
    p = Process(target=run_report, args=(path, report_id,))
    p.start()

    return render_template('queued.html', report_id=report_id)

@app.route('/snps/reports/<report_id>.json')
def show_report_json(report_id):
    snps = get_snps(report_id)
    return json.jsonify(snps)

@app.route('/snps/reports/<report_id>')
def show_report(report_id):
    snps = get_snps(report_id)
    return render_template('snps/report.html', snps=snps)

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return app.send_static_file(os.path.join('404.html'))

def get_snps(report_id):
    query = ("SELECT userid, rsid, genotype, summary FROM user_snps "
             "WHERE userid = %s")

    records = []
    with closing(g.conn.cursor()) as cur:
        cur.execute(query, (report_id,))
        for (userid, rsid, genotype, summary) in cur:
            values = {'rsid': rsid, 'genotype': genotype, 'summary': summary}
            records.append(values)

    snps = {'count': len(records), 'records': records}
    return snps

def run_report(genotype_datafile_path, report_id):
    cmd = ["python",
           "bigfootgenes/insert_23andme_report_to_mysql.py",
           "-i",
           genotype_datafile_path,
           "-u",
           report_id]

    logger.info("Running")
    logger.info(cmd)

    subprocess.call(cmd)

if __name__ == '__main__':
    app.run(debug=True)
