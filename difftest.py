import os
from flask import Flask, jsonify, render_template, request, send_from_directory
from transcription import diff

site_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'site_unseen')
app = Flask(__name__)

@app.route('/dna/sequences/submit', methods=['POST'])
def submit_dna_sequences():
    sequence_one = request.form['sequence_one']
    sequence_two = request.form['sequence_two']
    diffs = diff(sequence_one, sequence_two)

    return render_template('index.html', diffs=diffs, sequence_one=sequence_one, sequence_two=sequence_two)


@app.route('/')
def site_index():
    return render_template('index.html')


@app.route('/<path:path>')
def send_site_file(path):
    return send_from_directory(site_dir, path)
