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

# Session 1 Data
session_1 = [
    {
        "word": "unerlässlich",
        "translation": "essential / indispensable",
        "sentence_de": "Eine gute Vorbereitung ist für den Erfolg dieses Projekts unerlässlich.",
        "sentence_en": "Good preparation is essential for the success of this project."
    },
    {
        "word": "bewerten (hat bewertet)",
        "translation": "to evaluate / to assess",
        "verb_forms": "Präteritum: bewertete, Perfekt: hat bewertet",
        "sentence_de": "Wir müssen die aktuellen Marktdaten sorgfältig bewerten, bevor wir eine Entscheidung treffen.",
        "sentence_en": "We must carefully evaluate the current market data before making a decision."
    },
    {
        "word": "stark",
        "translation": "strong",
        "sentence_de": "Der Sturm war so stark, dass er mehrere Bäume entwurzelte.",
        "sentence_en": "The storm was so strong that it uprooted several trees."
    },
    {
        "word": "emotional",
        "translation": "emotional",
        "sentence_de": "Die Debatte wurde sehr emotional geführt.",
        "sentence_en": "The debate was conducted very emotionally."
    },
    {
        "word": "kulturell",
        "translation": "cultural",
        "sentence_de": "Berlin hat ein vielfältiges kulturelles Angebot.",
        "sentence_en": "Berlin has a diverse cultural offering."
    },
    {
        "word": "euphorisch",
        "translation": "euphoric",
        "sentence_de": "Die Fans reagierten euphorisch auf den Sieg ihrer Mannschaft.",
        "sentence_en": "The fans reacted euphorically to their team's victory."
    },
    {
        "word": "preiswert",
        "translation": "inexpensive / good value",
        "sentence_de": "Dieses Restaurant bietet sehr preiswerte Mittagsmenüs an.",
        "sentence_en": "This restaurant offers very inexpensive lunch menus."
    },
    {
        "word": "erschwinglich",
        "translation": "affordable",
        "sentence_de": "Wohnraum in der Innenstadt ist kaum noch erschwinglich.",
        "sentence_en": "Housing in the city center is hardly affordable anymore."
    },
    {
        "word": "erschließen (hat erschlossen)",
        "translation": "to develop / to open up",
        "verb_forms": "Präteritum: erschloss, Perfekt: hat erschlossen",
        "sentence_de": "Das Unternehmen plant, neue Märkte in Asien zu erschließen.",
        "sentence_en": "The company plans to open up new markets in Asia."
    },
    {
        "word": "arbeiten (hat gearbeitet)",
        "translation": "to work",
        "verb_forms": "Präteritum: arbeitete, Perfekt: hat gearbeitet, Preposition: an (+ Dat)",
        "sentence_de": "Wir arbeiten derzeit an einer Lösung für das Problem.",
        "sentence_en": "We are currently working on a solution to the problem."
    },
    {
        "word": "verlängern (hat verlängert)",
        "translation": "to extend",
        "verb_forms": "Präteritum: verlängerte, Perfekt: hat verlängert",
        "sentence_de": "Können Sie bitte meinen Aufenthalt um zwei Tage verlängern?",
        "sentence_en": "Could you please extend my stay by two days?"
    },
    {
        "word": "verpassen (hat verpasst)",
        "translation": "to miss",
        "verb_forms": "Präteritum: verpasste, Perfekt: hat verpasst",
        "sentence_de": "Wenn wir uns nicht beeilen, verpassen wir den Zug.",
        "sentence_en": "If we don't hurry, we will miss the train."
    },
    {
        "word": "finanzieren (hat finanziert)",
        "translation": "to finance",
        "verb_forms": "Präteritum: finanzierte, Perfekt: hat finanziert",
        "sentence_de": "Das Studium wird durch ein Stipendium finanziert.",
        "sentence_en": "The studies are financed by a scholarship."
    },
    {
        "word": "dirigieren (hat dirigiert)",
        "translation": "to conduct",
        "verb_forms": "Präteritum: dirigierte, Perfekt: hat dirigiert",
        "sentence_de": "Der berühmte Maestro dirigierte das Orchester mit großer Leidenschaft.",
        "sentence_en": "The famous maestro conducted the orchestra with great passion."
    },
    {
        "word": "kostenlos",
        "translation": "free of charge",
        "sentence_de": "Der Eintritt in das Museum ist für Studenten kostenlos.",
        "sentence_en": "Admission to the museum is free for students."
    },
    {
        "word": "niedrig",
        "translation": "low",
        "sentence_de": "Die Temperaturen sind für diese Jahreszeit ungewöhnlich niedrig.",
        "sentence_en": "The temperatures are unusually low for this time of year."
    },
    {
        "word": "kontrolliert (hat kontrolliert)",
        "translation": "controlled / to control",
        "verb_forms": "Präteritum: kontrollierte, Perfekt: hat kontrolliert",
        "sentence_de": "Der Zugang zum Gebäude wird streng kontrolliert.",
        "sentence_en": "Access to the building is strictly controlled."
    },
    {
        "word": "historisch",
        "translation": "historical",
        "sentence_de": "Wir haben eine historische Verantwortung.",
        "sentence_en": "We have a historical responsibility."
    },
    {
        "word": "verschreiben (hat verschrieben)",
        "translation": "to prescribe",
        "verb_forms": "Präteritum: verschrieb, Perfekt: hat verschrieben",
        "sentence_de": "Der Arzt hat mir ein starkes Schmerzmittel verschrieben.",
        "sentence_en": "The doctor prescribed me a strong painkiller."
    },
    {
        "word": "mäßig",
        "translation": "moderate / mediocre",
        "sentence_de": "Die Qualität des Essens war nur mäßig.",
        "sentence_en": "The quality of the food was only mediocre."
    }
]

