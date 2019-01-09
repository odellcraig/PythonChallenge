#!/usr/bin/env python -w
from PIL import Image
import requests
import wave
import math


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True, auth=('butter', 'fly'))
    with open(f'25/{local_filename}', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                # f.flush() commented by recommendation from J.F.Sebastian
    return local_filename


# for i in range(1, 26):
#     download_file(f'http://www.pythonchallenge.com/pc/hex/lake{i}.wav')

wavs = [wave.open('25/lake%d.wav' % i) for i in range(1, 26)]
parts = []
w = h = None
for i in range(25):
    data = wavs[i].readframes(wavs[i].getnframes())
    w = h = int(math.sqrt(len(data) // 3))
    img = Image.frombytes('RGB', (w, h), data)
    parts.append(img)

combined = Image.new('RGB', (w * 5, h * 5))
for i in range(25):
    r = i // 5
    c = i % 5
    print(r, c)
    combined.paste(parts[i], (c * w, r * h))
combined.show()

# decent
# http://www.pythonchallenge.com/pc/hex/decent.html
