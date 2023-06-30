from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap4
from forms import MyForm, Upload_file
from flask_wtf import CSRFProtect
from werkzeug.utils import secure_filename
import os
from PIL import Image
from image_processor import Image_processor

app = Flask(__name__)
app.secret_key = "my super secret key"

# Bootstrap-Flask requires this line
bootstrap = Bootstrap4(app)

# Flask-WTF requires this line
csrf = CSRFProtect(app)

img_processor = Image_processor()


@app.route("/", methods=["GET", "POST"])
def home():
    form = Upload_file()
    if request.method == "GET":
        image_href = "static/pictures/Puna_uscata.jpg"
        img_processor.make_all_the_circle(image_path=image_href, top_nr=10, window_color_width=25)
        nr_of_top = img_processor.nr_of_top
        dict_of_top_colors = img_processor.sorted_dictionary

    if form.validate_on_submit():
        f = form.file.data
        top_nr_form = int(request.form.get("nr_of_top"))
        window_of_colors = int(request.form.get('window_of_colors'))
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            "static/pictures", filename
        ))
        img_processor.make_all_the_circle(image_path=f, top_nr=top_nr_form,window_color_width=window_of_colors)
        image_href = os.path.join("static/pictures", filename)
        # img_processor.make_all_the_circle(image_path=image_href, top_nr=10,
        #                                   window_color_width=10)
        nr_of_top = img_processor.nr_of_top
        dict_of_top_colors = img_processor.sorted_dictionary

        return render_template("index.html", form = form, image = image_href, nr_of_top = nr_of_top, dict_of_top_colors = dict_of_top_colors)

    return render_template("index.html", form = form, image = image_href, nr_of_top = nr_of_top, dict_of_top_colors = dict_of_top_colors)


if __name__ == "__main__":
    app.run(port=5000, debug=True)

