#!/usr/bin/env python3
"""Génère le site statique amontanera.github.io (FR + EN). Lancer : python3 build.py"""
import os, html, datetime, markdown, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://amontanera.github.io'
PLAY = 'https://play.google.com/store/apps/details?id='
TODAY = datetime.date.today().isoformat()

APPS = {
 'sentinel': dict(
   pkg='albanm.dashcam', public=True, accent='#3b82c4', shots=8, video={'fr': 'KjieY9UvwD4', 'en': '4-6GKQ-NBxI'},
   privacy='https://raw.githubusercontent.com/amontanera/apps/main/sentinel/privacy-policy.md',
   fr=dict(
     name='Sentinel Dashcam',
     title='Sentinel Dashcam : votre téléphone Android devient une dashcam et une caméra de surveillance',
     desc="Appli Android gratuite : dashcam en boucle avec sauvegarde des chocs et GPS, et caméra de surveillance intelligente avec un vieux téléphone. Sans abonnement, sans cloud, sans compte.",
     h1='Votre téléphone devient une dashcam. Votre vieux téléphone, une caméra de surveillance.',
     lede="Sentinel Dashcam est une appli Android gratuite. Sur la route, elle filme en boucle et garde les mouvements brusques. À la maison, elle reconnaît une personne, un animal ou un véhicule et vous alerte. Tout reste sur le téléphone.",
     blocks=[
       ('Dashcam', ["Enregistrement en boucle : les plus anciens segments sont recyclés, la mémoire n'est jamais pleine",
                    "Freinage, choc, nid-de-poule : le clip est gardé automatiquement",
                    "Date, heure, GPS, vitesse et accélération incrustés dans la vidéo",
                    "Démarre seule quand le téléphone se connecte au Bluetooth de la voiture, s'arrête à l'arrivée",
                    "Profils Voiture et Moto, stabilisation, écran noir anti-distraction"]),
       ('Caméra de surveillance', ["Recyclez un ancien téléphone qui dort dans un tiroir",
                    "Détection intelligente : personne, animal, véhicule. Pas d'alerte pour une ombre ou la pluie",
                    "Alertes sonores : pleurs de bébé, bris de verre, alarme incendie, aboiements",
                    "Analyse sur le téléphone, même sans Internet"]),
       ('Sentinel Pro, achat unique', ["Route et habitacle filmés en même temps",
                    "Toutes vos caméras en direct sur la TV (Google TV, Chromecast)",
                    "Accès à distance depuis un autre téléphone, appairage par QR code",
                    "Copie automatique vers votre NAS, WebDAV ou dossier cloud",
                    "Notifications push (ntfy)"])],
     faq=[('Sentinel est-elle gratuite ?', "Oui. La dashcam, la surveillance et la détection sont gratuites, sans publicité. Sentinel Pro est un achat unique, sans abonnement."),
          ('Faut-il un compte ou un abonnement cloud ?', "Non. Aucun compte, aucun serveur. Les vidéos restent sur le téléphone, ou vont uniquement là où vous les envoyez (NAS, WebDAV, dossier cloud)."),
          ('Un vieux téléphone suffit-il ?', "Oui, Sentinel fonctionne sur Android 8 et plus. Un ancien téléphone branché sur secteur fait une très bonne caméra de surveillance."),
          ("Est-ce légal d'utiliser une dashcam ?", "Les règles varient selon les pays, en particulier pour l'audio et la diffusion des images. Renseignez-vous sur la loi locale.")]),
   en=dict(
     name='Sentinel Dashcam',
     title='Sentinel Dashcam: turn your Android phone into a dash cam and security camera',
     desc="Free Android app: loop-recording dash cam with impact save and GPS, and a smart security camera from an old phone. No subscription, no cloud, no account.",
     h1='Your phone becomes a dash cam. Your old phone, a security camera.',
     lede="Sentinel Dashcam is a free Android app. On the road it loop-records and keeps sudden moves. At home it recognizes a person, an animal or a vehicle and alerts you. Everything stays on the phone.",
     blocks=[
       ('Dash cam', ["Loop recording: oldest segments are recycled, storage never fills up",
                    "Hard braking, impact, pothole: the clip is kept automatically",
                    "Date, time, GPS, speed and g-force burned into the video",
                    "Starts on its own when the phone connects to the car's Bluetooth, stops on arrival",
                    "Car and Motorbike profiles, stabilization, black screen mode"]),
       ('Security camera', ["Reuse an old phone sleeping in a drawer",
                    "Smart detection: person, animal, vehicle. No alerts for shadows or rain",
                    "Sound alerts: baby crying, breaking glass, fire alarm, barking",
                    "Analyzed on the phone, even offline"]),
       ('Sentinel Pro, one-time purchase', ["Road and cabin recorded at the same time",
                    "All your cameras live on the TV (Google TV, Chromecast)",
                    "Remote access from another phone, QR code pairing",
                    "Automatic copy to your NAS, WebDAV or cloud folder",
                    "Push notifications (ntfy)"])],
     faq=[('Is Sentinel free?', "Yes. Dash cam, surveillance and detection are free, with no ads. Sentinel Pro is a one-time purchase, no subscription."),
          ('Do I need an account or a cloud plan?', "No. No account, no server. Videos stay on the phone, or go only where you send them (NAS, WebDAV, cloud folder)."),
          ('Will an old phone work?', "Yes, Sentinel runs on Android 8 and later. An old phone on a charger makes a great security camera."),
          ('Is a dash cam legal?', "Rules vary by country, especially for audio and sharing footage. Check your local law.")])),
 'kumul': dict(
   pkg='albanm.ardoise', public=False, accent='#4a5d9a', shots=6, video={'fr': 'Qshrpmltm9o', 'en': 'Yg2bEy2jcpQ'},
   privacy='https://raw.githubusercontent.com/amontanera/apps/main/kumul/privacy-policy.md',
   fr=dict(
     name='Kumul',
     title='Kumul : compteur de points pour tarot, belote, Skyjo, Yams et tous vos jeux',
     desc="Appli Android pour compter les points de vos jeux de cartes et de société : tarot, belote, Skyjo, Yams, Uno, rami… Classement en direct, statistiques, partage par QR code. Hors ligne, sans pub.",
     h1="Rangez le papier et le crayon : Kumul compte les points.",
     lede="Kumul tient les scores de vos soirées jeux et ne se trompe jamais dans les additions. 28 jeux déjà réglés, et tous les autres en deux secondes.",
     blocks=[
       ('Tous vos jeux', ["Tarot, belote, coinche, Skyjo, Yams, Uno, rami, 6 qui prend, Mille Bornes, Scrabble, Rummikub, Mölkky, Skull King…",
                          "Le plus haut ou le plus bas gagne, score à atteindre"]),
       ('Saisie éclair', ["Grand pavé numérique, joueur suivant automatique", "Calculette intégrée, correction d'une manche à tout moment"]),
       ('Qui gagne ?', ["Classement en direct et graphique de la partie", "Statistiques par joueur et par jeu, historique, revanche en un tap",
                        "Partage en direct : chacun suit les scores sur son téléphone via un QR code"])],
     faq=[('Kumul est-il un jeu ?', "Non : c'est une feuille de score. Il remplace le papier et le crayon autour de la table."),
          ('Faut-il Internet ?', "Non, Kumul fonctionne 100 % hors ligne, sans compte et sans publicité.")]),
   en=dict(
     name='Kumul',
     title='Kumul: score keeper for Skyjo, Yahtzee, rummy and all your card and board games',
     desc="Android score keeper for card and board games: Skyjo, Yahtzee, Uno, rummy, Rummikub… Live ranking, stats, QR code sharing. Offline, no ads.",
     h1='Put away the pen and paper: Kumul keeps score.',
     lede="Kumul keeps score at your game nights and never gets the math wrong. 28 games preset, and any other game in two seconds.",
     blocks=[
       ('All your games', ["Skyjo, Yahtzee, Uno, rummy, Rummikub, Scrabble, Mölkky, Skull King, hearts, 6 nimmt, tarot…",
                           "Highest or lowest wins, target score"]),
       ('Fast entry', ["Big number pad, next player automatically", "Built-in calculator, fix any round at any time"]),
       ("Who's winning?", ["Live ranking and game chart", "Per-player and per-game stats, history, one-tap rematch",
                           "Live share: everyone follows the score on their own phone with a QR code"])],
     faq=[('Is Kumul a game?', "No, it's a score sheet. It replaces pen and paper around the table."),
          ('Does it need internet?', "No, Kumul works 100% offline, with no account and no ads.")])),
}

