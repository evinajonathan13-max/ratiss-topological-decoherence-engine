# RATISS Quantum Topology Studio Cloud

> **Un studio unique pour concevoir un circuit, rejouer une trajectoire de simulation, cartographier ses relations topologiques et produire un artefact explicable.**

Le **RATISS Quantum Topology Studio Cloud** rassemble dans un dépôt clonable le modèle de conception de Quantum Circuit Studio, un moteur local à matrice densité, le noyau de qubit topologique logique RATISS, l’analyse de graphe, l’inspection TSP et quatre chemins d’ingestion externe. Il est nommé *Cloud* parce qu’il peut être déployé sur une machine plus puissante ; son démarrage par défaut reste **local-first**, sans fournisseur cloud obligatoire.

> Le projet est un environnement de **simulation et d’inspection logicielle**. Il ne fabrique pas de puce, ne calibre pas de dispositif, ne corrige pas un qubit physique et ne remplace pas une expérience matérielle.

![Espace de travail complet RATISS Quantum Topology Studio Cloud après une simulation interne](docs/media/cloud-studio-workspace.webp)

> **Preuve visuelle de l’interface complète.** Cette capture réelle montre, dans le même espace de travail, le document `transmon-microcell`, le schéma Quantum Studio, la scène topologique WebGL, la timeline RATISS, les métriques, l’overlay de diaphonie nominale et la console de provenance après une simulation interne. Les champs affichés conservent leurs limites : simulation à matrice densité et post-traitement topologique, sans certification matérielle.

## Pourquoi un studio unifié ?

Les chercheurs et développeurs ont besoin d’un chemin court entre une hypothèse de conception et une visualisation inspectable. Ici, un même document de circuit sert de source de conception, est compilé dans un scaffold logique déclaré, puis donne une timeline versionnée relue par l’interface WebGL. La séparation entre les couches reste explicite : **le Studio décrit un design**, le **moteur simule un modèle**, puis l’**Atlas rejoue les sorties calculées**.

| Couche | Ce que le dépôt fait | Ce qu’il ne prétend pas faire |
|---|---|---|
| Conception | Schéma, couches conceptuelles, fréquences nominales, risque de diaphonie et export JSON | Solveur électromagnétique, layout de fonderie ou calibration |
| Simulation | Évolution locale à matrice densité, état idéal/bruité et réductions de sous-systèmes | Exécution équivalente à un QPU réel |
| Cartographie | Cube temporel, graphe de relations, Betti, `P_sig`, criticité et TSP | Observable matérielle directe ou métrique universelle de performance |
| Noyau logique | Qubit topologique RATISS simulé, anneau/torsion/bruit logiciel et signature logique | Qubit topologique matériel démontré |
| Ingestion | Statevectors, comptages, distributions photoniques, matrices de corrélation déclarées | Tomographie, entanglement ou diagnostic inféré lorsqu’ils ne sont pas fournis |

## Interface Studio complète : conception et cartographie dans le même flux

Le Studio ne remplace pas le concepteur de circuit par une vue décorative. La colonne de conception garde le schéma, les composants, les couches conceptuelles, les fréquences nominales, la détection de collision et l’overlay de diaphonie. Le panneau de travail expose simultanément le schéma et la topologie produite par une simulation ; la ligne de temps conserve enfin les métriques de graphe, la signature logique, les nœuds critiques et la route TSP d’inspection.

| Zone visible dans l’interface | Fonction réelle | Frontière scientifique affichée |
|---|---|---|
| Conception Quantum Studio | Démo, ajout de transmon, optimisation heuristique et export JSON | Ni layout de fonderie, ni solveur EM, ni recette de fabrication |
| Schéma et couches | Composants, couplers, résonateurs, feedlines et proxies de couches | Représentation de conception, pas géométrie certifiée de puce |
| Risques fréquentiels et diaphonie | Séparation nominale et score d’overlay explicite | Ni mesure, ni calibration électromagnétique |
| Simulation et scène WebGL | Timeline versionnée, graphe, criticité, `P_sig` et signature logique | Résultats de simulation / post-traitement, pas QPU |
| Console de compilation | Scaffold logique, provenance et carte Studio → RATISS | N’interprète pas un scaffold comme une séquence de pulses |

## Démarrage en moins de cinq minutes

Le Studio Cloud fonctionne sur Python 3.11+ avec Qiskit Aer, NumPy et SciPy. Créez un environnement isolé, installez le paquet, puis lancez l’interface :

```bash
git clone https://github.com/evinajonathan13-max/ratiss-topological-decoherence-engine
cd ratiss-topological-decoherence-engine
python3 -m venv .venv
source .venv/bin/activate              # Windows PowerShell : .\.venv\Scripts\Activate.ps1
pip install -e .
ratiss-studio-cloud
```

Ouvrez ensuite `http://127.0.0.1:8765`. Pour tester le profil photonique direct local, installez l’extra optionnel :

```bash
pip install -e '.[photonic]'
```

