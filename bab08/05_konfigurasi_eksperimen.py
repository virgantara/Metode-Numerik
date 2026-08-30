"""Bab 8 - Konfigurasi sederhana eksperimen numerik."""

import json
import platform

import numpy as np


def buat_config():
    """Membuat konfigurasi eksperimen yang eksplisit dan mudah dicatat."""
    return {
        "metode": "rk4",
        "h": 0.01,
        "toleransi": 1e-8,
        "maks_iterasi": 1000,
        "dtype": "float64",
    }


def metadata_lingkungan():
    """Metadata minimum untuk membantu reproduksibilitas."""
    return {
        "python": platform.python_version(),
        "numpy": np.__version__,
        "platform": platform.platform(),
    }


if __name__ == "__main__":
    config = buat_config()

    catatan = {
        "config": config,
        "environment": metadata_lingkungan(),
    }

    print(
        json.dumps(
            catatan,
            indent=2,
        )
    )
