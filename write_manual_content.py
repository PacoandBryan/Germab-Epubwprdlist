import json
import os

OUTPUT_MD = 'foundation_book.md'

def write_session(session_id, entries):
    mode = 'w' if session_id == 1 else 'a'
    with open(OUTPUT_MD, mode, encoding='utf-8') as f:
        if session_id == 1:
            f.write("% The Platinum German Vocabulary Builder\n")
            f.write("% Leonardo Torres Hernández\n")
            f.write("% 2024\n\n")
            f.write("# Copyright\n\n")
            f.write("Copyright © 2024 by Leonardo Torres Hernández. All rights reserved.\n\n")
            f.write("\\newpage\n\n")

        f.write(f"# Session {session_id}\n\n")
        for entry in entries:
            f.write(f"*   **The Word:** {entry['word']}\n")
            f.write(f"*   **Translation:** {entry['translation']}\n")
            if 'verb_forms' in entry and entry['verb_forms']:
                f.write(f"*   **Verb Forms:** {entry['verb_forms']}\n")
            f.write(f"*   **B2 Example Sentence:** {entry['sentence_de']}\n")
            f.write(f"*   **Sentence Translation:** {entry['sentence_en']}\n\n")

# Session 1
session_1 = [
    {"word": "unerlässlich", "translation": "essential / indispensable", "sentence_de": "Eine gute Vorbereitung ist für den Erfolg dieses Projekts unerlässlich.", "sentence_en": "Good preparation is essential for the success of this project."},
    {"word": "bewerten (hat bewertet)", "translation": "to evaluate / to assess", "verb_forms": "Präteritum: bewertete, Perfekt: hat bewertet", "sentence_de": "Wir müssen die aktuellen Marktdaten sorgfältig bewerten.", "sentence_en": "We must carefully evaluate the current market data."},
    {"word": "stark", "translation": "strong", "sentence_de": "Der Sturm war so stark, dass er mehrere Bäume entwurzelte.", "sentence_en": "The storm was so strong that it uprooted several trees."},
    {"word": "emotional", "translation": "emotional", "sentence_de": "Die Debatte wurde sehr emotional geführt.", "sentence_en": "The debate was conducted very emotionally."},
    {"word": "kulturell", "translation": "cultural", "sentence_de": "Berlin hat ein vielfältiges kulturelles Angebot.", "sentence_en": "Berlin has a diverse cultural offering."},
    {"word": "euphorisch", "translation": "euphoric", "sentence_de": "Die Fans reagierten euphorisch auf den Sieg ihrer Mannschaft.", "sentence_en": "The fans reacted euphorically to their team's victory."},
    {"word": "preiswert", "translation": "inexpensive / good value", "sentence_de": "Dieses Restaurant bietet sehr preiswerte Mittagsmenüs an.", "sentence_en": "This restaurant offers very inexpensive lunch menus."},
    {"word": "erschwinglich", "translation": "affordable", "sentence_de": "Wohnraum in der Innenstadt ist kaum noch erschwinglich.", "sentence_en": "Housing in the city center is hardly affordable anymore."},
    {"word": "erschließen (hat erschlossen)", "translation": "to develop / to open up", "verb_forms": "Präteritum: erschloss, Perfekt: hat erschlossen", "sentence_de": "Das Unternehmen plant, neue Märkte in Asien zu erschließen.", "sentence_en": "The company plans to open up new markets in Asia."},
    {"word": "arbeiten (hat gearbeitet)", "translation": "to work", "verb_forms": "Präteritum: arbeitete, Perfekt: hat gearbeitet, Preposition: an (+ Dat)", "sentence_de": "Wir arbeiten derzeit an einer Lösung für das Problem.", "sentence_en": "We are currently working on a solution to the problem."},
    {"word": "verlängern (hat verlängert)", "translation": "to extend", "verb_forms": "Präteritum: verlängerte, Perfekt: hat verlängert", "sentence_de": "Können Sie bitte meinen Aufenthalt um zwei Tage verlängern?", "sentence_en": "Could you please extend my stay by two days?"},
    {"word": "verpassen (hat verpasst)", "translation": "to miss", "verb_forms": "Präteritum: verpasste, Perfekt: hat verpasst", "sentence_de": "Wenn wir uns nicht beeilen, verpassen wir den Zug.", "sentence_en": "If we don't hurry, we will miss the train."},
    {"word": "finanzieren (hat finanziert)", "translation": "to finance", "verb_forms": "Präteritum: finanzierte, Perfekt: hat finanziert", "sentence_de": "Das Studium wird durch ein Stipendium finanziert.", "sentence_en": "The studies are financed by a scholarship."},
    {"word": "dirigieren (hat dirigiert)", "translation": "to conduct", "verb_forms": "Präteritum: dirigierte, Perfekt: hat dirigiert", "sentence_de": "Der berühmte Maestro dirigierte das Orchester mit großer Leidenschaft.", "sentence_en": "The famous maestro conducted the orchestra with great passion."},
    {"word": "kostenlos", "translation": "free of charge", "sentence_de": "Der Eintritt in das Museum ist für Studenten kostenlos.", "sentence_en": "Admission to the museum is free for students."},
    {"word": "niedrig", "translation": "low", "sentence_de": "Die Temperaturen sind für diese Jahreszeit ungewöhnlich niedrig.", "sentence_en": "The temperatures are unusually low for this time of year."},
    {"word": "kontrolliert (hat kontrolliert)", "translation": "controlled / to control", "verb_forms": "Präteritum: kontrollierte, Perfekt: hat kontrolliert", "sentence_de": "Der Zugang zum Gebäude wird streng kontrolliert.", "sentence_en": "Access to the building is strictly controlled."},
    {"word": "historisch", "translation": "historical", "sentence_de": "Wir haben eine historische Verantwortung.", "sentence_en": "We have a historical responsibility."},
    {"word": "verschreiben (hat verschrieben)", "translation": "to prescribe", "verb_forms": "Präteritum: verschrieb, Perfekt: hat verschrieben", "sentence_de": "Der Arzt hat mir ein starkes Schmerzmittel verschrieben.", "sentence_en": "The doctor prescribed me a strong painkiller."},
    {"word": "mäßig", "translation": "moderate / mediocre", "sentence_de": "Die Qualität des Essens war nur mäßig.", "sentence_en": "The quality of the food was only mediocre."}
]

# Session 2
session_2 = [
    {"word": "schick", "translation": "chic / stylish", "sentence_de": "Sie trägt heute ein sehr schickes Kleid.", "sentence_en": "She is wearing a very chic dress today."},
    {"word": "aufbewahren (hat aufbewahrt)", "translation": "to keep / to store", "verb_forms": "Präteritum: bewahrte auf, Perfekt: hat aufbewahrt", "sentence_de": "Man sollte Medikamente für Kinder unzugänglich aufbewahren.", "sentence_en": "Medication should be kept out of reach of children."},
    {"word": "durchhalten (hat durchgehalten)", "translation": "to persevere / to hold out", "verb_forms": "Präteritum: hielt durch, Perfekt: hat durchgehalten", "sentence_de": "Es war ein langes Rennen, aber er hat bis zum Ende durchgehalten.", "sentence_en": "It was a long race, but he persevered until the end."},
    {"word": "kreativ", "translation": "creative", "sentence_de": "Wir suchen nach kreativen Lösungen für dieses Problem.", "sentence_en": "We are looking for creative solutions to this problem."},
    {"word": "einnehmen (hat eingenommen)", "translation": "to take / to occupy", "verb_forms": "Präteritum: nahm ein, Perfekt: hat eingenommen", "sentence_de": "Bitte nehmen Sie die Tabletten nach dem Essen ein.", "sentence_en": "Please take the tablets after the meal."},
    {"word": "abenteuerlustig", "translation": "adventurous", "sentence_de": "Mein Bruder ist sehr abenteuerlustig und reist gerne an exotische Orte.", "sentence_en": "My brother is very adventurous and likes to travel to exotic places."},
    {"word": "reparaturbedürftig", "translation": "in need of repair", "sentence_de": "Das alte Haus ist stark reparaturbedürftig.", "sentence_en": "The old house is in great need of repair."},
    {"word": "künstlerisch", "translation": "artistic", "sentence_de": "Sie hat großes künstlerisches Talent.", "sentence_en": "She has great artistic talent."},
    {"word": "einüben (hat eingeübt)", "translation": "to practice / to rehearse", "verb_forms": "Präteritum: übte ein, Perfekt: hat eingeübt", "sentence_de": "Die Schauspieler müssen ihre Rollen noch weiter einüben.", "sentence_en": "The actors still need to practice their roles further."},
    {"word": "retournieren (hat retourniert)", "translation": "to return (goods)", "verb_forms": "Präteritum: retournierte, Perfekt: hat retourniert", "sentence_de": "Ich möchte diese Schuhe retournieren, da sie nicht passen.", "sentence_en": "I would like to return these shoes because they don't fit."},
    {"word": "robust", "translation": "robust", "sentence_de": "Diese Pflanze ist sehr robust und braucht wenig Wasser.", "sentence_en": "This plant is very robust and needs little water."},
    {"word": "anstrengend", "translation": "exhausting", "sentence_de": "Die Wanderung war sehr anstrengend, aber der Ausblick hat sich gelohnt.", "sentence_en": "The hike was very exhausting, but the view was worth it."},
    {"word": "widerstandsfähig", "translation": "resistant", "sentence_de": "Das Material ist extrem widerstandsfähig gegen Hitze.", "sentence_en": "The material is extremely resistant to heat."},
    {"word": "leistungsstark", "translation": "powerful", "sentence_de": "Wir brauchen einen leistungsstarken Computer für die Videobearbeitung.", "sentence_en": "We need a powerful computer for video editing."},
    {"word": "bearbeiten (hat bearbeitet)", "translation": "to edit / to process", "verb_forms": "Präteritum: bearbeitete, Perfekt: hat bearbeitet", "sentence_de": "Ich muss noch einige E-Mails bearbeiten.", "sentence_en": "I still have to process a few emails."},
    {"word": "programmierbar", "translation": "programmable", "sentence_de": "Die Heizung ist programmierbar, sodass sie morgens automatisch anspringt.", "sentence_en": "The heating is programmable so that it starts automatically in the morning."},
    {"word": "ruhig", "translation": "quiet / calm", "sentence_de": "Bitte seien Sie während der Prüfung ruhig.", "sentence_en": "Please be quiet during the exam."},
    {"word": "rund", "translation": "round", "sentence_de": "Der Tisch in der Küche ist rund.", "sentence_en": "The table in the kitchen is round."},
    {"word": "aufnehmen (hat aufgenommen)", "translation": "to record / to admit", "verb_forms": "Präteritum: nahm auf, Perfekt: hat aufgenommen", "sentence_de": "Wir werden das Konzert live aufnehmen.", "sentence_en": "We will record the concert live."},
    {"word": "aufladen (hat aufgeladen)", "translation": "to charge", "verb_forms": "Präteritum: lud auf, Perfekt: hat aufgeladen", "sentence_de": "Ich muss mein Handy aufladen, der Akku ist fast leer.", "sentence_en": "I need to charge my phone, the battery is almost empty."}
]

