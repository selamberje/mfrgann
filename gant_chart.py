import streamlit as st
import pandas as pd

# ============================================================
# MFR GANN SQUARE OF 9 - STREAMLIT WEB EDITION
# ============================================================

st.set_page_config(
    page_title="MFR Gann Square of 9",
    page_icon="📊",
    layout="wide"
)

GRID_SIZE = 35
MAX_NUMBER = 210  # Had nombor 1..210

# Warna Asas
WHITE = "#FFFFFF"
BLUE = "#0000DD"
RED = "#BF0000"
YELLOW = "#F0F000"
GREEN = "#A6FA74"
BLACK = "#000000"
ORANGE_HIGHLIGHT = "#FF8C00"

COLOR_PATTERN = [
    "BWWWWWWWWWWWWWWWWRWWWWWWWWWWWWWWWWB",
    "WBWWWGWWWYWWWGWWWRWWWGWWWYWWWGWWWBW",
    "WWBWWWWWWWWWWWWWWRWWWWWWWWWWWWWWBWW",
    "WWWBWWWWWWYWWWWWWRWWWWWWYWWWWWWBWWW",
    "WWWWBWWWWWWWWWWWWRWWWWWWWWWWWWBWWWW",
    "WGWWWBWWGWWYWWGWWRWWGWWYWWGWWBWWWGW",
    "WWWWWWBWWWWWWWWWWRWWWWWWWWWWBWWWWWW",
    "WWWWWWWBWWWWYWWWWRWWWWYWWWWBWWWWWWW",
    "WWWWWGWWBWWWWWWWWRWWWWWWWWBWWGWWWWW",
    "WYWWWWWWWBWGWYWGWRWGWYWGWBWWWWWWWYW",
    "WWWYWWWWWWBWWWWWWRWWWWWWBWWWWWWYWWW",
    "WWWWWYWWWGWBWWYWWRWWYWWBWGWWWYWWWWW",
    "WWWWWWWYWWWWBWWWWRWWWWBWWWWYWWWWWWW",
    "WGWWWWWWWYWWWBGYGRGYGBWWWYWWWWWWWGW",
    "WWWWWGWWWWWYWGBWWRWWBGWYWWWWWGWWWWW",
    "WWWWWWWWWGWWWYWBYRYBWYWWWGWWWWWWWWW",
    "WWWWWWWWWWWWWGWYBRBYWGWWWWWWWWWWWWW",
    "RRRRRRRRRRRRRRRRRWRRRRRRRRRRRRRRRRR",
    "WWWWWWWWWWWWWGWYBRBYWGWWWWWWWWWWWWW",
    "WWWWWWWWWGWWWYWBYRYBWYWWWGWWWWWWWWW",
    "WWWWWGWWWWWYWGBWWRWWBGWYWWWWWGWWWWW",
    "WGWWWWWWWYWWWBGYGRGYGBWWWYWWWWWWWGW",
    "WWWWWWWYWWWWBWWWWRWWWWBWWWWYWWWWWWW",
    "WWWWWYWWWGWBWWYWWRWWYWWBWGWWWYWWWWW",
    "WWWYWWWWWWBWWWWWWRWWWWWWBWWWWWWYWWW",
    "WYWWWWWWWBWGWYWGWRWGWYWGWBWWWWWWWYW",
    "WWWWWGWWBWWWWWWWWRWWWWWWWWBWWGWWWWW",
    "WWWWWWWBWWWWYWWWWRWWWWYWWWWBWWWWWWW",
    "WWWWWWBWWWWWWWWWWRWWWWWWWWWWBWWWWWW",
    "WGWWWBWWGWWYWWGWWRWWGWWYWWGWWBWWWWW",
    "WWWWBWWWWWWWWWWWWRWWWWWWWWWWWWBWWWW",
    "WWWBWWWWWWYWWWWWWRWWWWWWYWWWWWWBWWW",
    "WWBWWWWWWWWWWWWWWRWWWWWWWWWWWWWWBWW",
    "WBWWWGWWWYWWWGWWWRWWWGWWWYWWWGWWWBW",
    "BWWWWWWWWWWWWWWWWRWWWWWWWWWWWWWWWWB",
]


@st.cache_data
def generate_gann_square(size=35):
    grid = [[0 for _ in range(size)] for _ in range(size)]
    center = size // 2
    x, y = center, center
    grid[y][x] = 1
    number = 2

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    step = 1
    direction_index = 0

    while number <= size * size:
        for _ in range(2):
            dx, dy = directions[direction_index]
            for _ in range(step):
                if number > size * size:
                    break
                x += dx
                y += dy
                if 0 <= x < size and 0 <= y < size:
                    grid[y][x] = number
                number += 1
            direction_index = (direction_index + 1) % 4
        step += 1

    return grid


