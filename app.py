from flask import Flask, render_template, request
from record import recorder, stopRecording


app = Flask(__name__)


summaries = []


@app.route("/")
def home():
    return render_template("index.html", summaries=summaries)


@app.route("/start_recording", methods=["POST"])
def start_recording():
    global summaries

    if request.method == "POST":
        company = request.form.get("company")
        participants = request.form.get("participant")
        summary = recorder()

        summary = summary.replace("Summary:", "!!!")
        summary = summary.replace("Key Insights:", "!!!")
        summary = summary.replace("Next Steps:", "!!!")
        summary = summary.replace("Questions:", "!!!")

        split_summary = summary.split("!!!")

        print(summary)

        print(split_summary)

        summaries.append([len(summaries), split_summary[1:], company, participants])

    return render_template("index.html")


@app.route("/stop_recording")
def stop_recording():
    stopRecording()
    return home()


@app.route("/summary", methods=["GET"])
def summary():
    if request.method == "GET":
        currSummary = summaries[int(request.args["summarynumber"])]

        if len(currSummary[1]) == 4:
            return render_template(
                "summary.html",
                summary=currSummary[1][0],
                keyinsights=currSummary[1][1],
                nextsteps=currSummary[1][2],
                questions=currSummary[1][3],
            )
        else:
            return render_template(
                "summary.html",
                summary="",
                keyinsights="",
                nextsteps="",
                questions="",
            )

    else:
        return ""
