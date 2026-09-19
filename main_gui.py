import os
import sys
import platform
import tkinter as tk
from tkinter import ttk, messagebox




class FizickoLice:
    __id: str
    __ime_prezime: str
    __adresa: str
    __postanski_broj: str
    __grad: str
    __broj_telefona: str
    __tekuci_racun: str
    __instagram: str

    def __init__(
        self,
        id,
        ime_prezime,
        adresa,
        postanski_broj,
        grad,
        broj_telefona,
        tekuci_racun,
        instagram
    ):
        self.__id = id
        self.__ime_prezime = ime_prezime
        self.__adresa = adresa
        self.__postanski_broj = postanski_broj
        self.__grad = grad
        self.__broj_telefona = broj_telefona
        self.__tekuci_racun = tekuci_racun
        self.__instagram = instagram

    @property
    def id(self):
        return self.__id

    @property
    def ime_prezime(self):
        return self.__ime_prezime

    @property
    def adresa(self):
        return self.__adresa

    @property
    def postanski_broj(self):
        return self.__postanski_broj

    @property
    def grad(self):
        return self.__grad

    @property
    def broj_telefona(self):
        return self.__broj_telefona

    @property
    def tekuci_racun(self):
        return self.__tekuci_racun

    @property
    def instagram(self):
        return self.__instagram

    @classmethod
    def ucitaj_iz_fajla(cls, fajl):
        lica = []

        if not os.path.exists(fajl):
            return lica

        f = open(fajl, "r", encoding="utf-8")
        niz = f.readlines()
        f.close()

        for red in niz:
            red = red.strip()

            if red == "":
                continue

            podaci = [p.strip() for p in red.split(",")]

            if len(podaci) == 8:
                lice = cls(
                    podaci[0],
                    podaci[1],
                    podaci[2],
                    podaci[3],
                    podaci[4],
                    podaci[5],
                    podaci[6],
                    podaci[7]
                )

                lica.append(lice)

        return lica

    def redosled_za_tabelu(self):
        return (
            self.id,
            self.ime_prezime,
            self.adresa,
            self.postanski_broj,
            self.grad,
            self.broj_telefona,
            self.tekuci_racun,
            self.instagram,
        )

    def odgovara_pretrazi(self, pretraga):
        pretraga = pretraga.lower()
        return (
            pretraga in self.id.lower()
            or pretraga in self.ime_prezime.lower()
            or pretraga in self.adresa.lower()
            or pretraga in self.postanski_broj.lower()
            or pretraga in self.grad.lower()
            or pretraga in self.broj_telefona.lower()
            or pretraga in self.tekuci_racun.lower()
            or pretraga in self.instagram.lower()
        )

    def tekst_za_stampu(self):
        tekst = "PODACI O FIZICKOM LICU\n"
        tekst += "============================\n"
        tekst += f"Ime i prezime: {self.ime_prezime}\n"
        tekst += f"Ulica/Adresa: {self.adresa}\n"
        tekst += f"Postanski broj: {self.postanski_broj}\n"
        tekst += f"Opstina/Grad: {self.grad}\n"
        tekst += f"Broj telefona: {self.broj_telefona}\n"
        tekst += "\n"
        tekst += "IZNOS ZA UPLATU: __________________\n"
        tekst += "\n"
        tekst += f"Tekuci racun: {self.tekuci_racun}\n"
        return tekst