| Commande | Produit |
|---|---|
| `ratiss-topo-demo --output artifacts/full_timeline.json` | POC local à matrice densité |
| `ratiss-topo-demo --studio-input examples/transmon-microcell.studio.json --output artifacts/studio_timeline.json` | Chemin interne Quantum Circuit Studio → timeline |
| `ratiss-topo-demo --statevector-input examples/qiskit-bell-statevector-trajectory.json --output artifacts/bell.json` | Import Statevector Qiskit |
| `ratiss-topo-demo --counts-input examples/qiskit-counts-trajectory.json --output artifacts/counts.json` | Comptages, associations classiques seulement |
| `ratiss-topo-demo --photon-input examples/photonic-mode-trajectory.json --output artifacts/photon.json` | Co-occupations de modes déclarées |
| `ratiss-topo-demo --bio-input examples/bio-correlation-trajectory.json --output artifacts/correlation.json` | Matrices de corrélation déclarées |
| `ratiss-topo-demo --ttf-smooth-ablation artifacts/full_timeline.json --output-dir artifacts/ttf_smooth_ablation` | Référence et régularisation TTF séparées |

## Démonstrations WebGL visibles directement dans ce README

GitHub Markdown ne peut pas exécuter une page HTML/WebGL interactive dans un README. Pour rendre le fonctionnement visible immédiatement, les deux expériences ci-dessous sont de **vrais aperçus animés** assemblés depuis les captures de leurs rendus WebGL et leurs contrôles réels. Un clic ouvre la vidéo WebM correspondante ; l’expérience interactive complète reste disponible localement après le démarrage du Studio.

### Démonstration 01 — document Quantum Studio → timeline topologique

[![Aperçu animé réel de la trajectoire Cloud : design, scènes WebGL et métriques](docs/media/cloud-trajectory-webgl-preview.gif)](docs/media/cloud-trajectory-webgl.webm)

