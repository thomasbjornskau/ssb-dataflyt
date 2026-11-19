---
name: ssb-dataflyt
description: "Bruk når Thomas kartlegger eller tegner dataflyt for SSB-statistikker (Dataflyt 3.0): leser 2.0-Excel, bruker malene D1–D4 og tegner nivå 1–3, linser og AS IS/TO BE som SVG."
---

# SSB Dataflyt 3.0 (versjon 0.1, for dialog)

Dataflyt er Thomas' rammeverk for å kartlegge hvordan data og systemer henger sammen i en statistikkproduksjon. 1.0 ble tegnet for hånd i Illustrator. 2.0 tegnes fra metadata i Excel og vises i Tableau (rundt 120 flyter). 3.0 er KI-støttet kartlegging som skal peke på **behov og verdiøkende Dapla-omlegging**, ikke bare dokumentere hva som må flyttes.

Skillen bygger på **ssb-konseptfigurer**. Formfaktor, palett, panel, tegnforklaring, etiketter, SVG-regler og arbeidsform hentes derfra og gjentas ikke her. Les den skillen også når du skal tegne.

## Grunnprinsipp

Én **modell per statistikk** (YAML) er kilden. Alt som kommer inn (2.0-Excel, malene D1–D3, B5/B6, workshopnotater, skjermbilder) oppdaterer modellen. Alle tegninger og lister lages fra modellen. Lever alltid den oppdaterte modellen som fil sammen med figurene, så neste økt kan fortsette.

## Arbeidsform

- Norsk bokmål, nøkternt og direkte. Ett avklaringsspørsmål om gangen, og bare når svaret endrer det du lager.
- «?» er et gyldig svar. Det som ikke er vurdert, gjettes aldri. Vis det som stiplet grått.
- Skill tydelig mellom det som står i kildene, det du tolker, og det du foreslår. Merk tolkning i bunnlinjen og i kvalitetssikringslisten.
- Fagmiljøet eier innholdet. KI lager utkast, ikke fasit.
- Hver leveranse avsluttes med en **kvalitetssikringsliste** fordelt på hvem som må bekrefte (fagmiljøet, prosjektledelsen, Thomas).

## Tre arbeidsmåter

### A. Lese inn en eksisterende 2.0-flyt
1. Les Excel-filen med openpyxl (arket heter ofte kortnavnet, f.eks. `kortnavn`). Bruk bare rader der `mark == "shape"`. Se «Oversettelse fra 2.0».
2. Bygg modellen: objekter med egen ID, koblinger fra `coord` → `next`.
3. Tell elementer, systemer, datasett og koblinger. Disse tallene er nyttige i undertitler.
4. Tegn flyten rett fra koordinatene (nivå 2-utseende) som kontroll, og se på den.
5. Foreslå en inndeling i 5–10 prosessteg (nivå 1). Inndelingen er alltid tolkning og merkes slik.
6. Lag spørsmålsliste: roller (finnes ikke i 2.0), avhengigheter ut, objekter uten kilde, uklare navn, `step` som ikke stemmer med plasseringen.
7. Tableau-skjermbilder brukes bare for det som ble tegnet inn for hånd: forklaringsbokser, ikoner, prosessnavn, rammer.

### B. Kartlegge med malene
1. Ta inn utfylte D1 (prosessteg og roller), D2 (data og systemer) og D3 (behov og verdi), og eventuelt B5/B6 og notater.
2. Oppdater modellen. Behold kildemerke per felt: `kilde: D1 | D2 | D3 | 2.0 | workshop | tolkning`.
3. Still oppfølgingsspørsmål ett om gangen, i denne rekkefølgen: prosessteg og faser → roller → plattformer → avhengigheter inn og ut → stabile datatilstander → behov.
4. Lag ny versjon av tegningene og kvalitetssikringslisten.

### C. Tegne
Lag det som trengs fra modellen (se «Figurtyper»). Render til PNG og se på bildet før levering: overlapp, piler gjennom tekst, tekst utenfor bokser, etiketter som kolliderer med tegnforklaring eller bunnlinje.

## Datamodellen (YAML)

