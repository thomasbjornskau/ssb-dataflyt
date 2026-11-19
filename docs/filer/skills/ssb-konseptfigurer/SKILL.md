---
name: "ssb-konseptfigurer"
description: "Bruk når Thomas skal lage, revidere eller planlegge konseptuelle figurer eller figurserier for SSB (arkitektur, dataflyt, prosess, ansvar, kapabilitet, strategi) som SVG til presentasjoner."
---

# SSB konseptfigurer

Metode og formfaktor for konseptfigurer i SSB, utviklet i arbeidet med Dapla-serien og figursamlingen for Bedre faktaformidling. Figurene er SVG i 16:9 (1920 × 1080) som kan settes rett inn i PowerPoint.

Kodebiblioteket ligger i repoet `ssb-konseptfigurer` (komponenter i `konseptfigurer/`, serier i `figurer/<serie>/`, mal i `figurer/_mal/`, register i `register/`, standard i `docs/standard.md`). Hvis repoet er tilgjengelig i økten: bruk komponentene derfra i stedet for å skrive nye. Hvis ikke: følg reglene under og bygg med samme primitiver (Fig-klasse med fokus/nedtoning, ramme, panel, tegnforklaring).

## Kilder for visuell profil

- **SSBs profilhåndbok:** https://profil.ssb.no/ (farger, typografi, ikoner, illustrasjoner). Den er overordnet kilde.
- **SSBs designsystem:** https://design.ssb.no/ og npm-pakken `@statisticsnorway/ssb-component-library` (`src/style/_variables.scss`). Brukes for detaljer profilen ikke dekker: hjørner, rammer, aksentkanter.
- Der de to er uenige, følger figurene profilhåndboken. Kjente avvik: lilla (profil `#7E5EE8`, bibliotek `#9272fc`) og H2 (profil Roboto, bibliotek Roboto Condensed).
- **Farger og fonter fra kildedokumenter tas ikke inn uten videre.** Et PPT-tema, et notat eller en skisse kan ha egne farger. Oversett dem til profilfargene og fargebetydningene under, og si fra om det som ikke lar seg oversette.

## Arbeidsform

- Språk: norsk bokmål, nøkternt og presist. Direkte vurderinger, ikke generisk ros.
- Still ett avklaringsspørsmål om gangen før du bygger, og bare når svaret endrer hva du lager.
- Lever tidlig og iterativt: send hver figur når den er klar, ikke alt til slutt.
- Si tydelig fra om svakheter, antakelser og det som ikke kan bekreftes.

## Arbeidsflyt

1. **Kritisk gjennomgang** av eksisterende figurer: hva de viser, nivå, begreper, overlapp og avvik mellom figurer, hva som er uklart eller blander nivåer. Lag en tabell over navnedrift på tvers.
2. **Matrise: målgruppe × perspektiv.** Merk celler som trengs, nyttig eller unødvendig. Tomme celler er bevisste. Tredje dimensjoner (nå/mål, oversikt/fokus) blir regler, ikke flere akser.
3. **Storyboard** før tegning, gjerne som dokument: per figur tittel, primær og sekundær målgruppe, spørsmål, hovedbudskap, diagramtype, elementer, uavklart, diskusjonsspørsmål og fokusvarianter. Anbefal 3–5 figurer å starte med, og begrunn rekkefølgen.
4. **Faktagrunnlag.** Sjekk mot primærkilder (manualer, ADR-er, notater) før tegning. Noter ADR-status (foreslått, vedtatt, akseptert). Respekter robots.txt og blokkerte nettsteder, og be heller brukeren legge ved dokumenter.
5. **Tegn oversikten, se på den, rett den.** Render til PNG og se på bildet før levering: overlappende tekst, piler gjennom tekst, tekst utenfor bokser. Kjør også profilsjekken (under).
6. **Fokusvarianter** på samme grunnfigur, med nedtoning og nummererte markører som svarer til panelet.
7. **Introduksjonsfoil** med matrisen, der figurene er plassert og status er vist.
8. **Kvalitetssikringsliste**: samle alt som er tolkning eller ubekreftet i en liste til faglige eiere.

