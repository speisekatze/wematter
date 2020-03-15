# WeMatter

### Einleitung
Für die Bearbeitung und das Verteilen von Aufgaben nutzt das Team intern Wekan (Kanboard, Trello, .. - viel später). Karten müssen vom Team manuell erstellt werden, da der Zugriff auf das Board auf das Team beschränkt ist.   
Das Ziel des Projektes ist eine Multichannel Integration für Wekan. Also das Erstellen von *Cards* via E-Mail, Chat (mattermost für den Anfang), Ticketsystem (später) und Webinterface ohne Wekan Login. Weiterhin sollen *Card Updates* wieder über den (gewählten) Eingangskanal kommuniziert werden.

### Erste Gedanken und Erkenntnisse

#### Wekan
Die Wekan-API arbeitet nur mit tatsächlich angelegten Nutzern, scheinbar muss der API-User auch Adminbrechtigung haben. Die API kann zwar auch Karten lesen, es dürfte aber unschön werden den Karten über darüber den Karten zu folgen und auf Updates zu reagieren. Vermutlich sind die ausgehenden Webhooks von Wekan besser geeignet um Kartenupdates in den Kanälen zu verbreiten.

#### Mattermost
Derzeit scheint es am sinnvollsten den mmpy_bot für die Integration in Mattermost zu nutzen. Würde man nur aus Chatcommandos Karten erzeugen wäre das vermutlich mit einem simplen Plugin für den Bot getan. Durch die anderen Anforderungen stellt sich aber die Frage ob man den mmpy_bot soweit zerlegt und in dieses Projekt integriert oder ob man nur ein Plugin dafür entwickelt das mit unserem Service spricht.

#### E-mail
Einfach per imap aus einem Postfach fischen.
* imap postfach (inbox default)
* smtp
* optional Betreff-Filter

#### Allgemein
* einen Teamkanal festlegen in dem sämtliche updates an allen Karten abgeworfen werden
* um den Ersteller über Updates an seiner Karte zu informieren wird eine simple DB benötigt
	- name des ersteller
	- kanal für die karte
	- id der karte
* eventuell eine nutzer DB um den benutzer immer per mail zu informieren - oder email als optionale angabe in allen anderen kanälen
* um später andere boards anzubinden sollte die API dynamisch geladen werden
* ebenso die Eingangskanäle
