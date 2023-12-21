#taille_logo = (100,100)
x_max = 1440
y_max = 900
coord_logo = (50,200)
coord_logo2 = (x_max-250,200)
coord_gagnant = (x_max/2,3*y_max/5)
coord_pub = (x_max/2,y_max/2)
coord_titre = (x_max/2,100)
taille_flocon = (20,20)

blanc = (255,255,255)
noir = (0,0,0)
rose = (237,61,102)
bleu_clair = (97,228,243)
bleu_fonce = (13,31,126)
couleurs = { "rouge": (255,0,0),
           "vert" : (0,255,0),
           "bleu" : (0,0,255)
           }


ordre = ["BDA","BDE","Impact","Impact","FIR","RAID","Commu's","BDS","PICS","Institut Carlance","Macdonald","BrassandCo","Lagiraf","Miam Local","Viarezo","JCS","WACS","Oliver Wyman"]

images_lots = {
    1 : ["images\\colere.jpeg",150],
    2 : ["images\\chienne.jpeg", 150],
    3 : ["images\\artifice.jpeg", 150],
    4 : ["images\\sac.jpg",300],
    5 : ["images\\sac.jpg",300],
    6 : ["images\\sac.jpg",300],
    7 : ["images\\pepin.png",300],
    8 : ["images\\pepin.png",300],
    9 : ["images\\pepin.png",300],
    10 : ["images\\choco.jpg",500],
    11 : ["images\\nnd.jpg",450],
    12 : ["images\\commuss.jpg",450],
    13: ["images\\toss.jpg",450],
    14 : ["images\\pics_stand.jpg",400],
    15 : ["images\\massage.png",400],
    16 : ["images\\massage.png",400],
    17 : ["images\\massage.png",400],
    18 : ["images\\massage.png",400],
    19 : ["images\\coca.jpeg",400],
    20 : ["images\\coca.jpeg",400],
    21 : ["images\\coca.jpeg",400],
    22 : ["images\\coca.jpeg",400],
    23 : ["images\\cadeaux.jpeg",400],
    24 : ["images\\brass.png",400],
    25 : ["images\\brass.png",400],
    26 : ["images\\brass.png",400],
    27 : ["images\\cadeaux.jpg",400],
    28 : ["images\\cadeaux.jpg",400],
    29 : ["images\\cadeaux.jpg",400],
    30 : ["images\\miam.jpg",400],
    31 : ["images\\lotrezo.png",400],
    32 : ["images\\champ.jpg",400],
    33 : ["images\\bonnet.webp",300],
    34 : ["images\\erreur.png",300],
    35 : ["images\\erreur.png",300],
    36 : ["images\\erreur.png",300],
    37 : ["images\\erreur.png",300],
    38 : ["images\\erreur.png",300],
    39 : ["images\\erreur.png",300],
    40 : ["images\\erreur.png",300],
    41 : ["images\\erreur.png",300],
    42 : ["images\\erreur.png",300],
    43 : ["images\\erreur.png",300],
    44 : ["images\\masque.png",300],
    45 : ["images\\fondue.jpg",400],
    46 : ["images\\raclette.jpg",400],
    47 : ["images\\Golden ticket.png",400],
    48 : ["images\\Golden ticket.png",400],
    
    
}




infos_partenaires = {
    "BDA": {
        "logo" : "images\\bda.png",
        "pub" : "",
        "phrases_lots" : "On remercie Le BDA qui offre 3 livres !",
        "images_lots" : "images\\lots_bda.png",
        "nombre_lots" : 3,
        "t_lots" : 500
    },
    "FIR": {
        "logo" : "images\\fir.png",
        "pub" : "",
        "phrases_lots" : "On remercie le FIR qui offre des chocolats Nepal et un panier pépin !",
        "images_lots" : "images\\choco.jpg",
        "nombre_lots" : 1,
        "t_lots" : 500
    },
    "Oliver Wyman" :{
        "logo" : "images\\oliver.png",
        "pub" : "",
        "phrases_lots" : "On remercie Oliver Wyman qui offre 2 tickets d'or !!!",
        "images_lots" : "images\\Golden ticket.png",
        "nombre_lots" : 2,
        "t_lots" : 400
    },
    "Impact": {
        "logo" : "images\\impact.png",
        "pub" : "",
        "phrases_lots" : "On remercie Impact qui offre 3 bons pépin de 5€ !",
        "images_lots" : "images\\pepin.png",
        "nombre_lots" : 3,
        "t_lots" : 300
    },
    "JCS" :{
        "logo" : "images\\jcs.png",
        "pub" : "",
        "phrases_lots" : "On mercie la JCS qui offre une magnifique bouteille de champagne !",
        "images_lots" : "images\\champ.jpg",
        "nombre_lots" : 1,
        "t_lots" : 400
    } ,
    "RAID":{
        "logo" : "images\\raid.png",
        "pub" : "",
        "phrases_lots" : "On remercie le RAID qui offre 2 places pour le NND !",
        "images_lots" : "images\\nnd.jpg",
        "nombre_lots" : 1,
        "t_lots" : 500
    } ,
    "Viarezo" : {
        "logo" : "images\\viarezo.png",
        "pub" : "",
        "phrases_lots" : "On remercie Viarezo qui offre un casque audio ou un abonnement réseau!",
        "images_lots" : "images\\lotrezo.png",
        "nombre_lots" : 1,
        "t_lots" : 400
    },
    "BDE" : {
        "logo" : "images\\bde.jpeg",
        "pub" : "",
        "phrases_lots" : "On remercie le BDE qui offre 3 sacs de sport promo !",
        "images_lots" : "images\\sac.jpg",
        "nombre_lots" : 3,
        "t_lots" : 300
    },
    "BDS" : {
        "logo" : "images\\bds.png",
        "pub" : "",
        "phrases_lots" : "On remerice le BDS qui offre 2 places au TOSS !",
        "images_lots" : "images\\toss.jpg",
        "nombre_lots" : 1,
        "t_lots" : 500
    },
    "Commu's" : {
        "logo" : "images\\commus.jpg",
        "pub" : "",
        "phrases_lots" : "On remercie la COMMU'S qui offre 2 places pour leur spectacle !",
        "images_lots" : "images\\commuss.jpg",
        "nombre_lots" : 1,
        "t_lots" : 500
    },
    "PICS" :{
        "logo" : "images\\pics.jpeg",
        "pub" : "",
        "phrases_lots" : "ON remercie PICS qui offre 5 impressions photo A5 !",
        "images_lots" : "images\\photos.jpg",
        "nombre_lots" : 1,
        "t_lots" : 400
    },
    "WACS" :{
        "logo" : "images\\wacs.png",
        "pub" : "",
        "phrases_lots" : "La WACS vous offre de multiples cadeaux !!",
        "images_lots" : "images\\lots_wacs.jpg",
        "nombre_lots" : 14,
        "t_lots" : 500
    },
    "Miam Local":{
        "logo" : "images\\logo_miam.png",
        "pub" : "",
        "phrases_lots" : "On remrecie la Miam Local qui offre un panier en collab avec la WACS ",
        "images_lots" : "images\\miam.jpg",
        "nombre_lots" : 1,
        "t_lots" : 500
    },
}