class Parfimerija:
    __id: str
    __ime: str
    __adresa: str
    __grad: str
    __broj_telefona: str
    __kontakt_osoba: str
    __instagram: str

    def __init__(
        self,
        id,
        ime,
        adresa,
        grad,
        broj_telefona,
        kontakt_osoba,
        instagram
    ):
        self.__id = id
        self.__ime = ime
        self.__adresa = adresa
        self.__grad = grad
        self.__broj_telefona = broj_telefona
        self.__kontakt_osoba = kontakt_osoba
        self.__instagram = instagram

    @property
    def id(self):
        return self.__id

    @property
    def ime(self):
        return self.__ime

    @property
    def adresa(self):
        return self.__adresa

    @property
    def grad(self):
        return self.__grad

    @property
    def broj_telefona(self):
        return self.__broj_telefona

    @property
    def kontakt_osoba(self):
        return self.__kontakt_osoba

    @property
    def instagram(self):
        return self.__instagram

    @classmethod
    def ucitaj_iz_fajla(cls, fajl):
        parfimerije = []

        if not os.path.exists(fajl):
            return parfimerije

        f = open(fajl, "r", encoding="utf-8")
        niz = f.readlines()
        f.close()

        for red in niz:
            red = red.strip()

            if red == "":
                continue

            podaci = [p.strip() for p in red.split(",")]

            if len(podaci) == 7:
                parfimerija = cls(
                    podaci[0],
                    podaci[1],
                    podaci[2],
                    podaci[3],
                    podaci[4],
                    podaci[5],
                    podaci[6]
                )

                parfimerije.append(parfimerija)

        return parfimerije

    def redosled_za_tabelu(self):
        return (
            self.id,
            self.ime,
            self.adresa,
            self.grad,
            self.broj_telefona,
            self.kontakt_osoba,
            self.instagram,
        )

    def odgovara_pretrazi(self, pretraga):
        pretraga = pretraga.lower()
        return (
            pretraga in self.id.lower()
            or pretraga in self.ime.lower()
            or pretraga in self.adresa.lower()
            or pretraga in self.grad.lower()
            or pretraga in self.broj_telefona.lower()
            or pretraga in self.kontakt_osoba.lower()
            or pretraga in self.instagram.lower()
        )

    def tekst_za_stampu(self):
        tekst = "PODACI O PARFIMERIJI\n"
        tekst += "============================\n"
        tekst += f"Ime parfimerije: {self.ime}\n"
        tekst += f"Ulica/Adresa: {self.adresa}\n"
        tekst += f"Grad: {self.grad}\n"
        tekst += f"Broj telefona: {self.broj_telefona}\n"
        tekst += f"Kontakt osoba: {self.kontakt_osoba}\n"
        return tekst


def sacuvaj_sve_u_fajl(fajl, podaci):
    

    linije = [",".join(stavka.redosled_za_tabelu()) for stavka in podaci]

    with open(fajl, "w", encoding="utf-8") as f:
        if linije:
            f.write("\n".join(linije) + "\n")
        else:
            f.write("")


def posalji_na_stampu(tekst):
    

    with open("stampa.txt", "w", encoding="utf-8") as f:
        f.write(tekst)

    if platform.system() == "Windows":
        os.startfile("stampa.txt", "print")
        return True, "Podaci su poslati na stampu."
    else:
        return False, (
            "Fajl 'stampa.txt' je sacuvan.\n"
            "Automatska stampa je dostupna samo na Windows-u - "
            "otvorite fajl rucno i odstampajte ga."
        )




