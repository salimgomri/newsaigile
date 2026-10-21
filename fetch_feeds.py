#!/usr/bin/env python3
"""Collecte sequentielle des flux de sources.txt.

Usage : python3 fetch_feeds.py [heures]   (defaut 72)
Sortie : un bloc par flux avec son statut (OK, VIDE, ECHEC) puis les articles recents,
et une section ETAT DES SOURCES pour le pied du mail.
VIDE = flux lu mais aucun article dans la fenetre. ECHEC = HTTP/parsing impossible.
"""
import sys, re, time, gzip, html, datetime, email.utils, urllib.request, urllib.error
import xml.etree.ElementTree as ET

HOURS = int(sys.argv[1]) if len(sys.argv) > 1 else 72
# Certains sites refusent un UA et acceptent l'autre (Le Monde : 406 sur le premier, Stratechery : 403 sur le second).
UAS = ["Mozilla/5.0 (compatible; feedreader)",
       "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"]
now = datetime.datetime.now(datetime.timezone.utc)
cut = now - datetime.timedelta(hours=HOURS)


def fetch(url):
    last = None
    ua = 0
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UAS[ua]})
            with urllib.request.urlopen(req, timeout=25) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            if e.code in (403, 406) and ua + 1 < len(UAS):
                ua += 1
                continue
            if e.code not in (429, 500, 502, 503, 504):
                break
        except Exception as e:
            last = type(e).__name__
        time.sleep(8 * (attempt + 1))
    raise RuntimeError(last)


def parse_date(s):
    if not s:
        return None
    s = s.strip()
    try:
        d = email.utils.parsedate_to_datetime(s)
    except Exception:
        try:
            d = datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except Exception:
            return None
    return d if d.tzinfo else d.replace(tzinfo=datetime.timezone.utc)


def items(data):
    if data[:2] == b"\x1f\x8b":  # certains serveurs (DeepMind) envoient du gzip sans le dire
        data = gzip.decompress(data)
    data = data.lstrip(b"\xef\xbb\xbf \t\r\n")
    root = ET.fromstring(data)
    for it in root.iter():
        if it.tag.split("}")[-1] not in ("item", "entry"):
            continue
        g = lambda n: next((c for c in it if c.tag.split("}")[-1] == n), None)
        t = g("title")
        l = g("link")
        d = next((parse_date(g(n).text) for n in ("pubDate", "published", "updated", "date") if g(n) is not None), None)
        sm = g("description") or g("summary")
        yield (d, (t.text or "").strip() if t is not None else "",
               (l.get("href") or l.text or "").strip() if l is not None else "",
               re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape((sm.text or "") if sm is not None else "")))[:200])


urls = [l.strip() for l in open("sources.txt", encoding="utf8") if l.startswith("http")]
status = []
for u in urls:
    try:
        recent = [x for x in items(fetch(u)) if x[0] and x[0] >= cut]
        status.append((u, "OK" if recent else "VIDE", len(recent)))
        print(f"## {u} [{'OK' if recent else 'VIDE'}] {len(recent)} article(s)")
        for d, t, l, s in sorted(recent, key=lambda x: x[0], reverse=True)[:15]:
            print(f"  {d:%d/%m/%Y %H:%M} | {t[:140]} | {l} | {s}")
    except Exception as e:
        status.append((u, "ECHEC", str(e)))
        print(f"## {u} [ECHEC] {e}")
    time.sleep(4 if "reddit.com" in u else 0.5)

print("\n== ETAT DES SOURCES ==")
for k in ("ECHEC", "VIDE"):
    print(k + " : " + (", ".join(u for u, st, _ in status if st == k) or "aucun"))
