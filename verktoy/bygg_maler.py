"""Bygger malene D1–D3 (docs/maler/d1.md … d3.md) fra spesifikasjonen under.

Kjør fra repoets rot:  python verktoy/bygg_maler.py

Hvert felt har en fast nøkkel (data-k). Ikke endre nøklene etter at malene er tatt i bruk,
ellers finner ikke nettleseren igjen svarene brukerne har skrevet.
"""
import html
import pathlib

ROT = pathlib.Path(__file__).resolve().parent.parent
UT = ROT / "docs" / "maler"

# ---------------------------------------------------------------- valglister
FASE = [("", ""), ("samle", "Samle inn"), ("klargj", "Klargjøre"), ("analyse", "Analysere"), ("formidle", "Formidle"),
        ("flere", "Flere faser"), ("?", "?")]
ALLE_NOEN = [("", ""), ("alle", "Alle"), ("noen", "Noen"), ("?", "?")]
OBJEKT = [("", ""), ("data", "data"), ("system", "system")]
TYPE = [("", ""), ("meta", "meta · metadata"), ("micro", "micro · mikrodata"), ("macro", "macro · makrodata"),
        ("stat", "stat · statistikk"), ("out", "out · utdata"), ("qual", "qual · kvalitetsindikator"),
        ("sys0", "system 0 · neste nivå"), ("sys1", "system 1 · skreddersydd kode"),
        ("sys2", "system 2 · rammeverk med meny"), ("sys3", "system 3 · rammeverk"), ("?", "?")]
RADER = [("", ""), ("1", "1 · lite"), ("2", "2 · middels"), ("3", "3 · mye"), ("?", "?")]
VARIABLER = [("", ""), ("1", "1 · svært få"), ("2", "2 · få"), ("3", "3 · mange"), ("4", "4 · svært mange"), ("?", "?")]
TILSTAND = [("", ""), ("K", "K · kildedata"), ("I", "I · inndata"), ("KL", "KL · klargjorte data"),
            ("S", "S · statistikk"), ("U", "U · utdata"), ("ingen", "ingen"), ("?", "?")]
STATUS = [("", ""), ("finnes", "finnes"), ("under arbeid", "under arbeid"), ("forslag", "forslag"), ("?", "?")]
KOBLING = [("", ""), ("dataflyt", "dataflyt"), ("metadata", "metadata"), ("avhengighet", "avhengighet")]
BEHOVTYPE = [("", ""), ("T", "T · tjeneste"), ("P", "P · prosess"), ("V", "V · variabler og tilstander"),
             ("A", "A · avhengighet"), ("?", "?")]
FINNES = [("", ""), ("ja", "Ja"), ("nei", "Nei"), ("?", "?")]
GJELDER = [("", ""), ("en", "Én statistikk"), ("gruppe", "En gruppe statistikker")]

DATALISTER = {
    "plattformer": ["FAME", "SAS", "Oracle ODI", "Oracle Forms", "ISEE", "Dynarev", "KOSTRA-innrapportering",
                    "Statistikkbanken", "Excel", "R", "Python", "Dapla"],
    "roller": ["saksbehandler", "statistikkansvarlig", "metode", "IT/utvikler", "formidling", "ekstern leverandør"],
}

E = html.escape


def velg(k, l, valg, cls=""):
    o = "".join(f'<option value="{E(v)}">{E(t)}</option>' for v, t in valg)
    return f'<select data-k="{E(k)}" data-l="{E(l)}" class="{cls}">{o}</select>'


def tekst(k, l, ph="", liste=None, cls=""):
    p = f' placeholder="{E(ph)}"' if ph else ""
    li = f' list="{liste}"' if liste else ""
    return f'<input type="text" data-k="{E(k)}" data-l="{E(l)}"{p}{li} class="{cls}">'


def omrade(k, l, ph="", rader=2):
    p = f' placeholder="{E(ph)}"' if ph else ""
    return f'<textarea data-k="{E(k)}" data-l="{E(l)}" rows="{rader}"{p}></textarea>'


def felt(innhold_html, lbl):
    return f'<label class="ark-felt"><span class="ark-lbl">{E(lbl)}</span>{innhold_html}</label>'


def del_(tittel, innhold, cls=""):
    return f'<section class="ark-del {cls}"><h3>{E(tittel)}</h3>{innhold}</section>'