UI = {
 'fr': dict(lang='fr', other='en', other_label='English', play='Télécharger sur Google Play', soon='Bientôt sur Google Play',
            faq='Questions fréquentes', video='La vidéo', shots='Captures', privacy='Confidentialité', apps='Mes applis Android',
            home_title="Applis Android d'Alban Montanera", home_h1='Des applis Android simples, sans pub et sans compte',
            home_lede="Je suis Alban, développeur indépendant. Je fais des applis qui marchent hors ligne, ne collectent rien et ne demandent pas d'abonnement.",
            by="Développée par Alban Montanera, développeur indépendant.", contact='Contact'),
 'en': dict(lang='en', other='fr', other_label='Français', play='Get it on Google Play', soon='Coming soon to Google Play',
            faq='FAQ', video='Video', shots='Screenshots', privacy='Privacy', apps='My Android apps',
            home_title='Android apps by Alban Montanera', home_h1='Simple Android apps, no ads, no account',
            home_lede="I'm Alban, an indie developer. I build apps that work offline, collect nothing and need no subscription.",
            by='Made by Alban Montanera, indie developer.', contact='Contact'),
}
E = html.escape

def path(app, lang):  # URL relative au site
    base = f'/{app}/' if app else '/'
    return base + ('en/' if lang == 'en' else '')

