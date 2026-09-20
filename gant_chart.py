import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# MFR GANN SQUARE OF 9 - STREAMLIT HTML/CSS GRID EDITION
# ============================================================

st.set_page_config(
    page_title="MFR Gann Square of 9",
    page_icon="📊",
    layout="wide"
)

GRID_SIZE = 35
MAX_NUMBER = 210  # Batas nomor 1..210

# Kode Warna Hex Persis Seperti Aplikasi Desktop
COLOR_HEX = {
    "R": "#BF0000", # Red (Very Strong)
    "B": "#0000DD", # Blue (Strong)
    "G": "#A6FA74", # Green (Weak)
    "Y": "#F0F000", # Yellow (Very Weak)
    "W": "#FFFFFF"  # White (Neutral)
}

TEXT_COLOR_HEX = {
    "R": "#FFFFFF",
    "B": "#FFFFFF",
    "G": "#000000",
    "Y": "#000000",
    "W": "#000000"
}

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
# STREAMLIT UI LAYOUT & CUSTOM CSS CANVAS RENDERER
# ============================================================

st.markdown("""
<style>
    .metric-card {
        background-color: #F8FAFC;
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #D9E1EA;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎯 MFR GANN SQUARE OF 9")

# Sidebar
with st.sidebar:
    st.header("⚙️ PRICE INPUT")
    cp_input = st.number_input(
        "Current Price (CP):",
        min_value=0.01,
        value=0.80,
        step=0.01,
        format="%.2f"
    )
    st.button("CALCULATE GANN LEVELS", use_container_width=True)

# Hitung Level
levels = calculate_levels(cp_input)

# Ringkasan Level (Metrics)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"<div class='metric-card'><small style='color:#0000DD;font-weight:bold;'>STOP LOSS (SL)</small><h2 style='margin:0;'>RM {levels['s']:.2f}</h2></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='metric-card'><small style='color:#7C3AED;font-weight:bold;'>ENTRY PRICE (EP)</small><h2 style='margin:0;'>RM {levels['ep']:.2f}</h2></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='metric-card'><small style='color:#D97706;font-weight:bold;'>TARGET (TP)</small><h2 style='margin:0;'>RM {levels['tp']:.2f}</h2></div>", unsafe_allow_html=True)

st.write("")

# Menghitung batas koordinat nomor 1..210
positions = [
    (row, col)
    for row in range(GRID_SIZE)
    for col in range(GRID_SIZE)
    if 1 <= SQUARE[row][col] <= MAX_NUMBER
]

min_r, max_r = min(p[0] for p in positions), max(p[0] for p in positions)
min_c, max_c = min(p[1] for p in positions), max(p[1] for p in positions)
visible_cols = max_c - min_c + 1

highlight_nums = {levels['s_num'], levels['ep_num'], levels['tp_num']}

# Generate HTML Grid Persis Seperti Canvas Tkinter
html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{
        margin: 0;
        padding: 10px;
        background-color: #F7F9FC;
        font-family: Arial, sans-serif;
        display: flex;
        justify-content: center;
    }}
    .gann-container {{
        display: grid;
        grid-template-columns: repeat({visible_cols}, minmax(18px, 1fr));
        gap: 1px;
        background-color: #777777;
        border: 1px solid #777777;
        padding: 1px;
        width: 100%;
        max-width: 900px;
    }}
    .gann-cell {{
        aspect-ratio: 1.8 / 1;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: clamp(8px, 1.1vw, 11px);
        font-weight: bold;
        user-select: none;
    }}
    @keyframes blink {{
        0% {{ background-color: #FFE5B4; color: #FF8C00; outline: 2px solid #FF8C00; z-index: 10; }}
        50% {{ background-color: #FF8C00; color: #FFFFFF; outline: 2px solid #FF8C00; z-index: 10; }}
        100% {{ background-color: #FFE5B4; color: #FF8C00; outline: 2px solid #FF8C00; z-index: 10; }}
    }}
    .blink-cell {{
        animation: blink 1s infinite;
    }}
</style>
</head>
<body>
<div class="gann-container">
"""

for r in range(min_r, max_r + 1):
    for c in range(min_c, max_c + 1):
        num = SQUARE[r][c]
        if 1 <= num <= MAX_NUMBER:
            symbol = COLOR_PATTERN[r][c]
            bg_color = COLOR_HEX.get(symbol, "#FFFFFF")
            text_color = TEXT_COLOR_HEX.get(symbol, "#000000")
            
            if num in highlight_nums:
                html_code += f'<div class="gann-cell blink-cell">{num}</div>'
            else:
                html_code += f'<div class="gann-cell" style="background-color: {bg_color}; color: {text_color};">{num}</div>'
        else:
            html_code += '<div class="gann-cell" style="background-color: #FFFFFF;"></div>'

html_code += """
</div>
</body>
</html>
"""

# Render HTML komponen ke Streamlit dengan tinggi responsif
components.html(html_code, height=450, scrolling=True)
