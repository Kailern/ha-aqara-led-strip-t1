# Aqara LED Strip T1 (lumi.light.acn132) – Home Assistant Scripts & Quirk

**Scripts et quirk pour activer les fonctionnalités avancées des bandeaux LED Aqara T1 via ZHA Toolkit.**

---

## 📌 Prérequis
- **Home Assistant** (version 2024.6 ou supérieure recommandée)
- **Intégration ZHA** (Zigbee Home Automation)
- **[ZHA Toolkit](https://github.com/mdeweerd/zha-toolkit)** (intégration requise)
- **Bandeau LED Aqara T1** (`lumi.light.acn132`)

---

---

## 🔧 Installation

### 1️⃣ Quirk pour ZHA Toolkit
**Chemin** : `config/custom_components/zhaquirks/aqara_led_strip_t1_quirk.py`

#### **Pourquoi ce quirk ?**
Après une mise à jour de ZHA Toolkit, les attributs du **cluster `0xFCC0`** (manufacturer-specific) ne sont plus accessibles par défaut.
Ce quirk réactive ces attributs pour le modèle **`lumi.light.acn132`** (Aqara T1 LED Strip).

#### **Comment l'installer ?**
1. Créer le dossier `config/custom_components/zhaquirks/` dans ton instance Home Assistant.
2. Copier le fichier `aqara_led_strip_t1_quirk.py` dans ce dossier.
3. **Redémarrer Home Assistant** pour appliquer le quirk.

> **Source** : Reverse engineering via [ZHA Toolkit Issue #123](https://github.com/mdeweerd/zha-toolkit/issues/123) et tests pratiques avec le matériel.

---

### 2️⃣ Scripts Home Assistant
**Chemin** : `scripts/`

#### **Comment les installer ?**
1. Copier les fichiers `.yaml` du dossier `scripts/` dans ton dossier local `scripts/` (dans le dossier `config` de Home Assistant).
2. **Redémarrer Home Assistant** pour les charger.
3. **Alternative** : Importer chaque script via **Paramètres > Automatisations & Scènes > Scripts > + Ajouter un script > Importer**.

---

---

## 📜 Scripts disponibles
   Script | Description | Paramètres | Exemple d'utilisation |
 |--------|-------------|------------|-----------------------|
 | **LED Strip - Enable Audio** | Active le mode musique (le bandeau réagit au son). | `led_strip` (device ZHA) | Pour activer le mode musique avant une soirée. |
 | **LED Strip - Disable Audio** | Désactive le mode musique. | `led_strip` (device ZHA) | Pour revenir au mode normal. |
 | **LED Strip - Set Length** | Définit la longueur physique du bandeau (1.0–10.0 m). **⚠️ Valeur interne = `longueur × 5`**. | `led_strip`, `length` (m) | Si ton bandeau fait 2.5 m, entre `2.5`. |
 | **LED Strip - Set Min Brightness** | Définit la luminosité minimale (0–99%). | `led_strip`, `min_brightness` (%) | Pour éviter que le bandeau soit trop sombre. |
 | **LED Strip - Set Max Brightness** | Définit la luminosité maximale (1–100%). | `led_strip`, `max_brightness` (%) | Pour limiter la puissance lumineuse. |
 | **LED Strip - Set Audio Sensitivity** | Définit la sensibilité du microphone (Low/Medium/High). | `led_strip`, `sensitivity` | Ajuste en fonction du volume sonore de la pièce. |
 | **LED Strip - Set Audio Effect** | Définit l'effet visuel en mode musique (Random/Blink/Rainbow/Wave). | `led_strip`, `effect` | Pour changer l'ambiance lumineuse. |
 | **LED Strip - Set Preset** | Sélectionne un préréglage (1–32). | `led_strip`, `preset` | Pour basculer entre des configurations sauvegardées. |
 | **LED Strip - Set Effect Speed** | Définit la vitesse des effets (1–100). | `led_strip`, `speed` | Pour ajuster la réactivité des animations. |

---

---

## 🔍 Attributs du cluster `0xFCC0` (Manufacturer-Specific)

**Manufacturer Code** : `0x115F` **(4447 en décimal)**
**Cluster ID** : `0xFCC0` **(64704 en décimal)**

> **Remarque** : Tous ces attributs sont **spécifiques au fabricant (Aqara)** et ne sont pas standardisés dans le protocole Zigbee. Ils ont été découverts par reverse engineering.
 | Attribut (Hex) | Attribut (Décimal) | Type       | Description | Valeurs possibles | Notes |
 |----------------|-------------------|------------|-------------|------------------|-------|
 | `0x0515` | 1301 | `uint8` | Luminosité minimale | 0–99 | Limite la luminosité minimale du bandeau. |
 | `0x0516` | 1302 | `uint8` | Luminosité maximale | 1–100 | Limite la luminosité maximale du bandeau. |
 | `0x051B` | 1307 | `uint8` | Longueur physique | **Valeur interne = `longueur × 5`** (ex: 1.0 m = 5, 2.5 m = 12.5 → **12** ou **13** selon l'arrondi) | **Important** : La valeur envoyée doit être un entier. Utilisez `{{ (length * 5) \| int }}` dans les scripts. |
 | `0x051C` | 1308 | `uint8` | Mode audio | 0 = OFF, 1 = ON | Active ou désactive le mode musique. |
 | `0x051D` | 1309 | `uint32` | Effet audio | 0 = Random, 1 = Blink, 2 = Rainbow, 3 = Wave | Définit le type d'animation en mode musique. |
 | `0x051E` | 1310 | `uint8` | Sensibilité audio | 0 = Low, 1 = Medium, 2 = High | Ajuste la réactivité du microphone. |
 | `0x051F` | 1311 | `uint32` | Préréglage | 1–32 | Sélectionne un préréglage sauvegardé dans le bandeau. |
 | `0x0520` | 1312 | `uint8` | Vitesse des effets | 1–100 | Contrôle la vitesse des animations (1 = lent, 100 = rapide). |

---

---

## 💡 Conseils d'utilisation

### **1. Longueur du bandeau (`Set Length`)**
- **Valeur interne** : Le bandeau attend une valeur **5 fois supérieure** à la longueur réelle en mètres.
  - Exemple : Pour un bandeau de **2.5 m**, entrez `2.5` dans le script. La valeur envoyée sera `12` (car `2.5 × 5 = 12.5` → arrondi à `12`).
- **Pourquoi ?** : C'est une particularité du firmware Aqara. La valeur est stockée sous forme d'entier dans le device.

### **2. Mode audio (`Enable/Disable Audio`)**
- **Prérequis** : Le bandeau doit être **alimenté en 24V** et connecté à un **microphone compatible** (intégré ou externe).
- **Fonctionnement** : En mode audio, le bandeau réagit aux sons ambiants (musique, voix, etc.) avec des animations basées sur l'effet sélectionné.

### **3. Sensibilité audio (`Set Audio Sensitivity`)**
- **Low (0)** : Réagit uniquement aux sons forts (ex: musique à volume élevé).
- **Medium (1)** : Réagit aux sons modérés (ex: voix normale).
- **High (2)** : Réagit aux sons faibles (ex: chuchotements).

### **4. Effets audio (`Set Audio Effect`)**
- **Random (0)** : Changement aléatoire des couleurs.
- **Blink (1)** : Clignotement au rythme de la musique.
- **Rainbow (2)** : Dégradé arc-en-ciel.
- **Wave (3)** : Vagues de couleurs qui se déplacent.

### **5. Préréglages (`Set Preset`)**
- Le bandeau Aqara T1 permet de sauvegarder **jusqu'à 32 préréglages** (couleurs, effets, etc.).
- Les préréglages **0–6** sont généralement réservés aux configurations d'usine.

### **6. Vitesse des effets (`Set Effect Speed`)**
- **1–30** : Effets lents et fluides.
- **31–70** : Effets modérés.
- **71–100** : Effets rapides et dynamiques.

---

---
## 🐛 Dépannage

### **Problème : Les scripts ne fonctionnent pas**
1. **Vérifie que le quirk est installé** :
   - Le fichier `aqara_led_strip_t1_quirk.py` doit être dans `config/custom_components/zhaquirks/`.
   - **Redémarre Home Assistant** après l'avoir ajouté.

2. **Vérifie l'intégration ZHA Toolkit** :
   - Va dans **Paramètres > Appareils et services**.
   - Cherche **ZHA Toolkit** et vérifie qu'il est **chargé et fonctionnel**.

3. **Vérifie le modèle du bandeau** :
   - Utilise **Développeur > États** et cherche ton bandeau.
   - Son `entity_id` doit commencer par `light.` et son `model` doit être `lumi.light.acn132`.

4. **Vérifie les logs** :
   - Va dans **Paramètres > Journaux**.
   - Filtre avec `zha_toolkit` ou `Aqara` pour voir les erreurs éventuelles.

---

### **Problème : Le mode audio ne réagit pas**
- **Vérifie que le microphone est connecté** (si externe).
- **Augmente la sensibilité** (`Set Audio Sensitivity` à `High`).
- **Teste dans une pièce silencieuse** puis fais un bruit fort pour voir si le bandeau réagit.

---
---
## 📚 Crédits et sources
- **Auteur des scripts** : Kailern (adapté depuis les exemples officiels Aqara et la communauté Home Assistant).
- **Quirk** : Adapté des contributions de la communauté [ZHA Toolkit](https://github.com/mdeweerd/zha-toolkit).
- **Inspiration** : [Issue #123](https://github.com/mdeweerd/zha-toolkit/issues/123) (ZHA Toolkit) et tests pratiques avec le matériel.
- **Documentation Aqara** : Informations non publiques, obtenues par reverse engineering.

---
---
## 📜 Licence
Ce projet est **open source** et peut être utilisé librement.
**Attribution appréciée** si vous partagez ou modifiez ce travail.