# Session 3
session_3 = [
    {"word": "akut", "translation": "acute", "sentence_de": "Es besteht akute Gefahr für die Bevölkerung.", "sentence_en": "There is an acute danger to the population."},
    {"word": "souverän", "translation": "confident / sovereign", "sentence_de": "Sie hat die schwierige Situation souverän gemeistert.", "sentence_en": "She mastered the difficult situation confidently."},
    {"word": "risikobereit", "translation": "willing to take risks", "sentence_de": "Unternehmer müssen oft risikobereit sein, um Erfolg zu haben.", "sentence_en": "Entrepreneurs often have to be willing to take risks to succeed."},
    {"word": "anwendungsorientiert", "translation": "application-oriented", "sentence_de": "Das Studium ist sehr praxisnah und anwendungsorientiert.", "sentence_en": "The study program is very practical and application-oriented."},
    {"word": "pünktlich", "translation": "punctual", "sentence_de": "Bitte seien Sie pünktlich zum Meeting.", "sentence_en": "Please be punctual for the meeting."},
    {"word": "ausreichend", "translation": "sufficient", "sentence_de": "Es gibt ausreichend Parkplätze für alle Gäste.", "sentence_en": "There are sufficient parking spaces for all guests."},
    {"word": "betreuen (hat betreut)", "translation": "to supervise / to look after", "verb_forms": "Präteritum: betreute, Perfekt: hat betreut", "sentence_de": "Wer betreut das Projekt während Ihrer Abwesenheit?", "sentence_en": "Who is supervising the project during your absence?"},
    {"word": "beraten (hat beraten)", "translation": "to advise", "verb_forms": "Präteritum: beriet, Perfekt: hat beraten", "sentence_de": "Wir lassen uns von einem Experten beraten.", "sentence_en": "We are being advised by an expert."},
    {"word": "bedienen (hat bedient)", "translation": "to serve / to operate", "verb_forms": "Präteritum: bediente, Perfekt: hat bedient", "sentence_de": "Können Sie diese komplexe Maschine bedienen?", "sentence_en": "Can you operate this complex machine?"},
    {"word": "erleben (hat erlebt)", "translation": "to experience", "verb_forms": "Präteritum: erlebte, Perfekt: hat erlebt", "sentence_de": "Wir haben im Urlaub viele schöne Momente erlebt.", "sentence_en": "We experienced many beautiful moments on vacation."},
    {"word": "gründen (hat gegründet)", "translation": "to found / to establish", "verb_forms": "Präteritum: gründete, Perfekt: hat gegründet", "sentence_de": "Sie wollen nächstes Jahr ihre eigene Firma gründen.", "sentence_en": "They want to found their own company next year."},
    {"word": "aufmerksam", "translation": "attentive", "sentence_de": "Das Publikum hörte dem Vortrag aufmerksam zu.", "sentence_en": "The audience listened attentively to the lecture."},
    {"word": "vorführen (hat vorgeführt)", "translation": "to demonstrate / to perform", "verb_forms": "Präteritum: führte vor, Perfekt: hat vorgeführt", "sentence_de": "Der Verkäufer führte uns die Funktionen des Geräts vor.", "sentence_en": "The salesperson demonstrated the functions of the device to us."},
    {"word": "salzig", "translation": "salty", "sentence_de": "Die Suppe ist leider etwas zu salzig geraten.", "sentence_en": "Unfortunately, the soup turned out a bit too salty."},
    {"word": "strukturiert", "translation": "structured", "sentence_de": "Er arbeitet sehr strukturiert und effizient.", "sentence_en": "He works in a very structured and efficient manner."},
    {"word": "beziehen (hat bezogen)", "translation": "to obtain / to refer to", "verb_forms": "Präteritum: bezog, Perfekt: hat bezogen", "sentence_de": "Wir beziehen unsere Rohstoffe aus nachhaltigen Quellen.", "sentence_en": "We obtain our raw materials from sustainable sources."},
    {"word": "erweitern (hat erweitert)", "translation": "to expand", "verb_forms": "Präteritum: erweiterte, Perfekt: hat erweitert", "sentence_de": "Wir planen, unser Sortiment bald zu erweitern.", "sentence_en": "We plan to expand our assortment soon."},
    {"word": "begeistert", "translation": "enthusiastic", "sentence_de": "Die Zuschauer waren von der Aufführung begeistert.", "sentence_en": "The audience was enthusiastic about the performance."},
    {"word": "konzentriert", "translation": "concentrated", "sentence_de": "Sie arbeitete hoch konzentriert an ihrer Abschlussarbeit.", "sentence_en": "She worked highly concentrated on her thesis."},
    {"word": "außergewöhnlich", "translation": "exceptional", "sentence_de": "Sie hat eine außergewöhnliche Begabung für Mathematik.", "sentence_en": "She has an exceptional talent for mathematics."}
]

# Session 4
session_4 = [
    {"word": "vorteilhaft", "translation": "advantageous", "sentence_de": "Eine frühe Buchung ist oft preislich vorteilhaft.", "sentence_en": "Booking early is often financially advantageous."},
    {"word": "anschließen (hat angeschlossen)", "translation": "to connect", "verb_forms": "Präteritum: schloss an, Perfekt: hat angeschlossen", "sentence_de": "Bitte schließen Sie den Drucker an den Computer an.", "sentence_en": "Please connect the printer to the computer."},
    {"word": "behandeln (hat behandelt)", "translation": "to treat", "verb_forms": "Präteritum: behandelte, Perfekt: hat behandelt", "sentence_de": "Der Arzt behandelt den Patienten mit Antibiotika.", "sentence_en": "The doctor is treating the patient with antibiotics."},
    {"word": "verhindern (hat verhindert)", "translation": "to prevent", "verb_forms": "Präteritum: verhinderte, Perfekt: hat verhindert", "sentence_de": "Wir müssen versuchen, diesen Fehler zu verhindern.", "sentence_en": "We must try to prevent this mistake."},
    {"word": "originell", "translation": "original", "sentence_de": "Das ist eine sehr originelle Idee für ein Geschenk.", "sentence_en": "That is a very original idea for a gift."},
    {"word": "ausbilden (hat ausgebildet)", "translation": "to train / to educate", "verb_forms": "Präteritum: bildete aus, Perfekt: hat ausgebildet", "sentence_de": "Unser Betrieb bildet jedes Jahr drei Lehrlinge aus.", "sentence_en": "Our company trains three apprentices every year."},
    {"word": "aufregend", "translation": "exciting", "sentence_de": "Die Reise nach Afrika war ein aufregendes Erlebnis.", "sentence_en": "The trip to Africa was an exciting experience."},
    {"word": "erkunden (hat erkundet)", "translation": "to explore", "verb_forms": "Präteritum: erkundete, Perfekt: hat erkundet", "sentence_de": "Wir wollen die Stadt zu Fuß erkunden.", "sentence_en": "We want to explore the city on foot."},
    {"word": "motiviert", "translation": "motivated", "sentence_de": "Das Team ist hoch motiviert, das Ziel zu erreichen.", "sentence_en": "The team is highly motivated to reach the goal."},
    {"word": "chaotisch", "translation": "chaotic", "sentence_de": "Auf meinem Schreibtisch sieht es momentan sehr chaotisch aus.", "sentence_en": "It looks very chaotic on my desk right now."},
    {"word": "selbstbewusst", "translation": "confident", "sentence_de": "Sie trat bei der Präsentation sehr selbstbewusst auf.", "sentence_en": "She appeared very confident during the presentation."},
    {"word": "verschwenden (hat verschwendet)", "translation": "to waste", "verb_forms": "Präteritum: verschwendete, Perfekt: hat verschwendet", "sentence_de": "Wir sollten keine Zeit mit unnötigen Diskussionen verschwenden.", "sentence_en": "We should not waste time on unnecessary discussions."},
    {"word": "professionell", "translation": "professional", "sentence_de": "Wir erwarten eine professionelle Abwicklung des Auftrags.", "sentence_en": "We expect a professional execution of the order."},
    {"word": "akustisch", "translation": "acoustic", "sentence_de": "Die akustische Qualität des Saales ist hervorragend.", "sentence_en": "The acoustic quality of the hall is excellent."},
    {"word": "harmonisch", "translation": "harmonious", "sentence_de": "Die Farben in diesem Bild wirken sehr harmonisch.", "sentence_en": "The colors in this picture appear very harmonious."},
    {"word": "menschlich", "translation": "human", "sentence_de": "Irren ist menschlich.", "sentence_en": "To err is human."},
    {"word": "verständnisvoll", "translation": "understanding", "sentence_de": "Der Lehrer reagierte verständnisvoll auf die Probleme des Schülers.", "sentence_en": "The teacher reacted understandingly to the student's problems."},
    {"word": "harmonieren (hat harmoniert)", "translation": "to harmonize", "verb_forms": "Präteritum: harmonierte, Perfekt: hat harmoniert", "sentence_de": "Der Wein harmoniert perfekt mit dem Käse.", "sentence_en": "The wine harmonizes perfectly with the cheese."},
    {"word": "diagnostizieren (hat diagnostiziert)", "translation": "to diagnose", "verb_forms": "Präteritum: diagnostizierte, Perfekt: hat diagnostiziert", "sentence_de": "Der Arzt diagnostizierte eine seltene Krankheit.", "sentence_en": "The doctor diagnosed a rare disease."},
    {"word": "standhaft", "translation": "steadfast", "sentence_de": "Er blieb trotz der Kritik standhaft bei seiner Meinung.", "sentence_en": "He remained steadfast in his opinion despite the criticism."}
]

# Session 5
session_5 = [
    {"word": "besichtigen (hat besichtigt)", "translation": "to visit / to view", "verb_forms": "Präteritum: besichtigte, Perfekt: hat besichtigt", "sentence_de": "Wir werden morgen das Schloss besichtigen.", "sentence_en": "We will visit the castle tomorrow."},
    {"word": "engagiert", "translation": "committed / dedicated", "sentence_de": "Sie ist eine sehr engagierte Mitarbeiterin.", "sentence_en": "She is a very committed employee."},
    {"word": "ansprechend", "translation": "appealing", "sentence_de": "Das Design der Webseite ist sehr ansprechend.", "sentence_en": "The design of the website is very appealing."},
    {"word": "ausdrucksstark", "translation": "expressive", "sentence_de": "Der Schauspieler hat eine sehr ausdrucksstarke Mimik.", "sentence_en": "The actor has very expressive facial expressions."},
    {"word": "begleiten (hat begleitet)", "translation": "to accompany", "verb_forms": "Präteritum: begleitete, Perfekt: hat begleitet", "sentence_de": "Darf ich Sie nach Hause begleiten?", "sentence_en": "May I accompany you home?"},
    {"word": "ausrichten (hat ausgerichtet)", "translation": "to align / to organize", "verb_forms": "Präteritum: richtete aus, Perfekt: hat ausgerichtet", "sentence_de": "Die Firma richtete eine große Feier für die Mitarbeiter aus.", "sentence_en": "The company organized a big party for the employees."},
    {"word": "steuerbar", "translation": "controllable", "sentence_de": "Die Drohne ist per App steuerbar.", "sentence_en": "The drone is controllable via app."},
    {"word": "einschalten (hat eingeschaltet)", "translation": "to switch on", "verb_forms": "Präteritum: schaltete ein, Perfekt: hat eingeschaltet", "sentence_de": "Bitte schalten Sie das Licht ein.", "sentence_en": "Please switch on the light."},
    {"word": "fokussieren (hat fokussiert)", "translation": "to focus", "verb_forms": "Präteritum: fokussierte, Perfekt: hat fokussiert", "sentence_de": "Wir müssen uns auf die wesentlichen Aufgaben fokussieren.", "sentence_en": "We must focus on the essential tasks."},
    {"word": "verlieren (hat verloren)", "translation": "to lose", "verb_forms": "Präteritum: verlor, Perfekt: hat verloren", "sentence_de": "Ich habe meinen Schlüssel verloren.", "sentence_en": "I have lost my key."},
    {"word": "beschränkt", "translation": "limited", "sentence_de": "Die Teilnehmerzahl ist auf 20 Personen beschränkt.", "sentence_en": "The number of participants is limited to 20 people."},
    {"word": "komplex", "translation": "complex", "sentence_de": "Das menschliche Gehirn ist ein äußerst komplexes Organ.", "sentence_en": "The human brain is an extremely complex organ."},
    {"word": "routiniert", "translation": "experienced / routine", "sentence_de": "Er erledigte die Aufgabe routiniert und schnell.", "sentence_en": "He completed the task routinely and quickly."},
    {"word": "abmelden (hat abgemeldet)", "translation": "to unsubscribe / to sign off", "verb_forms": "Präteritum: meldete ab, Perfekt: hat abgemeldet", "sentence_de": "Vergessen Sie nicht, sich vom Computer abzumelden.", "sentence_en": "Do not forget to sign off from the computer."},
    {"word": "zurückgeben (hat zurückgegeben)", "translation": "to return", "verb_forms": "Präteritum: gab zurück, Perfekt: hat zurückgegeben", "sentence_de": "Ich muss das Buch morgen an die Bibliothek zurückgeben.", "sentence_en": "I have to return the book to the library tomorrow."},
    {"word": "verdienen (hat verdient)", "translation": "to earn / to deserve", "verb_forms": "Präteritum: verdiente, Perfekt: hat verdient", "sentence_de": "Er verdient in seinem neuen Job sehr gut.", "sentence_en": "He earns very well in his new job."},
    {"word": "fokussiert", "translation": "focused", "sentence_de": "Sie wirkte während des Gesprächs sehr fokussiert.", "sentence_en": "She seemed very focused during the conversation."},
    {"word": "authentisch", "translation": "authentic", "sentence_de": "Das Restaurant bietet authentische italienische Küche.", "sentence_en": "The restaurant offers authentic Italian cuisine."},
    {"word": "erstaunlich", "translation": "astonishing / amazing", "sentence_de": "Es ist erstaunlich, wie schnell Kinder lernen.", "sentence_en": "It is astonishing how quickly children learn."},
    {"word": "anstreben (hat angestrebt)", "translation": "to strive for", "verb_forms": "Präteritum: strebte an, Perfekt: hat angestrebt", "sentence_de": "Wir streben eine langfristige Partnerschaft an.", "sentence_en": "We are striving for a long-term partnership."}
]

if __name__ == "__main__":
    write_session(1, session_1)
    write_session(2, session_2)
    write_session(3, session_3)
    write_session(4, session_4)
    write_session(5, session_5)