Cette animation rejoue trois états affichés par la démo Cloud, de l’initialisation à `cz(0,1)`. Elle montre le design `transmon-microcell`, ses couches et hypothèses nominales à gauche, puis la scène de relations et les métriques de timeline. Ouvrez l’expérience interactive après `ratiss-studio-cloud` : [`http://127.0.0.1:8765/demos/decoherence-trajectory.html`](http://127.0.0.1:8765/demos/decoherence-trajectory.html).

### Démonstration 02 — référence TTF et régularisation de graphe

[![Aperçu animé réel de l’ablation TTF Cloud : référence puis régularisation](docs/media/cloud-ttf-webgl-preview.gif)](docs/media/cloud-ttf-webgl.webm)

L’aperçu alterne les deux scénarios versionnés : `ttf_smooth_baseline` puis `ttf_smooth_regularized`. Le design reste affiché pendant la comparaison afin de ne pas confondre une ablation de graphe avec une modification physique d’un circuit. L’expérience interactive se lance localement à [`http://127.0.0.1:8765/demos/ttf-comparison.html`](http://127.0.0.1:8765/demos/ttf-comparison.html).

| Démonstration | Média intégré | Vidéo | Interaction locale |
|---|---|---|---|
| Trajectoire de conception → topologie | [`GIF animé`](docs/media/cloud-trajectory-webgl-preview.gif) | [`WebM`](docs/media/cloud-trajectory-webgl.webm) | Timeline, rotation, zoom et reset caméra |
| Ablation TTF | [`GIF animé`](docs/media/cloud-ttf-webgl-preview.gif) | [`WebM`](docs/media/cloud-ttf-webgl.webm) | Référence/régularisation, timeline, rotation et zoom |

Le catalogue détaillé, les artefacts source et les vérifications se trouvent dans [`docs/DEMO_CATALOG.md`](docs/DEMO_CATALOG.md) et dans la [vérification visuelle versionnée](docs/DEMO_VISUAL_AUDIT.md).

## Le pipeline de données

```mermaid
flowchart LR
  A[Document Quantum Circuit Studio] --> B[Importeur interne]
  B --> C[Scaffold logique déclaré]
  C --> D[Qiskit Aer\nréférence idéale et bruitée]
  D --> E[Réductions rho_i / rho_ij]
  E --> F[Cube M[k,i,j]]
  F --> G[Graphe de relations]
  G --> H[Rips / Betti / P_sig]
  D --> I[Fidélité, pureté et criticité]
  J[Noyau TopologicalQubit RATISS] --> K[Signature logique]
  I --> L[Ensemble d’inspection]
  L --> M[TSP séparé]
  H --> N[Timeline versionnée]
  K --> N
  M --> N
  N --> O[Studio Personnel / WebGL]
```

La matrice principale est une série cubique de relations :

\[
M[k,i,j] = \min\left(1, \frac{I(\rho_{ij})}{2}\right)
\]

où `k` est l’étape de la trajectoire, `i` et `j` deux qubits, et `I(ρij)` l’information mutuelle dérivée des réductions de densité. Cette formule est employée par le chemin de simulation densité ; les imports non-densité portent un type de relation différent et ne reçoivent jamais par défaut des métriques de fidélité ou d’entanglement.

## Preuves calculées livrées avec le dépôt

Le scénario par défaut `accelerated_decoherence_stress_demo` rend les ruptures assez visibles pour tester l’interface ; ses durées ne reproduisent pas un QPU précis. Les valeurs ci-dessous proviennent des artefacts versionnés, pas d’une décoration de documentation.

| Observation locale | Valeur exportée | Portée exacte |
|---|---:|---|
| Nombre d’étapes du POC | `11` | Initialisation et dix portes du circuit de démonstration |
| Signature logique initiale | `1.214` | `P_sig` du noyau topologique logique simulé RATISS |
| Signature logique finale | `0.766` | Sortie du modèle de bruit logiciel du noyau logique |
| Graphe final | Betti `[1, 0, 0]`, `P_sig = 0.000` | Aucun cycle H1 fini persistant détecté dans ce graphe, à ce seuil et cette étape |
| Route terminale | `3 → 4 → 3` | Inspection exacte Hold–Karp de nœuds critiques ; ce n’est pas `P_sig` |
| Ablation TTF, support terminal | `0.118 → 1.006` | Comparaison de deux graphes logiciels ; pas une correction d’erreur quantique |

Le `P_sig` du graphe et la signature du qubit logique sont deux champs distincts. Une variation dans l’un ne justifie jamais une conclusion automatique sur l’autre. Les détails de protocole sont consignés dans [`docs/PROOF_OF_CONCEPT.md`](docs/PROOF_OF_CONCEPT.md) et [`docs/TTF_SMOOTH_STABILIZATION.md`](docs/TTF_SMOOTH_STABILIZATION.md).

## API, formats et adaptations

```python
from ratiss_topological_decoherence import SimulationConfig, run_local_demo
from ratiss_topological_decoherence.logical_qubit import TopologicalQubit

timeline = run_local_demo(SimulationConfig())
logical = TopologicalQubit(protection=0.15, seed=42)
signature = logical.h_gate().noise(0.05).measure_state()
```

Les adaptateurs traduisent un format d’entrée déclaré vers le contrat `ratiss.topological-decoherence.timeline.v1` :

| Entrée | Calculé par l’adaptateur | Limite encodée |
|---|---|---|
| Statevector Qiskit | Matrices densité et relations dérivées | Un statevector de simulation n’est pas une validation de matériel |
| Comptages Qiskit | Association classique diagonale et covariance de bits | Pas de cohérence hors diagonale, tomographie ni entanglement déduits |
| Perceval / modes photoniques | Co-occupations de modes déclarées ou distribution locale | Pas de matrice densité photonique inventée |
| Corrélations bio | Matrices normalisées fournies par l’appelant | Pas de diagnostic, de causalité ou d’interprétation biomédicale |

Consultez [`docs/API_REFERENCE.md`](docs/API_REFERENCE.md), [`docs/INGESTION_CONTRACTS.md`](docs/INGESTION_CONTRACTS.md) et [`docs/EXTERNAL_INGEST.md`](docs/EXTERNAL_INGEST.md) avant d’intégrer une source externe.

## Architecture documentaire

| Document | Contenu |
|---|---|
| [`docs/ALGORITHM_GUIDE.md`](docs/ALGORITHM_GUIDE.md) | Algorithmes, frontières de métriques, cube, graphe, TSP et noyau logique |
| [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) | Recettes de reproduction, tests, artefacts et résultats attendus |
| [`docs/ARCHITECTURE_CONTRACT.md`](docs/ARCHITECTURE_CONTRACT.md) | Contrat de données et modèles d’exécution |
| [`docs/STUDIO_INTEGRATION_CONTRACT.md`](docs/STUDIO_INTEGRATION_CONTRACT.md) | Chemin Quantum Circuit Studio interne |
| [`docs/SOURCE_REUSE_MAP.md`](docs/SOURCE_REUSE_MAP.md) | Provenance de chaque composant RATISS réutilisé |
| [`docs/TWO_STUDIOS_CONTRACT.md`](docs/TWO_STUDIOS_CONTRACT.md) | Compatibilité Studio Cloud / Studio Personnel |
| [`docs/DEMO_CATALOG.md`](docs/DEMO_CATALOG.md) | Démonstrations, captures et artefacts WebGL |
| [`docs/EVIDENCE_INDEX.md`](docs/EVIDENCE_INDEX.md) | Lien entre capacités, fichiers, tests et frontières de validation |

## Tests et reproduction

```bash
PYTHONPATH=src pytest
node --check web/demos/trajectory-demo.js
```

Les tests couvrent le pipeline de simulation, la persistance, le TSP, le noyau logique, l’import Studio, les statevectors, les comptages, les distributions photoniques, les corrélations déclarées et l’ablation TTF. Les scripts et résultats attendus sont détaillés dans [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md).

## Licence et attribution

Ce dépôt est publié sous [licence MIT](LICENSE). La provenance des composants RATISS et du modèle Quantum Circuit Studio est documentée dans les cartes de réutilisation locales. Les métadonnées de citation sont dans [`CITATION.cff`](CITATION.cff). L’utilisation du code ne transforme pas les limites de simulation décrites ci-dessus en validation de matériel.

## Références

[1] [Qiskit Aer — documentation de l’AerSimulator](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html).

[2] [Perceval — documentation de la plateforme photonique](https://perceval.quandela.net/).
