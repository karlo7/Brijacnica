import sqlite3

def connect():
    db = sqlite3.connect("baza.db")
    return db

def prijava(korisnik, lozinka):
    
    db=connect()

    cur=db.cursor()

    cur.execute("SELECT * FROM Korisnici WHERE kor_ime = ? AND lozinka = ?", (korisnik, lozinka))
    
    korisnik = cur.fetchone()
    
    db.close()

    return korisnik

def registracija(ime, prezime, kor_ime, tel, email, lozinka):

    db = connect()

    cur = db.cursor()

    cur.execute("INSERT INTO Korisnici(ime, prezime, email, tel, kor_ime, lozinka) VALUES(?, ?, ?, ?, ?, ?)", (ime, prezime, email, tel, kor_ime, lozinka))

    db.commit()

    db.close()

    return id

def dohvati_korisnika_preko_id(kor_id):

    db = connect()

    cur = db.cursor()
    print('id: ', kor_id)
    cur.execute("SELECT * FROM Korisnici WHERE id = ?", (kor_id,))

    _korisnik = cur.fetchone()
    print('kor #2: ', kor_id)
    db.close()

    return _korisnik

def spremi_promjene(kor_id, ime, prezime, email, kor_ime, lozinka, tel):
    db = connect()

    cur = db.cursor()

    cur.execute("UPDATE Korisnici SET ime = ?, prezime = ?, email = ?, tel = ? , kor_ime = ?, lozinka = ? WHERE id = ?", (ime, prezime, email, tel, kor_ime, lozinka, kor_id))

    db.commit()

    db.close()

    return id


def spremi_rezervaciju(kor_id, ime, usluga, datum, vrijeme, tel):

    db = connect()

    cur = db.cursor()

    cur.execute("SELECT COUNT(*) FROM Rezervacije")
    print('r: ', kor_id, ime, usluga, datum, vrijeme, tel)
    b = cur.fetchall()
    
    broj = b[0][0] + 1
    cur.execute("INSERT INTO Rezervacije(ime, tel, usluga, vrijeme, datum, broj, kor_id) VALUES(?, ?, ?, ?, ?, ?, ?)", (ime, tel, usluga, vrijeme, datum, broj, kor_id))
    broj = broj + 1
    print('broj: #2', broj)
   

    db.commit()

    db.close()

    return broj

def dohvati_rezervacije_korisnika(kor_id):

    db=connect()

    cur=db.cursor()

    cur.execute("SELECT * FROM Rezervacije WHERE kor_id = ?", (kor_id,))
    
    rez = cur.fetchall()
    
    db.close()

    return rez

def dohvati_rezervaciju(rez_id):
    db=connect()

    cur=db.cursor()

    cur.execute("SELECT * FROM Rezervacije WHERE id = ?", (rez_id,))
    
    rez = cur.fetchone()
    
    db.close()

    return rez

def spremi_promjene_rezervacije(rez_id, ime, usluga, datum, vrijeme, tel):
    db = connect()

    cur = db.cursor()

    cur.execute("UPDATE Rezervacije SET ime = ?, usluga = ?, datum = ?, vrijeme = ? , tel = ? WHERE id = ?", (ime, usluga, datum, vrijeme, tel, rez_id))

    db.commit()

    db.close()

    return rez_id

def obrisi_rezervaciju(rez_id):
    db = connect()

    cur = db.cursor()

    cur.execute("DELETE FROM Rezervacije WHERE id = ?", (rez_id,))

    db.commit()

    db.close()

    return rez_id