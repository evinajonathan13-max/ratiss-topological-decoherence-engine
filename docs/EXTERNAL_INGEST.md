# Ingestion externe — Qiskit Statevector

Le Studio Cloud inclut un premier chemin d’entrée externe fonctionnel : une trajectoire de statevectors produite par Qiskit ou un export compatible peut être normalisée localement dans `timeline.v1`.

```bash
ratiss-topo-demo \
  --statevector-input examples/qiskit-bell-statevector-trajectory.json \
  --output artifacts/external_bell_timeline.json
```

Chaque étape doit contenir un `statevector` de longueur `2^n`, sous la forme de nombres réels, chaînes complexes, paires `[real, imag]` ou objets `{ "real": ..., "imag": ... }`. Le champ `gate` est conservé comme une étiquette de provenance. Sans métadonnée complète d’opération, l’adaptateur ne déduit pas une porte logique du noyau topologique RATISS.

| Source | Statut | Conversion | Limite |
|---|---|---|---|
| Statevector Qiskit | Fonctionnelle | Statevector → matrice densité → cube / graphe / topologie / timeline | L’import reste une donnée déclarée, pas une exécution QPU |
| Perceval photonique | Contrat à définir | Résultats de modes/interférences → matrice de relations | L’encodage modes ↔ nœuds doit être déclaré avant implémentation |
| Bio-cohérence | Contrat à définir | Matrices mesurées ou relations déclarées → timeline de structure | Aucun diagnostic biologique n’est inféré par le SDK |

L’adaptateur crée la provenance `external_qiskit_statevector`, laisse `validated_on_hardware=false` et exporte la source déclarée. Les trajectoires issues de matériel nécessiteraient, en plus, une preuve documentée du backend, des shots, du modèle de mesure, de la date et de l’identifiant de job avant toute formulation de validation.
