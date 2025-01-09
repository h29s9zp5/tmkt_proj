import zipfile
import time
import os


def test_compression(input_file, output_zip):
    # Mierzymy czas rozpoczęcia kompresji
    start_time = time.time()

    # Kompresja pliku
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(input_file, os.path.basename(input_file))

    # Mierzymy czas zakończenia kompresji
    end_time = time.time()

    # Rozmiar oryginalnego pliku
    original_size = os.path.getsize(input_file)

    # Rozmiar skompresowanego pliku
    compressed_size = os.path.getsize(output_zip)

    # Obliczamy czas kompresji, współczynnik kompresji i prędkość
    compression_time = end_time - start_time
    compression_ratio = compressed_size / original_size
    compression_speed = original_size / compression_time if compression_time > 0 else float('inf')

    # Wyświetlamy wyniki z większą dokładnością
    print(f"Czas kompresji: {compression_time:.6f} sekund")
    print(f"Współczynnik kompresji: {compression_ratio:.6f}")
    print(f"Prędkość kompresji: {compression_speed / (1024 * 1024):.6f} MB/s")
    print(f"Rozmiar przed kompresją: {original_size} bajtów")
    print(f"Rozmiar po kompresji: {compressed_size} bajtów")


# Przykład użycia:
input_file = '../Techniki Kodowania i Modulacji/kompresja/pythonProject1/Wuthering Heights.txt'  # Ścieżka do pliku tekstowego
output_zip = 'plik.zip'  # Ścieżka do pliku ZIP

test_compression(input_file, output_zip)
