# Amar Nagim & Bas van Beek
# bank robbery

import sys
import time


print('========================================================================================================================')
print('|  Je zit midden in een bankoverval!                                                                                   |')
print('|  Jouw keuzes bepalen of je word opgepakt en of je het overleefd. Er zijn meerdere uitkomsten.                        |')
print('|  Dus kies zorgvuldig. Als je dood gaat of wordt opgepakt is het game over! Kom je ermee weg, met of zonder buit heb  |')                          
print('|  je gewonnen. Afhankelijk van het hoeveelheid geld wat je hebt buit gemaakt krijg je een bepaalde score!             |')
print('========================================================================================================================') 


print('')
time.sleep(5)
                                                                                                                         # questions
vraag_1 = input("""Het alarm in de bank gaat af. Het duurt je iets te lang.
Kies je ervoor om nog 5 mimnuten in de bank te blijven om het 
geld te bemachtigen, of verlaat je de bank met lege handen? wachten/vluchten: """).lower()

print('')

if vraag_1 == 'wachten':
    exit_or_sewer = input("""
Buiten hoor je de politie sirenes erg dichtbij komen! Je hebt 1,2 miljoen kunnen bemachtigen.
Ga je via de uitgang van de bank naar je vluchtauto met het risico dat de politie jou staat op te wachten,
of ga je de riolering in? uitgang/riool: """).lower()
    if exit_or_sewer == 'uitgang':
        getCaughtOrKill = input("""
De politie staat met getrokken wapens voor de bank. Je hebt twee opties. Jezelf overgeven en je straf uitzitten,
of de agent die voor je vluchtauto staat neerschieten en snel je vluchtauto in gaan. neerschieten/meewerken: """).lower()
        if getCaughtOrKill == 'neerschieten':
            print("""
De agent is neer! Je rent richting je busje... Net voordat je de deur van je busje open kon trekken 
werd je neergeschoten door de andere agenten...""")
            print('')
            print('Game over! Helaas heb je het schotwond niet overleeft.')
            time.sleep(1)
            print('Je hebt 0/100 punten, omdat je het niet hebt overleefd.')
            time.sleep(5)
            sys.exit()
        elif getCaughtOrKill == 'meewerken':
            print('Je bent door de politie opgepakt en krijgt 5 jaar celstraf. Je hebt geen geld kunnen bemachtigen. ')
            print('')
            print('Game over! Helaas ben je opgepakt.')
            time.sleep(5)
            sys.exit()    

    else: #riool met geld
        ThrowMoneyAway = input(""" 
Je bent snel de riolering ingekropen vanuit het luik wat in de grond zit.
Op dit punt hoor je dat de politie bezig is met een inval. De volle tas met geld
begint nu zwaar de worden en je raakt uitgeput. Je hebt twee keuzes; je goot de helft 
van het geld op de grond en rent snel door. of je zet door met het volle geld bedrag. weggooien/doorzetten: """).lower()
        if ThrowMoneyAway == 'weggooien':
            call = input("""
Inmiddels heeft de politie de riolering al gevonden. Je hoort ze vanaf het begin van de tunnel jouw kant op komen,
maar gelukkig zie je het einde van de riolering al. Je hebt de keuze om een vriend te bellen voor een vluchtauto
of te voet verder te gaan. bellen/lopen: """)
            if call == 'bellen':
                print("""
Je vriend is helaas niet komen opdagen. Het heeft te lang geduurd. 
De politie heeft je te pakken gekregen. Je hebt 5 jaar celstraf gekregen.""")
                print('')
                time.sleep(1)
                print('Game over! Helaas, je bent door de politie gepakt. ')
                print(
"""Je hebt 25/100 punten, omdat je het hebt overleefd maar bent opgepakt en een celstraf moet uizitten""")
                time.sleep(5)
                sys.exit()
            if call == 'lopen':
                print('')
                print("""
Je bent de riolering uit gekomen en je trapt iemand van zijn fiets af
en je gaat ermee van door De politie heeft na een lange zoektocht jou niet gevonden.
Je bent weggekomen met 600.000 euro!""")
                print('')
                time.sleep(1)
                print("""
                
Je hebt 100/100 punten verdiend. Het maximaal aantal punten.
Je hebt 600.000 euro verdiend en bent weggekomen. Goed gedaan!""")  
                time.sleep(5)
                sys.exit()
        elif ThrowMoneyAway == 'doorzetten':
            print("""
Inmiddels heeft de politie de riolering al een tijdje gevonden. Je hoort ze jouw positie naderen. 
Ze komen zo dichtbij dat je geen enkele kans hebt om te vluchten. 
Je bent gepakt. Je hebt 5 jaar celstraf gekregen.""")
            print('')
            print('Game over! Helaas, je bent door de politie gepakt.')
            time.sleep(1)
            print(
"""Je hebt 25/100 punten, omdat je het hebt overleefd maar bent opgepakt en een celstraf moet uizitten""")
            time.sleep(5)
            sys.exit()
elif vraag_1 == 'vluchten':
    choosingTheEasyWay = input("""
Je hebt voor de veilige weg gekozen en zit in je vluchtauto.
Je rijdt rustig weg totdat je in je achteruitkijk spiegel kijkt en zwaailichten ziet naderen. 
Je raakt in paniek. Wat doe je; hangende uit je raam schiet je op de politie. 
Of je probeerd ze af te schudden schieten/vluchten: """).lower()
    if choosingTheEasyWay == 'schieten':
        print('')
        print("""
Je let niet op de weg en rijdt tegen een paal aan
met als gevolg de dood.""")
        print('')
        print('Game over! Helaas ben je dood gegaan!')
        time.sleep(1)
        print('Je hebt 0/100 punten, omdat je het niet hebt overleefd.')
        time.sleep(5)
        sys.exit()
    elif choosingTheEasyWay == 'vluchten':
        print('Je hebt succesvol de politie afgeschud, maar helaas heb je geen buit kunnen bemachtigen.')
        time.sleep(1)
        print("""
Je hebt 50/100 punten verdiend, omdat je niet bent opgepakt,
maar geen geld hebt bemachtigd.""")
        time.sleep(5)
        sys.exit()


def wachten():
   exit_or_sewer = input("""
    Buiten hoor je de sirenes erg dichtbij komen! Je hebt 1,2 miljoen kunnen bemachtigen.
    Ga je via de uitgang van de bank naar je vluchtauto met het risico dat de politie jou staat op te wachten,
    of ga je de riolering in? uitgang/riool: """).lower()