## Innholdsprinsipper

- Én figur, ett spørsmål, én primær målgruppe.
- Status skal synes og gjettes aldri: finnes i dag, under arbeid, forslag, uavklart. Ikke vurdert vises som «?».
- Bruk etablerte navn. Innfør aldri nye navn på noe som finnes. Hold en begrepsliste per serie.
- Skill typer ting visuelt: flate/tjeneste, data/innhold, rolle/ansvar, utenfor/uavklart.
- Hver piltype har én betydning og står i tegnforklaringen (f.eks. dataflyt, styrer/konfigurerer, API-kall, avhengighet, deling, tidsavgrenset tilgang).
- Skill kontrollflyt fra dataflyt. Endringsflyt (kode til drift) er en egen figur.
- Ikke tegn én sømløs reise hvis det skjuler faglige, juridiske eller organisatoriske skiller. Tegn skillet.
- Normative figurer får etiketten «Diskusjon» eller «Scenario». Scenarioer skal vise styrke og risiko på begge sider.
- Forslag og målbilder merkes FORSLAG. Tekniske interne detaljer merkes INTERN.
- Figurer som skal brukes i workshop (plassering, prioritering) plasserer ikke selv; de gir arbeidsflaten.

## Formfaktor (1920 × 1080)

- Tittel x 60, y 92, 46 px, Roboto Condensed Bold. Undertittel y 136, 24 px, Open Sans, grå. Linje y 160, 1 px mørk 2.
- Etikett øverst til høyre (Oversikt, Fokus n av m, Diskusjon, Scenario, Introduksjon, + INTERN/FORSLAG).
- Diagramflate x 60–1400, y 180–986.
- Forklaringspanel x 1440–1860: fyll mørk 1, 5 px grønn 4 aksentkant øverst, 3–5 nummererte punkter (overskrift 20 px Roboto Bold, tekst 17 px Open Sans).
- Tegnforklaring nederst til venstre (y 1046), bunnlinje nederst til høyre: dato · status · kilde.
- Foredragsfoiler kan bruke større tekst, men samme fonter, farger og formspråk. Formfaktoren over gjelder figurer.

## Typografi (profilhåndboken)

- **Hovedtittel:** Roboto Condensed Bold.
- **Mellomtitler** (paneloverskrifter, sonenavn, boksnavn som fungerer som overskrift): Roboto Bold.
- **Brødtekst, etiketter, tegnforklaring, bunnlinje:** Open Sans Regular; Open Sans Semibold/Bold for vekt i brikker.
- Erstatningsfont er Arial. Skriv `font-family="Roboto Condensed, Arial Narrow, Arial, sans-serif"`, `"Roboto, Arial, sans-serif"` og `"Open Sans, Segoe UI, Arial, sans-serif"`.
- Minste tekst 14 px (profilens minimum for digitale flater). 12 px bare i små brikker og markørtall, og helst ikke.
- Ingen andre fonter i figurer. Unntak bare etter avtale (f.eks. begrepsfilm).

## Palett og betydning

Profilfarger (hex fra profilhåndboken):

- Mørk 5 `#274247` (tekst, rammer, piler som styrer). Mørk 1 `#f0f8f9`, mørk 2 `#c3dcdc`: plattform, tjenester, flater, panel.
- Grønn 4 `#00824d`, grønn 2 `#b6e8b8`, grønn 1 `#ecfeed`: data, statistikk, metadata.
- Lilla 3 `#7e5ee8`, lilla 2 `#d2ceff`, lilla 1 `#f2f0ff`: brukere, roller, team, ansvar, eierskap.
- Hvit `#ffffff`.

Avledede farger (ikke i profilen, brukes bare til disse formålene):

- Grå tekst `#5e787a`, linje `#cdd3d4`.
- Lilla tekst `#4b2fb0` (lilla 3 har for lav kontrast som tekst).
- Grå `#b9c5c6` / `#f3f5f5`: uavklart, utenfor scope, utenfor SSB.
- Nedtoning i fokus: fyll `#f5f7f7`, strek `#dfe5e5`, tekst `#b9c5c6`.
- Varselfarge: SSB rød 3 `#dc3400`, bare for feil eller risiko, aldri som pynt.

