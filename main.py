from flask import Flask, request, render_template
import domain as db


app = Flask(__name__)



@app.route('/')
def pocetna():
	return render_template('prijava.html')

@app.route('/registracija', methods=["GET", "POST"])
def registracija():
	if request.method=="GET":
		return render_template("registracija.html")
	elif request.method=="POST":
		ime = request.form.get("ime")
		prezime = request.form.get("prezime")
		email = request.form.get("korisnickoIme")
		kor_ime = request.form.get("email")
		lozinka = request.form.get("tel")
		tel = request.form.get("lozinka")
		_korisnik = db.registracija(ime, prezime, email, kor_ime, lozinka, tel)
		if _korisnik:
			return render_template("prijava.html")

@app.route('/prijava', methods=["POST"])
def prijava():
	kor_ime = request.form.get("korisnickoIme")
	lozinka = request.form.get("lozinka")
	_korisnik = db.prijava(kor_ime, lozinka)
	_rezervacije = db.dohvati_rezervacije_korisnika(_korisnik[0])
	return render_template("pocetna.html", korisnik=_korisnik, rezervacije=_rezervacije)

@app.route('/pocetna/<kor_id>', methods=["GET"])
def pocetna_povratak(kor_id):
	_korisnik = db.dohvati_korisnika_preko_id(kor_id)
	_rezervacije = db.dohvati_rezervacije_korisnika(_korisnik[0])
	return render_template("pocetna.html", korisnik=_korisnik, rezervacije=_rezervacije)

@app.route('/odjava')
def odjava():
    return render_template('prijava.html')

@app.route('/rezervacije/<kor_id>', methods=["GET", "POST"])
def rezervacije(kor_id):
	if request.method=="GET":
		_korisnik = db.dohvati_korisnika_preko_id(kor_id)
		return render_template("rezervacije.html", korisnik=_korisnik)
	elif request.method=="POST":
		ime = request.form.get("ime")
		usluga = request.form.get("usluga")
		datum = request.form.get("datum")
		vrijeme = request.form.get("vrijeme")
		tel = request.form.get("tel")
		_rez = db.spremi_rezervaciju(kor_id, ime, usluga, datum, vrijeme, tel)
		if _rez:
			_korisnik = db.dohvati_korisnika_preko_id(kor_id)
			_rezervacije = db.dohvati_rezervacije_korisnika(_korisnik[0])
			return render_template("pocetna.html", korisnik=_korisnik, rezervacije=_rezervacije)


@app.route('/uredi_rezervaciju/<rez_id>/<kor_id>', methods=["GET", "POST"])
def uredi_rezervaciju(rez_id, kor_id):
	if request.method=="GET":
		_rez = db.dohvati_rezervaciju(rez_id)
		return render_template("izmjeniRezervaciju.html", rezervacija=_rez, korisnik=kor_id)
	elif request.method=="POST":
		ime = request.form.get("ime")
		usluga = request.form.get("usluga")
		datum = request.form.get("datum")
		vrijeme = request.form.get("vrijeme")
		tel = request.form.get("tel")
		_rez = db.spremi_promjene_rezervacije(rez_id, ime, usluga, datum, vrijeme, tel)
		if _rez:
			_korisnik = db.dohvati_korisnika_preko_id(kor_id)
			_rezervacije = db.dohvati_rezervacije_korisnika(kor_id)
			return render_template("pocetna.html", korisnik=_korisnik, rezervacije=_rezervacije)

@app.route('/obrisi_rezervaciju/<rez_id>/<kor_id>', methods=["GET"])
def obrisi_rezervaciju(rez_id, kor_id):
	print('k: ', kor_id)
	_rez = db.obrisi_rezervaciju(rez_id)
	if _rez:
		_korisnik = db.dohvati_korisnika_preko_id(kor_id)
		_rezervacije = db.dohvati_rezervacije_korisnika(kor_id)
		return render_template("pocetna.html", korisnik=_korisnik, rezervacije=_rezervacije)


@app.route('/uredi_profil/<kor_id>', methods=["GET", "POST"])
def uredi_profil(kor_id):
	if request.method=="GET":
		_korisnik = db.dohvati_korisnika_preko_id(kor_id)
		return render_template("profil.html", korisnik=_korisnik)
	elif request.method=="POST":
		ime = request.form.get("ime")
		prezime = request.form.get("prezime")
		email = request.form.get("email")
		kor_ime = request.form.get("korisnickoIme")
		lozinka = request.form.get("lozinka")
		tel = request.form.get("tel")
		_korisnik = db.spremi_promjene(kor_id, ime, prezime, email, kor_ime, lozinka, tel)
		if _korisnik:
			_korisnik = db.dohvati_korisnika_preko_id(kor_id)
			return render_template("profil.html", korisnik=_korisnik)



if __name__ == "__main__":
	app.run(debug=True)