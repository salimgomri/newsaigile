"""Synthèse vocale du podcast AIgile avec Cartesia (voix Henri).

Usage : python3 tools/podcast.py texte.txt audio/aigile-AAAA-MM-JJ.mp3
La clé est lue dans la variable d'environnement CARTESIA_API_KEY, jamais écrite dans un fichier.
"""
import json, os, sys, urllib.request

VOICE_ID = "d9f4af15-c402-4f50-bbda-d8823d028d6a"  # Henri, Express Host, fr-FR
MAX_CHARS = 3500


def chunks(text):
    out, cur = [], ""
    for para in text.split("\n\n"):
        if cur and len(cur) + len(para) + 2 > MAX_CHARS:
            out.append(cur)
            cur = ""
        cur = f"{cur}\n\n{para}" if cur else para
    if cur:
        out.append(cur)
    return out


def synth(key, transcript):
    body = {
        "model_id": "sonic-3",
        "transcript": transcript,
        "voice": {"mode": "id", "id": VOICE_ID},
        "language": "fr",
        "output_format": {"container": "mp3", "sample_rate": 44100, "bit_rate": 128000},
    }
    req = urllib.request.Request(
        "https://api.cartesia.ai/tts/bytes",
        data=json.dumps(body).encode(),
        headers={"X-API-Key": key, "Cartesia-Version": "2025-04-16", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def main():
    key = os.environ.get("CARTESIA_API_KEY")
    if not key:
        sys.exit("CARTESIA_API_KEY absente")
    text = open(sys.argv[1], encoding="utf-8").read().strip()
    audio = b"".join(synth(key, c) for c in chunks(text))
    os.makedirs(os.path.dirname(sys.argv[2]) or ".", exist_ok=True)
    open(sys.argv[2], "wb").write(audio)
    print(f"{sys.argv[2]} : {len(audio)} octets")


main()
