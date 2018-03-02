# Classwork 2

## Problem 1

1. We have a logical sentence, being in a knowledge base or otherwise, saying that that *entails* some other sentence $\alpha$ can be defined as: everywhere the knowledge base is true (i.e. in all of its models) so too is $\alpha$ true. We write $KB \models \alpha$ , or equivalently $M(KB)\subset M(\alpha)$ .

   In the light of the above, in order to show that resolution is *sound*, we need to show that it only derives clauses that are entailed by the knowledge base. In order to do this, we look at the idea of implication, whose truth table is as follows:

   | $P$  | $Q$  | $P\implies Q$ | $(P\implies Q) \land P$ |
   | ---- | ---- | ------------- | ----------------------- |
   | F    | F    | F             | F                       |
   | F    | T    | F             | F                       |
   | T    | F    | F             | F                       |
   | T    | T    | T             | T                       |

   We have included the truth table $(P\implies Q) \land P$ because, from *modus ponens*, we can derive $Q$. When we look at the models in which $(P\implies Q) \land P$ is true we see that it is a subset of those models in which $Q$ is ture (i.e. $\{row_4\} \subset \{row_2, row_4\}$). It follows from our original discussion that modus ponens is sound. Because resolution, is a general form of the modus ponens inference rule, this also means that resolution as a rule is sound $\square$.

2. If the knowledge base contained the two clauses `X` and `~X`, then no matter what the clause was that you were checking for entailment, you would reach the conclusion that the knowledge base entailed that clause.

## Problem 2

### Part 1

1. Forneybots were found to malfunction `M` if and only if they suffer water damage `D` or overheard a logical paradox `P`.

$M \iff (D \lor P)$

1. Forneybots may have been caught in a sudden rainstorm `R`, which are known to happen only during Winter `W` or Summer `S`, though not all Winters and Summers had rain.

$R \implies (W \lor S)$

1. It goes without saying that rainstorms and water damage would have gone hand in hand, since the Forneybots were not aware of their weakness.

$R \iff D$

1. Logical paradoxes, on the other hand, would have *only* been heard during election season (through TV or radio broadcast), which are held in the Fall `F` (and so all Fall seasons thus came hand in hand with paradoxes).

$P \iff F$

1. It also goes without saying that if it is one season, it cannot simultaneously be the others.

$(W \implies \lnot S \land \lnot F) \land (S \implies \lnot F \land \lnot W) \land (F \implies \lnot S \land \lnot W)$

1. The Great Forneybots Uprising occurred from a mass malfunction on Nov. 16, 2024.

$F \land M$

### Part 2

1. $(\lnot M \lor D \lor P) $
2.  $(M \lor \lnot D) $  
3. $(M \lor \lnot P)$
2. $(\lnot R \lor W \lor S)$
5. $(\lnot R \lor D) $ 
6. $ (\lnot D \lor R)$
7. $(\lnot P \lor F) $
8. $ (\lnot F \lor P)$
9. $(\lnot W \lor \lnot S) $
10. $ (\lnot W \lor \lnot F)$ 
11. $ (\lnot F \lor \lnot S)$
12. $F$
13. $M$

### Part 3

#### Test for $\alpha=\lnot D \land P$: Assume $\lnot \alpha= D \lor \lnot P$

14. $D \lor \lnot P$
15. $\lnot M \lor D$ [1, 14]
16. $\emptyset$              [2, 15]

**Therefore, **by contradiction, $\alpha$ is true.

#### Test for $\beta=\lnot P \land D$: Assume $\lnot \beta=P \lor \lnot D$

Since this statements is exactly the opposite of $\alpha$, and we have shown this to lead to a contradiction, then $\beta$ must be false.