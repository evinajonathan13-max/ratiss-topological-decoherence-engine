# RATISS Quantum Topology Studio Cloud

**RATISS Quantum Topology Studio Cloud** est le studio complet de la famille RATISS. Il réunit dans un seul dépôt clonable le modèle de conception Quantum Circuit Studio, la simulation locale en matrice densité, la cartographie topologique RATISS, la signature de qubit logique simulé, la criticité, les routes d’inspection et les adaptateurs de trajectoires externes.

> Ce dépôt prolonge directement le simulateur de qubit topologique trouvé dans la branche RATISS Experimental IA `decoherence-map` au commit `c67d2e7`. Le code source RATISS initial n’est pas modifié. La carte de provenance est disponible dans [`docs/SOURCE_REUSE_MAP.md`](docs/SOURCE_REUSE_MAP.md).

## Ce que le SDK fait aujourd’hui

| Capacité | Implémentation actuelle | Sortie |
|---|---|---|
| Circuit local | Qiskit Aer en mode matrice densité, avec référence idéale et trajectoire bruitée | Une observation par étape de porte |
| Cube | `M[k,i,j] = min(1, I(ρij)/2)` | Tranches `cube_slice` par pas temporel |
| Graphe | Liens issus d’information mutuelle, corrélations de Pauli et concurrence | Nœuds, tubes, degrés et stabilité |
| Topologie du graphe | Rips transparent, Betti et persistance H1 finie | `topology.psig`, diagrammes et Betti |
| Noyau RATISS | Qubit topologique logique simulé en anneau tordu, portes analogues et bruit logiciel | `logical_topology.P_sig`, protection, bit logique |
| Criticité | Composition transparente fidélité / force de graphe / rupture de liens | Nœuds critiques documentés |
| Inspection | TSP exact Hold–Karp ou heuristique déterministe | `tsp_inspection`, explicitement séparé de `P_sig` |
| Portabilité | Artefact JSON versionné | Chargement hors ligne dans `ratiss-decoherence-atlas` |

## Démarrage local et profil Cloud

Le moteur est conçu pour une exécution CPU locale. Les dépendances nécessaires sont Qiskit, Qiskit Aer, NumPy et SciPy.

```bash
git clone https://github.com/evinajonathan13-max/ratiss-topological-decoherence-engine
cd ratiss-topological-decoherence-engine
python3 -m venv .venv
source .venv/bin/activate              # Windows PowerShell : .\.venv\Scripts\Activate.ps1
pip install -e .
ratiss-studio-cloud
```

Ouvrir ensuite `http://127.0.0.1:8765`. Le Studio Cloud démarre localement par défaut ; il peut ensuite être placé sur une machine Linux plus puissante sans changer son contrat d’artefact. Il n’impose aucun fournisseur cloud au runtime.

Pour produire seulement une timeline depuis le terminal :

```bash
ratiss-topo-demo --output artifacts/full_timeline.json
ratiss-topo-demo --studio-input examples/transmon-microcell.studio.json --output artifacts/studio_timeline.json
ratiss-topo-demo --statevector-input examples/qiskit-bell-statevector-trajectory.json --output artifacts/external_bell_timeline.json
ratiss-topo-demo --counts-input examples/qiskit-counts-trajectory.json --output artifacts/qiskit_counts_timeline.json
ratiss-topo-demo --photon-input examples/photonic-mode-trajectory.json --output artifacts/photonic_modes_timeline.json
ratiss-topo-demo --bio-input examples/bio-correlation-trajectory.json --output artifacts/bio_correlation_timeline.json
```

Sans installation de package, l’exemple peut aussi être lancé depuis une copie de travail :

```bash
PYTHONPATH=src python3 -m ratiss_topological_decoherence.cli --output artifacts/full_timeline.json
PYTHONPATH=src pytest
```

## Architecture

```mermaid
flowchart LR
  A[Programme de portes] --> B[Qiskit Aer\nmatrice densité idéale + bruitée]
  B --> C[Réductions rho_i et rho_ij]
  C --> D[Cube M step × qubit × qubit\ninformation mutuelle normalisée]
  D --> E[Graphe de corrélations]
  E --> F[Rips / Betti / P_sig de graphe]
  B --> G[Scores locaux\nfidélité, pureté, criticité]
  H[TopologicalQubit RATISS\nanneau, torsion, bruit] --> I[Signature logique P_sig]
  G --> J[Nœuds critiques]
  J --> K[Route TSP d’inspection]
  F --> L[Artefact timeline.v1]
  I --> L
  K --> L
  L --> M[Atlas WebGL hors ligne]
```

Le `P_sig` de graphe et le `P_sig` du noyau logique sont toujours exportés comme deux valeurs distinctes. Cette distinction évite de présenter un changement dans une couche comme une mesure de l’autre.

## Exemple de résultat du POC fourni

Le scénario livré par défaut est `accelerated_decoherence_stress_demo`. Il est volontairement accéléré pour rendre les ruptures visibles sur onze étapes et donc tester le lecteur d’artefacts ; il ne reproduit pas la durée de porte d’un QPU spécifique.