# Session 6
session_6 = [
    {"word": "qualifizieren (hat qualifiziert)", "translation": "to qualify", "verb_forms": "Präteritum: qualifizierte, Perfekt: hat qualifiziert", "sentence_de": "Er hat sich für die Meisterschaft qualifiziert.", "sentence_en": "He qualified for the championship."},
    {"word": "beeindruckend", "translation": "impressive", "sentence_de": "Die Aussicht vom Gipfel war beeindruckend.", "sentence_en": "The view from the summit was impressive."},
    {"word": "langfristig", "translation": "long-term", "sentence_de": "Wir suchen nach einer langfristigen Lösung.", "sentence_en": "We are looking for a long-term solution."},
    {"word": "moderiert", "translation": "moderated", "sentence_de": "Die Diskussion wurde von einem erfahrenen Journalisten moderiert.", "sentence_en": "The discussion was moderated by an experienced journalist."},
    {"word": "initiativ", "translation": "proactive / initiative", "sentence_de": "Wir schätzen initiative Mitarbeiter.", "sentence_en": "We value proactive employees."},
    {"word": "erledigen (hat erledigt)", "translation": "to take care of / to complete", "verb_forms": "Präteritum: erledigte, Perfekt: hat erledigt", "sentence_de": "Ich muss noch einige Dinge erledigen.", "sentence_en": "I still have a few things to take care of."},
    {"word": "beeindrucken (hat beeindruckt)", "translation": "to impress", "verb_forms": "Präteritum: beeindruckte, Perfekt: hat beeindruckt", "sentence_de": "Ihre Leistung hat uns sehr beeindruckt.", "sentence_en": "Her performance impressed us very much."},
    {"word": "aushandeln (hat ausgehandelt)", "translation": "to negotiate", "verb_forms": "Präteritum: handelte aus, Perfekt: hat ausgehandelt", "sentence_de": "Die Gewerkschaften handelten einen neuen Tarifvertrag aus.", "sentence_en": "The unions negotiated a new collective agreement."},
    {"word": "abgeschieden", "translation": "secluded / isolated", "sentence_de": "Sie wohnen in einem abgeschiedenen Haus im Wald.", "sentence_en": "They live in a secluded house in the forest."},
    {"word": "vorübergehend", "translation": "temporary", "sentence_de": "Das Geschäft ist vorübergehend geschlossen.", "sentence_en": "The shop is temporarily closed."},
    {"word": "wesentlich", "translation": "essential / significant", "sentence_de": "Er hat einen wesentlichen Beitrag zum Erfolg geleistet.", "sentence_en": "He made a significant contribution to the success."},
    {"word": "begeistern (hat begeistert)", "translation": "to inspire / to enthuse", "verb_forms": "Präteritum: begeisterte, Perfekt: hat begeistert", "sentence_de": "Er konnte das Publikum mit seiner Rede begeistern.", "sentence_en": "He was able to inspire the audience with his speech."},
    {"word": "vermieten (hat vermietet)", "translation": "to rent out", "verb_forms": "Präteritum: vermietete, Perfekt: hat vermietet", "sentence_de": "Wir vermieten unsere Wohnung während wir im Urlaub sind.", "sentence_en": "We rent out our apartment while we are on vacation."},
    {"word": "anmelden (hat angemeldet)", "translation": "to register", "verb_forms": "Präteritum: meldete an, Perfekt: hat angemeldet", "sentence_de": "Sie müssen sich für den Kurs schriftlich anmelden.", "sentence_en": "You must register for the course in writing."},
    {"word": "aufbrauchen (hat aufgebraucht)", "translation": "to use up", "verb_forms": "Präteritum: brauchte auf, Perfekt: hat aufgebraucht", "sentence_de": "Wir haben alle Vorräte aufgebraucht.", "sentence_en": "We have used up all supplies."},
    {"word": "verstimmen (hat verstimmt)", "translation": "to upset / to detune", "verb_forms": "Präteritum: verstimmte, Perfekt: hat verstimmt", "sentence_de": "Die schlechte Nachricht verstimmte ihn sichtlich.", "sentence_en": "The bad news visibly upset him."},
    {"word": "realistisch", "translation": "realistic", "sentence_de": "Bleiben Sie bitte realistisch.", "sentence_en": "Please remain realistic."},
    {"word": "anbieten (hat angeboten)", "translation": "to offer", "verb_forms": "Präteritum: bot an, Perfekt: hat angeboten", "sentence_de": "Darf ich Ihnen etwas zu trinken anbieten?", "sentence_en": "May I offer you something to drink?"},
    {"word": "verlagern (hat verlagert)", "translation": "to relocate / to shift", "verb_forms": "Präteritum: verlagerte, Perfekt: hat verlagert", "sentence_de": "Das Unternehmen verlagert die Produktion ins Ausland.", "sentence_en": "The company is relocating production abroad."},
    {"word": "verwalten (hat verwaltet)", "translation": "to manage / to administer", "verb_forms": "Präteritum: verwaltete, Perfekt: hat verwaltet", "sentence_de": "Er verwaltet das Vermögen seiner Eltern.", "sentence_en": "He manages his parents' assets."}
]

# Session 7
session_7 = [
    {"word": "evaluieren (hat evaluiert)", "translation": "to evaluate", "verb_forms": "Präteritum: evaluierte, Perfekt: hat evaluiert", "sentence_de": "Wir müssen die Ergebnisse des Tests evaluieren.", "sentence_en": "We must evaluate the results of the test."},
    {"word": "praktisch", "translation": "practical", "sentence_de": "Diese Lösung ist sehr praktisch.", "sentence_en": "This solution is very practical."},
    {"word": "handhaben (hat gehandhabt)", "translation": "to handle", "verb_forms": "Präteritum: handhabte, Perfekt: hat gehandhabt", "sentence_de": "Wie handhaben Sie Reklamationen?", "sentence_en": "How do you handle complaints?"},
    {"word": "umgestalten (hat umgestaltet)", "translation": "to redesign / to remodel", "verb_forms": "Präteritum: gestaltete um, Perfekt: hat umgestaltet", "sentence_de": "Wir wollen unser Wohnzimmer umgestalten.", "sentence_en": "We want to redesign our living room."},
    {"word": "nutzbringend", "translation": "beneficial / useful", "sentence_de": "Wir sollten die Zeit nutzbringend verwenden.", "sentence_en": "We should use the time beneficially."},
    {"word": "komfortabel", "translation": "comfortable", "sentence_de": "Das neue Sofa ist sehr komfortabel.", "sentence_en": "The new sofa is very comfortable."},
    {"word": "wechseln (hat gewechselt)", "translation": "to change / to switch", "verb_forms": "Präteritum: wechselte, Perfekt: hat gewechselt", "sentence_de": "Ich möchte Geld wechseln.", "sentence_en": "I would like to change money."},
    {"word": "beleuchten (hat beleuchtet)", "translation": "to illuminate / to highlight", "verb_forms": "Präteritum: beleuchtete, Perfekt: hat beleuchtet", "sentence_de": "Der Artikel beleuchtet verschiedene Aspekte des Themas.", "sentence_en": "The article highlights different aspects of the topic."},
    {"word": "chronisch", "translation": "chronic", "sentence_de": "Er leidet an einer chronischen Krankheit.", "sentence_en": "He suffers from a chronic illness."},
    {"word": "luxuriös", "translation": "luxurious", "sentence_de": "Sie übernachteten in einem luxuriösen Hotel.", "sentence_en": "They stayed in a luxurious hotel."},
    {"word": "bestimmen (hat bestimmt)", "translation": "to determine", "verb_forms": "Präteritum: bestimmte, Perfekt: hat bestimmt", "sentence_de": "Das Angebot und die Nachfrage bestimmen den Preis.", "sentence_en": "Supply and demand determine the price."},
    {"word": "organisiert", "translation": "organized", "sentence_de": "Die Veranstaltung war sehr gut organisiert.", "sentence_en": "The event was very well organized."},
    {"word": "konsequent", "translation": "consistent", "sentence_de": "Er verfolgte seine Ziele konsequent.", "sentence_en": "He pursued his goals consistently."},
    {"word": "sanierungsbedürftig", "translation": "in need of renovation", "sentence_de": "Die Brücke ist stark sanierungsbedürftig.", "sentence_en": "The bridge is in great need of renovation."},
    {"word": "beharrlich", "translation": "persistent", "sentence_de": "Sie fragte beharrlich nach, bis sie eine Antwort bekam.", "sentence_en": "She asked persistently until she got an answer."},
    {"word": "vorbereiten (hat vorbereitet)", "translation": "to prepare", "verb_forms": "Präteritum: bereitete vor, Perfekt: hat vorbereitet", "sentence_de": "Ich muss mich auf die Präsentation vorbereiten.", "sentence_en": "I have to prepare for the presentation."},
    {"word": "präzise", "translation": "precise", "sentence_de": "Wir brauchen präzise Messungen.", "sentence_en": "We need precise measurements."},
    {"word": "berührend", "translation": "touching", "sentence_de": "Die Geschichte war sehr berührend.", "sentence_en": "The story was very touching."},
    {"word": "planmäßig", "translation": "according to plan", "sentence_de": "Der Zug kam planmäßig an.", "sentence_en": "The train arrived according to plan."},
    {"word": "mobil", "translation": "mobile", "sentence_de": "Im Alter mobil zu bleiben ist wichtig.", "sentence_en": "Staying mobile in old age is important."}
]

# Session 8
session_8 = [
    {"word": "erreichen (hat erreicht)", "translation": "to reach / to achieve", "verb_forms": "Präteritum: erreichte, Perfekt: hat erreicht", "sentence_de": "Wir wollen unser Umsatzziel erreichen.", "sentence_en": "We want to reach our sales target."},
    {"word": "delegieren (hat delegiert)", "translation": "to delegate", "verb_forms": "Präteritum: delegierte, Perfekt: hat delegiert", "sentence_de": "Ein guter Manager muss Aufgaben delegieren können.", "sentence_en": "A good manager must be able to delegate tasks."},
    {"word": "ankommen (ist angekommen)", "translation": "to arrive", "verb_forms": "Präteritum: kam an, Perfekt: ist angekommen", "sentence_de": "Wann kommen wir in Berlin an?", "sentence_en": "When do we arrive in Berlin?"},
    {"word": "konkret", "translation": "concrete / specific", "sentence_de": "Haben Sie einen konkreten Vorschlag?", "sentence_en": "Do you have a concrete proposal?"},
    {"word": "ausschalten (hat ausgeschaltet)", "translation": "to switch off", "verb_forms": "Präteritum: schaltete aus, Perfekt: hat ausgeschaltet", "sentence_de": "Bitte schalten Sie Ihre Handys aus.", "sentence_en": "Please switch off your mobile phones."},
    {"word": "geplant", "translation": "planned", "sentence_de": "Der Ausflug ist für Samstag geplant.", "sentence_en": "The trip is planned for Saturday."},
    {"word": "abnehmen (hat abgenommen)", "translation": "to decrease / to lose weight", "verb_forms": "Präteritum: nahm ab, Perfekt: hat abgenommen", "sentence_de": "Ich möchte fünf Kilo abnehmen.", "sentence_en": "I would like to lose five kilos."},
    {"word": "weiterbilden (hat weitergebildet)", "translation": "to continue education", "verb_forms": "Präteritum: bildete weiter, Perfekt: hat weitergebildet", "sentence_de": "Man sollte sich ständig weiterbilden.", "sentence_en": "One should constantly educate oneself further."},
    {"word": "musikalisch", "translation": "musical", "sentence_de": "Er ist sehr musikalisch und spielt drei Instrumente.", "sentence_en": "He is very musical and plays three instruments."},
    {"word": "aktiv", "translation": "active", "sentence_de": "Sie ist auch im hohen Alter noch sehr aktiv.", "sentence_en": "She is still very active even at an old age."},
    {"word": "langwierig", "translation": "lengthy / tedious", "sentence_de": "Es war ein langwieriger Prozess.", "sentence_en": "It was a lengthy process."},
    {"word": "abenteuerlich", "translation": "adventurous", "sentence_de": "Die Fahrt über die Berge war abenteuerlich.", "sentence_en": "The drive over the mountains was adventurous."},
    {"word": "abschließen (hat abgeschlossen)", "translation": "to lock / to complete", "verb_forms": "Präteritum: schloss ab, Perfekt: hat abgeschlossen", "sentence_de": "Haben Sie die Tür abgeschlossen?", "sentence_en": "Did you lock the door?"},
    {"word": "zertifizieren (hat zertifiziert)", "translation": "to certify", "verb_forms": "Präteritum: zertifizierte, Perfekt: hat zertifiziert", "sentence_de": "Das Unternehmen ist ISO-zertifiziert.", "sentence_en": "The company is ISO certified."},
    {"word": "beeindruckend", "translation": "impressive", "sentence_de": "Das Ergebnis ist wirklich beeindruckend.", "sentence_en": "The result is truly impressive."},
    {"word": "vorbeugen (hat vorgebeugt)", "translation": "to prevent / to bend forward", "verb_forms": "Präteritum: beugte vor, Perfekt: hat vorgebeugt", "sentence_de": "Gesunde Ernährung hilft, Krankheiten vorzubeugen.", "sentence_en": "Healthy eating helps to prevent diseases."},
    {"word": "abwechslungsreich", "translation": "varied", "sentence_de": "Meine Arbeit ist sehr abwechslungsreich.", "sentence_en": "My work is very varied."},
    {"word": "unterstützen (hat unterstützt)", "translation": "to support", "verb_forms": "Präteritum: unterstützte, Perfekt: hat unterstützt", "sentence_de": "Wir unterstützen Sie gerne bei Ihrem Projekt.", "sentence_en": "We are happy to support you with your project."},
    {"word": "Zusammenspiel", "translation": "interaction / interplay", "sentence_de": "Das Zusammenspiel der Instrumente war perfekt.", "sentence_en": "The interplay of the instruments was perfect."},
    {"word": "mutig", "translation": "brave", "sentence_de": "Das war eine sehr mutige Entscheidung.", "sentence_en": "That was a very brave decision."}
]

if __name__ == "__main__":
    write_session(1, session_1)
    write_session(2, session_2)
    write_session(3, session_3)
    write_session(4, session_4)
    write_session(5, session_5)
    write_session(6, session_6)
    write_session(7, session_7)
    write_session(8, session_8)