```yaml
statistikk: {kortnavn: NR IKR, navn: Inntekts- og kapitalregnskapet, seksjon: Seksjon for nasjonalregnskap, gruppe: false}
versjon: {dato: 2026-10-08, status: utkast, kilder: ["Dataflyt 2.0 Excel", "D1"]}
prosessteg:
  - id: P5
    navn: Summering og avstemming
    fase: analyse            # samle | klargj | analyse | formidle (kan være flere)
    hva: Summerer alle kilder og avstemmer
    rolle: "?"               # rolle, ikke navn
    plattformer: [SAS]
    gjelder: alle            # alle | noen: [initialer] (for grupper)
    kilde: tolkning
objekter:
  - id: S1
    navn: SAS SUM
    objekt: system           # system | data
    systemtype: 1            # 0 neste nivå, 1 skreddersydd kode, 2 rammeverk med meny, 3 rammeverk
    plattform: SAS
    prosessteg: P5
    beskrivelse: SAS-applikasjon som summerer alle kilder
    status: finnes           # finnes | under arbeid | forslag | "?"
    kilde: "2.0"
    ref_2_0: "7,5"           # opprinnelig koordinat, for sporbarhet
  - id: D1
    navn: ALT SAMLET
    objekt: data
    datatype: macro          # meta | micro | macro | stat | out | qual
    rader: 2                 # 1 lite, 2 middels, 3 mye
    variabler: 3             # 1 svært få, 2 få, 3 mange, 4 svært mange
    stabil: "?"              # K | I | KL | S | U | ingen | "?"
    prosessteg: P5
koblinger:
  - {fra: S1, til: D1, type: dataflyt}   # dataflyt | metadata | avhengighet
eksterne:
  - {id: X_REA, navn: REA, retning: inn, type: statistikk}   # inn | ut
behov:                       # fra D3/B6, bare i TO BE
  - id: B1
    tilstand: I              # K | I | KL | S | U
    type: tjeneste           # tjeneste | prosess | variabler | avhengighet
    behov: Felles mottak og omkoding av kilder
    erstatter: [P1]
    verdi: Én testet rutine, mindre vedlikehold
    risiko: 13 SAS-rutiner må flyttes før 2029
    finnes_i_dapla: "?"      # ja | nei | "?" (avklares i B7)
    kilde: tolkning
```

Regler:
- ID er uavhengig av plassering. Koordinater er valgfrie hint (`hint: {x: 3, y: 5}`).
- Samme system kan forekomme flere steder i løpet. Det er bevisst i Dataflyt: vis hvert sted det skjer en transformasjon.
- **Datatype og stabil tilstand er to ulike egenskaper.** Datatypen sier hva dataene er (aggregeringsnivå). `stabil` sier hvor datasettet lagres i en vedtatt Dapla-tilstand (kildedata, inndata, klargjorte data, statistikk, utdata). Mange mikrodatasett underveis har `stabil: ingen`.
- `out` og utdata betyr åpent tilgjengelig. En leveranse som ikke er åpen (f.eks. til Eurostat) er `stat`.

## Oversettelse fra 2.0

Kolonner i 2.0-malen: `object, coord, next, X-line, Y-line, X-shp, mark, rel, step, data, name, desc, system, data_rows, data_cols, id, line, symbol`. Hvert objekt har to rader (`shape` og `line`). Et objekt med flere utganger er duplisert, én rad per `next`.

| 2.0 | 3.0 | Merknad |
|---|---|---|
| `coord` ("x,y", komma) | `ref_2_0`, ny `id` | Koordinaten var ID. Lag ny ID (S1…, D1…). Slå sammen duplikater med samme `coord`. |
| `next` | `koblinger` | `next == coord` betyr sluttnode. |
| `object` | `objekt` | |
| `data` | `datatype` | `qual` er definert, men nesten aldri brukt og har ikke symbol. |
| `system` | `systemtype` | 0 er «neste nivå», men ble aldri tegnet som egen fane. |
| `data_rows`, `data_cols` | `rader`, `variabler` | For systemer er `data_rows` alltid 3 og kan ignoreres. |
| `step` | fase på prosesssteget | `step` styrer ikke fasebåndene i Tableau. Plasseringen og `step` kan være uenige; spør. Mange flyter mangler `collect`. |
| `name`, `desc` | `navn`, `beskrivelse` | Navn som «SAS» og «TAB» går igjen. Gi ikke nytt navn; bruk ID for å skille. |
| – | plattform | Utled forsiktig fra navn (SAS, FAME, Excel, Oracle, ISEE, Dynarev). Merk som tolkning. |
| – | rolle, avhengigheter ut, stabil tilstand, behov | Finnes ikke i 2.0. Sett «?». |

