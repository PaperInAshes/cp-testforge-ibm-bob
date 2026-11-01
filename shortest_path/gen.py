#!/usr/bin/env python3
"""
gen.py - Generator test cases untuk soal Shortest Path.
Menghasilkan folder tests/ berisi minimal 12 test dengan berbagai kategori.

Kategori:
  SAMPLE         - test dari soal asli
  MINIMAL        - kasus paling kecil (N=2)
  BOUNDARY       - nilai N, M mendekati maksimum
  EDGE           - struktur khusus (linear chain, disconnected, self-loop, multi-edge, dll)
  ANTI-WRONG-ANSWER - menjebak solusi salah (BFS unweighted, greedy salah)
  ANTI-OVERFLOW  - bobot besar, jalur panjang (potensi overflow int32)
  MAX/STRESS     - input maksimum untuk TLE slow.py
  RANDOM-KECIL   - graf acak kecil

Jebakan yang dicakup:
  T1: BFS tanpa bobot (salah untuk bobot berbeda, path pendek tapi mahal vs panjang tapi murah)
  T2: Tidak menangani graf tak terhubung (output -1)
  T3: Overflow int32 (jarak total > 2^31-1, perlu int64 / Python int)
  T4: Self-loop (harus diabaikan)
  T5: Multi-edge (harus pilih yang terpendek)
  T6: Node 1 = Node N (N=2, sisi langsung)
  T7: Dijkstra O(N^2) TLE pada graf sparse besar
  T8: Jalur tidak langsung lebih pendek (banyak relaksasi)
"""
import random
import os
import sys

SEED = 42
rng = random.Random(SEED)

TESTS_DIR = os.path.join(os.path.dirname(__file__), "tests")
os.makedirs(TESTS_DIR, exist_ok=True)

def write_test(name, content):
    path = os.path.join(TESTS_DIR, name)
    with open(path, 'w') as f:
        f.write(content)
    print(f"  Generated: {name}")

def make_graph(N, edges):
    """edges: list of (u, v, w)"""
    lines = [f"{N} {len(edges)}"]
    for u, v, w in edges:
        lines.append(f"{u} {v} {w}")
    return '\n'.join(lines) + '\n'

# ─────────────────────────────────────────────────────────────────────────────
# 01 SAMPLE - Test dari soal
# ─────────────────────────────────────────────────────────────────────────────
write_test("01_sample.in", make_graph(4, [
    (1, 2, 5),
    (2, 4, 5),
    (1, 3, 1),
    (3, 4, 20),
]))
# Expected: 10

# ─────────────────────────────────────────────────────────────────────────────
# 02 MINIMAL - N=2, satu sisi langsung
# ─────────────────────────────────────────────────────────────────────────────
write_test("02_minimal_direct.in", make_graph(2, [
    (1, 2, 1),
]))
# Expected: 1

# ─────────────────────────────────────────────────────────────────────────────
# 03 MINIMAL DISCONNECTED - N=2, tidak ada sisi
# ─────────────────────────────────────────────────────────────────────────────
write_test("03_minimal_disconnected.in", "2 1\n2 2 5\n")
# N=2, hanya self-loop di node 2, node 1 dan 2 tidak terhubung
# Expected: -1

# ─────────────────────────────────────────────────────────────────────────────
# 04 ANTI-WRONG-ANSWER T1: BFS trap
# Jalur 1->N via "hop sedikit tapi mahal" vs "hop banyak tapi murah"
# BFS memilih hop sedikit, Dijkstra memilih total terkecil
# ─────────────────────────────────────────────────────────────────────────────
# Graph: 1->5 langsung bobot 1000, atau 1->2->3->4->5 bobot masing2 1
write_test("04_anti_bfs_trap.in", make_graph(5, [
    (1, 5, 1000),   # 1 hop, mahal
    (1, 2, 1),
    (2, 3, 1),
    (3, 4, 1),
    (4, 5, 1),      # 4 hop, murah: total 4
]))
# Expected: 4