# Session 9
session_9 = [
    {"word": "entwerfen (hat entworfen)", "translation": "to design / to draft", "verb_forms": "Präteritum: entwarf, Perfekt: hat entworfen", "sentence_de": "Der Architekt entwirft einen Plan für das neue Gebäude.", "sentence_en": "The architect is designing a plan for the new building."},
    {"word": "relevant", "translation": "relevant", "sentence_de": "Diese Information ist für uns sehr relevant.", "sentence_en": "This information is very relevant for us."},
    {"word": "vorschreiben (hat vorgeschrieben)", "translation": "to prescribe / to stipulate", "verb_forms": "Präteritum: schrieb vor, Perfekt: hat vorgeschrieben", "sentence_de": "Das Gesetz schreibt bestimmte Sicherheitsstandards vor.", "sentence_en": "The law prescribes certain safety standards."},
    {"word": "konsumieren (hat konsumiert)", "translation": "to consume", "verb_forms": "Präteritum: konsumierte, Perfekt: hat konsumiert", "sentence_de": "Jugendliche konsumieren heute mehr Medien als früher.", "sentence_en": "Teenagers consume more media today than in the past."},
    {"word": "transferieren (hat transferiert)", "translation": "to transfer", "verb_forms": "Präteritum: transferierte, Perfekt: hat transferiert", "sentence_de": "Der Spieler wurde zu einem anderen Verein transferiert.", "sentence_en": "The player was transferred to another club."},
    {"word": "einzigartig", "translation": "unique", "sentence_de": "Das ist eine einzigartige Gelegenheit.", "sentence_en": "That is a unique opportunity."},
    {"word": "danebenliegen (hat danebengelegen)", "translation": "to be wrong / to be off the mark", "verb_forms": "Präteritum: lag daneben, Perfekt: hat danebengelegen", "sentence_de": "Mit seiner Schätzung lag er völlig daneben.", "sentence_en": "He was completely off with his estimate."},
    {"word": "qualifiziert", "translation": "qualified", "sentence_de": "Wir suchen qualifiziertes Personal.", "sentence_en": "We are looking for qualified personnel."},
    {"word": "perfekt", "translation": "perfect", "sentence_de": "Niemand ist perfekt.", "sentence_en": "Nobody is perfect."},
    {"word": "kurzfristig", "translation": "short-term / on short notice", "sentence_de": "Wir mussten das Treffen kurzfristig absagen.", "sentence_en": "We had to cancel the meeting on short notice."},
    {"word": "kooperieren (hat kooperiert)", "translation": "to cooperate", "verb_forms": "Präteritum: kooperierte, Perfekt: hat kooperiert", "sentence_de": "Die beiden Firmen kooperieren eng miteinander.", "sentence_en": "The two companies cooperate closely with each other."},
    {"word": "proaktiv", "translation": "proactive", "sentence_de": "Wir müssen proaktiv handeln, um Probleme zu vermeiden.", "sentence_en": "We must act proactively to avoid problems."},
    {"word": "leidenschaftlich", "translation": "passionate", "sentence_de": "Sie ist eine leidenschaftliche Tänzerin.", "sentence_en": "She is a passionate dancer."},
    {"word": "dramatisch", "translation": "dramatic", "sentence_de": "Die Situation hat sich dramatisch verschlechtert.", "sentence_en": "The situation has deteriorated dramatically."},
    {"word": "ausleihen (hat ausgeliehen)", "translation": "to borrow / to lend", "verb_forms": "Präteritum: lieh aus, Perfekt: hat ausgeliehen", "sentence_de": "Kann ich mir deinen Stift ausleihen?", "sentence_en": "Can I borrow your pen?"},
    {"word": "gestalten (hat gestaltet)", "translation": "to design / to shape", "verb_forms": "Präteritum: gestaltete, Perfekt: hat gestaltet", "sentence_de": "Wir wollen unsere Zukunft aktiv gestalten.", "sentence_en": "We want to actively shape our future."},
    {"word": "aufführen (hat aufgeführt)", "translation": "to perform / to list", "verb_forms": "Präteritum: führte auf, Perfekt: hat aufgeführt", "sentence_de": "Das Theaterstück wird heute Abend aufgeführt.", "sentence_en": "The play is being performed tonight."},
    {"word": "aktualisieren (hat aktualisiert)", "translation": "to update", "verb_forms": "Präteritum: aktualisierte, Perfekt: hat aktualisiert", "sentence_de": "Bitte aktualisieren Sie Ihre Software.", "sentence_en": "Please update your software."},
    {"word": "positiv", "translation": "positive", "sentence_de": "Er hat eine sehr positive Einstellung.", "sentence_en": "He has a very positive attitude."},
    {"word": "ich", "translation": "I", "sentence_de": "Ich bin müde.", "sentence_en": "I am tired."}
]

# Session 10
session_10 = [
    {"word": "sie", "translation": "she / they", "sentence_de": "Sie geht heute ins Kino.", "sentence_en": "She is going to the cinema today."},
    {"word": "das", "translation": "the / that", "sentence_de": "Das ist ein schönes Haus.", "sentence_en": "That is a beautiful house."},
    {"word": "ist", "translation": "is", "sentence_de": "Das Wetter ist heute gut.", "sentence_en": "The weather is good today."},
    {"word": "du", "translation": "you (informal)", "sentence_de": "Kommst du mit?", "sentence_en": "Are you coming along?"},
    {"word": "nicht", "translation": "not", "sentence_de": "Ich weiß es nicht.", "sentence_en": "I do not know."},
    {"word": "die", "translation": "the", "sentence_de": "Die Sonne scheint.", "sentence_en": "The sun is shining."},
    {"word": "es", "translation": "it", "sentence_de": "Es regnet.", "sentence_en": "It is raining."},
    {"word": "und", "translation": "and", "sentence_de": "Ich mag Kaffee und Kuchen.", "sentence_en": "I like coffee and cake."},
    {"word": "der", "translation": "the", "sentence_de": "Der Mann wartet auf den Bus.", "sentence_en": "The man is waiting for the bus."},
    {"word": "wir", "translation": "we", "sentence_de": "Wir fahren in den Urlaub.", "sentence_en": "We are going on vacation."},
    {"word": "was", "translation": "what", "sentence_de": "Was machst du?", "sentence_en": "What are you doing?"},
    {"word": "er", "translation": "he", "sentence_de": "Er spielt Fußball.", "sentence_en": "He is playing football."},
    {"word": "ein", "translation": "a / an", "sentence_de": "Das ist ein Apfel.", "sentence_en": "That is an apple."},
    {"word": "in", "translation": "in", "sentence_de": "Wir wohnen in Berlin.", "sentence_en": "We live in Berlin."},
    {"word": "mir", "translation": "me (dative)", "sentence_de": "Kannst du mir helfen?", "sentence_en": "Can you help me?"},
    {"word": "mit", "translation": "with", "sentence_de": "Ich gehe mit meinem Freund ins Kino.", "sentence_en": "I am going to the cinema with my friend."},
    {"word": "ja", "translation": "yes", "sentence_de": "Ja, ich komme gerne.", "sentence_en": "Yes, I'd love to come."},
    {"word": "den", "translation": "the (accusative)", "sentence_de": "Ich sehe den Hund.", "sentence_en": "I see the dog."},
    {"word": "wie", "translation": "how / like", "sentence_de": "Wie geht es dir?", "sentence_en": "How are you?"},
    {"word": "mich", "translation": "me (accusative)", "sentence_de": "Er liebt mich.", "sentence_en": "He loves me."}
]

# Session 11
session_11 = [
    {"word": "auf", "translation": "on / up", "sentence_de": "Das Buch liegt auf dem Tisch.", "sentence_en": "The book is on the table."},
    {"word": "dass", "translation": "that (conjunction)", "sentence_de": "Ich weiß, dass du recht hast.", "sentence_en": "I know that you are right."},
    {"word": "eine", "translation": "a / one (feminine)", "sentence_de": "Sie hat eine Katze.", "sentence_en": "She has a cat."},
    {"word": "aber", "translation": "but", "sentence_de": "Ich bin müde, aber glücklich.", "sentence_en": "I am tired but happy."},
    {"word": "so", "translation": "so / like this", "sentence_de": "Warum bist du so traurig?", "sentence_en": "Why are you so sad?"},
    {"word": "hat", "translation": "has", "sentence_de": "Er hat ein neues Auto.", "sentence_en": "He has a new car."},
    {"word": "haben", "translation": "to have", "sentence_de": "Wir haben viel zu tun.", "sentence_en": "We have a lot to do."},
    {"word": "sind", "translation": "are", "sentence_de": "Wir sind Freunde.", "sentence_en": "We are friends."},
    {"word": "für", "translation": "for", "sentence_de": "Das Geschenk ist für dich.", "sentence_en": "The gift is for you."},
    {"word": "von", "translation": "from / of", "sentence_de": "Das ist das Buch von Peter.", "sentence_en": "That is Peter's book."},
    {"word": "dich", "translation": "you (accusative)", "sentence_de": "Ich liebe dich.", "sentence_en": "I love you."},
    {"word": "war", "translation": "was", "sentence_de": "Gestern war es kalt.", "sentence_en": "Yesterday it was cold."},
    {"word": "wenn", "translation": "if / when", "sentence_de": "Wenn es regnet, bleiben wir zu Hause.", "sentence_en": "If it rains, we stay at home."},
    {"word": "ihr", "translation": "you (plural) / her", "sentence_de": "Habt ihr Zeit?", "sentence_en": "Do you have time?"},
    {"word": "habe", "translation": "have (1st person)", "sentence_de": "Ich habe Hunger.", "sentence_en": "I am hungry."},
    {"word": "nein", "translation": "no", "sentence_de": "Nein, danke.", "sentence_en": "No, thank you."},
    {"word": "an", "translation": "at / on", "sentence_de": "Das Bild hängt an der Wand.", "sentence_en": "The picture hangs on the wall."},
    {"word": "bin", "translation": "am", "sentence_de": "Ich bin Arzt.", "sentence_en": "I am a doctor."},
    {"word": "noch", "translation": "still / yet", "sentence_de": "Bist du noch wach?", "sentence_en": "Are you still awake?"},
    {"word": "dir", "translation": "you (dative)", "sentence_de": "Ich gebe dir das Buch.", "sentence_en": "I give you the book."}
]

# Session 12
session_12 = [
    {"word": "einen", "translation": "a / an (accusative)", "sentence_de": "Ich möchte einen Kaffee.", "sentence_en": "I would like a coffee."},
    {"word": "sich", "translation": "oneself / each other", "sentence_de": "Er freut sich auf den Urlaub.", "sentence_en": "He is looking forward to the vacation."},
    {"word": "uns", "translation": "us", "sentence_de": "Besuch uns bald mal wieder.", "sentence_en": "Visit us again soon."},
    {"word": "hast", "translation": "have (2nd person)", "sentence_de": "Hast du Geschwister?", "sentence_en": "Do you have siblings?"},
    {"word": "dem", "translation": "the (dative)", "sentence_de": "Ich gehe mit dem Hund spazieren.", "sentence_en": "I am walking the dog."},
    {"word": "kann", "translation": "can", "sentence_de": "Ich kann schwimmen.", "sentence_en": "I can swim."},
    {"word": "sein", "translation": "his / to be", "sentence_de": "Das ist sein Auto.", "sentence_en": "That is his car."},
    {"word": "ihn", "translation": "him", "sentence_de": "Ich kenne ihn gut.", "sentence_en": "I know him well."},
    {"word": "schon", "translation": "already", "sentence_de": "Bist du schon fertig?", "sentence_en": "Are you already finished?"},
    {"word": "als", "translation": "as / than / when", "sentence_de": "Er ist größer als ich.", "sentence_en": "He is taller than me."},
    {"word": "mal", "translation": "times / once", "sentence_de": "Sag das noch mal.", "sentence_en": "Say that again."},
    {"word": "aus", "translation": "out / from", "sentence_de": "Er kommt aus Deutschland.", "sentence_en": "He comes from Germany."},
    {"word": "um", "translation": "around / at", "sentence_de": "Der Termin ist um 14 Uhr.", "sentence_en": "The meeting is at 2 pm."},
    {"word": "meine", "translation": "my", "sentence_de": "Das ist meine Mutter.", "sentence_en": "That is my mother."},
    {"word": "dann", "translation": "then", "sentence_de": "Erst essen wir, dann gehen wir spazieren.", "sentence_en": "First we eat, then we go for a walk."},
    {"word": "wird", "translation": "will / becomes", "sentence_de": "Es wird dunkel.", "sentence_en": "It is getting dark."},
    {"word": "im", "translation": "in the", "sentence_de": "Wir sind im Kino.", "sentence_en": "We are in the cinema."},
    {"word": "bist", "translation": "are (2nd person)", "sentence_de": "Du bist mein bester Freund.", "sentence_en": "You are my best friend."},
    {"word": "mein", "translation": "my", "sentence_de": "Das ist mein Buch.", "sentence_en": "That is my book."},
    {"word": "doch", "translation": "however / but / yes (contradiction)", "sentence_de": "Du kommst doch, oder?", "sentence_en": "You are coming, aren't you?"}
]

if __name__ == "__main__":
    write_session(1, session_1)
    write_session(2, session_2)
    write_session(3, session_3)
    write_session(4, session_4)
    write_session(5, session_5)
    write_session(6, session_6)
    write_session(7, session_7)
    write_session(8, session_8)
    write_session(9, session_9)
    write_session(10, session_10)
    write_session(11, session_11)
    write_session(12, session_12)

