/* Malene D1–D3: lagring i nettleseren, eksport, utskrift og tekst til skillen ssb-dataflyt.
   Alt ligger i localStorage under én nøkkel. Ingenting sendes noe sted. */
(function () {
  "use strict";
  var LS = "ssb-dataflyt-maler-v1";
  var REKKEFOLGE = ["D1", "D2", "D3"];
  var FELLES = [
    ["felles.statistikk", "Statistikk"], ["felles.kortnavn", "Kortnavn"], ["felles.seksjon", "Seksjon"],
    ["felles.kontakt", "Kontaktperson"], ["felles.gjelder", "Gjelder"], ["felles.gruppe", "Statistikker i gruppen"],
    ["felles.dato", "Dato"]
  ];

  function les() {
    try { return JSON.parse(window.localStorage.getItem(LS)) || {}; } catch (e) { return {}; }
  }
  function skriv(d) {
    try { window.localStorage.setItem(LS, JSON.stringify(d)); return true; } catch (e) { return false; }
  }
  function alle(rot, sel) { return Array.prototype.slice.call(rot.querySelectorAll(sel)); }
  function rens(s) { return String(s == null ? "" : s).replace(/\|/g, "/").replace(/\s*\n\s*/g, " ").trim(); }

  function verdi(el) {
    if (el.type === "checkbox") return el.checked;
    return el.value;
  }
  function visning(el) {
    if (el.tagName === "SELECT") {
      var o = el.options[el.selectedIndex];
      return o && o.value ? o.textContent : "";
    }
    return el.value;
  }

  function fyll(ark, d) {
    alle(ark, "[data-k]").forEach(function (el) {
      if (!/^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName)) return;
      var v = d[el.dataset.k];
      if (v === undefined) return;
      if (el.type === "checkbox") el.checked = !!v; else el.value = v;
    });
    alle(ark, ".ark-hent").forEach(function (h) {
      var p = h.querySelector("p");
      var v = d[h.dataset.fra];
      p.textContent = v ? v : p.dataset.tom;
      p.classList.toggle("ark-tomt", !v);
    });
  }

  /* Tabellene blir markdown-tabeller med bare utfylte rader */
  function tabellMd(tab) {
    var hode = alle(tab, "thead th").map(function (th) { return th.textContent; });
    var rader = [];
    alle(tab, "tbody tr").forEach(function (tr) {
      var celler = alle(tr, "td").map(function (td, i) {
        var el = td.querySelector("[data-k]");
        return el ? rens(visning(el)) : rens(td.textContent);
      });
      var utfylt = celler.slice(1).some(function (c) { return c; });
      if (utfylt) rader.push(celler);
    });
    if (!rader.length) return "–";
    var ut = ["| " + hode.join(" | ") + " |", "|" + hode.map(function () { return "---"; }).join("|") + "|"];
    rader.forEach(function (r) { ut.push("| " + r.map(function (c) { return c || " "; }).join(" | ") + " |"); });
    return ut.join("\n");
  }

  function fellesMd(d) {
    var linjer = [];
    FELLES.forEach(function (f) { if (d[f[0]]) linjer.push("- **" + f[1] + ":** " + d[f[0]]); });
    return linjer.join("\n");
  }

  function tilMarkdown(ark, d) {
    var linjer = ["# Mal " + ark.dataset.ark + ": " + ark.dataset.tittel, ""];
    var f = fellesMd(d);
    if (f) linjer.push(f, "");
    alle(ark, ".ark-del").forEach(function (del) {
      if (del.classList.contains("ark-felles-del")) return;
      linjer.push("## " + del.querySelector("h3").textContent, "");
      alle(del, "table.ark-t, .ark-felt > [data-k], .ark-hent").forEach(function (el) {
        if (el.tagName === "TABLE") { linjer.push(tabellMd(el), ""); return; }
        if (el.classList.contains("ark-hent")) {
          linjer.push("- **" + el.querySelector(".ark-lbl").textContent + ":** " + (d[el.dataset.fra] || "–"));
          return;
        }
        var t = rens(visning(el));
        linjer.push("- **" + el.dataset.l + ":** " + (t || "–"));
      });
      linjer.push("");
    });
    return linjer.join("\n").replace(/\n{3,}/g, "\n\n").trim() + "\n";
  }

  function skillTekst(arkIder, d) {
    var navn = d["felles.statistikk"] || "statistikken";
    var oppdrag = arkIder.map(function (id) { return d["_oppdrag." + id]; }).filter(Boolean);
    var deler = arkIder.map(function (id) { return d["_md." + id]; }).filter(Boolean);
    var ut = [
      "Bruk skillen ssb-dataflyt, arbeidsmåte B (kartlegge med malene).",
      "",
      "Under står utfylte maler for " + navn + ". «?» betyr at noe ikke er vurdert. Det skal ikke gjettes.",
      "",
      "Oppgave:"
    ];
    oppdrag.forEach(function (o) { ut.push("- " + o); });
    ut.push("- Lever modellfilen (YAML) og en kvalitetssikringsliste fordelt på hvem som må bekrefte.");
    ut.push("- Still oppfølgingsspørsmål ett om gangen før du tegner noe som bygger på antakelser.");
    ut.push("", "---", "");
    return ut.join("\n") + deler.join("\n---\n\n");
  }

  function lagre(ark, status) {
    var d = les();
    alle(ark, "[data-k]").forEach(function (el) {
      if (!/^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName)) return;
      d[el.dataset.k] = verdi(el);
    });
    /* Lister som andre maler kan hente */
    alle(ark, "[data-liste]").forEach(function (tab) {
      var navn = [];
      alle(tab, "tbody tr").forEach(function (tr, i) {
        var el = tr.querySelector("[data-k]");
        if (el && el.value.trim()) navn.push((i + 1) + " " + el.value.trim());
      });
      d[tab.dataset.liste] = navn.join(" · ");
    });
    d["_md." + ark.dataset.ark] = tilMarkdown(ark, d);
    d["_oppdrag." + ark.dataset.ark] = ark.dataset.oppdrag;
    d["_t." + ark.dataset.ark] = new Date().toISOString();
    var ok = skriv(d);
    if (status) {
      var t = new Date();
      status.textContent = ok
        ? "Lagret i denne nettleseren kl. " + String(t.getHours()).padStart(2, "0") + ":" + String(t.getMinutes()).padStart(2, "0")
        : "Kunne ikke lagre i nettleseren. Last ned svarene før du lukker siden.";
    }
    return d;
  }

  function lastNed(navn, tekst, type) {
    var blob = new Blob([tekst], { type: type || "text/markdown;charset=utf-8" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = navn;
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }

  function kopier(tekst, status) {
    function reserve() {
      var ta = document.createElement("textarea");
      ta.value = tekst; document.body.appendChild(ta); ta.select();
      try { document.execCommand("copy"); status.textContent = "Kopiert."; } catch (e) { status.textContent = "Kunne ikke kopiere. Merk teksten og kopier selv."; }
      ta.remove();
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(tekst).then(function () { status.textContent = "Kopiert."; }, reserve);
    } else reserve();
  }

  function visSkill(boks, tekst, status) {
    var ta = boks.querySelector("textarea");
    ta.value = tekst;
    boks.hidden = false;
    ta.style.height = "auto"; ta.style.height = Math.min(ta.scrollHeight + 4, 520) + "px";
    boks.scrollIntoView({ behavior: "smooth", block: "nearest" });
    if (status) status.textContent = "Teksten til skillen er laget. Kopier den inn i Claude.";
  }

  function startArk(ark) {
    var status = ark.querySelector(".ark-status");
    var skillboks = ark.querySelector(".ark-skill");
    fyll(ark, les());
    var tid;
    ark.addEventListener("input", function () { clearTimeout(tid); tid = setTimeout(function () { lagre(ark, status); }, 300); });
    ark.addEventListener("change", function () { lagre(ark, status); });
    alle(ark, "textarea:not([readonly])").forEach(function (t) {
      var vokse = function () { t.style.height = "auto"; t.style.height = (t.scrollHeight + 2) + "px"; };
      t.addEventListener("input", vokse); vokse();
    });
    ark.addEventListener("click", function (ev) {
      var b = ev.target.closest("button[data-gjor]"); if (!b) return;
      var d = lagre(ark, status);
      var md = d["_md." + ark.dataset.ark];
      var g = b.dataset.gjor;
      if (g === "kopier") kopier(md, status);
      if (g === "lastned") lastNed("dataflyt-mal-" + ark.dataset.ark + ".md", md);
      if (g === "skill") visSkill(skillboks, skillTekst([ark.dataset.ark], d), status);
      if (g === "kopierskill") kopier(skillboks.querySelector("textarea").value, status);
      if (g === "skrivut") window.print();
      if (g === "tom" && window.confirm("Tømme alle feltene på mal " + ark.dataset.ark + "? Feltene om statistikken beholdes.")) {
        var dd = les();
        Object.keys(dd).forEach(function (k) {
          if (k.indexOf(ark.dataset.ark + ".") === 0 || /^_(md|t|oppdrag|liste)\./.test(k) && k.slice(-2) === ark.dataset.ark) delete dd[k];
        });
        skriv(dd);
        alle(ark, "[data-k]").forEach(function (el) {
          if (el.dataset.k.indexOf("felles.") === 0) return;
          if (el.type === "checkbox") el.checked = false; else if (/^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName)) el.value = "";
        });
        skillboks.hidden = true;
        status.textContent = "Malen er tømt.";
      }
    });
  }

  function startOversikt(rot) {
    var d = les();
    alle(document, "[data-status-ark]").forEach(function (el) {
      var t = d["_t." + el.dataset.statusArk];
      el.textContent = t ? "påbegynt " + new Date(t).toLocaleDateString("nb-NO") : "ikke påbegynt";
      el.classList.toggle("ark-pabegynt", !!t);
    });
    var status = rot.querySelector(".ark-status");
    var skillboks = rot.querySelector(".ark-skill");
    if (rot.dataset.koblet) return;
    rot.dataset.koblet = "1";
    rot.addEventListener("click", function (ev) {
      var b = ev.target.closest("button[data-gjor]"); if (!b) return;
      var dd = les();
      var fylt = REKKEFOLGE.filter(function (k) { return dd["_md." + k]; });
      var g = b.dataset.gjor;
      if ((g === "alle" || g === "skill") && !fylt.length) { status.textContent = "Du har ikke fylt ut noen av malene ennå."; return; }
      if (g === "alle") lastNed("dataflyt-maler-" + (dd["felles.kortnavn"] || "alle").replace(/[^\wæøåÆØÅ-]+/g, "_") + ".md",
        fylt.map(function (k) { return dd["_md." + k]; }).join("\n---\n\n"));
      if (g === "skill") visSkill(skillboks, skillTekst(fylt, dd), status);
      if (g === "kopierskill") kopier(skillboks.querySelector("textarea").value, status);
      if (g === "kopi") lastNed("dataflyt-maler-sikkerhetskopi.json", JSON.stringify(dd, null, 1), "application/json");
      if (g === "hent") rot.querySelector("input[type=file]").click();
      if (g === "slett" && window.confirm("Slette alle svarene på alle malene i denne nettleseren?")) {
        try { window.localStorage.removeItem(LS); } catch (e) { /* ingenting å gjøre */ }
        skillboks.hidden = true;
        status.textContent = "Alle svar er slettet."; startOversikt(rot);
      }
    });
    var fil = rot.querySelector("input[type=file]");
    if (fil) {
      fil.addEventListener("change", function () {
        var f = fil.files[0]; if (!f) return;
        f.text().then(function (t) {
          try {
            var inn = JSON.parse(t), dd = les();
            Object.keys(inn).forEach(function (k) { dd[k] = inn[k]; });
            skriv(dd); status.textContent = "Svarene er hentet fra filen."; startOversikt(rot);
          } catch (e) { status.textContent = "Filen kunne ikke leses."; }
        });
      });
    }
  }

  function start() {
    alle(document, ".ark").forEach(startArk);
    var o = document.querySelector(".ark-oversikt");
    if (o) startOversikt(o);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
