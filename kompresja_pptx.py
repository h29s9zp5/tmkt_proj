import os
import time
import zipfile
import gzip
import shutil
import py7zr
import rarfile
import psutil  # do mierzenia zużycia pamięci


# Funkcja do obliczania współczynnika kompresji
def compression_ratio(original_size, compressed_size):
    return original_size / compressed_size if compressed_size > 0 else 0


# Funkcja do mierzenia zużycia pamięci
def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # pamięć w MB


# Funkcja do kompresji ZIP
def compress_zip(input_file, output_file):
    start_time = time.time()
    initial_memory = memory_usage()

    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(input_file, os.path.basename(input_file))

    end_time = time.time()
    end_memory = memory_usage()

    compression_time = end_time - start_time
    compressed_size = os.path.getsize(output_file)
    original_size = os.path.getsize(input_file)
    compression_ratio_value = compression_ratio(original_size, compressed_size)

    return compression_time, compression_ratio_value, initial_memory, end_memory


# Funkcja do kompresji Gzip
def compress_gzip(input_file, output_file):
    start_time = time.time()
    initial_memory = memory_usage()

    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    end_time = time.time()
    end_memory = memory_usage()

    compression_time = end_time - start_time
    compressed_size = os.path.getsize(output_file)
    original_size = os.path.getsize(input_file)
    compression_ratio_value = compression_ratio(original_size, compressed_size)

    return compression_time, compression_ratio_value, initial_memory, end_memory


# Funkcja do kompresji 7-Zip
def compress_7zip(input_file, output_file):
    start_time = time.time()
    initial_memory = memory_usage()

    with py7zr.SevenZipFile(output_file, mode='w') as zf:
        zf.write(input_file, os.path.basename(input_file))

    end_time = time.time()
    end_memory = memory_usage()

    compression_time = end_time - start_time
    compressed_size = os.path.getsize(output_file)
    original_size = os.path.getsize(input_file)
    compression_ratio_value = compression_ratio(original_size, compressed_size)

    return compression_time, compression_ratio_value, initial_memory, end_memory


# Funkcja do kompresji RAR
def compress_rar(input_file, output_file):
    start_time = time.time()
    initial_memory = memory_usage()

    with rarfile.RarFile(output_file, 'w') as rf:
        rf.write(input_file, os.path.basename(input_file))

    end_time = time.time()
    end_memory = memory_usage()

    compression_time = end_time - start_time
    compressed_size = os.path.getsize(output_file)
    original_size = os.path.getsize(input_file)
    compression_ratio_value = compression_ratio(original_size, compressed_size)

    return compression_time, compression_ratio_value, initial_memory, end_memory


# Przykład pliku PPT do kompresji
input_file = 'wtmkt.pptx'  # Zamień na ścieżkę do pliku PPT, który chcesz skompresować

# Wyniki kompresji ZIP
zip_output = 'example.zip'
zip_time, zip_ratio, zip_initial_mem, zip_final_mem = compress_zip(input_file, zip_output)
print(f"ZIP Compression Time: {zip_time:.2f} s")
print(f"ZIP Compression Ratio: {zip_ratio:.2f}")
print(f"ZIP Memory Usage: {zip_initial_mem:.2f} MB -> {zip_final_mem:.2f} MB")

# Wyniki kompresji Gzip
gzip_output = 'example.pptx.gz'
gzip_time, gzip_ratio, gzip_initial_mem, gzip_final_mem = compress_gzip(input_file, gzip_output)
print(f"Gzip Compression Time: {gzip_time:.2f} s")
print(f"Gzip Compression Ratio: {gzip_ratio:.2f}")
print(f"Gzip Memory Usage: {gzip_initial_mem:.2f} MB -> {gzip_final_mem:.2f} MB")

# Wyniki kompresji 7-Zip
sevenzip_output = 'example.7z'
sevenzip_time, sevenzip_ratio, sevenzip_initial_mem, sevenzip_final_mem = compress_7zip(input_file, sevenzip_output)
print(f"7-Zip Compression Time: {sevenzip_time:.2f} s")
print(f"7-Zip Compression Ratio: {sevenzip_ratio:.2f}")
print(f"7-Zip Memory Usage: {sevenzip_initial_mem:.2f} MB -> {sevenzip_final_mem:.2f} MB")

# Wyniki kompresji RAR
rar_output = 'example.rar'
rar_time, rar_ratio, rar_initial_mem, rar_final_mem = compress_rar(input_file, rar_output)
print(f"RAR Compression Time: {rar_time:.2f} s")
print(f"RAR Compression Ratio: {rar_ratio:.2f}")
print(f"RAR Memory Usage: {rar_initial_mem:.2f} MB -> {rar_final_mem:.2f} MB")