def tabell(prefiks, kolonner, n, eksempel=None, liste=None):
    """kolonner: [(nøkkel, overskrift, type, valg/datalist, bredde)]. type: t (tekst), o (område), v (valg)."""
    hode = "<th>#</th>" + "".join(f"<th>{E(h)}</th>" for _, h, *_ in kolonner)
    rader = []
    for r in range(1, n + 1):
        celler = [f"<td class=\"ark-nr\">{r}</td>"]
        for nk, h, typ, ekstra, bredde in kolonner:
            k = f"{prefiks}.{r}.{nk}"
            ph = eksempel.get(nk, "") if (eksempel and r == 1) else ""
            if typ == "v":
                el = velg(k, h, ekstra)
            elif typ == "o":
                el = f'<textarea data-k="{E(k)}" data-l="{E(h)}" rows="1"' + (f' placeholder="{E(ph)}"' if ph else "") + "></textarea>"
            else:
                el = tekst(k, h, ph, ekstra)
            celler.append(f'<td style="min-width:{bredde}em">{el}</td>')
        rader.append("<tr>" + "".join(celler) + "</tr>")
    dl = f' data-liste="{liste}"' if liste else ""
    return (f'<div class="ark-tabell"><table class="ark-t"{dl}><thead><tr>{hode}</tr></thead>'
            f'<tbody>{"".join(rader)}</tbody></table></div>')


def felles():
    rad1 = "".join([
        felt(tekst("felles.statistikk", "Statistikk", "Eksempel: Inntekts- og kapitalregnskapet"), "Statistikk"),
        felt(tekst("felles.kortnavn", "Kortnavn", "Eksempel: NR IKR"), "Kortnavn"),
        felt(tekst("felles.seksjon", "Seksjon", "Eksempel: Seksjon for nasjonalregnskap"), "Seksjon"),
        felt(tekst("felles.kontakt", "Kontaktperson", "Rolle eller navn"), "Kontaktperson"),
    ])
    rad2 = "".join([
        felt(velg("felles.gjelder", "Gjelder", GJELDER), "Gjelder malen én statistikk eller en gruppe?"),
        felt(tekst("felles.gruppe", "Statistikker i gruppen", "Bare for grupper: kortnavn eller initialer"), "Statistikker i gruppen"),
        felt(tekst("felles.dato", "Dato", "Eksempel: 19.11.2026"), "Dato"),
    ])
    return del_("Om statistikken (følger med på alle malene)",
                f'<div class="ark-rad" style="--kol:4">{rad1}</div><div class="ark-rad" style="--kol:3">{rad2}</div>',
                "ark-felles-del")


def verktoy():
    return ('<div class="ark-verktoy">'
            '<button type="button" class="md-button md-button--primary" data-gjor="skill">Lag tekst til skillen</button>'
            '<button type="button" class="md-button" data-gjor="kopier">Kopier svarene</button>'
            '<button type="button" class="md-button" data-gjor="lastned">Last ned (.md)</button>'
            '<button type="button" class="md-button" data-gjor="skrivut">Skriv ut</button>'
            '<button type="button" class="md-button ark-tom" data-gjor="tom">Tøm malen</button>'
            '<span class="ark-status" aria-live="polite"></span></div>'
            '<div class="ark-skill" hidden><p class="ark-lbl">Tekst til skillen ssb-dataflyt. Kopier den inn i en samtale med Claude, '
            'gjerne sammen med en eventuell 2.0-fil i Excel.</p>'
            '<textarea readonly rows="8" aria-label="Tekst til skillen"></textarea>'
            '<button type="button" class="md-button" data-gjor="kopierskill">Kopier teksten</button></div>')


def datalister():
    return "".join(f'<datalist id="{i}">' + "".join(f'<option value="{E(v)}">' for v in vs) + "</datalist>"
                   for i, vs in DATALISTER.items())


def ark(id_, tittel, oppdrag, deler):
    return (f'<div class="ark" data-ark="{id_}" data-tittel="{E(tittel)}" data-oppdrag="{E(oppdrag)}">'
            f'{verktoy()}<form class="ark-skjema" onsubmit="return false">{datalister()}{felles()}{"".join(deler)}</form></div>')


