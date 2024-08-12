from flask import Flask, request, render_template
from stories import stories



app = Flask(__name__)

@app.route('/')
def ask_story():

    '''Present the list of stories in the form'''

    return render_template('story-list.html', stories=stories.values())


@app.route('/questions')
def present_questions():
    '''Generate and show form to ask word'''

    story_id = request.args['story_id']
    story = stories[story_id]

    prompts = story.prompts

    return render_template('questions.html', story_id=story_id, title=story.title, prompts=prompts)



@app.route("/story")
def show_story():
    """Show story result."""

    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template("story.html",title=story.title, text=text)