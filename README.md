# tax_record_number

Είναι γνωστό ότι αρκετός κόσμος χρησιμοποιεί το ΑΦΜ του σαν password σε διάφορα πράγματα 
(αρκετά συνηθισμένο φαινόμενο σε accesss points).
Άρα ένας pentester στην Ελλάδα θα ήταν καλή ιδέα να έχει πρόσβαση σε μια λίστα με όλα τα πιθανα afm (δεν ξέρεις ποτέ).  

Αυτό το script υπολογίζει όλα τα (100.000.000) πιθανά ΑΦΜ της Ελλάδας, με βάση τον αλγόριθμο με τον οποίο εκδίδονται. 
Η wordlist που θα προκύψει θα έχει μέγεθος 1GB και ανάλογα με το μηχάνημά σας μπορεί να πάρει λίγο χρόνο να παραχθεί.

Να σημειωθεί, ότι στο μηχάνημα που τέσταρα το script (i5 και 8gb ram), 
1ον) χρειάστηκαν περίπου 10 λεπτά για να τελειώσει τo script, και, 
2ον το μηχάνημα "hangαρε" μετά από κάποιο σημείο, όταν φαγώθηκε όλη η ram. 
Οπότε λίγο υπομονή.

Θα ανέβαζα την ίδια την λίστα αλλά ο χώρος στο github είναι περιορισμένος, και το script είναι in any case πιο portable.

Σημείωση: είναι για python 2.7
