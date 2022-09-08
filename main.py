from flask import *

from app import assign_time_slot

app = Flask(__name__)
df = assign_time_slot()


@app.route('/', methods=("POST", "GET"))
def hello_world():
    data = assign_time_slot()
    track1 = (data.loc[data['Track'] == 1]).sort_index()
    track2 = (data.loc[data['Track'] == 2]).sort_index()
    return render_template('index.html', tables=[track1.to_html(classes='track1'), track2.to_html(classes='track2')],
                           titles=['na', 'Track1 schedule', 'Track2 schedule'])


if __name__ == "__main__":
    app.run(debug=True)