# ─────────────────────────────────────────────────────────────────────────────
# 05 ANTI-WRONG-ANSWER T1 variant: BFS menang hop tapi kalah bobot
# ─────────────────────────────────────────────────────────────────────────────
# 1->2 bobot 100, 1->3->4->2 bobot 1+1+1=3
write_test("05_anti_bfs_indirect.in", make_graph(4, [
    (1, 2, 100),
    (1, 3, 1),
    (3, 4, 1),
    (4, 2, 1),
    (2, 4, 50),
]))
# Expected: 3 (1->3->4->2, not 1->2=100)

# ─────────────────────────────────────────────────────────────────────────────
# 06 EDGE: Self-loop - harus diabaikan (T4)
# ─────────────────────────────────────────────────────────────────────────────
write_test("06_self_loop.in", make_graph(3, [
    (1, 1, 999999999),  # self-loop
    (2, 2, 1),          # self-loop
    (3, 3, 1),          # self-loop
    (1, 2, 5),
    (2, 3, 5),
]))
# Expected: 10

# ─────────────────────────────────────────────────────────────────────────────
# 07 EDGE: Multi-edge - harus pilih terkecil (T5)
# ─────────────────────────────────────────────────────────────────────────────
write_test("07_multi_edge.in", make_graph(3, [
    (1, 2, 100),
    (1, 2, 3),     # edge lebih murah
    (1, 2, 50),
    (2, 3, 7),
    (2, 3, 1),     # edge lebih murah
]))
# Expected: 4 (1->2=3, 2->3=1)

# ─────────────────────────────────────────────────────────────────────────────
# 08 ANTI-OVERFLOW: Bobot besar, jalur panjang - T3
# N=5 simpul, rantai panjang dengan bobot hampir max per sisi
# Total: 4 * 1_000_000_000 = 4_000_000_000 > 2^31-1 (2_147_483_647)
# ─────────────────────────────────────────────────────────────────────────────
W = 1_000_000_000
write_test("08_anti_overflow.in", make_graph(5, [
    (1, 2, W),
    (2, 3, W),
    (3, 4, W),
    (4, 5, W),
]))
# Expected: 4000000000

# ─────────────────────────────────────────────────────────────────────────────
# 09 EDGE: Disconnected - banyak komponen (T2)
# ─────────────────────────────────────────────────────────────────────────────
write_test("09_disconnected.in", make_graph(6, [
    (1, 2, 1),
    (2, 3, 1),
    # node 4, 5, 6 terhubung sendiri tapi tidak ke node 1
    (4, 5, 1),
    (5, 6, 1),
]))
# Expected: -1 (tidak ada jalur 1->6)

# ─────────────────────────────────────────────────────────────────────────────
# 10 EDGE: Linear chain - path paling panjang (T8)
# N=1000, rantai 1->2->3->...->1000
# ─────────────────────────────────────────────────────────────────────────────
N_chain = 1000
chain_edges = [(i, i+1, i) for i in range(1, N_chain)]
write_test("10_linear_chain.in", make_graph(N_chain, chain_edges))
# Expected: sum(1..999) = 499500

# ─────────────────────────────────────────────────────────────────────────────
# 11 ANTI-WRONG-ANSWER: Greedy edge weight (T1 + T8)
# Greedy: selalu pilih sisi terkecil saat ini, bisa terperangkap lokal
# ─────────────────────────────────────────────────────────────────────────────
write_test("11_anti_greedy.in", make_graph(6, [
    (1, 2, 1),
    (2, 3, 1),
    (3, 6, 1000),   # jalur via 2,3 tampak murah tapi mahal di akhir
    (1, 4, 2),
    (4, 5, 2),
    (5, 6, 2),      # total 6
    (1, 6, 100),
]))
# Expected: 6 (1->4->5->6)
# Greedy: 1->2 (1) ->3 (1) -> 6 (1000) = 1002 SALAH

