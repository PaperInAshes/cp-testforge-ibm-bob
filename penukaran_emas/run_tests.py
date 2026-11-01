#!/usr/bin/env python3
"""
run_tests.py — Menjalankan semua test pada solusi yang diberikan.
Usage:
    python3 run_tests.py sol.py          # untuk solusi Python
    python3 run_tests.py sol.cpp         # untuk solusi C++ (dikompilasi otomatis)

Laporan: PASS / WA / TLE / RE per test.
Time limit: 1 detik (sesuai soal).
"""
import sys
import os
import subprocess
import glob
import shutil
import time

TIME_LIMIT = 1.0  # detik
TESTS_DIR = "tests"

def compile_cpp(source_file):
    """Kompilasi C++ dengan g++. Return path binary atau None jika gagal."""
    if not shutil.which("g++"):
        print("ERROR: g++ tidak ditemukan. Install g++ untuk menjalankan solusi C++.")
        return None
    binary = source_file.replace(".cpp", "")
    r = subprocess.run(
        ["g++", "-O2", "-o", binary, source_file],
        capture_output=True, text=True
    )
    if r.returncode != 0:
        print(f"COMPILE ERROR:\n{r.stderr}")
        return None
    print(f"Compiled: {source_file} -> {binary}")
    return binary

def run_solution(cmd, input_text, time_limit):
    """
    Jalankan solusi dengan input_text.
    Return: (output, verdict)
    verdict: 'PASS', 'WA', 'TLE', 'RE'
    """
    try:
        start = time.perf_counter()
        r = subprocess.run(
            cmd,
            input=input_text,
            capture_output=True,
            text=True,
            timeout=time_limit * 2  # subprocess timeout lebih longgar, kita ukur sendiri
        )
        elapsed = time.perf_counter() - start
        
        if r.returncode != 0:
            return r.stdout.strip(), "RE", elapsed
        
        if elapsed > time_limit:
            return r.stdout.strip(), "TLE", elapsed
        
        return r.stdout.strip(), "OK", elapsed
    
    except subprocess.TimeoutExpired:
        return "", "TLE", time_limit * 2

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 run_tests.py <solution_file>")
        print("  <solution_file>: file .py atau .cpp")
        sys.exit(1)
    
    solution_file = sys.argv[1]
    
    if not os.path.exists(solution_file):
        print(f"ERROR: File '{solution_file}' tidak ditemukan.")
        sys.exit(1)
    
    # Tentukan command untuk menjalankan solusi
    ext = os.path.splitext(solution_file)[1].lower()
    if ext == ".py":
        cmd = ["python3", solution_file]
    elif ext == ".cpp":
        binary = compile_cpp(solution_file)
        if binary is None:
            sys.exit(1)
        cmd = [f"./{binary}"]
    else:
        print(f"ERROR: Ekstensi '{ext}' tidak didukung. Gunakan .py atau .cpp")
        sys.exit(1)
    
    # Cari semua test
    test_inputs = sorted(glob.glob(os.path.join(TESTS_DIR, "*.in")))
    if not test_inputs:
        print(f"ERROR: Tidak ada file .in di folder '{TESTS_DIR}/'")
        sys.exit(1)
    
    print(f"\n{'='*70}")
    print(f"  Solusi  : {solution_file}")
    print(f"  Tests   : {len(test_inputs)} test case")
    print(f"  Limit   : {TIME_LIMIT}s")
    print(f"{'='*70}")
    print(f"{'No':<4} {'File':<35} {'Verdict':<8} {'Time':>7}  {'Detail'}")
    print(f"{'-'*70}")
    
    results = {"PASS": 0, "WA": 0, "TLE": 0, "RE": 0}
    
    for i, in_file in enumerate(test_inputs, 1):
        out_file = in_file.replace(".in", ".out")
        
        with open(in_file) as f:
            input_text = f.read()
        
        if not os.path.exists(out_file):
            print(f"{i:<4} {os.path.basename(in_file):<35} {'SKIP':<8} {'N/A':>7}  .out tidak ada")
            continue
        
        with open(out_file) as f:
            expected = f.read().strip()
        
        actual, verdict_raw, elapsed = run_solution(cmd, input_text, TIME_LIMIT)
        
        if verdict_raw == "TLE":
            verdict = "TLE"
        elif verdict_raw == "RE":
            verdict = "RE"
        elif actual == expected:
            verdict = "PASS"
        else:
            verdict = "WA"
        
        results[verdict] = results.get(verdict, 0) + 1
        
        detail = ""
        if verdict == "WA":
            detail = f"expected={expected!r}, got={actual!r}"
        elif verdict == "RE":
            detail = "runtime error"
        elif verdict == "TLE":
            detail = f">{TIME_LIMIT}s"
        
        time_str = f"{elapsed*1000:.0f}ms"
        print(f"{i:<4} {os.path.basename(in_file):<35} {verdict:<8} {time_str:>7}  {detail}")
    
    print(f"{'='*70}")
    print(f"  PASS={results['PASS']}  WA={results['WA']}  TLE={results['TLE']}  RE={results['RE']}")
    total = sum(results.values())
    if results["PASS"] == total:
        print(f"  ✓ SEMUA {total} TEST LULUS")
    else:
        failed = total - results["PASS"]
        print(f"  ✗ {failed}/{total} TEST GAGAL")
    print(f"{'='*70}\n")
    
    # Return exit code: 0 jika semua pass, 1 jika ada yang gagal
    sys.exit(0 if results["PASS"] == total else 1)

if __name__ == "__main__":
    main()