Objekter i første kolonne som er andre statistikker (f.eks. REA, AR, UR, OFF i NR) er **avhengigheter**. Flytt dem til `eksterne` når det er tydelig, og spør ellers.

Minimal innlesing:
```python
import openpyxl
ws = openpyxl.load_workbook(sti).worksheets[0]
noder, kanter = {}, []
for r in ws.iter_rows(min_row=2, values_only=True):
    if r[6] != "shape":
        continue
    obj, coord, nxt, step, dtype, name, desc, sysx, rows, cols = r[0], r[1], r[2], r[8], r[9], r[10], r[11], r[12], r[13], r[14]
    gx, gy = [int(v) for v in coord.split(",")]
    noder[coord] = dict(obj=obj, gx=gx, gy=gy, step=step, dtype=dtype, name=name, desc=desc, sys=sysx, rows=rows or 1, cols=cols or 2)
    if nxt != coord:
        kanter.append((coord, nxt))
```

## Symbolspråket

Behold kodene og symbolene fra 2.0. Tegn dem som SVG-primitiver (sirkler og linjer), ikke som bilder.

**Datasymbol** (sirkel):
- Radius etter `rader`: 1 → 13 px, 2 → 17 px, 3 → 21 px (nivå 2). Ytre sirkel hvit med mørk strek `#274246`.
- Eiker etter `variabler`: 1 → 3, 2 → 8, 3 → 12, 4 → 20, fra indre sirkel (radius × 0,48) til ytre.
- Kjerne etter `datatype`: `meta` ingen kjerne (bare eiker), `micro` hvit, `macro` grågrønn `#9fb6b8`, `stat` mørk `#274246`, `out` mørk med fire «blader» (`#9fb6b8`) bak sirkelen på 45°, 135°, 225°, 315° (radius × 0,5, sentrum radius × 0,72 ut). Metaforen er at data springer ut og blomstrer.
- **Stabil tilstand** (nytt): grønn pille `#00824d` med hvit tekst K, I, KL, S eller U oppe til høyre på symbolet.

**Systemsymbol** (avrundet rektangel, ca. 24 × 34 px): 1 mørk `#3f6266`, 2 grå `#a9bdbe`, 3 hvit med mørk strek, 0 oransje `#f6b48f` med lupe. Betydning: 1 seksjonen utvikler og kontrollerer koden, 2 seksjonen kan tilpasse noe, 3 seksjonen kan ikke endre, 0 kan åpnes som detaljfigur.

**Nytt i 3.0**:
- Prosessteg (nivå 1): hvit boks med mørk kant, tittel, systemsymboler nederst til venstre, plattformbrikker nederst til høyre.
- Plattformbrikke: grå pille. I linsen «plattform og frist»: FAME mørk (`#274246`), SAS mellom (`#5e787a`), Oracle lys (`#a9bdbe`), andre hvite.
- Rolle: lilla pille (`#f1f1fe` / `#7d5fea`, tekst `#4b2fb0`). Uavklart rolle: stiplet «Rolle: ?».
- Koblinger: dataflyt heltrukken `#6f8a8c`, tykkelse etter `rader` hos kilden (1,3 / 2,0 / 2,8); metadata tynn grønn `#00824d`; avhengighet stiplet grå `#5e787a`.
- Status: stiplet grå = uavklart («?»), stiplet lilla = forslag eller målbilde (behov).
- Eksterne (andre statistikker, kilder utenfor): grå stiplet boks utenfor fasebåndene.

**Fasebånd** (svake bakgrunner, i tillegg til SSB-paletten): Samle inn `#eef7f0` (etikett `#3d7a55`), Klargjøre `#eaf4f8` (`#2f6f86`), Analysere `#f4f2fc` (`#5a4aa8`), Formidle `#fcf8e6` (`#7a6410`). Bare de fire GSBPM-fasene brukes. Faser settes på prosessteg, ikke på enkeltobjekter, og båndene kan overlappe der løpet gjør det.

Lilla betyr roller og forslag. Fasebåndet for Analysere er så lyst at det ikke forveksles, men hold øye med det.

## Oppsettregler

