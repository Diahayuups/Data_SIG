from django.shortcuts import render
import requests


def home(request):

    url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"

    gempa = []

    try:

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )

        print("STATUS:", response.status_code)

        data = response.json()

        print(data)

        # AMBIL DATA GEMPA
        gempa = data['Infogempa']['gempa']

        # kalau object tunggal
        if isinstance(gempa, dict):
            gempa = [gempa]

        print("JUMLAH GEMPA:", len(gempa))

    except Exception as e:

        print("ERROR:", e)

    return render(request, 'home.html', {
        'gempa': gempa
    })


def berita(request):
    return render(request, 'berita.html')