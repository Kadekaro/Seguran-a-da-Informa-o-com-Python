from threading import Thread
import time


def carro(velocidade, piloto):
    distancia_km = 0
    while distancia_km <= 10:
        distancia_km += velocidade
        time.sleep(0.5)
        print(f"Piloto: {piloto} - Km: {distancia_km}")
        if piloto == "Bianca":
            print("=" * 50)


thread_carro1 = Thread(target=carro, args=[1, "Bruno"])
thread_carro2 = Thread(target=carro, args=[1.5, "Bianca"])

thread_carro1.start()
thread_carro2.start()