class Aplikacija(tk.Tk):

    KOLONE_LICA = (
        "id", "ime_prezime", "adresa", "postanski_broj",
        "grad", "broj_telefona", "tekuci_racun", "instagram"
    )
    NASLOVI_LICA = (
        "ID", "Ime i prezime", "Adresa", "Post. broj",
        "Grad", "Telefon", "Tekuci racun", "Instagram"
    )

    KOLONE_PARF = (
        "id", "ime", "adresa", "grad",
        "broj_telefona", "kontakt_osoba", "instagram"
    )
    NASLOVI_PARF = (
        "ID", "Ime parfimerije", "Adresa", "Grad",
        "Telefon", "Kontakt osoba", "Instagram"
    )

    def __init__(self):
        super().__init__()

        self.title("Evidencija - Fizicka lica i Parfimerije")
        self.geometry("1100x600")
        self.minsize(850, 450)

        self.fizicka_lica = FizickoLice.ucitaj_iz_fajla("fizicka_lica.txt")
        self.parfimerije = Parfimerija.ucitaj_iz_fajla("parfimerije.txt")

        self._napravi_stil()

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_lica = self._napravi_tab(
            notebook,
            naslov="Fizicka lica",
            podaci=self.fizicka_lica,
            kolone=self.KOLONE_LICA,
            naslovi=self.NASLOVI_LICA,
            klasa=FizickoLice,
            fajl="fizicka_lica.txt",
        )

        self.tab_parf = self._napravi_tab(
            notebook,
            naslov="Parfimerije",
            podaci=self.parfimerije,
            kolone=self.KOLONE_PARF,
            naslovi=self.NASLOVI_PARF,
            klasa=Parfimerija,
            fajl="parfimerije.txt",
        )

        notebook.add(self.tab_lica["frame"], text="Fizicka lica")
        notebook.add(self.tab_parf["frame"], text="Parfimerije")

        
        self._osvezi_tabelu(self.tab_lica)
        self._osvezi_tabelu(self.tab_parf)

    def _napravi_stil(self):
        stil = ttk.Style(self)
        try:
            stil.theme_use("clam")
        except tk.TclError:
            pass
        stil.configure("Treeview", rowheight=26, font=("Segoe UI", 10))
        stil.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

    def _napravi_tab(self, notebook, naslov, podaci, kolone, naslovi, klasa, fajl):
        frame = ttk.Frame(notebook)

        
        gornja = ttk.Frame(frame)
        gornja.pack(fill="x", padx=10, pady=(10, 5))

        ttk.Label(gornja, text="Pretraga:").pack(side="left")

        var_pretraga = tk.StringVar()
        entry = ttk.Entry(gornja, textvariable=var_pretraga, width=40)
        entry.pack(side="left", padx=(5, 5))

        info = {
            "frame": frame,
            "naslov": naslov,
            "podaci": podaci,
            "kolone": kolone,
            "naslovi": naslovi,
            "var_pretraga": var_pretraga,
            "klasa": klasa,
            "fajl": fajl,
        }

        dugme_trazi = ttk.Button(
            gornja, text="Trazi",
            command=lambda: self._osvezi_tabelu(info)
        )
        dugme_trazi.pack(side="left", padx=(0, 5))

        dugme_reset = ttk.Button(
            gornja, text="Prikazi sve",
            command=lambda: self._reset_pretraga(info)
        )
        dugme_reset.pack(side="left", padx=(0, 5))

        dugme_dodaj = ttk.Button(
            gornja, text="Dodaj novo...",
            command=lambda: self._dodaj_stavku(info)
        )
        dugme_dodaj.pack(side="left", padx=(0, 5))

        dugme_obrisi = ttk.Button(
            gornja, text="Obrisi izabrano",
            command=lambda: self._obrisi_stavku(info)
        )
        dugme_obrisi.pack(side="left")

        entry.bind("<Return>", lambda e: self._osvezi_tabelu(info))

        
        srednja = ttk.Frame(frame)
        srednja.pack(fill="both", expand=True, padx=10, pady=5)

        tree = ttk.Treeview(
            srednja, columns=kolone, show="headings", selectmode="browse"
        )
        for kol, nas in zip(kolone, naslovi):
            tree.heading(kol, text=nas)
            sirina = 160 if kol in ("adresa", "tekuci_racun") else 110
            tree.column(kol, width=sirina, anchor="w")

        vsb = ttk.Scrollbar(srednja, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)

        tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")

        info["tree"] = tree

        
        donja = ttk.Frame(frame)
        donja.pack(fill="x", padx=10, pady=(5, 10))

        label_broj = ttk.Label(donja, text="")
        label_broj.pack(side="left")
        info["label_broj"] = label_broj

        dugme_stampaj = ttk.Button(
            donja, text="Stampaj izabrano",
            command=lambda: self._stampaj(info)
        )
        dugme_stampaj.pack(side="right")

        tree.bind("<Double-1>", lambda e: self._stampaj(info))

        return info

    def _obrisi_stavku(self, info):
        tree = info["tree"]
        izabrani = tree.selection()

        if not izabrani:
            messagebox.showwarning(
                "Nista nije izabrano",
                "Izaberite red iz tabele koji zelite da obrisete."
            )
            return

        id_stavke = izabrani[0]

        stavka = None
        for s in info["podaci"]:
            if s.id == id_stavke:
                stavka = s
                break

        if stavka is None:
            messagebox.showerror("Greska", "Izabrana stavka nije pronadjena.")
            return

        potvrda = messagebox.askyesno(
            "Potvrda brisanja",
            f"Da li ste sigurni da zelite da obrisete stavku sa ID-jem "
            f"'{id_stavke}'?\n\nOva radnja se ne moze ponistiti."
        )

        if not potvrda:
            return

        info["podaci"].remove(stavka)

        try:
            sacuvaj_sve_u_fajl(info["fajl"], info["podaci"])
        except Exception as e:
            messagebox.showerror("Greska pri cuvanju", str(e))
            return

        self._osvezi_tabelu(info)

    def _dodaj_stavku(self, info):
        prozor = tk.Toplevel(self)
        prozor.title(f"Novi unos - {info['naslov']}")
        prozor.transient(self)
        prozor.grab_set()
        prozor.resizable(False, False)

        unosi = {}
        prva_entry = None

        for i, (kol, nas) in enumerate(zip(info["kolone"], info["naslovi"])):
            ttk.Label(prozor, text=nas + ":").grid(
                row=i, column=0, sticky="e", padx=8, pady=4
            )
            var = tk.StringVar()
            entry = ttk.Entry(prozor, textvariable=var, width=40)
            entry.grid(row=i, column=1, padx=8, pady=4)
            unosi[kol] = var

            if prva_entry is None:
                prva_entry = entry

        def sacuvaj():
            vrednosti = {}

            for kol, var in unosi.items():
                vrednost = var.get().strip()

                if vrednost == "":
                    messagebox.showwarning(
                        "Nepotpuni podaci",
                        "Sva polja moraju biti popunjena.",
                        parent=prozor
                    )
                    return

                if "," in vrednost:
                    messagebox.showwarning(
                        "Nedozvoljen znak",
                        "Polja ne smeju sadrzati zarez (,) jer se koristi "
                        "kao razdvajac u fajlu.",
                        parent=prozor
                    )
                    return

                vrednosti[kol] = vrednost

            novi_id = vrednosti["id"]

            for stavka in info["podaci"]:
                if stavka.id == novi_id:
                    messagebox.showwarning(
                        "ID vec postoji",
                        f"Stavka sa ID-jem '{novi_id}' vec postoji. "
                        "Izaberite drugi ID.",
                        parent=prozor
                    )
                    return

            argumenti = [vrednosti[kol] for kol in info["kolone"]]
            nova_stavka = info["klasa"](*argumenti)

            info["podaci"].append(nova_stavka)

            try:
                sacuvaj_sve_u_fajl(info["fajl"], info["podaci"])
            except Exception as e:
                info["podaci"].remove(nova_stavka)
                messagebox.showerror(
                    "Greska pri cuvanju", str(e), parent=prozor
                )
                return

            self._reset_pretraga(info)
            prozor.destroy()

        dugmici = ttk.Frame(prozor)
        dugmici.grid(
            row=len(info["kolone"]), column=0, columnspan=2, pady=(10, 10)
        )

        ttk.Button(dugmici, text="Sacuvaj", command=sacuvaj).pack(
            side="left", padx=5
        )
        ttk.Button(dugmici, text="Otkazi", command=prozor.destroy).pack(
            side="left", padx=5
        )

        if prva_entry is not None:
            prva_entry.focus_set()

        prozor.bind("<Escape>", lambda e: prozor.destroy())

    def _reset_pretraga(self, info):
        info["var_pretraga"].set("")
        self._osvezi_tabelu(info)

    def _osvezi_tabelu(self, info):
        tree = info["tree"]
        tree.delete(*tree.get_children())

        pretraga = info["var_pretraga"].get().strip()

        if pretraga == "":
            rezultati = info["podaci"]
        else:
            rezultati = [
                stavka for stavka in info["podaci"]
                if stavka.odgovara_pretrazi(pretraga)
            ]

        for stavka in rezultati:
            tree.insert("", "end", iid=stavka.id, values=stavka.redosled_za_tabelu())

        if pretraga == "":
            info["label_broj"].config(text=f"Ukupno: {len(rezultati)}")
        else:
            info["label_broj"].config(text=f"Pronadjeno: {len(rezultati)}")

    def _stampaj(self, info):
        tree = info["tree"]
        izabrani = tree.selection()

        if not izabrani:
            messagebox.showwarning(
                "Nista nije izabrano",
                "Izaberite red iz tabele koji zelite da odstampate."
            )
            return

        id_stavke = izabrani[0]

        stavka = None
        for s in info["podaci"]:
            if s.id == id_stavke:
                stavka = s
                break

        if stavka is None:
            messagebox.showerror("Greska", "Izabrana stavka nije pronadjena.")
            return

        tekst = stavka.tekst_za_stampu()

        try:
            uspeh, poruka = posalji_na_stampu(tekst)
        except Exception as e:
            messagebox.showerror("Greska pri stampi", str(e))
            return

        if uspeh:
            messagebox.showinfo("Stampa", poruka)
        else:
            messagebox.showwarning("Stampa", poruka)


if __name__ == "__main__":
    app = Aplikacija()
    app.mainloop()