def page(lang, app, title, desc, body, accent='#3b6ea5'):
    u = UI[lang]; other = u['other']
    canon = SITE + path(app, lang)
    alt = ''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{path(app, l)}">' for l in ('fr', 'en'))
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canon}">{alt}<link rel="alternate" hreflang="x-default" href="{SITE}{path(app, 'en')}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{canon}">
{f'<meta property="og:image" content="{SITE}/img/{app}/{lang}-1.webp">' if app else ''}
<link rel="stylesheet" href="/style.css"><style>:root{{--accent:{accent}}}</style>
{f'<link rel="icon" href="/img/{app}/icon.png">' if app else ''}
</head><body>
<header class="top"><a href="{path(None, lang)}" class="home">{E(u['apps'])}</a><a href="{path(app, other)}" hreflang="{other}">{u['other_label']}</a></header>
<main>{body}</main>
<footer><p>{E(u['by'])} {E(u['contact'])} : albanm.apps@gmail.com</p></footer>
</body></html>'''

def app_page(key, lang):
    a = APPS[key]; t = a[lang]; u = UI[lang]
    cta = (f'<a class="cta" href="{PLAY}{a["pkg"]}&hl={lang}">{u["play"]}</a>' if a['public']
           else f'<span class="cta off">{u["soon"]}</span>')
    blocks = ''.join(f'<section class="feat"><h2>{E(h)}</h2><ul>' + ''.join(f'<li>{E(x)}</li>' for x in items) + '</ul></section>'
                     for h, items in t['blocks'])
    shots = ''.join(f'<img src="/img/{key}/{lang}-{i}.webp" alt="{E(t["name"])} {i}" loading="lazy" width="270" height="480">'
                    for i in range(1, a['shots'] + 1))
    vid = ''
    if a.get('video'):
        v = a['video'][lang]
        vid = (f'<section><h2>{u["video"]}</h2><div class="vid"><iframe src="https://www.youtube-nocookie.com/embed/{v}" title="{E(t["name"])}" '
               f'loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div></section>')
    faq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(r)}</p></details>' for q, r in t['faq'])
    ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareApplication",'
          f'"name":"{t["name"]}","operatingSystem":"Android","applicationCategory":"{"UtilitiesApplication" if key=="sentinel" else "GameApplication"}",'
          f'"offers":{{"@type":"Offer","price":"0","priceCurrency":"EUR"}},"author":{{"@type":"Person","name":"Alban Montanera"}}'
          + (f',"downloadUrl":"{PLAY}{a["pkg"]}"' if a['public'] else '') + '}</script>')
    body = f'''<section class="hero"><img src="/img/{key}/icon.png" alt="" width="72" height="72" class="icon">
<p class="eyebrow">{E(t['name'])} · Android</p><h1>{E(t['h1'])}</h1><p class="lede">{E(t['lede'])}</p>{cta}</section>
<section><h2>{u['shots']}</h2><div class="shots">{shots}</div></section>
<div class="feats">{blocks}</div>{vid}
<section><h2>{u['faq']}</h2>{faq}</section>
<p class="small"><a href="/{key}/privacy/">{u['privacy']}</a></p>{ld}'''
    return page(lang, key, t['title'], t['desc'], body, a['accent'])

def home(lang):
    u = UI[lang]
    cards = ''.join(f'''<a class="card" href="{path(k, lang)}"><img src="/img/{k}/icon.png" alt="" width="56" height="56">
<span><b>{E(a[lang]['name'])}</b><br>{E(a[lang]['desc'].split('.')[0])}.</span></a>''' for k, a in APPS.items())
    body = f'<section class="hero"><h1>{E(u["home_h1"])}</h1><p class="lede">{E(u["home_lede"])}</p></section><div class="cards">{cards}</div>'
    return page(lang, None, u['home_title'], u['home_lede'], body)

def privacy(key):
    md = urllib.request.urlopen(APPS[key]['privacy'], timeout=30).read().decode()
    body = '<article class="doc">' + markdown.markdown(md) + '</article>'
    out = page('en', key, f'{APPS[key]["en"]["name"]} privacy policy', f'Privacy policy of {APPS[key]["en"]["name"]} for Android.', body)
    return out.replace(f'<link rel="canonical" href="{SITE}/{key}/en/">', f'<link rel="canonical" href="{SITE}/{key}/privacy/">')

def write(rel, s):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(s)

urls = []
for lang in ('fr', 'en'):
    write(('en/' if lang == 'en' else '') + 'index.html', home(lang)); urls.append(path(None, lang))
    for k in APPS:
        write(f'{k}/' + ('en/' if lang == 'en' else '') + 'index.html', app_page(k, lang)); urls.append(path(k, lang))
for k in APPS:
    write(f'{k}/privacy/index.html', privacy(k)); urls.append(f'/{k}/privacy/')
write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
      + ''.join(f'<url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n' for u in urls) + '</urlset>\n')
write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
print('ok', len(urls), 'pages')
