from flask import *
import pickle

f = None
try:
	f = open("churn.model", "rb")
	model = pickle.load(f)
except Exception as e:
	print("issue ", e)
finally:
	if f is not None:
		f.close()

app = Flask(__name__)
app.secret_key = "created_by_vedant"
@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		try:
			id = float(request.form["id"])
			cs = float(request.form["cs"])
			country = int(request.form["country"])
			gender = int(request.form["gender"])
			age = float(request.form["age"])
			ten = float(request.form["ten"])
			bal = float(request.form["bal"])
			pno = float(request.form["pno"])
			cc = float(request.form["cc"])
			am = float(request.form["am"])
			sal = float(request.form["sal"])
			
			country_france, country_germany, country_spain = 0, 0, 0
			gender_female, gender_male = 0, 0
			if country == 1:
				country_france = 1
			elif country == 2:
				country_germany = 1
			elif country == 3:
				country_spain = 1
			
			if gender == 1:
				gender_female = 1
			else:
				gender_male = 1
			d = [[id, cs, country_france, country_germany, country_spain, gender_female, gender_male, age, ten, bal, pno, cc, am, sal]]
			# Change model prediction code to use Decision Tree Classifier
			predict = model.predict(d)
			if predict [0] == 0:
				msg = "Churn Prediction: The customer is likely to leave the bank."
			else:
				msg = "Churn Prediction: The customer is likely to stay with the bank."
			#msg = "Churn is " + str(predict[0])
			return render_template("home.html", msg=msg)
		except Exception as e:
			msg = "Issue: " + str(e)
			return render_template("home.html", msg=msg)
	else:
		return render_template("home.html")
	

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)