# Session 13
session_13 = [
    {"word": "keine", "translation": "no / none", "sentence_de": "Ich habe keine Zeit.", "sentence_en": "I have no time."},
    {"word": "weiß", "translation": "know / white", "sentence_de": "Ich weiß es nicht.", "sentence_en": "I don't know."},
    {"word": "oder", "translation": "or", "sentence_de": "Kaffee oder Tee?", "sentence_en": "Coffee or tea?"},
    {"word": "nach", "translation": "after / to", "sentence_de": "Wir fahren nach Hause.", "sentence_en": "We are driving home."},
    {"word": "wo", "translation": "where", "sentence_de": "Wo wohnst du?", "sentence_en": "Where do you live?"},
    {"word": "ihnen", "translation": "them (dative) / You (formal)", "sentence_de": "Ich gebe Ihnen meine Nummer.", "sentence_en": "I give you my number."},
    {"word": "etwas", "translation": "something", "sentence_de": "Möchtest du etwas essen?", "sentence_en": "Would you like to eat something?"},
    {"word": "muss", "translation": "must / have to", "sentence_de": "Ich muss jetzt gehen.", "sentence_en": "I have to go now."},
    {"word": "will", "translation": "want", "sentence_de": "Ich will ein Eis.", "sentence_en": "I want an ice cream."},
    {"word": "geht", "translation": "goes / works", "sentence_de": "Wie geht es dir?", "sentence_en": "How are you?"},
    {"word": "oh", "translation": "oh", "sentence_de": "Oh, das tut mir leid.", "sentence_en": "Oh, I am sorry."},
    {"word": "also", "translation": "so / therefore", "sentence_de": "Also, was machen wir jetzt?", "sentence_en": "So, what are we doing now?"},
    {"word": "bei", "translation": "at / with", "sentence_de": "Er wohnt bei seinen Eltern.", "sentence_en": "He lives with his parents."},
    {"word": "warum", "translation": "why", "sentence_de": "Warum weinst du?", "sentence_en": "Why are you crying?"},
    {"word": "hab", "translation": "have (colloquial)", "sentence_de": "Hab dich lieb.", "sentence_en": "Love you."},
    {"word": "vor", "translation": "before / in front of", "sentence_de": "Wir treffen uns vor dem Kino.", "sentence_en": "We meet in front of the cinema."},
    {"word": "los", "translation": "go / loose", "sentence_de": "Was ist los?", "sentence_en": "What is going on?"},
    {"word": "machen (hat gemacht)", "translation": "to make / to do", "verb_forms": "Präteritum: machte, Perfekt: hat gemacht", "sentence_de": "Was machst du heute?", "sentence_en": "What are you doing today?"},
    {"word": "alle", "translation": "all / everyone", "sentence_de": "Alle sind da.", "sentence_en": "Everyone is here."},
    {"word": "Mann", "translation": "man / husband", "sentence_de": "Das ist mein Mann.", "sentence_en": "That is my husband."}
]

# Session 14
session_14 = [
    {"word": "okay", "translation": "okay", "sentence_de": "Ist das okay für dich?", "sentence_en": "Is that okay for you?"},
    {"word": "gehen (ist gegangen)", "translation": "to go / to walk", "verb_forms": "Präteritum: ging, Perfekt: ist gegangen", "sentence_de": "Wir gehen in den Park.", "sentence_en": "We are going to the park."},
    {"word": "denn", "translation": "because / then (particle)", "sentence_de": "Was hast du denn gemacht?", "sentence_en": "What have you done then?"},
    {"word": "zum", "translation": "to the", "sentence_de": "Ich gehe zum Arzt.", "sentence_en": "I am going to the doctor."},
    {"word": "tun (hat getan)", "translation": "to do", "verb_forms": "Präteritum: tat, Perfekt: hat getan", "sentence_de": "Es tut mir leid.", "sentence_en": "I am sorry."},
    {"word": "ihm", "translation": "him (dative)", "sentence_de": "Ich helfe ihm.", "sentence_en": "I am helping him."},
    {"word": "diese", "translation": "this / these", "sentence_de": "Diese Schuhe sind schön.", "sentence_en": "These shoes are beautiful."},
    {"word": "danke", "translation": "thank you", "sentence_de": "Danke für deine Hilfe.", "sentence_en": "Thank you for your help."},
    {"word": "wer", "translation": "who", "sentence_de": "Wer ist das?", "sentence_en": "Who is that?"},
    {"word": "einem", "translation": "a / an (dative)", "sentence_de": "Ich wohne in einem Haus.", "sentence_en": "I live in a house."},
    {"word": "euch", "translation": "you (plural dative/accusative)", "sentence_de": "Ich sehe euch.", "sentence_en": "I see you."},
    {"word": "komm", "translation": "come (imperative)", "sentence_de": "Komm schnell!", "sentence_en": "Come quickly!"},
    {"word": "einer", "translation": "one (pronoun)", "sentence_de": "Einer von uns muss gehen.", "sentence_en": "One of us has to go."},
    {"word": "ihre", "translation": "her / their", "sentence_de": "Das ist ihre Tasche.", "sentence_en": "That is her bag."},
    {"word": "werde", "translation": "will / become (1st person)", "sentence_de": "Ich werde Arzt.", "sentence_en": "I will become a doctor."},
    {"word": "gibt", "translation": "gives", "sentence_de": "Es gibt viele Probleme.", "sentence_en": "There are many problems."},
    {"word": "über", "translation": "over / about", "sentence_de": "Wir sprechen über das Wetter.", "sentence_en": "We are talking about the weather."},
    {"word": "deine", "translation": "your", "sentence_de": "Wo ist deine Brille?", "sentence_en": "Where are your glasses?"},
    {"word": "müssen", "translation": "must / to have to", "sentence_de": "Wir müssen jetzt gehen.", "sentence_en": "We have to go now."},
    {"word": "wirklich", "translation": "really", "sentence_de": "Das ist wirklich schön.", "sentence_en": "That is really beautiful."}
]

# Session 15
session_15 = [
    {"word": "soll", "translation": "should", "sentence_de": "Was soll ich tun?", "sentence_en": "What should I do?"},
    {"word": "weg", "translation": "away / gone", "sentence_de": "Er ist weg.", "sentence_en": "He is gone."},
    {"word": "hey", "translation": "hey", "sentence_de": "Hey, wie geht's?", "sentence_en": "Hey, how are you?"},
    {"word": "kein", "translation": "no / none", "sentence_de": "Ich habe kein Geld.", "sentence_en": "I have no money."},
    {"word": "des", "translation": "of the (genitive)", "sentence_de": "Das Haus des Vaters.", "sentence_en": "The father's house."},
    {"word": "würde", "translation": "would", "sentence_de": "Ich würde gerne kommen.", "sentence_en": "I would like to come."},
    {"word": "am", "translation": "at the", "sentence_de": "Ich warte am Bahnhof.", "sentence_en": "I am waiting at the station."},
    {"word": "tut", "translation": "does", "sentence_de": "Das tut weh.", "sentence_en": "That hurts."},
    {"word": "willst", "translation": "want (2nd person)", "sentence_de": "Willst du essen?", "sentence_en": "Do you want to eat?"},
    {"word": "kommen (ist gekommen)", "translation": "to come", "verb_forms": "Präteritum: kam, Perfekt: ist gekommen", "sentence_de": "Wann kommst du?", "sentence_en": "When are you coming?"},
    {"word": "Zeit", "translation": "time", "sentence_de": "Ich habe keine Zeit.", "sentence_en": "I have no time."},
    {"word": "nun", "translation": "now", "sentence_de": "Was machen wir nun?", "sentence_en": "What do we do now?"},
    {"word": "hatte", "translation": "had", "sentence_de": "Ich hatte keine Zeit.", "sentence_en": "I had no time."},
    {"word": "dein", "translation": "your", "sentence_de": "Ist das dein Auto?", "sentence_en": "Is that your car?"},
    {"word": "weil", "translation": "because", "sentence_de": "Ich esse, weil ich Hunger habe.", "sentence_en": "I eat because I am hungry."},
    {"word": "kommt", "translation": "comes", "sentence_de": "Er kommt morgen.", "sentence_en": "He is coming tomorrow."},
    {"word": "wollen", "translation": "want", "sentence_de": "Wir wollen ins Kino.", "sentence_en": "We want to go to the cinema."},
    {"word": "weißt", "translation": "know (2nd person)", "sentence_de": "Weißt du die Antwort?", "sentence_en": "Do you know the answer?"},
    {"word": "damit", "translation": "with it / so that", "sentence_de": "Was machst du damit?", "sentence_en": "What are you doing with it?"},
    {"word": "Frau", "translation": "woman / wife / Mrs.", "sentence_de": "Das ist meine Frau.", "sentence_en": "That is my wife."}
]

# Session 16
session_16 = [
    {"word": "gesagt", "translation": "said", "sentence_de": "Er hat nichts gesagt.", "sentence_en": "He said nothing."},
    {"word": "wäre", "translation": "would be", "sentence_de": "Das wäre schön.", "sentence_en": "That would be nice."},
    {"word": "ganz", "translation": "whole / quite", "sentence_de": "Das war ganz gut.", "sentence_en": "That was quite good."},
    {"word": "wurde", "translation": "became / was", "sentence_de": "Er wurde Arzt.", "sentence_en": "He became a doctor."},
    {"word": "bis", "translation": "until", "sentence_de": "Bis morgen!", "sentence_en": "Until tomorrow!"},
    {"word": "kannst", "translation": "can (2nd person)", "sentence_de": "Kannst du mir helfen?", "sentence_en": "Can you help me?"},
    {"word": "zurück", "translation": "back", "sentence_de": "Wann kommst du zurück?", "sentence_en": "When are you coming back?"},
    {"word": "dieser", "translation": "this (masculine)", "sentence_de": "Dieser Mann ist mein Vater.", "sentence_en": "This man is my father."},
    {"word": "wollte", "translation": "wanted", "sentence_de": "Ich wollte dich anrufen.", "sentence_en": "I wanted to call you."},
    {"word": "Leid", "translation": "suffering / harm", "sentence_de": "Es tut mir leid.", "sentence_en": "I am sorry."},
    {"word": "lassen (hat gelassen)", "translation": "to let / to leave", "verb_forms": "Präteritum: ließ, Perfekt: hat gelassen", "sentence_de": "Lass mich in Ruhe.", "sentence_en": "Leave me alone."},
    {"word": "macht", "translation": "makes / does", "sentence_de": "Das macht nichts.", "sentence_en": "That doesn't matter."},
    {"word": "na", "translation": "well", "sentence_de": "Na, wie geht's?", "sentence_en": "Well, how are you?"},
    {"word": "Gott", "translation": "God", "sentence_de": "Oh mein Gott!", "sentence_en": "Oh my God!"},
    {"word": "hallo", "translation": "hello", "sentence_de": "Hallo, wie geht es dir?", "sentence_en": "Hello, how are you?"},
    {"word": "seine", "translation": "his", "sentence_de": "Das ist seine Tasche.", "sentence_en": "That is his bag."},
    {"word": "zwei", "translation": "two", "sentence_de": "Ich habe zwei Katzen.", "sentence_en": "I have two cats."},
    {"word": "lass", "translation": "let (imperative)", "sentence_de": "Lass das!", "sentence_en": "Stop that!"},
    {"word": "hätte", "translation": "would have", "sentence_de": "Ich hätte gerne ein Wasser.", "sentence_en": "I would like a water."},
    {"word": "zur", "translation": "to the (feminine)", "sentence_de": "Ich gehe zur Schule.", "sentence_en": "I am going to school."}
]

if __name__ == "__main__":
    write_session(1, session_1)
    write_session(2, session_2)
    write_session(3, session_3)
    write_session(4, session_4)
    write_session(5, session_5)
    write_session(6, session_6)
    write_session(7, session_7)
    write_session(8, session_8)
    write_session(9, session_9)
    write_session(10, session_10)
    write_session(11, session_11)
    write_session(12, session_12)
    write_session(13, session_13)
    write_session(14, session_14)
    write_session(15, session_15)
    write_session(16, session_16)

