from flask import Flask, request, render_template
from stories import story



app = Flask(__name__)
# app.config('SECRET_KEY') == 'secret'

# debug = DebugToolbarExtension(app)

@app.route('/')
def ask_question():
    '''Create and show form for word completion'''

    prompts = story.prompts


    return render_template('questions.html', prompts=prompts)

@app.route('/stories')
def present_stories():
    '''Will show story result'''

    text = story.generate(request.args)

    return render_template('story.html', text=text)