# Session 2 Data
session_2 = [
    {"word": "schick", "translation": "chic / stylish", "sentence_de": "Sie trägt heute ein sehr schickes Kleid.", "sentence_en": "She is wearing a very chic dress today."},
    {"word": "aufbewahren (hat aufbewahrt)", "translation": "to keep / to store", "verb_forms": "Präteritum: bewahrte auf, Perfekt: hat aufbewahrt", "sentence_de": "Man sollte Medikamente für Kinder unzugänglich aufbewahren.", "sentence_en": "Medication should be kept out of reach of children."},
    {"word": "durchhalten (hat durchgehalten)", "translation": "to persevere / to hold out", "verb_forms": "Präteritum: hielt durch, Perfekt: hat durchgehalten", "sentence_de": "Es war ein langes Rennen, aber er hat bis zum Ende durchgehalten.", "sentence_en": "It was a long race, but he persevered until the end."},
    {"word": "kreativ", "translation": "creative", "sentence_de": "Wir suchen nach kreativen Lösungen für dieses Problem.", "sentence_en": "We are looking for creative solutions to this problem."},
    {"word": "einnehmen (hat eingenommen)", "translation": "to take (medicine/meal) / to occupy", "verb_forms": "Präteritum: nahm ein, Perfekt: hat eingenommen", "sentence_de": "Bitte nehmen Sie die Tabletten nach dem Essen ein.", "sentence_en": "Please take the tablets after the meal."},
    {"word": "abenteuerlustig", "translation": "adventurous", "sentence_de": "Mein Bruder ist sehr abenteuerlustig und reist gerne an exotische Orte.", "sentence_en": "My brother is very adventurous and likes to travel to exotic places."},
    {"word": "reparaturbedürftig", "translation": "in need of repair", "sentence_de": "Das alte Haus ist stark reparaturbedürftig.", "sentence_en": "The old house is in great need of repair."},
    {"word": "künstlerisch", "translation": "artistic", "sentence_de": "Sie hat großes künstlerisches Talent.", "sentence_en": "She has great artistic talent."},
    {"word": "einüben (hat eingeübt)", "translation": "to practice / to rehearse", "verb_forms": "Präteritum: übte ein, Perfekt: hat eingeübt", "sentence_de": "Die Schauspieler müssen ihre Rollen noch weiter einüben.", "sentence_en": "The actors still need to practice their roles further."},
    {"word": "retournieren (hat retourniert)", "translation": "to return (goods)", "verb_forms": "Präteritum: retournierte, Perfekt: hat retourniert", "sentence_de": "Ich möchte diese Schuhe retournieren, da sie nicht passen.", "sentence_en": "I would like to return these shoes because they don't fit."},
    {"word": "robust", "translation": "robust / sturdy", "sentence_de": "Diese Pflanze ist sehr robust und braucht wenig Wasser.", "sentence_en": "This plant is very robust and needs little water."},
    {"word": "anstrengend", "translation": "exhausting / strenuous", "sentence_de": "Die Wanderung war sehr anstrengend, aber der Ausblick hat sich gelohnt.", "sentence_en": "The hike was very exhausting, but the view was worth it."},
    {"word": "widerstandsfähig", "translation": "resistant / resilient", "sentence_de": "Das Material ist extrem widerstandsfähig gegen Hitze.", "sentence_en": "The material is extremely resistant to heat."},
    {"word": "leistungsstark", "translation": "powerful / high-performance", "sentence_de": "Wir brauchen einen leistungsstarken Computer für die Videobearbeitung.", "sentence_en": "We need a powerful computer for video editing."},
    {"word": "bearbeiten (hat bearbeitet)", "translation": "to edit / to process", "verb_forms": "Präteritum: bearbeitete, Perfekt: hat bearbeitet", "sentence_de": "Ich muss noch einige E-Mails bearbeiten.", "sentence_en": "I still have to process a few emails."},
    {"word": "programmierbar", "translation": "programmable", "sentence_de": "Die Heizung ist programmierbar, sodass sie morgens automatisch anspringt.", "sentence_en": "The heating is programmable so that it starts automatically in the morning."},
    {"word": "ruhig", "translation": "quiet / calm", "sentence_de": "Bitte seien Sie während der Prüfung ruhig.", "sentence_en": "Please be quiet during the exam."},
    {"word": "rund", "translation": "round", "sentence_de": "Der Tisch in der Küche ist rund.", "sentence_en": "The table in the kitchen is round."},
    {"word": "aufnehmen (hat aufgenommen)", "translation": "to record / to admit", "verb_forms": "Präteritum: nahm auf, Perfekt: hat aufgenommen", "sentence_de": "Wir werden das Konzert live aufnehmen.", "sentence_en": "We will record the concert live."},
    {"word": "aufladen (hat aufgeladen)", "translation": "to charge (battery)", "verb_forms": "Präteritum: lud auf, Perfekt: hat aufgeladen", "sentence_de": "Ich muss mein Handy aufladen, der Akku ist fast leer.", "sentence_en": "I need to charge my phone, the battery is almost empty."}
]