Regler:

- Stiplet grå = uavklart/ubekreftet. Stiplet lilla = forslag/målbilde.
- Grønn 3 `#1a9d49` er diagramfarge på ssb.no, ikke konseptfigurfarge. Bland ikke grønn 3 og grønn 4 i samme figur.
- Fasefarger (GSBPM) hentes fra `ssb-dataflyt` når faser vises, og brukes bare som svake bånd.
- Farge betyr alltid noe. Ingen fargede flater uten betydning i tegnforklaringen eller fargelogikken over.

## Formspråk

- **Flater** er rektangulære. Bokser får 2 px hjørneradius (som knapper i designsystemet), aldri store avrundinger. Brikker og tagger kan være piller (full radius). Markører og noder er sirkler.
- **Rammer** er 1 px. 2 px bare for fokus eller valgt element. Ingen doble rammer.
- **Aksentkant:** 5 px grønn 4 øverst eller til venstre markerer panel, forklaringsboks eller faktaboks (som Card og FactBox i designsystemet). Lilla aksentkant for rolle- og ansvarsbokser. Bruk sparsomt.
- **Skillelinjer:** 1 px, mørk 2 (rolig) eller mørk 5 (sterk).
- **Ingen gradienter, skygger, 3D eller dekor.** Profilens vinkelelement (30° og 105°) brukes ikke i konseptfigurer.
- **Piler:** 2 px strek, pilspiss som fylt trekant i strekfargen, samme spiss overalt i serien.
- **Ikoner:**
  - Små ikoner (under ca. 57 px): Feather-stil, ensfargede strekikoner i mørk 5, grønn 4 eller grønn 2. Ikke bland stiler.
  - Store ikoner: SSBs egne ikoner. Bruk skillen `ssb-ikoner` for å finne eller lage dem.
  - Egentegnede ikoner merkes i kvalitetssikringslisten og bør vises til profil (profil@ssb.no) før bruk utenfor SSB.
- **Illustrasjoner** (sjelden i konseptfigurer): enkle, lette og geometriske, 2–4 farger inkludert hvit, bakgrunn hvit, mørk 1 eller grønn 1. Skal godkjennes av profileier.

## Profilsjekk før levering

- Bare farger fra paletten over? (Søk etter hex-koder i SVG-en.)
- Tittel i Roboto Condensed, mellomtitler i Roboto, resten Open Sans?
- Ingen tekst under 14 px utenom brikker og markører?
- Hjørneradius 2 px på bokser, ingen skygger eller gradienter?
- Ikoner i én stil, fra Feather eller `ssb-ikoner`?
- Er farger fra kildedokumentet oversatt, ikke kopiert?

## Diagramtyper som har fungert

Lagkart med 3 × 3 kapabiliteter; soner og grenser (C4-inspirert) for struktur; svømmebaner × datatilstander for prosess, med egen kontrollrad; ansvarskjede person → gruppe → mekanisme → ressurs; realiseringsmatrise kapabilitet × sone med linser (modenhet, hull, overlapp); brukerblueprint (hva skjer, hva gjør du, verktøy, dokumentasjon); sporbarhetskjede; trapp med porter; filtertrakt; innflytelsessirkler; beslutningskart i trinn; kontrastfigur; 2 × 2 som arbeidsflate. Fokus kan være utsnitt, tema, tid (i dag/forslag) eller linser.

## SVG-regler

Bare `rect`, `line`, `polyline`, `polygon`, `circle`, `ellipse`, `path`, `text`. Ingen CSS-klasser, filtre, markører eller `foreignObject`. Pilspisser som polygoner. Tekst brytes manuelt. Farger og fonter som attributter.

## Leveranse

SVG per figur med beskrivende filnavn, PNG-forhåndsvisning for egen kontroll, zip per serie når settet er komplett. Følgetekst: hva figuren viser, hvilke valg som er gjort, hva som er tolkning, og ett neste spørsmål.