- Flyten går fra venstre (Samle inn) til høyre (Formidle). Rekkefølgen utledes av koblingene (lagdelt oppsett), ikke av koordinater.
- Eksterne inn står til venstre, utenfor båndene. «Brukes av» og leveranser ut står til høyre i Formidle.
- Linjer tegnes før symboler og blokker, så symbolene ligger oppå.
- Mange parallelle like objekter (f.eks. 13 mottak) samles i ett prosessteg og vises som et rutenett av små systemsymboler med antall i teksten.
- Datasett mellom prosessteg står på koblingen, med navn under. Hvis det er trangt: kort navn, 10–12 px, eller dropp navnet og forklar i panelet.
- Unngå at linjer krysser kilder og etiketter. Led avhengighetslinjer langs bunnen heller enn gjennom kildekolonnen.
- Diagramflaten er x 60–1400, y 180–986. Panel x 1440–1860. Tegnforklaring nederst til venstre (y 1046) må ikke kollidere med bunnlinjen; forkort etiketter ved behov.

## Figurtyper

| Figur | Viser | Kilde |
|---|---|---|
| Nivå 1 Oversikt | 5–10 prosessteg over fasebåndene, plattformer, roller (eller «?»), eksterne inn og ut, nøkkeldatasett mellom stegene | D1, B5, 2.0 |
| Nivå 2 Fokus | Ett prosessteg med alle data- og systemsymboler og navn | D2, 2.0 |
| Nivå 3 Detalj | Innsiden av ett system (typisk systemtype 0). Ukjent innhold tegnes stiplet grått med «?» | Eget møte |
| Full 2.0-flyt | Alle objekter rett fra koordinatene, med markører på det som er skjult | 2.0 |
| Linse: plattform og frist | Nivå 1 med plattformbrikker farget etter frist | modell + frister |
| Linse: avhengigheter | Nivå 1 med eksterne inn og ut framhevet | modell |
| Linse: stabile datatilstander | Nivå 1 med K, I, KL, S, U der de ligger, eller «?» | modell |
| Linse: behov og verdi | Fokusvariant med nummererte lilla markører på stedene med mulig gevinst | D3, tolkning |
| Målbildeskjelett (TO BE) | Rutenett som B6: kolonner K, I, KL, S, U under fasene, rader tjenester, prosesser, variabler og tilstander, avhengigheter. Celler med behov (stiplet lilla) eller «?» | D3, B6 |
| Fra dagens løp til målbilde | AS IS øverst, TO BE-skjelett nederst, forskjellen som behovsliste | B5 + B6 |
| Tomme maler | D1, D2, D3 som arbeidsflater | – |

Fokusvarianter lages på samme grunnfigur med nedtoning (fyll `#f5f7f7`, strek `#dfe5e5`, tekst `#b9c5c6`) og nummererte markører som svarer til panelet. Bruk lilla markører når de peker på verdi eller forslag.

**TO BE-regler**: målbildet viser behov, ikke løsninger. Ingen systemsymboler før B7 har avklart hva som finnes eller må utvikles. Merk figuren «Scenario · FORSLAG». Datatilstandene er faste ankerpunkter.

## Malverket

**D1 Prosessteg og roller** (nivå 1, bygger på B5). Felt øverst: én statistikk / gruppe, statistikk eller gruppe, kontaktperson, dato, versjon. Kolonner: #, Prosessteg, Fase (S K A F), Hva skjer, Hvem (rolle), Plattform og systemer, Data inn → ut, Avhengigheter, Alle / Noen. En grå eksempelrad (E). Brikker for plattformer (FAME, SAS, Oracle ODI, Oracle Forms, ISEE, Dynarev, KOSTRA-innrapportering, Statistikkbanken, Excel, blanke) og forslag til roller (saksbehandler, statistikkansvarlig, metode, IT/utvikler, formidling, ekstern leverandør). Regler: ofte 5–10 steg; ett steg endrer dataene og kan beskrives med én setning; skriv rolle, ikke navn; plattform først, programnavn på nivå 2.

**D2 Data og systemer** (nivå 2, erstatter 2.0-Excel). Ett prosessteg om gangen. Tabell Objekter: ID, Navn, Objekt, Type, Rader, Variabler, Plattform, Tilstand (K I KL S U), Beskrivelse, Status. Tabell Koblinger: Fra ID, Til ID, Type (dataflyt, metadata, avhengighet), Merknad. Ingen koordinater.

