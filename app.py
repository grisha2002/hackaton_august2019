from flask import Flask, render_template, urls_for
app = Flask(__name__)
@app.route("/")
def main():
	return render_template('SITE.html')
	return render_template('SITE.css')
if __name__ == "__main__":
    app.run()