# ─────────────────────────────────────────────────────────────────────────────
# 12 RANDOM KECIL - Graf acak kecil seed tetap
# ─────────────────────────────────────────────────────────────────────────────
N_r, M_r = 10, 20
edges_r = []
# Pastikan ada jalur 1->N
path_nodes = rng.sample(range(2, N_r), min(3, N_r-2))
path_nodes = [1] + path_nodes + [N_r]
for i in range(len(path_nodes)-1):
    w = rng.randint(1, 100)
    edges_r.append((path_nodes[i], path_nodes[i+1], w))
# Tambah edge acak
for _ in range(M_r - len(edges_r)):
    u = rng.randint(1, N_r)
    v = rng.randint(1, N_r)
    w = rng.randint(1, 100)
    edges_r.append((u, v, w))
write_test("12_random_small.in", make_graph(N_r, edges_r))

# ─────────────────────────────────────────────────────────────────────────────
# 13 RANDOM KECIL 2 - Graf acak disconnected
# ─────────────────────────────────────────────────────────────────────────────
N_r2, M_r2 = 15, 10
edges_r2 = []
# Hanya hubungkan node 1..7, node 8..15 terisolasi dari node 1
for _ in range(M_r2):
    u = rng.randint(1, 7)
    v = rng.randint(8, N_r2)
    # u ke v tapi pastikan tidak dari node 1 ke N_r2=15
    # Buat terisolasi: hubungkan hanya cluster 1..7 internal dan 8..15 internal
    pass
# Cluster 1: node 1..7
for _ in range(5):
    u = rng.randint(1, 7)
    v = rng.randint(1, 7)
    w = rng.randint(1, 50)
    edges_r2.append((u, v, w))
# Cluster 2: node 8..15
for _ in range(5):
    u = rng.randint(8, N_r2)
    v = rng.randint(8, N_r2)
    w = rng.randint(1, 50)
    edges_r2.append((u, v, w))
write_test("13_random_disconnected.in", make_graph(N_r2, edges_r2))
# Expected: -1

# ─────────────────────────────────────────────────────────────────────────────
# 14 BOUNDARY: N=100000, M=200000 - bintang (1 terhubung ke semua, N di ujung)
# Menjebak TLE untuk O(N^2) Dijkstra
# ─────────────────────────────────────────────────────────────────────────────
N_star = 100000
M_star = min(200000, N_star - 1)
star_edges = []
# Hub node 1 ke semua node 2..M_star+1 dengan bobot acak
for i in range(2, M_star + 2):
    if i > N_star:
        break
    star_edges.append((1, i, rng.randint(1, 1_000_000_000)))
write_test("14_boundary_star.in", make_graph(N_star, star_edges))

# ─────────────────────────────────────────────────────────────────────────────
# 15 MAX/STRESS: N=100000, M=200000 sparse random - TLE test
# ─────────────────────────────────────────────────────────────────────────────
N_max = 100000
M_max = 200000
max_edges = []
# Pastikan ada jalur dari 1 ke N_max
for i in range(1, N_max):
    max_edges.append((i, i+1, rng.randint(1, 1_000_000_000)))
remaining = M_max - (N_max - 1)
for _ in range(remaining):
    u = rng.randint(1, N_max)
    v = rng.randint(1, N_max)
    w = rng.randint(1, 1_000_000_000)
    max_edges.append((u, v, w))
rng.shuffle(max_edges)
write_test("15_max_stress.in", make_graph(N_max, max_edges))

# ─────────────────────────────────────────────────────────────────────────────
# 16 BOUNDARY: N=2, M=200000 - multi-edge ekstrem antara node 1 dan 2
# ─────────────────────────────────────────────────────────────────────────────
N_me = 2
M_me = 200000
me_edges = []
min_w = 1_000_000_000
for _ in range(M_me):
    w = rng.randint(1, 1_000_000_000)
    min_w = min(min_w, w)
    me_edges.append((1, 2, w))
write_test("16_boundary_multiedge.in", make_graph(N_me, me_edges))
# Expected: min of all weights

print(f"\nTotal test generated: 16")
print(f"Tests dir: {TESTS_DIR}")
