"""Quirk V2 pour Aqara LED Strip T1 (lumi.light.acn132) - tous les attributs cluster 0xFCC0."""

from typing import Final
import zigpy.types as t
from zigpy.zcl.foundation import ZCLAttributeDef, BaseAttributeDefs
from zigpy.quirks import CustomCluster
from zigpy.quirks.v2 import QuirkBuilder


class AqaraFCC0Cluster(CustomCluster):
    """Cluster Aqara 0xFCC0 avec tous les attributs du ruban T1."""

    cluster_id = 0xFCC0

    class AttributeDefs(BaseAttributeDefs):
        min_brightness: Final = ZCLAttributeDef(
            id=0x0515,
            type=t.uint8_t,
            access="rwp",
            is_manufacturer_specific=True,
            manufacturer_code=0x115F,
        )
        max_brightness: Final = ZCLAttributeDef(
            id=0x0516,
            type=t.uint8_t,
            access="rwp",
            is_manufacturer_specific=True,
            manufacturer_code=0x115F,
        )
        length: Final = ZCLAttributeDef(
            id=0x051B,
            type=t.uint8_t,     # valeur brute, ×0.2 = mètres
            access="rwp",
            is_manufacturer_specific=True,
            manufacturer_code=0x115F,
        )
        audio: Final = ZCLAttributeDef(
            id=0x051C,
            type=t.uint8_t,     # 0=OFF, 1=ON
            access="rwp",
            is_manufacturer_specific=True,
            manufacturer_code=0x115F,
        )
        audio_effect: Final = ZCLAttributeDef(
            id=0x051D,
            type=t.uint32_t,    # 0=random, 1=blink, 2=rainbow, 3=wave
            access="rwp",
            is_manufacturer_specific=True,
            manufacturer_code=0x115F,
        )
        audio_sensitivity: Final = ZCLAttributeDef(
            id=0x051E,
            type=t.uint8_t,     # 0=low, 1=medium, 2=high
            access="rwp",
            is_manufacturer_specific=True,
            manufacturer_code=0x115F,
        )
        preset: Final = ZCLAttributeDef(
            id=0x051F,
            type=t.uint32_t,    # 1–32 (0–6 = presets par défaut)
            access="rwp",
            is_manufacturer_specific=True,
            manufacturer_code=0x115F,
        )
        speed: Final = ZCLAttributeDef(
            id=0x0520,
            type=t.uint8_t,     # 1–100
            access="rwp",
            is_manufacturer_specific=True,
            manufacturer_code=0x115F,
        )


(
    QuirkBuilder("Aqara", "lumi.light.acn132")
    .replaces(AqaraFCC0Cluster, endpoint_id=1)
    .add_to_registry()
)