# Session 17
session_17 = [
    {"word": "waren", "translation": "were", "sentence_de": "Wir waren gestern im Kino.", "sentence_en": "We were at the cinema yesterday."},
    {"word": "genau", "translation": "exactly", "sentence_de": "Das ist genau das, was ich wollte.", "sentence_en": "That is exactly what I wanted."},
    {"word": "könnte", "translation": "could", "sentence_de": "Das könnte wahr sein.", "sentence_en": "That could be true."},
    {"word": "Vater", "translation": "father", "sentence_de": "Mein Vater arbeitet bei der Bank.", "sentence_en": "My father works at the bank."},
    {"word": "Leute", "translation": "people", "sentence_de": "Viele Leute warten auf den Bus.", "sentence_en": "Many people are waiting for the bus."},
    {"word": "klar", "translation": "clear / sure", "sentence_de": "Ist das klar?", "sentence_en": "Is that clear?"},
    {"word": "ok", "translation": "okay", "sentence_de": "Alles ok?", "sentence_en": "Everything okay?"},
    {"word": "ab", "translation": "from / off", "sentence_de": "Ab morgen mache ich Diät.", "sentence_en": "Starting tomorrow I am on a diet."},
    {"word": "Tag", "translation": "day", "sentence_de": "Guten Tag!", "sentence_en": "Good day!"},
    {"word": "gerade", "translation": "just / straight", "sentence_de": "Ich bin gerade angekommen.", "sentence_en": "I have just arrived."},
    {"word": "gesehen", "translation": "seen", "sentence_de": "Hast du den Film gesehen?", "sentence_en": "Have you seen the movie?"},
    {"word": "glaube", "translation": "believe", "sentence_de": "Ich glaube dir.", "sentence_en": "I believe you."},
    {"word": "Liebe", "translation": "love", "sentence_de": "Liebe ist alles.", "sentence_en": "Love is everything."},
    {"word": "Geld", "translation": "money", "sentence_de": "Ich habe kein Geld.", "sentence_en": "I have no money."},
    {"word": "durch", "translation": "through", "sentence_de": "Wir gehen durch den Wald.", "sentence_en": "We go through the forest."},
    {"word": "reden (hat geredet)", "translation": "to talk", "verb_forms": "Präteritum: redete, Perfekt: hat geredet", "sentence_de": "Wir müssen reden.", "sentence_en": "We need to talk."},
    {"word": "unsere", "translation": "our", "sentence_de": "Das ist unsere Katze.", "sentence_en": "That is our cat."},
    {"word": "mach", "translation": "make / do (imperative)", "sentence_de": "Mach das Fenster zu.", "sentence_en": "Close the window."},
    {"word": "raus", "translation": "out", "sentence_de": "Geh raus!", "sentence_en": "Get out!"},
    {"word": "sagte", "translation": "said", "sentence_de": "Er sagte ja.", "sentence_en": "He said yes."}
]

# Session 18
session_18 = [
    {"word": "keinen", "translation": "no / none (accusative)", "sentence_de": "Ich habe keinen Hunger.", "sentence_en": "I am not hungry."},
    {"word": "ob", "translation": "whether / if", "sentence_de": "Ich weiß nicht, ob er kommt.", "sentence_en": "I don't know if he is coming."},
    {"word": "sollte", "translation": "should", "sentence_de": "Du solltest zum Arzt gehen.", "sentence_en": "You should go to the doctor."},
    {"word": "gemacht", "translation": "made / done", "sentence_de": "Das hast du gut gemacht.", "sentence_en": "You did that well."},
    {"word": "Mutter", "translation": "mother", "sentence_de": "Meine Mutter ist Lehrerin.", "sentence_en": "My mother is a teacher."},
    {"word": "dieses", "translation": "this (neuter)", "sentence_de": "Dieses Buch ist interessant.", "sentence_en": "This book is interesting."},
    {"word": "Paar", "translation": "pair / couple", "sentence_de": "Ein Paar Schuhe.", "sentence_en": "A pair of shoes."},
    {"word": "Sir", "translation": "Sir", "sentence_de": "Ja, Sir.", "sentence_en": "Yes, Sir."},
    {"word": "passiert", "translation": "happened", "sentence_de": "Was ist passiert?", "sentence_en": "What happened?"},
    {"word": "musst", "translation": "must (2nd person)", "sentence_de": "Du musst lernen.", "sentence_en": "You must study."},
    {"word": "wohl", "translation": "probably / well", "sentence_de": "Das ist wohl wahr.", "sentence_en": "That is probably true."},
    {"word": "möchte", "translation": "would like", "sentence_de": "Ich möchte ein Bier.", "sentence_en": "I would like a beer."},
    {"word": "besser", "translation": "better", "sentence_de": "Heute geht es mir besser.", "sentence_en": "I feel better today."},
    {"word": "dachte", "translation": "thought", "sentence_de": "Ich dachte, du bist krank.", "sentence_en": "I thought you were sick."},
    {"word": "selbst", "translation": "self / even", "sentence_de": "Ich habe es selbst gemacht.", "sentence_en": "I did it myself."},
    {"word": "her", "translation": "here (direction)", "sentence_de": "Komm her!", "sentence_en": "Come here!"},
    {"word": "hör", "translation": "hear / listen (imperative)", "sentence_de": "Hör mir zu!", "sentence_en": "Listen to me!"},
    {"word": "gehört", "translation": "belongs / heard", "sentence_de": "Das gehört mir.", "sentence_en": "That belongs to me."},
    {"word": "wirst", "translation": "will (2nd person)", "sentence_de": "Du wirst es schaffen.", "sentence_en": "You will make it."},
    {"word": "sag", "translation": "say (imperative)", "sentence_de": "Sag mir die Wahrheit.", "sentence_en": "Tell me the truth."}
]

# Session 19
session_19 = [
    {"word": "ohne", "translation": "without", "sentence_de": "Ich trinke Kaffee ohne Zucker.", "sentence_en": "I drink coffee without sugar."},
    {"word": "Nacht", "translation": "night", "sentence_de": "Gute Nacht!", "sentence_en": "Good night!"},
    {"word": "diesen", "translation": "this (accusative)", "sentence_de": "Ich möchte diesen Pullover.", "sentence_en": "I would like this sweater."},
    {"word": "anderen", "translation": "other", "sentence_de": "Ich nehme den anderen.", "sentence_en": "I'll take the other one."},
    {"word": "meiner", "translation": "mine / my (dative/genitive)", "sentence_de": "Das ist einer meiner Freunde.", "sentence_en": "That is one of my friends."},
    {"word": "wieso", "translation": "why / how come", "sentence_de": "Wieso fragst du?", "sentence_en": "Why do you ask?"},
    {"word": "helfen (hat geholfen)", "translation": "to help", "verb_forms": "Präteritum: half, Perfekt: hat geholfen", "sentence_de": "Kann ich dir helfen?", "sentence_en": "Can I help you?"},
    {"word": "meinem", "translation": "my (dative)", "sentence_de": "Ich gehe mit meinem Bruder.", "sentence_en": "I go with my brother."},
    {"word": "lange", "translation": "long", "sentence_de": "Wie lange bleibst du?", "sentence_en": "How long are you staying?"},
    {"word": "gute", "translation": "good", "sentence_de": "Gute Fahrt!", "sentence_en": "Have a good trip!"},
    {"word": "Ordnung", "translation": "order", "sentence_de": "Alles in Ordnung.", "sentence_en": "Everything is in order."},
    {"word": "weiter", "translation": "further / continue", "sentence_de": "Gehen wir weiter.", "sentence_en": "Let's move on."},
    {"word": "sei", "translation": "be (imperative)", "sentence_de": "Sei nicht traurig.", "sentence_en": "Don't be sad."},
    {"word": "ins", "translation": "into the", "sentence_de": "Wir gehen ins Kino.", "sentence_en": "We are going to the cinema."},
    {"word": "gar", "translation": "at all / even", "sentence_de": "Das schmeckt mir gar nicht.", "sentence_en": "I don't like the taste at all."},
    {"word": "geh", "translation": "go (imperative)", "sentence_de": "Geh weg!", "sentence_en": "Go away!"},
    {"word": "diesem", "translation": "this (dative)", "sentence_de": "Mit diesem Stift kann man nicht schreiben.", "sentence_en": "You can't write with this pen."},
    {"word": "vom", "translation": "from the", "sentence_de": "Ich komme vom Arzt.", "sentence_en": "I am coming from the doctor."},
    {"word": "sagt", "translation": "says", "sentence_de": "Er sagt nichts.", "sentence_en": "He says nothing."},
    {"word": "denke", "translation": "think", "sentence_de": "Ich denke an dich.", "sentence_en": "I am thinking of you."}
]

# Session 20
session_20 = [
    {"word": "seit", "translation": "since / for", "sentence_de": "Ich wohne seit drei Jahren hier.", "sentence_en": "I have been living here for three years."},
    {"word": "gleich", "translation": "same / immediately", "sentence_de": "Ich komme gleich.", "sentence_en": "I'm coming right away."},
    {"word": "ach", "translation": "oh", "sentence_de": "Ach so!", "sentence_en": "I see!"},
    {"word": "Mädchen", "translation": "girl", "sentence_de": "Das Mädchen spielt im Garten.", "sentence_en": "The girl is playing in the garden."},
    {"word": "davon", "translation": "of it / from it", "sentence_de": "Was hältst du davon?", "sentence_en": "What do you think of it?"},
    {"word": "sieht", "translation": "sees", "sentence_de": "Er sieht gut aus.", "sentence_en": "He looks good."},
    {"word": "ihren", "translation": "her / their (accusative)", "sentence_de": "Sie sucht ihren Schlüssel.", "sentence_en": "She is looking for her key."},
    {"word": "Recht", "translation": "right / law", "sentence_de": "Du hast Recht.", "sentence_en": "You are right."},
    {"word": "dafür", "translation": "for it", "sentence_de": "Ich bin dafür.", "sentence_en": "I am in favor of it."},
    {"word": "wegen", "translation": "because of", "sentence_de": "Wegen des Regens bleiben wir zu Hause.", "sentence_en": "Because of the rain we stay at home."},
    {"word": "Hause", "translation": "home", "sentence_de": "Ich bin zu Hause.", "sentence_en": "I am at home."},
    {"word": "hin", "translation": "there (direction)", "sentence_de": "Wo gehst du hin?", "sentence_en": "Where are you going?"},
    {"word": "warte", "translation": "wait", "sentence_de": "Warte auf mich!", "sentence_en": "Wait for me!"},
    {"word": "drei", "translation": "three", "sentence_de": "Ich habe drei Kinder.", "sentence_en": "I have three children."},
    {"word": "deinen", "translation": "your (accusative)", "sentence_de": "Iss deinen Teller leer.", "sentence_en": "Eat up your plate."},
    {"word": "Abend", "translation": "evening", "sentence_de": "Guten Abend!", "sentence_en": "Good evening!"},
    {"word": "Freund", "translation": "friend / boyfriend", "sentence_de": "Das ist mein bester Freund.", "sentence_en": "That is my best friend."},
    {"word": "guten", "translation": "good (accusative)", "sentence_de": "Guten Morgen!", "sentence_en": "Good morning!"},
    {"word": "sollen", "translation": "should", "sentence_de": "Wir sollen leise sein.", "sentence_en": "We should be quiet."},
    {"word": "sollten", "translation": "should (subjunctive)", "sentence_de": "Wir sollten gehen.", "sentence_en": "We should go."}
]

if __name__ == "__main__":
    write_session(1, session_1)
    write_session(2, session_2)
    write_session(3, session_3)
    write_session(4, session_4)
    write_session(5, session_5)
    write_session(6, session_6)
    write_session(7, session_7)
    write_session(8, session_8)
    write_session(9, session_9)
    write_session(10, session_10)
    write_session(11, session_11)
    write_session(12, session_12)
    write_session(13, session_13)
    write_session(14, session_14)
    write_session(15, session_15)
    write_session(16, session_16)
    write_session(17, session_17)
    write_session(18, session_18)
    write_session(19, session_19)
    write_session(20, session_20)

# Session 21
session_21 = [
    {"word": "Haus", "translation": "house", "sentence_de": "Wir haben ein Haus gekauft.", "sentence_en": "We bought a house."},
    {"word": "Menschen", "translation": "people / humans", "sentence_de": "Viele Menschen leben in Städten.", "sentence_en": "Many people live in cities."},
    {"word": "viele", "translation": "many", "sentence_de": "Ich habe viele Freunde.", "sentence_en": "I have many friends."},
    {"word": "bleiben (ist geblieben)", "translation": "to stay / to remain", "verb_forms": "Präteritum: blieb, Perfekt: ist geblieben", "sentence_de": "Bleibst du heute zu Hause?", "sentence_en": "Are you staying at home today?"},
    {"word": "machst", "translation": "make / do (2nd person)", "sentence_de": "Was machst du da?", "sentence_en": "What are you doing there?"},
    {"word": "Musik", "translation": "music", "sentence_de": "Ich höre gerne Musik.", "sentence_en": "I like listening to music."},
    {"word": "unser", "translation": "our", "sentence_de": "Das ist unser Haus.", "sentence_en": "That is our house."},
    {"word": "Angst", "translation": "fear", "sentence_de": "Ich habe keine Angst.", "sentence_en": "I have no fear."},
    {"word": "Welt", "translation": "world", "sentence_de": "Die Welt ist groß.", "sentence_en": "The world is big."},
    {"word": "habt", "translation": "have (2nd person plural)", "sentence_de": "Habt ihr Hunger?", "sentence_en": "Are you hungry?"},
    {"word": "unter", "translation": "under / among", "sentence_de": "Die Katze ist unter dem Tisch.", "sentence_en": "The cat is under the table."},
    {"word": "Scheiße", "translation": "shit", "sentence_de": "Verdammte Scheiße!", "sentence_en": "Damn it!"},
    {"word": "eines", "translation": "one / a (genitive)", "sentence_de": "Eines Tages werde ich reich sein.", "sentence_en": "One day I will be rich."},
    {"word": "Herr", "translation": "Mr. / gentleman", "sentence_de": "Guten Tag, Herr Müller.", "sentence_en": "Good day, Mr. Müller."},
    {"word": "andere", "translation": "other", "sentence_de": "Ich habe andere Pläne.", "sentence_en": "I have other plans."},
    {"word": "getan", "translation": "done", "sentence_de": "Ich habe nichts getan.", "sentence_en": "I haven't done anything."},
    {"word": "rein", "translation": "in / pure", "sentence_de": "Komm rein!", "sentence_en": "Come in!"},
    {"word": "ganze", "translation": "whole", "sentence_de": "Die ganze Zeit.", "sentence_en": "The whole time."},
    {"word": "Kinder", "translation": "children", "sentence_de": "Die Kinder spielen draußen.", "sentence_en": "The children are playing outside."},
    {"word": "genug", "translation": "enough", "sentence_de": "Ich habe genug.", "sentence_en": "I have enough."}
]

