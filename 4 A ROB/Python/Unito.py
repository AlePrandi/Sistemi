''''
    Algoritmo di Gale-Shapley per il matrimonio stabile
    Versione parametrica rispetto al gruppo proponente


    N = intero positivo fissato (nell'esempio N = 4)
    P = insieme di N propoponenti
    R = insieme di N riceventi (le proposte)
    
    Pref = {>p, >r | p in P, r in R} dove 
    >p e' l'ordine totale su R delle preferenze di p
    >r e' l'ordine totale su P delle preferenze di r

    M = matching parziale: insieme di coppie in P x R t.c. 
        ogni p ed ogni r occorre una sola volta

    p in P e' libero secondo M se non esiste r t.c. (p,r) in M 
    r in R e' libero secondo M se non esiste p t.c. (p,r) in M

    Pesudocodice:

    M := 0 // tutti i p ed r sono liberi secondo M
    while esiste p in P libero secondo M
        r := il massimo secondo >p cui p non abbia fatto proposte
        if r e' libero secondo M 
            then M := M + {(p,r)}
            else sia (p',r) in M
                if p >r p' 
                    then M := M - {(p',r)} + {(p,r)}
                    else r rifiuta la proposta di r // dunque M rimane invariato
    return M

    Def. Siano M(p) e' il solo r cui e' associato p in M (se esiste) e
    M(r) il solo p cui e' associato r. La coppia (p, r) e' instabile se

        p >r M(r)  e  r >p M(p)
    
    M e' stabile se non contiene coppie instabili.

    Teorema: l'algoritmo termina restituendo M stabile con |M| = N.
'''

N = 4  # cardinalita' di P ed R

# P e' rappresentato dagli interi 0, ... , N - 1
# R e' rappresentato dagli interi N, ... , 2N - 1

# Pref e' una matrice 2N x N dove
# se p in P = 0, ... , N - 1 allora
#   Pref[p] elenca le preferenze di p in R dalla maggiore alla minore:
#       r >p r' <==> i < j dove r = Pref[p][i] e r' = Pref[p][j]
# se r in R = N, ... , 2N - 1 allora
#   Pref[r] elenca le preferenze di r in P dalla maggiore alla minore:
#       p >r p' <==> h < k dove p = Pref[r][h] e p' = Pref[r][k]


# prefers(a, b1, b2, Pr) = True se b1 >a b2 nella tabella Pr

def prefers(a, b1, b2, Pr):
    for i in range(N):
        if Pr[a][i] == b1:
            break
    for j in range(N):
        if Pr[a][j] == b2:
            break
    return i < j


def stableMarriage(pref):

    # match[a] = b se a e b sono impegnati; -1 altrimenti
    match = [-1 for i in range(2*N)]

    # next[p] = il prossimo r in R cui p puo' fare la proposta
    next = [0 for i in range(N)]

    freeProp = N  # numero dei proponenti liberi, inizialmente N

    # inserire qui il codice per completare ...
    while freeProp > 0:
        for p in range(N):
            if match[p] == -1:  # p e' libero
                break 
    
    r = pref[p][next[p]]
    next[p] += 1
    if match[r] == -1:
        match[p] = r
        match[r] = p 
        freeProp -= 1
    else:
        p1 = match[r]
        if prefers(r, p, p1, pref):
            match[p] = r
            match[r] = p
            match[p1] = -1
            freeProp += 1

    return match

# ---------- Routine per la visualizzazione degli esempi ----------


N = 4


def initProposing():
    return 0, 1, 2, 3


def initReceiving():
    return 4, 5, 6, 7


def NameKtoQ(n):
    if n == 0:
        return "Kf"
    elif n == 1:
        return "Kq"
    elif n == 2:
        return "Kc"
    elif n == 3:
        return "Kp"
    elif n == 4:
        return "Qf"
    elif n == 5:
        return "Qq"
    elif n == 6:
        return "Qc"
    else:
        return "Qp"


def NameQtoK(n):
    if n == 0:
        return "Qf"
    elif n == 1:
        return "Qq"
    elif n == 2:
        return "Qc"
    elif n == 3:
        return "Qp"
    elif n == 4:
        return "Kf"
    elif n == 5:
        return "Kq"
    elif n == 6:
        return "Kc"
    else:
        return "Kp"


def printMarriageKtoQ(match):
    for p in range(N):
        print(NameKtoQ(p), "\t", NameKtoQ(match[p]))


def printMarriageQtoK(match):
    for p in range(N):
        print(NameQtoK(match[p]), "\t", NameQtoK(p))

# ----------  Esempi -------------


N = 4

# Regine: Qx con  x in {c = cuori, q = quadri, f = fiori, p = picche}
Qf, Qq, Qc, Qp = initProposing()
# Re:     Kx con x in {c = cuori, q = quadri, f = fiori, p = picche}
Kf, Kq, Kc, Kp = initReceiving()

# Versione tratta dal documentario BBC

BBCQ = [[Kp, Kf, Kq, Kc],  # Qf
        [Kp, Kf, Kq, Kc],  # Qq
        [Kf, Kq, Kp, Kc],  # Qc
        [Kp, Kq, Kc, Kf],  # Qp

        [Qf, Qq, Qc, Qp],  # Kf
        [Qc, Qq, Qp, Qf],  # Kq
        [Qq, Qc, Qf, Qp],  # Kc
        [Qq, Qc, Qf, Qp]  # Kp
        ]

BBCMatch = stableMarriage(BBCQ)
print("Matrimonio stabile (BBC): Q propone a K")
printMarriageQtoK(BBCMatch)

# Esempio per dimostrare l'asimmetria tra proponenti e riceventi

# Re:     Kx con x in {c = cuori, q = quadri, f = fiori, p = picche}
Kf, Kq, Kc, Kp = initProposing()
# Regine: Qx con  x in {c = cuori, q = quadri, f = fiori, p = picche}
Qf, Qq, Qc, Qp = initReceiving()

KtoQ = [[Qq, Qf, Qc, Qp],  # Kf
        [Qq, Qc, Qf, Qp],  # Kq
        [Qf, Qc, Qq, Qp],  # Kc
        [Qc, Qf, Qq, Qp],  # Kp

        [Kq, Kf, Kc, Kp],  # Qf
        [Kc, Kq, Kf, Kp],  # Qq
        [Kf, Kc, Kq, Kp],  # Qc
        [Kc, Kf, Kq, Kp]  # Qp
        ]

MatchKtoQ = stableMarriage(KtoQ)
print("Esempio asimmetrico: K propone a Q")
printMarriageKtoQ(MatchKtoQ)


# Regine: Qx con  x in {c = cuori, q = quadri, f = fiori, p = picche}
Qf, Qq, Qc, Qp = initProposing()
# Re: Kx con x in {c = cuori, q = quadri, f = fiori, p = picche}
Kf, Kq, Kc, Kp = initReceiving()

QtoK = [[Kq, Kf, Kc, Kp],  # Qf
        [Kc, Kq, Kf, Kp],  # Qq
        [Kf, Kc, Kq, Kp],  # Qc
        [Kc, Kf, Kq, Kp],  # Qp

        [Qq, Qf, Qc, Qp],  # Kf
        [Qq, Qc, Qf, Qp],  # Kq
        [Qf, Qc, Qq, Qp],  # Kc
        [Qc, Qf, Qq, Qp]  # Kp
        ]

MatchQtoK = stableMarriage(QtoK)
print("Esempio asimmetrico: Q propone a K")
printMarriageQtoK(MatchQtoK)
