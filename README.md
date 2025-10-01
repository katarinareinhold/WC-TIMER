# WC-TIMER
Kuna Tamme WC-d on alati täis, siis oleks vaja timeri süsteemi, mis paneks liikluse vetsudes paremini toimima.
Liikmed: Lisette-Amanda Pulk, Katarina Reinhold, Marin Emma Teller

https://trello.com/b/YtGJEGvT/wc-timer

https://github.com/katarinareinhold/WC-TIMER/blob/main/Paberprotot%C3%BC%C3%BCp.jpg

Progesime osaliselt koos, et kõik omavahel töötaks. Failijaotus: Marin - app.py & models.py; Katarina - login.html & feedback.html; Lisette - index.html & style.css

Hetkel on kolm VIP kasutajat 
marin	parool1	
lisette	parool2	
kata	parool3	

Juhend: Lae alla wc-timer-projekt.zip ja unzipi 

  Arvutis lokaalselt jooksutamiseks: 
  
  Linux 
  1. Eeltingimused: Värskenda pakke ja paigalda Python ning venv (kui pole juba süsteemis olemas)
  sudo apt update
  sudo apt install python3 python3-pip python3-venv
  2. Liigu projekti kausta (ASENDA OMA PROJEKTI TEEGA)
  cd /tee/sinu/wc-timer-projektini
  3. Loo virtuaalkeskkond (venv)
  python3 -m venv venv
  4. Aktiveeri virtuaalkeskkond (terminali alguses peaks ilmuma '(venv)')
  source venv/bin/activate
  5. Paigalda vajalikud teegid
  pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
  6. Käivita rakendus
  python app.py
  7. Ava brauser ja mine aadressile: http://127.0.0.1:5000/
  8. Töö lõpetamisel deaktiveeri (sulge) virtuaalkeskkond
  deactivate
  
  macOS
  1. Eeltingimused: Paigalda Python 3, kui see pole veel paigaldatud (kasutades Homebrew'd)
  brew install python3
  2. Liigu projekti kausta (ASENDA OMA PROJEKTI TEEGA)
  cd /tee/sinu/wc-timer-projektini
  3. Loo virtuaalkeskkond (venv)
  python3 -m venv venv
  4. Aktiveeri virtuaalkeskkond (terminali alguses peaks ilmuma '(venv)')
  source venv/bin/activate
  5. Paigalda vajalikud teegid
  pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
  6. Käivita rakendus
  python app.py
  7. Ava brauser ja mine aadressile: http://127.0.0.1:5000/
  8. Töö lõpetamisel deaktiveeri (sulge) virtuaalkeskkond
  deactivate
  
  Windows
  1. Eeltingimused: Veendu, et Python 3 on paigaldatud koos "Add to PATH" valikuga.
  2. Liigu projekti kausta (ASENDA OMA PROJEKTI TEEGA)
  cd C:\Users\Kasutaja\Dokumendid\wc-timer-projekt
  3. Loo virtuaalkeskkond (venv)
  python -m venv venv
  4. Aktiveeri virtuaalkeskkond (terminali alguses peaks ilmuma '(venv)')
  .\venv\Scripts\Activate
  5. Paigalda vajalikud teegid
  pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
  6. Käivita rakendus
  python app.py
  7. Ava brauser ja mine aadressile: http://127.0.0.1:5000/
  8. Töö lõpetamisel deaktiveeri (sulge) virtuaalkeskkond
  deactivate
