---
title: Malene
---

# Malene

Tre maler som kontaktpersonen for en statistikk fyller ut før og etter workshopen. De kan fylles ut her på nettsiden, og svarene blir værende i nettleseren til du sletter dem. Når du er ferdig, lager du en tekst som du limer inn i en samtale med Claude. Skillen [ssb-dataflyt](../7-verktoy.md#ki-stotte) gjør teksten om til en modell, tegninger og en liste over det som må kvalitetssikres.

| Mal | Spørsmålet | Nivå | Status |
|---|---|---|---|
| [D1 Prosessteg og roller](d1.md) | Hva skjer, hvem gjør det, på hvilken plattform, og hva henger sammen? | Nivå 1, oversikt | <span data-status-ark="D1">ikke påbegynt</span> |
| [D2 Data og systemer](d2.md) | Hvilke datasett og systemer inngår i hvert steg, og hvordan henger de sammen? | Nivå 2, fokus | <span data-status-ark="D2">ikke påbegynt</span> |
| [D3 Behov og verdi](d3.md) | Hva må på plass i Dapla, hva erstatter det, og hva blir bedre? | Målbilde | <span data-status-ark="D3">ikke påbegynt</span> |

Malene bygger på malene B5 og B6 fra kartleggingen av komplekse statistikker, og på Excel-malen fra Dataflyt 2.0. [Kapittel 5](../5-slik-kartlegger-du.md) forklarer hvor i løpet de brukes.

## Fra mal til tegning

1. **Fyll ut D1** før workshopen, så langt du kommer. «?» er et gyldig svar.
2. **Fyll ut D2** for de prosesstegene som skal tegnes i detalj. Har statistikken en tegning fra Dataflyt 2.0, kan den brukes i stedet for eller i tillegg til D2.
3. **Fyll ut D3** etter workshopen, når dagens løp er gått gjennom.
4. **Lag tekst til skillen** her på oversikten. Teksten samler alle malene du har fylt ut, og ber skillen om modell, tegninger og kvalitetssikringsliste.
5. **Lim teksten inn i Claude** med skillen ssb-dataflyt slått på. Legg gjerne ved Excel-filen fra 2.0.
6. **Kontroller resultatet.** Det KI lager, er et utkast. Fagmiljøet bekrefter før noe går videre.

## Svarene dine

<div class="ark-oversikt" markdown="0">
<div class="ark-verktoy">
<button type="button" class="md-button md-button--primary" data-gjor="skill">Lag samlet tekst til skillen</button>
<button type="button" class="md-button" data-gjor="alle">Last ned alle svar (.md)</button>
<button type="button" class="md-button" data-gjor="kopi">Ta sikkerhetskopi (.json)</button>
<button type="button" class="md-button" data-gjor="hent">Hent fra sikkerhetskopi</button>
<button type="button" class="md-button ark-tom" data-gjor="slett">Slett alle svar</button>
<input type="file" accept="application/json,.json" hidden>
<span class="ark-status" aria-live="polite"></span>
</div>
<div class="ark-skill" hidden><p class="ark-lbl">Tekst til skillen ssb-dataflyt. Kopier den inn i en samtale med Claude.</p><textarea readonly rows="10" aria-label="Tekst til skillen"></textarea><button type="button" class="md-button" data-gjor="kopierskill">Kopier teksten</button></div>
</div>

Svarene lagres i nettleserens lokale lager på din egen maskin. Ingenting sendes til GitHub eller noe annet sted. Vil du fortsette på en annen maskin, tar du en sikkerhetskopi og henter den inn der.

!!! warning "Skriv ikke inn opplysninger som ikke kan deles"
    Malene handler om systemer, datasett og prosesser, ikke om personer eller tall. Skriv ikke inn personopplysninger, upubliserte tall eller passord og tilgangsinformasjon. Teksten du lager, skal limes inn i et KI-verktøy: følg SSBs retningslinjer for bruk av KI.
