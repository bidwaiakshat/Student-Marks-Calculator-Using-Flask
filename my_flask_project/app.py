from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/calculate", methods=["POST"])
def calc():
    name = request.form.get("name","").strip()

    subjects = ["maths", "science", "computer","english", "sst"]
    marks = []

    if not name:
        return render_template(
            "index.html", error="Please enter the student's name."
        )

    try:
        for subject in subjects:
            value = request.form.get(subject,"").strip()

            if not value:
                raise ValueError

            mark = float(value)

            if not 0 <= mark <=100:
                raise ValueError

            marks.append(mark)

    except ValueError:
        return render_template(
            "index.html",
            error = "ENter valid marks between 0 and 100."
        )

    total = sum(marks)
    percentage = total/len(marks)

    result = ("Pass" if all(mark >=40 for mark in marks)
              else "Fail")

    return render_template(
        "result.html",
        name = name,
        marks=marks,
        total=total,
        percentage = round(percentage, 2),
        result= result
    )

if __name__ == "__main__":
    app.run(debug=True)