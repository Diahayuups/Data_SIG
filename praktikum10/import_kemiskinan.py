import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from beranda.models import Provinsi, Datprof, NamaData

csv_file = "Jumlah Penduduk Miskin, 2021.csv"

df = pd.read_csv(csv_file)

namadata = NamaData.objects.get(id=2)

for _, row in df.iterrows():

    nama_provinsi = str(row.iloc[0]).strip().upper()

    try:
        provinsi = Provinsi.objects.get(name__iexact=nama_provinsi)

        nilai = float(row.iloc[1])

        Datprof.objects.create(
            provinsi=provinsi,
            namadata=namadata,
            tahun=2021,
            jumlah=nilai
        )

        print(f"OK -> {nama_provinsi}")

    except Provinsi.DoesNotExist:
        print(f"TIDAK DITEMUKAN -> {nama_provinsi}")

    except Exception as e:
        print(f"ERROR -> {nama_provinsi} : {e}")

print("IMPORT SELESAI")