def side(id_, tittel, figur, ingress, slik, skjema, forrige, neste):
    nav = []
    if forrige:
        nav.append(f"[← Mal {forrige}]({forrige.lower()}.md)")
    nav.append("[Alle malene](index.md)")
    if neste:
        nav.append(f"[Mal {neste} →]({neste.lower()}.md)")
    punkter = "\n".join(f"    {i}. {p}" for i, p in enumerate(slik, 1))
    return f'''---
title: "{id_} {tittel}"
---

# Mal {id_}: {tittel}

{ingress} Malen bygger på [figur {id_}](../5-slik-kartlegger-du.md#figur-{id_.lower()}).

!!! info "Slik fyller du ut"

{punkter}

    Svarene lagres bare i denne nettleseren. Når du er ferdig, trykker du **Lag tekst til skillen** og kopierer teksten inn i Claude. Du kan også laste ned svarene eller ta en sikkerhetskopi fra [oversikten](index.md#svarene-dine).

{skjema}

??? note "Malen som figur (til utskrift eller tavle)"

    ![Mal {id_} som figur](../figurer/{id_}.svg){{ loading=lazy }}

    [Last ned SVG](../figurer/{id_}.svg){{ download }}

{" · ".join(nav)}
'''


def d1():
    kol = [("navn", "Prosessteg", "t", None, 11), ("fase", "Fase", "v", FASE, 8), ("hva", "Hva skjer", "o", None, 14),
           ("rolle", "Hvem (rolle)", "t", "roller", 9), ("plattform", "Plattform og systemer", "t", "plattformer", 11),
           ("data", "Data inn → ut", "o", None, 12), ("avh", "Avhengigheter", "o", None, 11),
           ("gjelder", "Alle / noen", "v", ALLE_NOEN, 6)]
    eks = {"navn": "Summering og avstemming", "hva": "Summerer alle kilder og avstemmer", "rolle": "?",
           "plattform": "SAS", "data": "FIN, IKKE-FIN → INPUT EXCEL", "avh": "Inn: RG (kilde ?)"}
    deler = [
        del_("Prosessteg i rekkefølge", '<p class="ark-under">Ett steg endrer dataene og kan beskrives med én setning. '
             'Ofte 5–10 steg. Første rad viser et eksempel fra NR IKR.</p>' + tabell("D1.steg", kol, 10, eks, "_liste.D1")),
        del_("Avhengigheter for hele løpet", '<div class="ark-rad" style="--kol:2">'
             + felt(omrade("D1.inn", "Henter fra andre", "Eksempel: REA, AR, UR, OFF, registre"), "Hva henter løpet fra andre statistikker, registre eller eksterne?")
             + felt(omrade("D1.ut", "Leverer til andre", "Eksempel: Statistikkbanken, Eurostat, NR"), "Hvem bruker det som kommer ut?")
             + "</div>"),
        del_("Usikkert og spørsmål", felt(omrade("D1.sporsmal", "Usikkert og spørsmål", "Det du ikke vet, eller vil drøfte i workshopen", 3),
                                          "Hva er uklart, og hvem kan svare?")),
    ]
    oppdrag = "D1 Prosessteg og roller: oppdater modellen og lag et utkast til nivå 1 (oversikt) med prosessteg, faser, roller, plattformer og avhengigheter."
    s = ark("D1", "Prosessteg og roller", oppdrag, deler)
    return side("D1", "Prosessteg og roller", "D1",
                "Dagens løp på nivå 1: hva som skjer, hvem som gjør det, på hvilken plattform og hva som henger sammen.",
                ["**Fyll ut feltene om statistikken.** De følger med på alle malene.",
                 "**Del løpet i steg** fra innsamling til formidling. Skriv rolle, ikke navn.",
                 "**Plattform først.** Programnavn kommer i mal D2.",
                 "**Skriv «?»** der du ikke vet. Det er et gyldig svar."],
                s, None, "D2")


