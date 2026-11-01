#!/usr/bin/env python3
"""
run_tests.py - Runner tes untuk soal Shortest Path.

Usage:
  python3 run_tests.py <file_solusi>

Mendukung:
  - .py  : dijalankan dengan python3
  - .cpp : dikompilasi dengan g++ -O2, lalu dijalankan

Batas waktu: 2 detik (sesuai soal).
Laporan: PASS / WA / TLE / RE per test.
"""
import sys
import os
import subprocess
import time
import tempfile
import shutil

TIME_LIMIT = 2.0  # detik
TESTS_DIR = os.path.join(os.path.dirname(__file__), "tests")
CHECKER = os.path.join(os.path.dirname(__file__), "checker.py")

RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

def compile_cpp(source):
    """Kompilasi file .cpp, kembalikan path executable atau None jika gagal."""
    exe = source.replace(".cpp", "")
    result = subprocess.run(
        ["g++", "-O2", "-o", exe, source],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"{RED}Kompilasi gagal:{RESET}")
        print(result.stderr)
        return None
    return exe

def run_solution(cmd, input_file, time_limit):
    """
    Jalankan solusi dengan input dari file.
    Return: (stdout, stderr, elapsed, status)
    status: 'OK', 'TLE', 'RE'
    """
    with open(input_file, 'rb') as f:
        input_data = f.read()

    start = time.perf_counter()
    try:
        proc = subprocess.run(
            cmd,
            input=input_data,
            capture_output=True,
            timeout=time_limit + 0.5,  # sedikit lebih longgar untuk overhead
        )
        elapsed = time.perf_counter() - start

        if elapsed > time_limit:
            return None, proc.stderr.decode(errors='replace'), elapsed, 'TLE'
        if proc.returncode != 0:
            return None, proc.stderr.decode(errors='replace'), elapsed, 'RE'
        return proc.stdout.decode(errors='replace'), proc.stderr.decode(errors='replace'), elapsed, 'OK'

    except subprocess.TimeoutExpired:
        elapsed = time.perf_counter() - start
        return None, "", elapsed, 'TLE'

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 run_tests.py <file_solusi>")
        sys.exit(1)

    solution_file = sys.argv[1]
    if not os.path.exists(solution_file):
        print(f"File tidak ditemukan: {solution_file}")
        sys.exit(1)

    # Tentukan command
    ext = os.path.splitext(solution_file)[1].lower()
    if ext == '.py':
        cmd = ['python3', solution_file]
    elif ext == '.cpp':
        print(f"Mengkompilasi {solution_file}...")
        exe = compile_cpp(solution_file)
        if exe is None:
            sys.exit(1)
        cmd = [exe]
    else:
        print(f"Ekstensi tidak didukung: {ext}. Gunakan .py atau .cpp")
        sys.exit(1)

    # Ambil semua file .in
    if not os.path.exists(TESTS_DIR):
        print(f"Folder tests/ tidak ditemukan: {TESTS_DIR}")
        sys.exit(1)

    test_files = sorted([
        f for f in os.listdir(TESTS_DIR) if f.endswith('.in')
    ])

    if not test_files:
        print("Tidak ada file .in di folder tests/")
        sys.exit(1)

    print(f"\n{BOLD}{'='*65}{RESET}")
    print(f"{BOLD}  Solusi : {solution_file}{RESET}")
    print(f"{BOLD}  Tests  : {len(test_files)} file .in{RESET}")
    print(f"{BOLD}  TL     : {TIME_LIMIT}s{RESET}")
    print(f"{BOLD}{'='*65}{RESET}")
    print(f"{'No':<4} {'Test':<35} {'Status':<8} {'Time':>8}  {'Info'}")
    print(f"{'-'*65}")

    results = {'PASS': 0, 'WA': 0, 'TLE': 0, 'RE': 0, 'NO_OUT': 0}
    detail_rows = []

    with tempfile.TemporaryDirectory() as tmpdir:
        for i, test_name in enumerate(test_files, 1):
            input_path = os.path.join(TESTS_DIR, test_name)
            expected_path = os.path.join(TESTS_DIR, test_name.replace('.in', '.out'))
            actual_path = os.path.join(tmpdir, test_name.replace('.in', '.actual'))

            # Jalankan solusi
            stdout, stderr, elapsed, run_status = run_solution(cmd, input_path, TIME_LIMIT)

            if run_status == 'TLE':
                status_str = f"{YELLOW}TLE{RESET}"
                info = f">{TIME_LIMIT}s"
                results['TLE'] += 1
            elif run_status == 'RE':
                status_str = f"{RED}RE{RESET}"
                info = stderr.strip()[:50] if stderr else "runtime error"
                results['RE'] += 1
            else:
                # Tulis output aktual
                with open(actual_path, 'w') as f:
                    f.write(stdout)

                if not os.path.exists(expected_path):
                    status_str = f"{CYAN}NO_OUT{RESET}"
                    info = ".out tidak ada"
                    results['NO_OUT'] += 1
                else:
                    # Cek kebenaran via checker
                    checker_result = subprocess.run(
                        ['python3', CHECKER, input_path, expected_path, actual_path],
                        capture_output=True, text=True
                    )
                    if checker_result.returncode == 0:
                        status_str = f"{GREEN}PASS{RESET}"
                        info = ""
                        results['PASS'] += 1
                    else:
                        status_str = f"{RED}WA{RESET}"
                        info = checker_result.stdout.strip()[:50]
                        results['WA'] += 1

            time_str = f"{elapsed:.3f}s"
            # status_str contains ANSI codes so pad the plain version
            plain_status = run_status if run_status != 'OK' else ('PASS' if 'PASS' in status_str else 'WA')
            plain_padded = plain_status.ljust(8)
            print(f"{i:<4} {test_name:<35} {status_str}{' ' * (8 - len(plain_status))} {time_str:>8}  {info}")
            detail_rows.append((test_name, run_status if run_status != 'OK' else ('PASS' if results['PASS'] > sum(results.values())-1 else 'WA'), elapsed))

    print(f"{'-'*65}")
    total = sum(results.values())
    print(f"\n{BOLD}RINGKASAN:{RESET}")
    print(f"  {GREEN}PASS  : {results['PASS']}/{total}{RESET}")
    if results['WA']     > 0: print(f"  {RED}WA    : {results['WA']}{RESET}")
    if results['TLE']    > 0: print(f"  {YELLOW}TLE   : {results['TLE']}{RESET}")
    if results['RE']     > 0: print(f"  {RED}RE    : {results['RE']}{RESET}")
    if results['NO_OUT'] > 0: print(f"  {CYAN}NO_OUT: {results['NO_OUT']}{RESET}")
    print()

    # Return code: 0 jika semua PASS, lainnya 1
    if results['WA'] + results['TLE'] + results['RE'] + results['NO_OUT'] == 0:
        print(f"{GREEN}{BOLD}Semua test PASS!{RESET}")
        sys.exit(0)
    else:
        print(f"{RED}{BOLD}Ada test yang tidak PASS.{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
