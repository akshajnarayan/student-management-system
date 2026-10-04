import time

def spinner(text = "Loading", display = "", loop=20, delay=0.1, end="\n"):
    frames = ["|", "/", "-", "\\"]
    text = text.strip()

    for i in range(loop):
        print(f"\r{text} {frames[i % len(frames)]}", end="")
        time.sleep(delay)
    print("\r\033[2K", end="")
    print(display, end=end)

def loading(text="Loading", display="", loop=3, symbol='.', dots=3, delay=0.4, end="\n"):
    text = text.strip()
    for _ in range(loop):
        for i in range(dots):
            print(f"\r{text} {symbol*(i+1)}", end="")
            time.sleep(delay)
        print("\r\033[2K", end="")
    print(display, end=end)

def progress_bar(width = 40, display="", filler=" ", delay=0.05):
    for filled in range(width+1):
        percentage = round((filled/width)*100)
        empty = width - filled
        bar = ("█" * filled) + (filler * empty)

        print(f"\r[{bar}] {percentage}%", end="")
        time.sleep(delay)
    print("\r\033[2K", end="")
    print(display)

def changing_status(texts, wait=0.2, status_display="", status_loop=3, status_symbol='.', status_dots=3, status_delay=0.4, end="\n"):
    for text in texts:
        loading(text=text, loop=status_loop, symbol=status_symbol, dots=status_dots, delay=status_delay)
        print("\033[1A", end="")
        time.sleep(wait)
    print("\r\033[2K", end="")
    print(status_display, end=end)

def import_data(texts):
    changing_status(texts, end="")
    print("\r\033[2K", end="")