| Observation du run de référence local | Valeur exportée | Interprétation exacte |
|---|---:|---|
| Étapes | 11 | Initialisation plus dix portes du circuit de démonstration |
| Signature logique initiale | `1.214` | `P_sig` du qubit topologique logique simulé RATISS |
| Signature logique finale | `0.766` | Dégradation dans le modèle de bruit logiciel du noyau logique |
| Topologie de graphe finale | Betti `[1,0,0]`, `P_sig=0.000` | Le graphe issu de cette trajectoire ne contient pas de cycle H1 fini persistant à cette étape |
| Route d’inspection finale | `3 → 4 → 3` | TSP exact sur deux nœuds qui dépassent le seuil de criticité du scénario ; **ce n’est pas `P_sig`** |

## Interfaces principales

```python
from ratiss_topological_decoherence import SimulationConfig, run_local_demo
from ratiss_topological_decoherence.logical_qubit import TopologicalQubit

artifact = run_local_demo(SimulationConfig())
logical_qubit = TopologicalQubit(protection=0.15, seed=42)
signature = logical_qubit.h_gate().noise(0.05).measure_state()
```

Le détail des champs et contrats se trouve dans [`docs/API_REFERENCE.md`](docs/API_REFERENCE.md). Les limites de portée, les seuils et la séparation TSP/persistance sont décrits dans [`docs/ARCHITECTURE_CONTRACT.md`](docs/ARCHITECTURE_CONTRACT.md).

## Deux studios, un contrat

Le Studio Cloud est autonome : sa copie traçable du modèle Quantum Circuit Studio est incluse sous `web/studio-model.mjs`, son interface réunit le schéma, les couches, fréquences, diaphonie nominale, la simulation RATISS, les métriques et le WebGL. Le Studio Personnel est un second dépôt autonome et léger qui sait concevoir localement, importer les mêmes timelines et les rejouer hors ligne.

Le contrat complet est détaillé dans [`docs/TWO_STUDIOS_CONTRACT.md`](docs/TWO_STUDIOS_CONTRACT.md).

## Réutilisation et extension

Le SDK prépare trois types d’entrée, avec une frontière nette :

| Entrée | Statut | Chemin d’extension |
|---|---|---|
| Circuit simulé | Fonctionnel localement | Personnaliser la liste de `GateSpec` ou fournir un programme compatible |
| Résultats mesurés / QPU | Adaptateur à construire, optionnel | Convertir les comptes Pauli ou matrices d’état vers `timeline.v1`, sans jeton dans le dépôt |
| Comptages Qiskit | Association classique déclarée | Convertir une distribution de mesures vers une structure de co-occurrence, sans tomographie ni entanglement inférés |
| Modes photoniques | Association de co-occupation déclarée | Convertir des probabilités d’occupation de modes vers une structure de relations, sans matrice densité photonique inférée |
| Corrélations bio ou autre phénomène fourni | Matrices déclarées normalisées | Importer une trajectoire de relations/corrélations avec protocole de mesure, sans diagnostic biomédical |

## Portée et honnêteté

Le dépôt ne fabrique pas de qubit matériel, ne constitue pas un modèle de fabrication, ne déclenche aucune correction matérielle et ne remplace pas une expérience QPU. Son apport actuel est un **SDK local d’analyse topologique et de visualisation** fondé sur un simulateur logique RATISS existant, enrichi d’une matrice densité, d’artefacts versionnés et d’un atlas WebGL indépendant.

## Documents

| Document | Contenu |
|---|---|
| [`ARCHITECTURE_CONTRACT.md`](docs/ARCHITECTURE_CONTRACT.md) | Maths, matrice cubique, topologie, criticité, TSP et profils local/connectable |
| [`SOURCE_REUSE_MAP.md`](docs/SOURCE_REUSE_MAP.md) | Provenance RATISS de chaque brique réutilisée |
| [`API_REFERENCE.md`](docs/API_REFERENCE.md) | API Python, contrat JSON et règles de compatibilité |
| [`PROOF_OF_CONCEPT.md`](docs/PROOF_OF_CONCEPT.md) | Protocole, résultat du run, tests et interprétation |
| [`INTEGRATION_GUIDE.md`](docs/INTEGRATION_GUIDE.md) | Intégration locale, atlas et futur adaptateur externe |
| [`STUDIO_INTEGRATION_CONTRACT.md`](docs/STUDIO_INTEGRATION_CONTRACT.md) | Compilation du modèle Quantum Circuit Studio vers une timeline RATISS |
| [`TWO_STUDIOS_CONTRACT.md`](docs/TWO_STUDIOS_CONTRACT.md) | Répartition Studio Cloud / Studio Personnel et compatibilité |
| [`EXTERNAL_INGEST.md`](docs/EXTERNAL_INGEST.md) | Adaptateur Qiskit Statevector fonctionnel et frontières Perceval / bio-cohérence |
| [`CLOUD_STUDIO_VERIFICATION.md`](docs/CLOUD_STUDIO_VERIFICATION.md) | Vérification UI du Studio Cloud unifié |
