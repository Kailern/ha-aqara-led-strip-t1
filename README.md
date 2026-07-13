# Aqara LED Strip T1 (lumi.light.acn132) – Home Assistant Scripts & Quirk

**Scripts et quirk pour activer les fonctionnalités avancées des bandeaux LED Aqara T1 via ZHA Toolkit.**

---

## 📌 Prérequis
- **Home Assistant** (version récente)
- **Intégration ZHA** (Zigbee Home Automation)
- **[ZHA Toolkit](https://github.com/mdeweerd/zha-toolkit)** (intégration requise)
- **Bandeau LED Aqara T1** (`lumi.light.acn132`)

---

## 🔧 Installation

### 1️⃣ Quirk pour ZHA Toolkit
**Chemin** : `config/custom_components/zhaquirks/aqara_led_strip_t1_quirk.py`
**Action** :
1. Créer le dossier `config/custom_components/zhaquirks/` dans ton instance Home Assistant.
2. Copier le fichier [`aqara_led_strip_t1_quirk.py`](config/custom_components/zhaquirks/aqara_led_strip_t1_quirk.py) dans ce dossier.
3. **Redémarrer Home Assistant** pour appliquer le quirk.

> **Pourquoi ce quirk ?**
> Après une mise à jour de ZHA Toolkit, les attributs du **cluster `0xFCC0`** (manufacturer-specific) ne sont plus accessibles par défaut.
> **Source** : Reverse engineering via [ZHA Toolkit Issue #123](https://github.com/mdeweerd/zha-toolkit/issues/123).

---

### 2️⃣ Scripts Home Assistant
**Chemin** : `scripts/`
**Action** :
1. Copier les fichiers `.yaml` du dossier [`scripts/`](scripts/) dans ton dossier local `scripts/` (dans le dossier `config` de Home Assistant).
2. **Redémarrer Home Assistant** pour les charger.
3. **Alternative** : Importer chaque script via **Paramètres > Automatisations & Scènes > Scripts > + Ajouter un script > Importer**.

---

## 📜 Scripts disponibles
   Script | Description | Paramètres |
 |--------|-------------|------------|
 | **LED Strip - Enable Audio** | Active le mode musique. | `led_strip` (device ZHA) |
 | **LED Strip - Disable Audio** | Désactive le mode musique. | `led_strip` (device ZHA) |
 | **LED Strip - Set Length** | Définit la longueur physique (1.0–10.0 m). **⚠️ Valeur interne = `longueur × 5`**. | `led_strip`, `length` (m) |
 | **LED Strip - Set Min Brightness** | Luminosité minimale (0–99%). | `led_strip`, `min_brightness` (%) |
 | **LED Strip - Set Max Brightness** | Luminosité maximale (1–100%). | `led_strip`, `max_brightness` (%) |
 | **LED Strip - Set Audio Sensitivity** | Sensibilité du micro (Low/Medium/High). | `led_strip`, `sensitivity` |
 | **LED Strip - Set Audio Effect** | Effet visuel (Random/Blink/Rainbow/Wave). | `led_strip`, `effect` |
 | **LED Strip - Set Preset** | Sélectionne un préréglage (1–32). | `led_strip`, `preset` |
 | **LED Strip - Set Effect Speed** | Vitesse des effets (1–100). | `led_strip`, `speed` |

---

## 🔍 Attributs du cluster `0xFCC0` (Manufacturer-Specific)

**Manufacturer Code** : `0x115F` **(4447 en décimal)**
**Cluster ID** : `0xFCC0` **(64704 en décimal)**
 | Attribut (Hex) | Attribut (Décimal) | Type       | Description                     | Valeurs possibles                     | Notes                                  |
 |----------------|-------------------|------------|---------------------------------|---------------------------------------|----------------------------------------|
 | `0x0515`       | 1301              | `uint8`    | Luminosité minimale             | 0–99                                  |                                        |
 | `0x0516`       | 1302              | `uint8`    | Luminosité maximale             | 1–100                                 |                                        |
 | `0x051B`       | 1307              | `uint8`    | Longueur physique               | **Valeur interne = `longueur × 5`** (ex: 1.0 m = 5) |
 | `0x051C`       | 1308              | `uint8`    | Mode audio                       | 0 = OFF, 1 = ON                       |                                        |
 | `0x051D`       | 1309              | `uint32`   | Effet audio                      | 0 = Random, 1 = Blink, 2 = Rainbow, 3 = Wave |                                        |
 | `0x051E`       | 1310              | `uint8`    | Sensibilité audio               | 0 = Low, 1 = Medium, 2 = High         |                                        |
 | `0x051F`       | 1311
