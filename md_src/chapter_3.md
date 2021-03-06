# Κεφάλαιο 3: Βασικές αρχές

Ένα πρόγραμμα αποτελείται από:

* *Σχόλια*: Τα σχόλια δεν συμμετέχουν στην εκτέλεση του προγράμματος αλλά το κάνουν πιο κατανοητό για κάποιον που θέλει να το διαβάσει είτε για να το καταλάβει ή για να το εξελίξει / διορθώσει. Στην Python μπορούμε να γράψουμε τα σχόλιά μας με 2 τρόπους:
	* Με τη χρήση του συμβόλου της δίεσης, εάν το σχόλιό μας δεν θα χρειαστεί παραπάνω από μια γραμμή
	* Με την χρήση τριών αποστρόφων (`) εάν θέλουμε να γράψουμε μεγαλύτερο κείμενο για σχόλιο.

όπως φαίνεται παρακάτω:

```python
	# One line comment

	```
	A block of comments
	that may take more than
	one line.
	```
```

* *Μεταβλητές*: Οι μεταβλητές αντιπροσωπεύουν κάποιες τιμές που είναι αποθηκευμένες στη μνήμη και θα τις χρησιμοποιήσουμε στις συναρτήσεις μας για να κάνουμε κάποιες πράξεις.

* *Δομές ελέγχου ροής*: Είναι έλεγχοι για το αν κάποιες συνθήκες είναι αληθείς ή όχι. Οι έλεγχοι ροής βοηθάνε στο πρόγραμμά μας να αποφασίσει τι θα κάνει κάθε φορά.

* *Δομές επανάληψης*: Πολλά πράγματα στον προγραμματισμό χρειάζεται να επαναλαμβάνονται πολλές φορές. Για να μη γράφουμε χιλιάδες φορές το ίδιο πράγμα, ζητάμε από το πρόγραμμα να επαναλάβει ένα σύνολο εντολών με την χρήση δομών επανάληψης.

* *Συναρτήσεις*: Οι συναρτήσεις είναι ένα σύνολο διαδικασιών / εντολών, πακεταρισμένο σε μια οντότητα η οποία μπορεί να κληθεί πολλές φορές. Λεπτομέρειες θα δούμε παρακάτω.

!!! node "Σημείωση: Οι βασικές πράξεις στην Python είναι: Πρόσθεση (+), Αφαίρεση (-), Πολλαπλασιασμός (*), Διαίρεση (/)"

## 3.1 Αριθμητικές Μεταβλητές

Με τον όρο *μεταβλητή* εννοούμε μια ποσότητα που δεν έχει απαραίτητα μια σταθερή τιμή. Η τιμή της δηλαδή μπορεί να αλλάζει. 

Φανταστείτε ότι κάπου στη μνήμη του υπολογιστή σας υπάρχουν κάποια συρτάρια με κάποιες ετικέτες πάνω. Για παράδειγμα το συρτάρι `a`, το συρτάρι `b` και το συρτάρι `sum`.
Το κάθε συρτάρι έχει μέσα του μια τιμή. Μπορεί να είναι ένας ακέραιος αριθμός (1, 2, ...) ή ένας δεκαδικός αριθμός (1.2, 2.34, 3.45, ...) ή ακόμα και ένα κείμενο ("one", "test", ...). Μπορούμε να πάρουμε την τιμή από το συρτάρι ή και να ορίσουμε εμείς μια τιμή σε αυτό. Το συρτάρι αυτό ονομάζεται **μεταβλητή** ενώ το τι περιέχει μέσα είναι η **τιμή της μεταβλητής**.

Για να δούμε ένα παράδειγμα μεταβλητών στην Python:

```python
	a = 5;
	b = 6;
	sum = a + b;

	print(a)
	print(b)
	print(sum)
```

Ας δούμε μια πιο ολοκληρωμένη εφαρμογή της μέχρι τώρα γνώσης μας. Θα φτιάξουμε ένα απλό πρόγραμμα που θα μας βοηθήσει στο μάθημα των μαθηματικών. Στα μαθηματικά συναντήσαμε τις εξισώσεις πρώτου βαθμού οι οποίες είναι της μορφής \(\alpha \cdot x + \beta = 0\) με \(\alpha \neq 0\). Ξέρουμε ότι για να τις λύσουμε αυτές ακολουθούμε τα εξής βήματα:

\[
\alpha \cdot x = - \beta \\
x = - \frac{\beta}{\alpha}
\]

Άρα θα μπορούσαμε να γράψουμε το ακόλουθο πρόγραμμα:

```python
# 2x - 6 = 0
alpha = 2
beta = -6
x = -(beta / alpha)

print("x = ", x)
```

Προφανώς για κάθε εξίσωση που μας δίνεται να λύσουμε, μπορούμε να αντικαταστήσουμε τις τιμές των `alpha` και `beta` και να πάρουμε την λύση της εξίσωσής μας.

*Σημείωση:*

Στα μαθηματικά έχουμε την έννοια του ποσοστού. Για παράδειγμα αν έχουμε έναν αριθμό `x` και θέλουμε να βρούμε το `a%` του `x` κάνουμε:
\[
y = \frac{a}{100}\cdot x
\]

!!! note "Άσκηση: Σε ένα κατάστημα υπάρχουν γιορτινές προσφορές στα ηλεκτρονικά παιχνίδια και όλα τα παιχνίδια είναι 20% φθηνότερα. Γράψτε ένα πρόγραμμα που να βρίσκει την τιμή του κάθε παιχνιδιού μετά την έκπτωση αν ξέρετε πόσο έκανε πριν την έκπτωση."

### Σειρά των πράξεων

Η σειρά των πράξεων στην Python γίνεται όπως και στα μαθηματικά. Πρώτα γίνονται οι πολλαπλασιασμοί και οι διαιρέσεις (με τη σειρά που είναι γραμμένες), στη συνέχεια οι προσθέσεις και οι αφαιρέσεις.

Αν υπάρχουν πράξεις μέσα σε παρενθέσεις, θα γίνουν πρώτα αυτές. Σε περίπτωση που υπάρχουν παρενθέσεις μέσα σε παρενθέσεις, οι πράξεις γίνονται από μέσα προς τα έξω.

Δοκιμάστε τις παρακάτω πράξεις και δείτε τα αποτελέσματα:

```python
5 + 30 * 20 / 10
(5 + 30) * 20 / 10
(10 + (5 + 30) * 20) / 10
```

### Άλλοι τύποι μεταβλητών

Εκτός από απλές μεταβλητές με αριθμητικές τιμές, μπορούμε να έχουμε και πιο σύνθετες μορφές. Ας δούμε τους πιο βασικούς τύπους μεταβλητών.

## 3.2 Κείμενο (strings)

Σε μια μεταβλητή, εκτός από μια αριθμητική τιμή, μπορούμε να αποθηκεύσουμε και κείμενο. Οι μεταβλητές που περιέχουν κείμενο ονομάζονται strings. Είναι μια ειδική μορφή μεταβλητής γιατί στην πραγματικότητα αποτελούνται αποτελούνται από μια σειρά από χαρακτήρες. 

Για να δημιουργήσουμε τέτοιες μεταβλητές χρησιμοποιούμε τα μονά ή διπλά εισαγωγικά:

```python
end_message = "Game Over"
start_message = "Press Enter to continue..."
```

Για να δούμε την τιμή της κάθε μεταβλητής, χρησιμοποιούμε την εντολή `print`:

```python
print(end_message)
```

**Προσοχή**

* Όταν ξεκινάτε τον ορισμό ενός κειμένου με μονά ή διπλά εισαγωγικά, θα πρέπει να τελειώνετε με τα ίδια εισαγωγικά. Αν ξεκινάτε με μονά και τελειώνεται με διπλά εισαγωγικά, θα οδηγηθείτε σε σφάλμα.
* Δεν μπορείτε να ξεκινήσετε μια γραμμή με εισαγωγικά και να μην τα κλείσετε.
* Αν θέλετε μέσα στο κείμενό σας να υπάρχει το σύμβολο του εισαγωγικού, θα πρέπει να προηγηθεί μια κάθετος (back slash) "**\\**". Για παράδειγμα:

```python
message = "He said, \"Here take this gift! It isn\'t heavy.\""
print(message)
```

θα μας δώσει σαν αποτέλεσμα:

```bash 
He said, "Here take this gift! It isn't heavy."
```

*Σημείωση:* Η χρήση του backslash (\\) για να τυπώσετε τον χαρακτήρα αντί να τον χρησιμοποιήσετε σαν σύμβολο, λέγεται *escaping the character*.

* Αν ορίσετε το κείμενο με διπλά εισαγωγικά, μπορείτε να χρησιμοποιείτε μέσα στο κείμενο απλά εισαγωγικά χωρίς τη χρήση του backslash, και ανάποδα. Επίσης, μπορείτε να χρησιμοποιήσετε τρεις φορές το μονό εισαγωγικό (''') για να ορίσετε κείμενο.

```python
message = '''He said, "Here take this gift! It isn't heavy."'''
```

* Αν θέλετε να ορίσετε κείμενο με πολλές γραμμές μπορείτε να το κάνετε με την χρήση των τριών αποστρόφων όπως είπαμε παραπάνω.

```python
message = '''Welcome to my new game.
This is my first game! Press Enter to start!
Good luck!'''

print(message)
```

### Εισάγωντας τιμές μεταβλητών σε ένα κείμενο

Έστω ότι έχετε μια μεταβλητή `my_score` στην οποία κρατάτε τους πόντους σας στο παιχνίδι που φτιάχνετε. Θέλετε στο τέλος κάθε πίστας να ενημερώνετε τον παίκτη με ένα κείμενο, ποιο είναι το σκορ του. Φυσικά, θα μπορούσατε να τυπώσετε ένα μήνυμα και μετά το σκορ. Όμως μπορείτε να συνθέσετε και κείμενο που να περιέχει τιμές μεταβλητών, οπως φαίνεται στο παρακάτω παράδειγμα:

```python
my_score = 1000
message = "Congratulations! Stage 1 completed! Your score is %s points!"

print(message % my_score)  
```

Στο παραπάνω παράδειγμα, η παράμετρος `%s` στο κείμενο, σημαίνει ότι εδώ θα μπει τιμή μιας μεταβλητής. Δοκιμάστε το!

Αν έχετε παραπάνω από μια μεταβλητή που θέλετε να ενσωματώσετε στο κείμενό σας, τότε πρέπει οι τιμές στο `print` να μπουν σε παρένθεση.

```python
stage = 1
my_score = 1000
message = "Congratulations! Stage %s completed! Your score is %s points!"

print(message % (stage, my_score))
```

Πειραματιστείτε! Γράψτε μερικά κείμενα και τυπώστε τα χρησιμοποιώντας το IDLE.

## 3.2 Λίστες (lists)

Ας υποθέσουμε ότι θέλουμε να φτιάξουμε ένα πρόγραμμα όπου θα έχει τη λίστα με τα παιχνίδια με τις περισσότερες πωλήσεις. Σύμφωνα με την Wikipedia τα 10 παιχνίδια με τις περισσότερες πωλήσεις είναι:

1. Tetris (1984) (495 εκατομμύρια πωλήσεις)
2. Minecraft (122 εκατομμύρια πωλήσεις)
3. Wii Sports (82.7 εκατομμύρια πωλήσεις)
4. Grand Theft Auto V (75 εκατομμύρια πωλήσεις)
5. Super Mario Bros (40.24 εκατομμύρια πωλήσεις)
6. Mario Kart Wii (36.8 εκατομμύρια πωλήσεις)
7. Tetris (1989) (35 εκατομμύρια πωλήσεις)
8. Wii Sports Resor (32.8 εκατομμύρια πωλήσεις)
9. New Super Mario Bros (30.79 εκατομμύρια πωλήσεις)
10. The Elder Scrolls V: Skyrim (30 εκατομμύρια πωλήσεις)

Φυσικά, μπορούμε να γράψουμε τη λίστα αυτή σε μορφή κειμένου και να την τυπώσουμε, όπως παρακάτω:

```python
top_games = '''
Tetris (1984), 
Minecraft, 
Wii Sports, 
Grand Theft Auto V, 
Super Mario Bros, 
Mario Kart Wii, 
Tetris (1989), 
Wii Sports Resor, 
New Super Mario Bros, 
The Elder Scrolls V: Skyrim'''

print("Top 10 Games: %s" % top_games)
```

Όμως αυτή η λίστα δεν είναι εύκολα επεξεργάσιμη. Και αν θέλαμε να δούμε το παιχνίδι που βρίσκεται στην τρίτη θέση, θα έπρεπε να τα δούμε όλα και να μετρήσουμε μόνοι μας ποιο βρίσκεται στην θέση που ψάχνουμε. Γι' αυτό η Python μας δίνει τη δυνατότητα να δημιουργούμε λίστες με αντικείμενα, τις οποίες μπορούμε πιο εύκολα να χειριστούμε. 

Στην Python οι λίστες ορίζονται με αγκύλες **[]**.

Οπότε θα μπορούσαμε αντίστοιχα να κάνουμε:

```python
top_games =  ["Tetris (1984)", "Minecraft", "Wii Sports", 
"Grand Theft Auto V", "Super Mario Bros", "Mario Kart Wii", 
"Tetris (1989)", "Wii Sports Resor", "New Super Mario Bros", 
"The Elder Scrolls V: Skyrim"]

print(top_games[2])
```

**Σημαντικό:** Στην Python (όπως και στις περισσότερες γλώσσες προγραμματισμού) το μέτρημα ξεκινάει από το μηδέν (0). Που σημαίνει, αν θέλουμε να πάρουμε το πρώτο στοιχείο της λίστας μας, θα πούμε `top_games[0]`.

Μπορούμε φυσικά να τυπώσουμε και ολόκληρη τη λίστα: 

```python
print(top_games)

['Tetris (1984)', 'Minecraft', 'Wii Sports', 'Grand Theft Auto V', 
'Super Mario Bros', 'Mario Kart Wii', 'Tetris (1989)', 
'Wii Sports Resor', 'New Super Mario Bros', 'The Elder Scrolls V: Skyrim']
```

Μια λίστα μπορεί να περιέχει και αριθμούς και κείμενο, ακόμα και ανάμεικτα. Επίσης, μια λίστα μπορεί να αποτελείται από άλλες λίστες.

Ας πούμε ότι έχουμε λίστα με δυο αντικείμενα, το όνομα και το επίθετο ενός επιστήμονα. Αν θέλουμε να έχουμε μια λίστα με επιστήμονες θα λέγαμε:

```python
scientists = [
['Albert', 'Einstein'],
['Isaac', 'Newton'],
['Stephen', 'Hawking']
]
```

### Προσθέτοντας / αλλάζοντας αντικείμενα σε μια λίστα

Ένα πλεονέκτημα στην χρήση λιστών είναι ότι μπορούμε να προσθέσουμε, να αφαιρέσουμε και να τροποποιήσουμε τις τιμές σε μια λίστα. Για να προσθέσουμε αντικείμενα σε μια λίστα καλούμε την *μέθοδο* `.append()`, όπως στο ακόλουθο παράδειγμα:

```python
top_games.append('Diablo II')
```

Έτσι, στη λίστα μας προστέθηκε ακόμα ένα παιχνίδι. Όμως, αυτό που προσθέσαμε είναι λάθος. Γιατί στην πραγματικότητα την 11η θέση στη λίστα μας κατέχει το Diablo III με 30 εκατομμύρια πωλήσεις. Για να το διορθώσουμε αυτό, αλλάζουμε το ενδέκατο στοιχείο (δηλαδή αυτό που βρίσκεται στη θέση 10 - καθώς η μέτρηση ξεκινάει από το 0):

```python
top_games[10] = 'Diablo III'
```

Έτσι, μάθαμε πως προσθέτουμε στο τέλος ή αλλάζουμε τις τιμές μιας λίστας.

*Σημείωση:* Το `.append` προσθέτει νέο αντικείμενο στο τέλος της λίστας. Αν θέλουμε να προσθέσουμε ένα αντικείμενο σε μια συγκεκριμένη θέση, χρησιμοποιούμε το `.insert(index, value)`. Αυτό θα έχει σαν αποτέλεσμα, η νέα μας τιμή να μπει στη θέση *index* και όλα τα επόμενα αντικείμενα να μετακινηθούν μια θέση μετά. Παράδειγμα:

```python
numbers = [1, 2, 3, 4]
numbers.insert(2, 2.5)

#print(numbrs)
#[1, 2, 2.5, 3, 4]
```

### Διαγραφή στοιχείο από τη λίστα

Για την διαγραφή ενός αντικειμένου από συγκεκριμένη θέση μιας λίστας, χρησιμοποιούμε την εντολή `del`.

```python
del numbers[2]
```

Αυτό θα διαγράψει το στοιχείο που βρίσκεται στη θέση 2 της λίστας, δηλαδή τον αριθμό 2.5 που εισάγαμε παραπάνω.

### Πράξεις με λίστες

Υπάρχει η δυνατότητα να κάνουμε κάποιες πράξεις με τις λίστες. Αν έχουμε για παράδειγμα δυο λίστες, μπορούμε να τις προσθέσουμε και να πάρουμε μια νέα λίστα που να περιέχει τα αντικείμενα των δυο λιστών:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list1 + list2)

# [1, 2, 3, 4, 5, 6]
```

**Προσοχή:** Η πρόσθεση μπορεί να γίνει μόνο μεταξύ λιστών και όχι λίστας με απλό αριθμό. Δηλαδή αυτό `list1 + 5` θα ήταν λάθος.

Επίσης, μπορούμε να πολλαπλασιάσουμε μια λίστα με έναν αριθμό. Αυτό θα είχε ως αποτέλεσμα μια νέα λίστα με τα στοιχεία της αρχικής λίστας να επαναλαμβάνονται:

```python
print(list1 * 2)

# [1, 2, 3, 1, 2, 3]
```

**Προσοχή:** Ο πολλαπλασιασμός γίνεται μόνο μεταξύ λίστας και αριθμού και όχι μεταξύ λιστών.

Να θυμάστε ότι δεν μπορείτε να κάνετε αφαίρεση ή διαίρεση με λίστες.

## 3.3 Πλειάδες (tuples)

Ένα *tuple* είναι ακριβώς ό,τι και η λίστα με κάποιες διαφορές:

1. Τα *tuples* ορίζονται με παρένθεση αντί για αγκύλη `tuple1 = (1, 2, 3)`.

2. Τα *tuples* δεν αλλάζουν. Ορίζονται μια φορά και δεν μπορεί κάποιος να προσθέσει, αφαιρέσει ή να τροποποιήσει τα περιεχόμενά του.

Ακριβώς επειδή δεν μπορούν να τροποποιηθούν, τα *tuples* είναι σημαντικά, γιατί ο χρήστης είναι σίγουρος ότι το αποτέλεσμα που του έδωσε το πρόγραμμά του δεν έχει αλλάξει από κανέναν.

## 3.4 Λεξικά (dictionaries)

Το λεξικό, γνωστό και ως *dict*, *dictionary* ή *map* είναι επίσης μια συλλογή από αντικείμενα, όπως οι λίστες και οι πλειάδες. Η διαφορά στο λεξικό είναι ότι τα αντικείμενα είναι ζευγάρια *κλειδιού* => *τιμής* (*key* => *value*). Για να ορίσουμε ένα λεξικό, χρησιμοποιούμε τα άγκιστρα (γνωστά και ως μύστακες) **{}** και διαχωρίζουμε το κλειδί από την τιμή με άνω-κάτω τελεία **:**. Ας δούμε λίγο το παράδειγμα με τα παιχνίδια και τις πωλήσεις τους:

```python
top_games = {
'Tetris (1984)' : 495.0,
'Minecraft' : 122.0,
'Wii Sports' : 82.7,
'Grand Theft Auto V' : 75.0,
'Super Mario Bros' : 40.24,
'Mario Kart Wii' : 36.8,
'Tetris (1989)' : 35.0,
'Wii Sports Resor' : 32.8,
'New Super Mario Bros' : 30.79,
'The Elder Scrolls V: Skyrim': 30.0
}
```

Έτσι έχουμε σε ένα λεξικό την αντιστοίχηση του τίτλου του παιχνιδιού με τον αριθμό των πωλήσεων (σε εκατομμύρια).

**Προσοχή:** Όπως στις λίστες και τις πλειάδες είχαμε έναν αριθμό που έδειχνε τη θέση (index) της κάθε τιμής, εδώ έχουμε το κλειδί της κάθε τιμής. Οπότε αν θέλουμε να δούμε τον αριθμό των πωλήσεων πχ για το *Minecraft* αρκεί να πούμε:

```python
print(top_games['Minecraft'])

# 122.0
```

Αν θέλουμε να προσθέσουμε μια νέα τιμή αρκεί απλά να την ορίσουμε:

```python
top_games['Diablo III'] = 30.0
```

Αν θέλουμε να αλλάξουμε την τιμή για ένα κλειδί κάνουμε το ίδιο με παραπάνω. Απλά ορίζουμε τη νέα τιμή.

Αν θέλουμε να διαγράψουμε ένα αντικείμενο (ζευγάρι κλειδιού - τιμής) από το λεξικό, χρησιμοποιούμε την εντολή `del`:

```python
del top_games['Minecraft']
```

Δοκιμάστε όλα τα παραπάνω και εξασκηθείτε στην python. Να θυμάστε ότι όσο παίζετε με τα παραδείγματα, τόσο καλύτερα θα τα καταλάβετε.

Τα υπόλοιπα τμήματα του προγράμματος (δομές ελέγχου ροής, δομές επανάληψης, συναρτήσεις) θα τα δούμε αναλυτικά σε επόμενα κεφάλαια.

## Ασκήσεις

1. Δώστε σε μια μεταβλητή το όνομά σας και σε μια δεύτερη μεταβλητή το επίθετό σας. Δημιουργείστε ένα κείμενο (string) που να λέει "Hello, <onoma> <epitheto>" και να περιέχει τις τιμές των μεταβλητών που ορίσατε. Τυπώστε το κείμενο αυτό. 

2. Φτιάξτε μια λίστα με τα αγαπημένα σας χόμπι. Φτιάξτε μια δεύτερη λίστα με τα αγαπημένα σας φαγητά. Φτιάξτε μια τρίτη λίστα που θα είναι τα αγαπημένα σας χόμπι και φαγητά μαζί. Τυπώστε την τελευταία λίστα.

3. Φτιάξτε ένα λεξικό (dictionary) που να περιέχει τους 5 αγαπημένους σας ποδοσφαιριστές και τον αντίστοιχο αριθμό γκολ που βάλανε σε ένα πρωτάθλημα.<br>
Για όσους δεν ασχολούνται με ποδόσφαιρο, βρείτε μια συνταγή και δημιουργείστε ένα λεξικό με τα συστατικά τους και τα γραμμάρια που απαιτούνται για το καθένα.<br>
Τυπώστε το λεξικό που δημιουργήσατε.