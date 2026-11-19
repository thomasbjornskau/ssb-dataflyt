# Dataflyt i SSB

Dokumentasjon av Dataflyt 3.0: en metode for å kartlegge og tegne dataflyten i statistikkproduksjonen i Statistisk sentralbyrå. Veiledning i sju kapitler, symbolspråket, utfyllbare maler, konseptfigurer, Excel- og Tableau-malene fra Dataflyt 2.0 og skillene for KI-støtte.

Nettstedet: https://thomasbjornskau.github.io/ssb-dataflyt/

> **Utkast.** Dataflyt 3.0 er under utprøving. Eksemplet fra NR IKR inneholder tolkninger som ikke er bekreftet av fagmiljøet.

## Innhold

| Mappe eller fil | Hva |
|---|---|
| `docs/index.md`, `docs/1-…md` – `docs/7-…md` | Forsiden og de sju kapitlene i veiledningen |
| `docs/maler/` | Oversikten og de tre utfyllbare malene D1–D3 |
| `docs/figurer/` | Konseptfigurene som SVG (1920 × 1080), navngitt etter figurnummer. `KB5` og `KB6` er malene B5 og B6 fra kartleggingen |
| `docs/symboler/` | Alle 121 symboler som SVG |
| `docs/bilder/` | Skjermbilder og illustrasjoner fra Dataflyt 1.0 og 2.0 |
| `docs/filer/maler/` | Excel-malen, Tableau-malen, eksemplet fra NR IKR og A3-rutenettene |
| `docs/filer/tableau-symboler/` | Symbolene til Tableau som PNG (også samlet i `tableau-symboler.zip`) |
| `docs/filer/skills/` | Skillene ssb-dataflyt og ssb-konseptfigurer, som SKILL.md og zip |
| `docs/assets/` | Stil (`ssb.css`) og skriptet som lagrer og eksporterer svarene i malene (`ark.js`) |
| `verktoy/bygg_maler.py` | Bygger malsidene `docs/maler/d1.md`–`d3.md` |
| `mkdocs.yml` | Oppsett for nettstedet og menyen |
| `.github/workflows/pages.yml` | Bygger nettstedet og publiserer det på GitHub Pages ved hver push til `main` |

## Publisere

1. Lag et nytt repo på GitHub og last opp innholdet i denne mappen.
2. Gå til **Settings → Pages** og velg **GitHub Actions** som kilde.
3. Push til `main`. Nettstedet ligger på `https://<bruker>.github.io/<repo>/` etter et par minutter.
4. Kontroller adressene i `site_url` og `repo_url` i `mkdocs.yml`.

## Se nettstedet lokalt

```
pip install -r requirements.txt
mkdocs serve
```

Åpne http://127.0.0.1:8000.

## Redigere

- **Tekst:** rediger markdown-filene i `docs/`. Overskrifter med `#` blir innholdslisten.
- **Figur:** bytt SVG-filen i `docs/figurer/` og behold filnavnet. Bildeteksten står i markdown-filen.
- **Maler:** endre spesifikasjonen i `verktoy/bygg_maler.py` og kjør `python verktoy/bygg_maler.py`. Hvert felt har en nøkkel (`data-k`). Ikke endre nøklene etter at malene er tatt i bruk, ellers finner ikke nettleseren igjen svarene brukerne har skrevet.
- **Teksten til skillen:** oppdraget for hver mal står i `bygg_maler.py` (`oppdrag`). Innledningen står i `skillTekst` i `docs/assets/ark.js`.

## Malene og personvern

Svarene lagres i nettleserens `localStorage` på brukerens egen maskin. Ingenting sendes til GitHub eller noe annet sted. Brukerne kan laste ned svarene som markdown, ta sikkerhetskopi som JSON og hente den inn igjen på en annen maskin. Teksten til skillen limes inn i Claude av brukeren selv. Malene skal ikke brukes til personopplysninger, upubliserte tall eller tilgangsinformasjon.
