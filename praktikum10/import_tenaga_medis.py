import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from beranda.models import Provinsi, Datprof, NamaData

csv_file = "Jumlah Tenaga Medis, 2023.csv"

df = pd.read_csv(csv_file)

namadata = NamaData.objects.get(id=3)

for _, row in df.iterrows():

    nama_provinsi = str(row.iloc[0]).strip().upper()

    try:
        provinsi = Provinsi.objects.get(name__iexact=nama_provinsi)

        nilai = str(row.iloc[1]).strip()

        if nilai in ["-", "–", "", "nan"]:
            nilai = 0

        nilai = float(nilai)

        Datprof.objects.create(
            provinsi=provinsi,
            namadata=namadata,
            tahun=2023,
            jumlah=nilai
        )

        print(f"OK -> {nama_provinsi}")

    except Provinsi.DoesNotExist:
        print(f"TIDAK DITEMUKAN -> {nama_provinsi}")

    except Exception as e:
        print(f"ERROR -> {nama_provinsi} : {e}")

print("IMPORT SELESAI")