# Session 22
session_22 = [
    {"word": "darf", "translation": "may (1st/3rd person)", "sentence_de": "Darf ich reinkommen?", "sentence_en": "May I come in?"},
    {"word": "Junge", "translation": "boy", "sentence_de": "Der Junge spielt Fußball.", "sentence_en": "The boy is playing football."},
    {"word": "stimmt", "translation": "is correct / keep the change", "sentence_de": "Das stimmt.", "sentence_en": "That is correct."},
    {"word": "brauchen (hat gebraucht)", "translation": "to need", "verb_forms": "Präteritum: brauchte, Perfekt: hat gebraucht", "sentence_de": "Wir brauchen Hilfe.", "sentence_en": "We need help."},
    {"word": "gegen", "translation": "against / around (time)", "sentence_de": "Ich bin gegen Krieg.", "sentence_en": "I am against war."},
    {"word": "Moment", "translation": "moment", "sentence_de": "Einen Moment, bitte.", "sentence_en": "One moment, please."},
    {"word": "erst", "translation": "only / first", "sentence_de": "Es ist erst 8 Uhr.", "sentence_en": "It is only 8 o'clock."},
    {"word": "seid", "translation": "are (2nd person plural)", "sentence_de": "Seid ihr fertig?", "sentence_en": "Are you finished?"},
    {"word": "einmal", "translation": "once", "sentence_de": "Ich war schon einmal dort.", "sentence_en": "I have been there once."},
    {"word": "sonst", "translation": "otherwise / else", "sentence_de": "Beeil dich, sonst kommen wir zu spät.", "sentence_en": "Hurry up, otherwise we will be late."},
    {"word": "Arbeit", "translation": "work", "sentence_de": "Ich muss zur Arbeit.", "sentence_en": "I have to go to work."},
    {"word": "steht", "translation": "stands", "sentence_de": "Das Auto steht vor der Tür.", "sentence_en": "The car is standing in front of the door."},
    {"word": "dabei", "translation": "with it / there", "sentence_de": "Ich bin dabei.", "sentence_en": "I'm in."},
    {"word": "Jahre", "translation": "years", "sentence_de": "Er ist 20 Jahre alt.", "sentence_en": "He is 20 years old."},
    {"word": "halt", "translation": "just / simply", "sentence_de": "Das ist halt so.", "sentence_en": "That's just how it is."},
    {"word": "verdammt", "translation": "damn", "sentence_de": "Verdammt noch mal!", "sentence_en": "Damn it!"},
    {"word": "ihrer", "translation": "her / their (dative/genitive)", "sentence_de": "Er hilft ihrer Mutter.", "sentence_en": "He helps her mother."},
    {"word": "bevor", "translation": "before", "sentence_de": "Bevor wir gehen, essen wir.", "sentence_en": "Before we go, we eat."},
    {"word": "Sohn", "translation": "son", "sentence_de": "Das ist mein Sohn.", "sentence_en": "That is my son."},
    {"word": "Familie", "translation": "family", "sentence_de": "Meine Familie ist groß.", "sentence_en": "My family is big."}
]

# Session 23
session_23 = [
    {"word": "heißt", "translation": "is called / means", "sentence_de": "Wie heißt du?", "sentence_en": "What is your name?"},
    {"word": "jeder", "translation": "everyone / each", "sentence_de": "Jeder weiß das.", "sentence_en": "Everyone knows that."},
    {"word": "sprechen (hat gesprochen)", "translation": "to speak", "verb_forms": "Präteritum: sprach, Perfekt: hat gesprochen", "sentence_de": "Sprechen Sie Deutsch?", "sentence_en": "Do you speak German?"},
    {"word": "gefunden", "translation": "found", "sentence_de": "Ich habe meinen Schlüssel gefunden.", "sentence_en": "I found my key."},
    {"word": "Sache", "translation": "thing / matter", "sentence_de": "Das ist meine Sache.", "sentence_en": "That is my business."},
    {"word": "Problem", "translation": "problem", "sentence_de": "Kein Problem.", "sentence_en": "No problem."},
    {"word": "fertig", "translation": "finished / ready", "sentence_de": "Bist du fertig?", "sentence_en": "Are you ready?"},
    {"word": "wann", "translation": "when", "sentence_de": "Wann kommst du?", "sentence_en": "When are you coming?"},
    {"word": "brauche", "translation": "need (1st person)", "sentence_de": "Ich brauche Hilfe.", "sentence_en": "I need help."},
    {"word": "Bruder", "translation": "brother", "sentence_de": "Mein Bruder ist älter als ich.", "sentence_en": "My brother is older than me."},
    {"word": "Hilfe", "translation": "help", "sentence_de": "Ich brauche Hilfe.", "sentence_en": "I need help."},
    {"word": "halten (hat gehalten)", "translation": "to hold / to stop", "verb_forms": "Präteritum: hielt, Perfekt: hat gehalten", "sentence_de": "Der Bus hält hier.", "sentence_en": "The bus stops here."},
    {"word": "hatten", "translation": "had (plural)", "sentence_de": "Wir hatten Spaß.", "sentence_en": "We had fun."},
    {"word": "Kind", "translation": "child", "sentence_de": "Das Kind schläft.", "sentence_en": "The child is sleeping."},
    {"word": "siehst", "translation": "see (2nd person)", "sentence_de": "Siehst du das?", "sentence_en": "Do you see that?"},
    {"word": "darüber", "translation": "about it", "sentence_de": "Wir müssen darüber reden.", "sentence_en": "We need to talk about it."},
    {"word": "konnte", "translation": "could", "sentence_de": "Ich konnte nicht kommen.", "sentence_en": "I couldn't come."},
    {"word": "wahr", "translation": "true", "sentence_de": "Das ist nicht wahr.", "sentence_en": "That is not true."},
    {"word": "warst", "translation": "were (2nd person)", "sentence_de": "Wo warst du?", "sentence_en": "Where were you?"},
    {"word": "beim", "translation": "at the", "sentence_de": "Ich bin beim Arzt.", "sentence_en": "I am at the doctor."}
]

# Session 24
session_24 = [
    {"word": "ne", "translation": "nope (colloquial)", "sentence_de": "Ne, keine Lust.", "sentence_en": "Nope, don't feel like it."},
    {"word": "seinen", "translation": "his (accusative)", "sentence_de": "Er sucht seinen Hund.", "sentence_en": "He is looking for his dog."},
    {"word": "beide", "translation": "both", "sentence_de": "Wir kommen beide.", "sentence_en": "We are both coming."},
    {"word": "Jahren", "translation": "years (dative)", "sentence_de": "Seit zwei Jahren.", "sentence_en": "For two years."},
    {"word": "daran", "translation": "on it / about it", "sentence_de": "Ich glaube daran.", "sentence_en": "I believe in it."},
    {"word": "kam", "translation": "came", "sentence_de": "Er kam spät.", "sentence_en": "He came late."},
    {"word": "dazu", "translation": "to it / in addition", "sentence_de": "Ich sage nichts dazu.", "sentence_en": "I say nothing to that."},
    {"word": "gib", "translation": "give (imperative)", "sentence_de": "Gib mir das.", "sentence_en": "Give me that."},
    {"word": "würden", "translation": "would (plural)", "sentence_de": "Wir würden gerne bestellen.", "sentence_en": "We would like to order."},
    {"word": "verstehe", "translation": "understand (1st person)", "sentence_de": "Ich verstehe dich nicht.", "sentence_en": "I don't understand you."},
    {"word": "deinem", "translation": "your (dative)", "sentence_de": "Wie geht es deinem Vater?", "sentence_en": "How is your father?"},
    {"word": "ihrem", "translation": "her / their (dative)", "sentence_de": "Sie hilft ihrem Bruder.", "sentence_en": "She helps her brother."},
    {"word": "deiner", "translation": "your (genitive/dative)", "sentence_de": "Das ist einer deiner Freunde.", "sentence_en": "That is one of your friends."},
    {"word": "wusste", "translation": "knew", "sentence_de": "Ich wusste das nicht.", "sentence_en": "I didn't know that."},
    {"word": "könnten", "translation": "could (plural)", "sentence_de": "Wir könnten ins Kino gehen.", "sentence_en": "We could go to the cinema."},
    {"word": "Fall", "translation": "case / fall", "sentence_de": "Auf jeden Fall.", "sentence_en": "In any case."},
    {"word": "lieber", "translation": "rather / prefer", "sentence_de": "Ich trinke lieber Tee.", "sentence_en": "I prefer drinking tea."},
    {"word": "eigentlich", "translation": "actually", "sentence_de": "Was willst du eigentlich?", "sentence_en": "What do you actually want?"},
    {"word": "jeden", "translation": "every (accusative)", "sentence_de": "Jeden Tag.", "sentence_en": "Every day."},
    {"word": "sieh", "translation": "look (imperative)", "sentence_de": "Sieh mal!", "sentence_en": "Look!"}
]

# Session 25
session_25 = [
    {"word": "Dank", "translation": "thanks", "sentence_de": "Vielen Dank!", "sentence_en": "Many thanks!"},
    {"word": "mag", "translation": "like (1st/3rd person)", "sentence_de": "Ich mag Pizza.", "sentence_en": "I like pizza."},
    {"word": "sehe", "translation": "see (1st person)", "sentence_de": "Ich sehe dich.", "sentence_en": "I see you."},
    {"word": "Frage", "translation": "question", "sentence_de": "Ich habe eine Frage.", "sentence_en": "I have a question."},
    {"word": "gern", "translation": "gladly", "sentence_de": "Ich helfe gern.", "sentence_en": "I like helping."},
    {"word": "komme", "translation": "come (1st person)", "sentence_de": "Ich komme sofort.", "sentence_en": "I'm coming right now."},
    {"word": "Stadt", "translation": "city", "sentence_de": "Wir fahren in die Stadt.", "sentence_en": "We are going to the city."},
    {"word": "sage", "translation": "say (1st person)", "sentence_de": "Ich sage nichts.", "sentence_en": "I say nothing."},
    {"word": "Kopf", "translation": "head", "sentence_de": "Mein Kopf tut weh.", "sentence_en": "My head hurts."},
    {"word": "Männer", "translation": "men", "sentence_de": "Zwei Männer stehen dort.", "sentence_en": "Two men are standing there."},
    {"word": "egal", "translation": "doesn't matter", "sentence_de": "Das ist mir egal.", "sentence_en": "I don't care."},
    {"word": "letzte", "translation": "last", "sentence_de": "Das ist die letzte Warnung.", "sentence_en": "This is the last warning."},
    {"word": "Namen", "translation": "names / name (accusative)", "sentence_de": "Ich habe seinen Namen vergessen.", "sentence_en": "I forgot his name."},
    {"word": "gab", "translation": "gave", "sentence_de": "Er gab mir das Buch.", "sentence_en": "He gave me the book."},
    {"word": "kleine", "translation": "small", "sentence_de": "Eine kleine Maus.", "sentence_en": "A small mouse."},
    {"word": "mache", "translation": "make / do (1st person)", "sentence_de": "Ich mache das.", "sentence_en": "I'll do that."},
    {"word": "all", "translation": "all", "sentence_de": "All das Geld.", "sentence_en": "All that money."},
    {"word": "Uhr", "translation": "clock / o'clock", "sentence_de": "Es ist 12 Uhr.", "sentence_en": "It is 12 o'clock."},
    {"word": "Ende", "translation": "end", "sentence_de": "Das Ende des Films.", "sentence_en": "The end of the movie."},
    {"word": "Baby", "translation": "baby", "sentence_de": "Das Baby schläft.", "sentence_en": "The baby is sleeping."}
]

# Session 26
session_26 = [
    {"word": "gehe", "translation": "go (1st person)", "sentence_de": "Ich gehe jetzt.", "sentence_en": "I am going now."},
    {"word": "Glück", "translation": "luck / happiness", "sentence_de": "Viel Glück!", "sentence_en": "Good luck!"},
    {"word": "Dinge", "translation": "things", "sentence_de": "Es gibt wichtigere Dinge.", "sentence_en": "There are more important things."},
    {"word": "Freunde", "translation": "friends", "sentence_de": "Wir sind gute Freunde.", "sentence_en": "We are good friends."},
    {"word": "bisschen", "translation": "a little bit", "sentence_de": "Ein bisschen Zucker.", "sentence_en": "A little bit of sugar."},
    {"word": "darauf", "translation": "on it", "sentence_de": "Ich warte darauf.", "sentence_en": "I am waiting for it."},
    {"word": "Minuten", "translation": "minutes", "sentence_de": "Fünf Minuten.", "sentence_en": "Five minutes."},
    {"word": "echt", "translation": "really / genuine", "sentence_de": "Ist das echt?", "sentence_en": "Is that real?"},
    {"word": "bereit", "translation": "ready", "sentence_de": "Ich bin bereit.", "sentence_en": "I am ready."},
    {"word": "eins", "translation": "one", "sentence_de": "Nummer eins.", "sentence_en": "Number one."},
    {"word": "Augen", "translation": "eyes", "sentence_de": "Er hat blaue Augen.", "sentence_en": "He has blue eyes."},
    {"word": "runter", "translation": "down", "sentence_de": "Komm runter!", "sentence_en": "Come down!"},
    {"word": "Jungs", "translation": "guys / boys", "sentence_de": "Hallo Jungs!", "sentence_en": "Hello guys!"},
    {"word": "seiner", "translation": "his (dative/genitive)", "sentence_de": "Er hilft seiner Mutter.", "sentence_en": "He helps his mother."},
    {"word": "Polizei", "translation": "police", "sentence_de": "Ruf die Polizei!", "sentence_en": "Call the police!"},
    {"word": "Auto", "translation": "car", "sentence_de": "Das Auto ist rot.", "sentence_en": "The car is red."},
    {"word": "eure", "translation": "your (plural)", "sentence_de": "Wo ist eure Mutter?", "sentence_en": "Where is your mother?"},
    {"word": "vielen", "translation": "many (dative)", "sentence_de": "Vielen Dank!", "sentence_en": "Many thanks!"},
    {"word": "meinst", "translation": "mean / think (2nd person)", "sentence_de": "Was meinst du?", "sentence_en": "What do you mean?"},
    {"word": "draußen", "translation": "outside", "sentence_de": "Es ist kalt draußen.", "sentence_en": "It is cold outside."}
]