**D3 Behov og verdi** (bygger på B6). Kolonner: #, Datatilstand (K I KL S U), Behov, Type (T tjeneste, P prosess, V variabler og tilstander, A avhengighet), Erstatter i dag, Verdi, Risiko ved å la være, Finnes i Dapla? (Ja, Nei, ?). «Finnes i Dapla?» avklares i B7. Behovene registreres i Jira.

**D4 Løpet**: innledende møte (omfang, B4) → før workshop (kontaktperson fyller D1/D2; KI lager utkast fra 2.0-flyt og faktaark og lister spørsmål) → **port 1: utkast klart** → workshop (B5/B6 med utkastet, avklare «?») → etterarbeid (KI gjør notater om til modell, tegner nivå 1 og 2, lager kvalitetssikringsliste; prosjektgruppen kontrollerer; kontaktperson bekrefter) → **port 2: bekreftet av fag** → resultat (tegninger, behovsliste til Jira, innspill til B7, linser samlet på tvers).

## Kontekst: kartleggingen av komplekse statistikker

- Frister: FAME ca. 1.11.2028, SAS 2029 (internt mål), Oracle 2030. Sjekk mot nyeste kilde hvis de skal stå på en figur.
- Malene B4–B13 i kartleggingsserien: B5 dagens produksjonsløp (rader: hvem gjør hva, prosessteg, systemer, data inn og ut, avhengigheter), B6 fremtidig løsning og behov (kolonner etter datatilstand), B7 funksjonalitet (avklarer om noe finnes eller må utvikles). Alle har felt for én statistikk eller gruppe og «Alle / Noen».
- Dataflyt dekker godt rader for systemer og data i B5, delvis prosessteg, nesten ikke roller. B5/B6 legger til roller, prosessteg, avhengigheter, datatilstander og behov.

## Gjennomgått eksempel: NR IKR

2.0-filen har 70 elementer (28 systemer, 42 datasett) og 76 koblinger. Inndeling i sju prosessteg (tolkning, godkjent som utkast av Thomas):

1. Mottak og omkoding (klargj): 13 SAS EXCEL-mottak fra 11 kilder (VOF, NO1 NO2, Saldoskjema, Skatt selskap, BRREG, Skatt person, Aksje, Forsikr./pensj., VPS, NO-VP, OLJE) og 6 andre regnskap (REA, AR, UR, OFF, NAV via UR, TOMT). Plattform SAS, Excel.
2. Finansielle sektorer (klargj): FINANS med omkodingskatalogen OMKOD (meta). Ut: REA.
3. Ikke-finansielle sektorer (klargj): SAS BEREGN. Ut: IKKE-FIN.
4. Kapital, aksjer, AR og OFF (klargj): SAS IBERKAP, SAS-balansering, AR2IKR, OFF-app. Ut: IBERKAP, AKSJE.
5. Summering og avstemming (analyse): SAS SUM → ALT SAMLET → SAS AVSTEM → INPUT EXCEL. Inn også RG (kilde ukjent).
6. Inspeksjon og manuell editering (analyse): EXCEL EDIT (systemtype 0) → TAB.
7. Omkoding til NO og ESA (analyse): 2 × SAS, 2 × FAME. Ut: SB (out) → Statistikkbanken, EUROSTAT (stat) → Eurostat.

Mulig verdi (tolkning, må bekreftes av fagmiljøet): 13 like mottak → én felles rutine; manuell Excel-editering → sporbar editering med logg; parallelle NO- og ESA-løp → samordnes; seks regnskap styrer når IKR kan flyttes. Linsen for plattform viser at slutten av løpet (FAME) har tidligste frist, så rekkefølgen snus.

## Leveranse

- Modellfil `<kortnavn>_dataflyt.yaml`.
- SVG per figur i 1920 × 1080 med beskrivende filnavn, PNG for egen kontroll, zip når et sett er komplett.
- Kvalitetssikringsliste (`kvalitetssikringsliste.md`) fordelt på hvem som må bekrefte.
- Følgetekst: hva figurene viser, valg som er gjort, hva som er tolkning, og ett neste spørsmål.

## Kjente begrensninger i 0.1

- Koden for innlesing og tegning ligger ikke i skillen. Skriv den etter reglene over, og gjenbruk den i økten. Senere versjoner flytter koden til et repo.
- Skillen kommer ikke til SharePoint eller Tableau Server. Be om at filene lastes opp.
- Plattform utledes av navn i 2.0 og er derfor alltid tolkning til noen bekrefter.
