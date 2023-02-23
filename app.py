from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story1

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


@app.route("/home")
def home():
    prompt_list = story1.prompts
    return render_template("home.html", story_prompts=prompt_list)

# my try also works, but creating another dict is unnecessary
# @app.route("/story")
# def story():
#     prompt_list = story1.prompts
#     prompt_dict = {}
#     for prompt in prompt_list:
#         prompt_dict[prompt] = request.args.get(prompt)
#     story = story1.generate(prompt_dict)
#     return render_template("story.html", dict=prompt_dict, story=story)


@app.route("/story")
def show_story():
    """Show story result."""

    text = story1.generate(request.args)

    return render_template("story.html", story=text)


@app.route("/")
def blank():
    return "Nothing Here"