SQUARE = generate_gann_square()


def find_number_position(number):
    if number is None or number < 1 or number > MAX_NUMBER:
        return None
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if SQUARE[row][col] == number:
                return row, col
    return None


def get_cell_color(number):
    pos = find_number_position(number)
    if not pos:
        return 'W'
    row, col = pos
    return COLOR_PATTERN[row][col]


def calculate_levels(cp):
    if cp <= 0:
        return None

    scale = 100.0 if cp < 2.10 else 10.0

    base_num = int(round(cp * scale))
    base_num = max(1, min(base_num, MAX_NUMBER))

    ep_colors = ('Y',) if 50 <= base_num <= 80 else ('R', 'B')

    # Entry Price (EP)
    if get_cell_color(base_num) in ep_colors:
        entry_num = base_num
    else:
        entry_num = base_num
        for n in range(base_num - 1, 0, -1):
            valid_colors = ('Y',) if 50 <= n <= 80 else ('R', 'B')
            if get_cell_color(n) in valid_colors:
                entry_num = n
                break

    # Target (TP)
    target_num = base_num
    for n in range(entry_num + 1, MAX_NUMBER + 1):
        valid_colors = ('Y',) if 50 <= n <= 80 else ('R', 'B')
        if get_cell_color(n) in valid_colors:
            target_num = n
            break

    # Support / Stop Loss (S)
    support_num = max(1, entry_num - 1)

    return {
        "cp": cp,
        "s_num": support_num,
        "ep_num": entry_num,
        "tp_num": target_num,
        "s": round(support_num / scale, 2),
        "ep": round(entry_num / scale, 2),
        "tp": round(target_num / scale, 2),
    }


# ============================================================
# STREAMLIT UI LAYOUT
# ============================================================

st.title("🎯 MFR GANN SQUARE OF 9")
st.markdown("Calculator & Interactive Chart Generator")

# Sidebar untuk Input
with st.sidebar:
    st.header("⚙️ PRICE INPUT")
    cp_input = st.number_input(
        "Masukkan Current Price (CP):",
        min_value=0.01,
        value=0.80,
        step=0.01,
        format="%.2f"
    )
    calculate_btn = st.button("CALCULATE GANN LEVELS", use_container_width=True)

# Lakukan pengiraan
levels = calculate_levels(cp_input)

# Paparan Hasil (Metrics)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="🛑 STOP LOSS (SL)", value=f"RM {levels['s']:.2f}")
with col2:
    st.metric(label="🎯 ENTRY PRICE (EP)", value=f"RM {levels['ep']:.2f}")
with col3:
    st.metric(label="🚀 TARGET (TP)", value=f"RM {levels['tp']:.2f}")

st.divider()

# Paparan Carta Jadual Gann
st.subheader("📌 Gann Square Chart Visualizer")

# Menjana susunan visual carta
highlight_nums = {levels['s_num'], levels['ep_num'], levels['tp_num']}

color_map = {
    'R': '#FFCCCC',  # Red
    'B': '#CCE5FF',  # Blue
    'Y': '#FFF5CC',  # Yellow
    'G': '#D4EDDA',  # Green
    'W': '#FFFFFF'   # White
}

# Dapatkan julat kawasan carta yang ada nombor 1..210
positions = [
    (row, col)
    for row in range(GRID_SIZE)
    for col in range(GRID_SIZE)
    if 1 <= SQUARE[row][col] <= MAX_NUMBER
]

min_r, max_r = min(p[0] for p in positions), max(p[0] for p in positions)
min_c, max_c = min(p[1] for p in positions), max(p[1] for p in positions)


def style_gann_grid(val):
    if val == "" or val == "0":
        return ""
    num = int(val.replace("★ ", ""))
    
    # Warna sorotan khas untuk SL, EP, TP
    if num in highlight_nums:
        return f"background-color: {ORANGE_HIGHLIGHT}; color: white; font-weight: bold; border: 2px solid black;"

    symbol = get_cell_color(num)
    bg = color_map.get(symbol, '#FFFFFF')
    return f"background-color: {bg}; color: black;"


# Bina DataFrame untuk paparan Streamlit
table_data = []
for r in range(min_r, max_r + 1):
    row_data = []
    for c in range(min_c, max_c + 1):
        val = SQUARE[r][c]
        if 1 <= val <= MAX_NUMBER:
            row_data.append(f"★ {val}" if val in highlight_nums else str(val))
        else:
            row_data.append("")
    table_data.append(row_data)

df = pd.DataFrame(table_data)

# Tampilkan dataframe dengan gaya warna
styled_df = df.style.map(style_gann_grid)
st.dataframe(styled_df, height=600, use_container_width=True)