# Session 21 Data (Demonstrating Nouns)
session_21 = [
    {"word": "das Haus (Pl: Häuser)", "translation": "house", "sentence_de": "Sie haben sich ein kleines Haus am See gekauft.", "sentence_en": "They bought a small house by the lake."},
    {"word": "der Mensch (Pl: Menschen)", "translation": "human / person", "sentence_de": "Jeder Mensch hat das Recht auf Freiheit.", "sentence_en": "Every human has the right to freedom."},
    {"word": "viele", "translation": "many", "sentence_de": "Viele Leute waren mit der Entscheidung nicht einverstanden.", "sentence_en": "Many people did not agree with the decision."},
    {"word": "bleiben (ist geblieben)", "translation": "to stay / to remain", "verb_forms": "Präteritum: blieb, Perfekt: ist geblieben", "sentence_de": "Bitte bleiben Sie kurz am Apparat.", "sentence_en": "Please stay on the line for a moment."},
    {"word": "die Musik (Pl: -)", "translation": "music", "sentence_de": "Musik spielt eine wichtige Rolle in meinem Leben.", "sentence_en": "Music plays an important role in my life."},
    {"word": "unser", "translation": "our", "sentence_de": "Unser Ziel ist es, die Kundenzufriedenheit zu steigern.", "sentence_en": "Our goal is to increase customer satisfaction."},
    {"word": "die Angst (Pl: Ängste)", "translation": "fear / anxiety", "sentence_de": "Er hatte große Angst vor der Prüfung.", "sentence_en": "He was very afraid of the exam."},
    {"word": "die Welt (Pl: Welten)", "translation": "world", "sentence_de": "Die Welt verändert sich ständig.", "sentence_en": "The world is constantly changing."},
    {"word": "der Herr (Pl: Herren)", "translation": "gentleman / Mr.", "sentence_de": "Ein älterer Herr half mir über die Straße.", "sentence_en": "An elderly gentleman helped me cross the street."},
    {"word": "das Kind (Pl: Kinder)", "translation": "child", "sentence_de": "Das Kind spielte fröhlich im Garten.", "sentence_en": "The child played happily in the garden."}
]

if __name__ == "__main__":
    write_session(1, session_1)
    write_session(2, session_2)
    write_session(21, session_21)