def d2():
    kol = [("steg", "Steg", "t", None, 4), ("id", "ID", "t", None, 5), ("navn", "Navn", "t", None, 10),
           ("objekt", "Objekt", "v", OBJEKT, 6), ("type", "Type", "v", TYPE, 11), ("rader", "Rader", "v", RADER, 7),
           ("variabler", "Variabler", "v", VARIABLER, 8), ("plattform", "Plattform", "t", "plattformer", 8),
           ("tilstand", "Stabil tilstand", "v", TILSTAND, 9), ("beskr", "Beskrivelse", "o", None, 14),
           ("status", "Status", "v", STATUS, 7)]
    eks = {"steg": "5", "id": "S1", "navn": "SAS SUM", "plattform": "SAS", "beskr": "Summerer alle kilder"}
    kkol = [("fra", "Fra ID", "t", None, 6), ("til", "Til ID", "t", None, 6), ("type", "Type", "v", KOBLING, 8),
            ("merknad", "Merknad", "t", None, 18)]
    keks = {"fra": "S1", "til": "D1", "merknad": "Eksempel: summen går videre til avstemming"}
    hent = ('<div class="ark-hent" data-fra="_liste.D1"><span class="ark-lbl">Prosesstegene fra mal D1</span>'
            '<p data-tom="Ikke fylt ut ennå. Du kan likevel bruke stegnummer her.">–</p></div>')
    deler = [
        del_("Prosesstegene", hent),
        del_("Objekter: data og systemer", '<p class="ark-under">Én rad per datasett eller system. '
             'ID-en er fri, men må være unik (for eksempel S1, S2 for systemer og D1, D2 for data). '
             'Samme system kan stå flere ganger hvis det brukes flere steder.</p>' + tabell("D2.obj", kol, 16, eks)),
        del_("Koblinger", '<p class="ark-under">Hva går fra hvor til hvor? Bruk ID-ene over. Ingen koordinater: '
             'tegningen ordner plasseringen.</p>' + tabell("D2.kob", kkol, 16, keks)),
        del_("Fra Dataflyt 2.0", felt(tekst("D2.fil20", "Eksisterende 2.0-tegning", "Filnavn eller lenke, hvis det finnes"),
                                      "Finnes det en tegning fra Dataflyt 2.0? Last den gjerne opp sammen med teksten.")),
    ]
    oppdrag = "D2 Data og systemer: bygg objekter og koblinger i modellen, og lag nivå 2 (fokus) for prosesstegene som er fylt ut."
    s = ark("D2", "Data og systemer", oppdrag, deler)
    return side("D2", "Data og systemer", "D2",
                "Nivå 2: datasettene og systemene i hvert prosessteg, og koblingene mellom dem. Malen erstatter Excel-malen fra Dataflyt 2.0.",
                ["**Ta ett prosessteg om gangen,** og skriv stegnummeret fra D1 i første kolonne.",
                 "**Velg type, rader og variabler** med de samme kodene som i Dataflyt 2.0.",
                 "**Skriv koblingene** med ID-ene fra objekttabellen.",
                 "**Stabil tilstand** er der datasettet lagres i en vedtatt Dapla-tilstand. Velg «?» hvis du ikke vet."],
                s, "D1", "D3")


def d3():
    kol = [("tilstand", "Datatilstand", "v", TILSTAND, 9), ("behov", "Behov", "o", None, 14), ("type", "Type", "v", BEHOVTYPE, 9),
           ("erstatter", "Erstatter i dag", "o", None, 11), ("verdi", "Verdi", "o", None, 12),
           ("risiko", "Risiko ved å la være", "o", None, 12), ("finnes", "Finnes i Dapla?", "v", FINNES, 7)]
    eks = {"behov": "Felles mottak og omkoding av kilder", "erstatter": "13 mottak i SAS/Excel (steg 1)",
           "verdi": "Én testet rutine, mindre vedlikehold", "risiko": "13 SAS-rutiner må flyttes før 2029"}
    deler = [
        del_("Behov per datatilstand", '<p class="ark-under">Skriv hva som trengs, ikke hvilket verktøy som skal brukes. '
             '«Finnes i Dapla?» avklares senere (B7).</p>' + tabell("D3.behov", kol, 10, eks)),
        del_("Oppsummering", '<div class="ark-rad" style="--kol:3">'
             + felt(omrade("D3.viktigst", "Det viktigste behovet", "", 3), "Hva er det viktigste behovet?")
             + felt(omrade("D3.verdi", "Mest verdi", "", 3), "Hvor gir omleggingen mest verdi?")
             + felt(omrade("D3.avklare", "Må avklares", "", 3), "Hva må avklares før løsningen kan velges?")
             + "</div>"),
    ]
    oppdrag = "D3 Behov og verdi: lag målbildeskjelettet (TO BE) med datatilstandene som ankerpunkter, og linsen behov og verdi. Behov, ikke løsninger."
    s = ark("D3", "Behov og verdi", oppdrag, deler)
    return side("D3", "Behov og verdi", "D3",
                "Målbildet: hva som må på plass i Dapla, hva det erstatter, og hva som blir bedre.",
                ["**Velg datatilstand** for hvert behov: kildedata, inndata, klargjorte data, statistikk eller utdata.",
                 "**Skriv behovet,** ikke løsningen.",
                 "**Knytt til dagens løp:** hva erstatter behovet?",
                 "**Verdi og risiko:** hva blir bedre, og hva skjer hvis vi bare flytter som i dag?"],
                s, "D2", None)


if __name__ == "__main__":
    UT.mkdir(parents=True, exist_ok=True)
    for navn, fn in [("d1.md", d1), ("d2.md", d2), ("d3.md", d3)]:
        (UT / navn).write_text(fn(), encoding="utf-8")
        print("skrev", UT / navn)