# Session 27
session_27 = [
    {"word": "Tür", "translation": "door", "sentence_de": "Mach die Tür zu.", "sentence_en": "Close the door."},
    {"word": "Dad", "translation": "Dad", "sentence_de": "Mein Dad ist cool.", "sentence_en": "My dad is cool."},
    {"word": "wurden", "translation": "became / were (passive)", "sentence_de": "Sie wurden Freunde.", "sentence_en": "They became friends."},
    {"word": "verrückt", "translation": "crazy", "sentence_de": "Bist du verrückt?", "sentence_en": "Are you crazy?"},
    {"word": "Kerl", "translation": "guy", "sentence_de": "Er ist ein netter Kerl.", "sentence_en": "He is a nice guy."},
    {"word": "hätten", "translation": "would have (plural)", "sentence_de": "Wir hätten gerne zwei Bier.", "sentence_en": "We would like two beers."},
    {"word": "einzige", "translation": "only / single", "sentence_de": "Das ist die einzige Möglichkeit.", "sentence_en": "That is the only possibility."},
    {"word": "vorbei", "translation": "over / past", "sentence_de": "Der Sommer ist vorbei.", "sentence_en": "Summer is over."},
    {"word": "treffen (hat getroffen)", "translation": "to meet / to hit", "verb_forms": "Präteritum: traf, Perfekt: hat getroffen", "sentence_de": "Wir treffen uns um 8.", "sentence_en": "We meet at 8."},
    {"word": "ganzen", "translation": "whole (accusative)", "sentence_de": "Den ganzen Tag.", "sentence_en": "The whole day."},
    {"word": "hi", "translation": "hi", "sentence_de": "Hi, wie geht's?", "sentence_en": "Hi, how are you?"},
    {"word": "Ahnung", "translation": "idea / clue", "sentence_de": "Keine Ahnung.", "sentence_en": "No idea."},
    {"word": "Teufel", "translation": "devil", "sentence_de": "Scher dich zum Teufel!", "sentence_en": "Go to hell!"},
    {"word": "kenne", "translation": "know (1st person)", "sentence_de": "Ich kenne ihn.", "sentence_en": "I know him."},
    {"word": "hinter", "translation": "behind", "sentence_de": "Hinter dem Haus.", "sentence_en": "Behind the house."},
    {"word": "fast", "translation": "almost", "sentence_de": "Ich bin fast fertig.", "sentence_en": "I am almost finished."},
    {"word": "Name", "translation": "name", "sentence_de": "Mein Name ist Bond.", "sentence_en": "My name is Bond."},
    {"word": "gerne", "translation": "gladly", "sentence_de": "Ich mache das gerne.", "sentence_en": "I like doing that."},
    {"word": "dran", "translation": "turn / on it", "sentence_de": "Wer ist dran?", "sentence_en": "Whose turn is it?"},
    {"word": "neue", "translation": "new", "sentence_de": "Ich habe eine neue Nummer.", "sentence_en": "I have a new number."}
]

# Session 28
session_28 = [
    {"word": "ziemlich", "translation": "quite / fairly", "sentence_de": "Es ist ziemlich kalt.", "sentence_en": "It is quite cold."},
    {"word": "ging", "translation": "went", "sentence_de": "Er ging nach Hause.", "sentence_en": "He went home."},
    {"word": "Sorgen", "translation": "worries", "sentence_de": "Mach dir keine Sorgen.", "sentence_en": "Don't worry."},
    {"word": "verstanden", "translation": "understood", "sentence_de": "Haben Sie mich verstanden?", "sentence_en": "Did you understand me?"},
    {"word": "Tochter", "translation": "daughter", "sentence_de": "Meine Tochter geht zur Schule.", "sentence_en": "My daughter goes to school."},
    {"word": "toll", "translation": "great", "sentence_de": "Das ist toll!", "sentence_en": "That is great!"},
    {"word": "jemanden", "translation": "someone (accusative)", "sentence_de": "Ich suche jemanden.", "sentence_en": "I am looking for someone."},
    {"word": "sogar", "translation": "even", "sentence_de": "Sogar er war da.", "sentence_en": "Even he was there."},
    {"word": "überhaupt", "translation": "at all / generally", "sentence_de": "Das stimmt überhaupt nicht.", "sentence_en": "That is not true at all."},
    {"word": "he", "translation": "hey", "sentence_de": "He, warte mal!", "sentence_en": "Hey, wait a minute!"},
    {"word": "hört", "translation": "hears / listen", "sentence_de": "Er hört schlecht.", "sentence_en": "He hears poorly."},
    {"word": "Frauen", "translation": "women", "sentence_de": "Frauen und Kinder zuerst.", "sentence_en": "Women and children first."},
    {"word": "Hand", "translation": "hand", "sentence_de": "Gib mir deine Hand.", "sentence_en": "Give me your hand."},
    {"word": "drin", "translation": "inside", "sentence_de": "Ist jemand drin?", "sentence_en": "Is anyone inside?"},
    {"word": "schau", "translation": "look (imperative)", "sentence_de": "Schau mal her.", "sentence_en": "Look here."},
    {"word": "nimm", "translation": "take (imperative)", "sentence_de": "Nimm das!", "sentence_en": "Take that!"},
    {"word": "seinem", "translation": "his (dative)", "sentence_de": "Er geht mit seinem Hund.", "sentence_en": "He is walking with his dog."},
    {"word": "Mama", "translation": "mom", "sentence_de": "Meine Mama ist die Beste.", "sentence_en": "My mom is the best."},
    {"word": "lang", "translation": "long", "sentence_de": "Der Weg ist lang.", "sentence_en": "The way is long."},
    {"word": "solltest", "translation": "should (2nd person)", "sentence_de": "Du solltest schlafen.", "sentence_en": "You should sleep."}
]

# Session 29
session_29 = [
    {"word": "verloren", "translation": "lost", "sentence_de": "Ich habe mein Handy verloren.", "sentence_en": "I lost my phone."},
    {"word": "Art", "translation": "kind / type / way", "sentence_de": "Das ist nicht meine Art.", "sentence_en": "That is not my way."},
    {"word": "sah", "translation": "saw", "sentence_de": "Ich sah ihn gestern.", "sentence_en": "I saw him yesterday."},
    {"word": "große", "translation": "big / large", "sentence_de": "Eine große Pizza, bitte.", "sentence_en": "A large pizza, please."},
    {"word": "darum", "translation": "therefore / that's why", "sentence_de": "Darum bin ich hier.", "sentence_en": "That's why I am here."},
    {"word": "denkst", "translation": "think (2nd person)", "sentence_de": "Was denkst du?", "sentence_en": "What do you think?"},
    {"word": "Job", "translation": "job", "sentence_de": "Ich habe einen neuen Job.", "sentence_en": "I have a new job."},
    {"word": "Ruhe", "translation": "quiet / peace / rest", "sentence_de": "Lass mich in Ruhe.", "sentence_en": "Leave me alone."},
    {"word": "braucht", "translation": "needs", "sentence_de": "Er braucht Hilfe.", "sentence_en": "He needs help."},
    {"word": "woher", "translation": "where from", "sentence_de": "Woher kommst du?", "sentence_en": "Where do you come from?"},
    {"word": "Idee", "translation": "idea", "sentence_de": "Das ist eine gute Idee.", "sentence_en": "That is a good idea."},
    {"word": "je", "translation": "ever", "sentence_de": "Warst du je in Paris?", "sentence_en": "Have you ever been to Paris?"},
    {"word": "kommst", "translation": "come (2nd person)", "sentence_de": "Kommst du morgen?", "sentence_en": "Are you coming tomorrow?"},
    {"word": "liegt", "translation": "lies / is located", "sentence_de": "Berlin liegt in Deutschland.", "sentence_en": "Berlin is located in Germany."},
    {"word": "Grund", "translation": "reason / ground", "sentence_de": "Es gibt keinen Grund zur Panik.", "sentence_en": "There is no reason to panic."},
    {"word": "versuchen (hat versucht)", "translation": "to try", "verb_forms": "Präteritum: versuchte, Perfekt: hat versucht", "sentence_de": "Ich werde es versuchen.", "sentence_en": "I will try it."},
    {"word": "Jahr", "translation": "year", "sentence_de": "Nächstes Jahr.", "sentence_en": "Next year."},
    {"word": "gekommen", "translation": "come (participle)", "sentence_de": "Er ist nicht gekommen.", "sentence_en": "He didn't come."},
    {"word": "Wasser", "translation": "water", "sentence_de": "Ein Glas Wasser, bitte.", "sentence_en": "A glass of water, please."},
    {"word": "gewesen", "translation": "been", "sentence_de": "Ich bin dort gewesen.", "sentence_en": "I have been there."}
]

# Session 30
session_30 = [
    {"word": "endlich", "translation": "finally", "sentence_de": "Endlich Wochenende!", "sentence_en": "Finally weekend!"},
    {"word": "Schwester", "translation": "sister", "sentence_de": "Meine Schwester ist älter als ich.", "sentence_en": "My sister is older than me."},
    {"word": "keiner", "translation": "no one", "sentence_de": "Keiner war da.", "sentence_en": "No one was there."},
    {"word": "Tod", "translation": "death", "sentence_de": "Der Tod gehört zum Leben.", "sentence_en": "Death is part of life."},
    {"word": "versucht", "translation": "tries / tried", "sentence_de": "Er versucht es immer wieder.", "sentence_en": "He tries it again and again."},
    {"word": "letzten", "translation": "last (dative/accusative)", "sentence_de": "Letzten Sommer.", "sentence_en": "Last summer."},
    {"word": "Geschichte", "translation": "history / story", "sentence_de": "Erzähl mir eine Geschichte.", "sentence_en": "Tell me a story."},
    {"word": "erste", "translation": "first", "sentence_de": "Das erste Mal.", "sentence_en": "The first time."},
    {"word": "Alter", "translation": "age / old man (slang)", "sentence_de": "In meinem Alter.", "sentence_en": "At my age."},
    {"word": "kurz", "translation": "short", "sentence_de": "Warte kurz.", "sentence_en": "Wait a moment."},
    {"word": "bedeutet", "translation": "means", "sentence_de": "Was bedeutet das?", "sentence_en": "What does that mean?"},
    {"word": "niemals", "translation": "never", "sentence_de": "Sag niemals nie.", "sentence_en": "Never say never."},
    {"word": "ah", "translation": "ah", "sentence_de": "Ah, ich verstehe.", "sentence_en": "Ah, I understand."},
    {"word": "fünf", "translation": "five", "sentence_de": "Ich habe fünf Euro.", "sentence_en": "I have five euros."},
    {"word": "welche", "translation": "which", "sentence_de": "Welche Farbe magst du?", "sentence_en": "Which color do you like?"},
    {"word": "etwa", "translation": "about / approximately", "sentence_de": "Es dauerte etwa eine Stunde.", "sentence_en": "It took about an hour."},
    {"word": "erzählt", "translation": "tells / told", "sentence_de": "Er erzählt gerne Witze.", "sentence_en": "He likes telling jokes."},
    {"word": "finde", "translation": "find (1st person)", "sentence_de": "Ich finde das gut.", "sentence_en": "I think that's good."},
    {"word": "Land", "translation": "country / land", "sentence_de": "Dieses Land ist schön.", "sentence_en": "This country is beautiful."},
    {"word": "lasst", "translation": "let (2nd person plural)", "sentence_de": "Lasst uns gehen.", "sentence_en": "Let's go."}
]

if __name__ == "__main__":
    write_session(1, session_1)
    write_session(2, session_2)
    write_session(3, session_3)
    write_session(4, session_4)
    write_session(5, session_5)
    write_session(6, session_6)
    write_session(7, session_7)
    write_session(8, session_8)
    write_session(9, session_9)
    write_session(10, session_10)
    write_session(11, session_11)
    write_session(12, session_12)
    write_session(13, session_13)
    write_session(14, session_14)
    write_session(15, session_15)
    write_session(16, session_16)
    write_session(17, session_17)
    write_session(18, session_18)
    write_session(19, session_19)
    write_session(20, session_20)
    write_session(21, session_21)
    write_session(22, session_22)
    write_session(23, session_23)
    write_session(24, session_24)
    write_session(25, session_25)
    write_session(26, session_26)
    write_session(27, session_27)
    write_session(28, session_28)
    write_session(29, session_29)
    write_session(30, session_30)
